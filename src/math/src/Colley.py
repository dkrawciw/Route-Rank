import numpy as np
import numpy.typing as npt
from typing import cast

IntArray = npt.NDArray[np.int64]
FloatArray = npt.NDArray[np.float64]

class Colley:
    def __init__(
            self,
            num_routes: int,
    ):
        self.num_routes: int = num_routes
        self.wins: IntArray = np.zeros(num_routes, dtype=np.int64)                                  # times a route was ranked as harder than another route
        self.losses: IntArray = np.zeros(num_routes, dtype=np.int64)                                # times a route was ranked easier than another route
        self.games_played: IntArray = np.zeros(num_routes, dtype=np.int64)                          # times a route has been climbed
        self.comparisons_against: IntArray = np.zeros((num_routes, num_routes), dtype=np.int64)     # counting the comparisons between two routes
    
    def add_comparison(self, winner_idx: int, loser_idx: int) -> None:
        # Update the win/loss count for each route
        self.wins[winner_idx] += 1
        self.losses[loser_idx] += 1

        # Update the number of times that the routes have been climbed
        self.games_played[winner_idx] += 1
        self.games_played[loser_idx] += 1

        # Update that these routes were compared
        self.comparisons_against[winner_idx, loser_idx] += 1
        self.comparisons_against[loser_idx, winner_idx] += 1
    
    def get_rankings(self) -> FloatArray:
        C = -self.comparisons_against
        C_diag = 2 + self.games_played
        np.fill_diagonal(C, C_diag)
        
        b = 1 + (self.wins - self.losses) / 2

        r: FloatArray = cast(FloatArray, np.linalg.solve(C, b))
        return r