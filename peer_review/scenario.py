import logging
import numpy as np
from dataclasses import dataclass
from scipy import stats
from tabulate import tabulate
from textwrap import indent
from typing import Tuple, List, Optional
from pydantic import BaseModel, validator
from copy import copy

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ScenarioSettings(BaseModel):
    axis_range: int
    n_reviewers: int
    n_errors: int
    detect_rate: float

    def __copy__(self):
        Scenario(**__dict__)

    def __deepcopy__(self):
        Scenario(**__dict__)

    @validator("n_errors", "n_reviewers", "axis_range", pre=True, always=True)
    def validate_positive_integer(cls, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("expected positive integer")
        return value

    @validator("detect_rate", pre=True, always=True)
    def validate_probability(cls, value):
        if not isinstance(value, float) or value < 0 or value > 1:
            raise ValueError("expected float in [0, 1]")
        return value


class Distribution:
    target: int
    xx: np.ndarray
    yy: np.ndarray
    zz: np.ndarray

    def __init__(self, scenario: ScenarioSettings, target: Optional[int] = None):
        if not target:
            target = scenario.n_errors
        self.target = target
        self.xx, self.yy, self.zz = self.pdist_full(scenario, target=target)

    def __repr__(self):
        table = tabulate(
            self.zz,
            showindex=True,
            headers="keys",
            tablefmt="psql",
            floatfmt=".5f",
        )
        return (
            "Distribution(\n"
            + indent(f"TARGET: {self.target}+ ERRORS DETECTED\n", " " * 4)
            + indent(table, " " * 4)
            + "\n)"
        )

    @property
    def shape(self):
        return len(self.xx), len(self.yy)

    @classmethod
    def _p_binomial(
        cls, n_reviewers: int, n_errors: int, detect_rate: float, target: int
    ):
        if target > n_errors:
            return None
        else:
            p_success = 1 - (1 - detect_rate) ** n_reviewers
            return sum(
                stats.binom.pmf(range(target, n_errors + 1), n_errors, p_success)
            )

    @classmethod
    def pdist_full(
        cls, scenario: ScenarioSettings, target=None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        if not target:
            target = scenario.n_errors
        x = np.arange(1, scenario.axis_range + 1)
        y = np.arange(1, scenario.axis_range + 1)
        p = np.vectorize(
            lambda x, y: cls._p_binomial(x, y, scenario.detect_rate, target)
        )
        xx, yy = np.meshgrid(x, y)
        zz = p(xx, yy)
        return xx, yy, zz

    def get(self, n_reviewers: int, n_errors: int) -> float:
        return self.zz[n_reviewers][n_errors]


class Scenario:
    name: str
    settings: ScenarioSettings
    data: List[Distribution]

    def __init__(self, name: str, settings: ScenarioSettings):
        self.name = name
        self.settings = settings
        self.data = self.generate_data()

    def clear(self) -> None:
        self.data = []

    def generate_data(self) -> List[Distribution]:
        return [
            Distribution(self.settings, target=errors)
            for errors in range(1, self.settings.axis_range + 1)
        ]

    def _dump(self) -> None:
        # HACK: relies on __str__ from ScenarioSettings
        settings = indent(str(str(self.settings).split(" ")), " " * 4)

        for distribution in self.data:
            print("*" * 110)
            print(f"SCENARIO:\n{settings}\n")
            print(str(distribution) + "\n")
