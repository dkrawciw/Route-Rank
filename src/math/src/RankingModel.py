from abc import ABC, abstractmethod
import numpy as np
import numpy.typing as npt

IntArray = npt.NDArray[np.int64]
FloatArray = npt.NDArray[np.float64]

class RankingModel(ABC):
    
    @abstractmethod
    def add_comparison(self, winner_idx: int, loser_idx: int) -> None:
        pass

    @abstractmethod
    def get_rankings(self) -> FloatArray:
        pass