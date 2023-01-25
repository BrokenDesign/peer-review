
from peer_review.scenario import ScenarioSettings, Scenario
settings = ScenarioSettings(
    axis_range=10, detect_rate=0.25, n_errors=5, n_reviewers=2
)
scenario = Scenario("EXAMPLE", settings)
scenario._dump()