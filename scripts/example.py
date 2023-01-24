import logging
import coloredlogs
from peer_review.scenario import ScenarioSettings, Scenario, logger

logger = logging.getLogger(__name__)
logger.info("test")
# fh = logging.FileHandler('logs/example.log')
# fh.setLevel(logging.DEBUG)
# logger.addHandler(fh)

settings = ScenarioSettings(
    axis_range=10, detect_rate=0.25, n_errors=5, n_reviewers=2
)

scenario = Scenario("EXAMPLE", settings)
scenario._dump()