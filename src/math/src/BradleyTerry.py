import numpy as np
import numpy.typing as npt
from src.RankingModel import RankingModel

FloatArray = npt.NDArray[np.float64]

GRADIENT_DESCENT_STEP_SIZE = 1

class BradleyTerry(RankingModel):
    def __init__(self, num_routes: int):
        self.num_routes: int = num_routes

        self.route_ranks: FloatArray = np.zeros(num_routes, dtype=np.float64)
    
    def comparison_prediction(self, route_A_idx: int, route_B_idx: int) -> float:
        theta_A: float = self.route_ranks[route_A_idx]
        theta_B: float = self.route_ranks[route_B_idx]

        return 1 / (1 + np.exp(-(theta_A - theta_B)))


    def add_comparison(self, winner_idx: int, loser_idx: int) -> None:
        route_comparison_prediction: float = self.comparison_prediction(winner_idx, loser_idx)

        theta_A: float = self.route_ranks[winner_idx]
        theta_B: float = self.route_ranks[loser_idx]

        self.route_ranks[winner_idx] = theta_A + GRADIENT_DESCENT_STEP_SIZE * (1 - route_comparison_prediction)
        self.route_ranks[loser_idx] = theta_B - GRADIENT_DESCENT_STEP_SIZE * (1 - route_comparison_prediction)
    
    def get_rankings(self) -> FloatArray:
        return self.route_ranks