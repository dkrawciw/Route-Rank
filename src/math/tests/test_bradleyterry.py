import numpy as np
from src.BradleyTerry import BradleyTerry

def test_one_comparison():
    num_routes = 10
    model = BradleyTerry(num_routes)

    winner_idx = 0
    loser_idx = 1

    model.add_comparison(winner_idx=winner_idx, loser_idx=loser_idx)
    rankings = model.get_rankings()
    assert rankings[1] < rankings[0]