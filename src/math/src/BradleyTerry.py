import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

"""Plot setup"""
sns.set_style("whitegrid")
sns.set_color_codes(palette="colorblind")

plt.rcParams.update({
	"text.usetex": False,  # keep False to avoid requiring a LaTeX installation
	"mathtext.fontset": "cm",  # Computer Modern (LaTeX-like)
	"font.family": "serif",
	"font.serif": ["Computer Modern Roman", "DejaVu Serif"],
    "axes.labelsize": 14,      # increase axis label size
    "axes.titlesize": 16,
    "xtick.labelsize": 14,     # increase tick / bin label size
    "ytick.labelsize": 14,
    "legend.fontsize": 12,
})

GRADIENT_DESCENT_STEP_SIZE = 1
DOCS_DIR = Path(__file__).parent.parent / "docs"
DOCS_DIR.mkdir(exist_ok=True)

class BradleyTerry():
    def __init__(self, num_routes: int):
        self.num_routes = num_routes

        self.route_ranks = np.zeros(num_routes)
    
    def comparison_prediction(self, route_A_idx: int, route_B_idx: int) -> float:
        theta_A = self.route_ranks[route_A_idx]
        theta_B = self.route_ranks[route_B_idx]

        return 1 / (1 + np.exp(-(theta_A - theta_B)))


    def update_rankings(self, winner_idx: int, loser_idx: int) -> None:
        route_comparison_prediction = self.comparison_prediction(winner_idx, loser_idx)

        theta_A = self.route_ranks[winner_idx]
        theta_B = self.route_ranks[loser_idx]

        self.route_ranks[winner_idx] = theta_A + GRADIENT_DESCENT_STEP_SIZE * (1 - route_comparison_prediction)
        self.route_ranks[loser_idx] = theta_B - GRADIENT_DESCENT_STEP_SIZE * (1 - route_comparison_prediction)

    def plot_comparison(self, figure_path: Path = DOCS_DIR / "bradley_terry.svg") -> None:
        plt.figure(figsize=(10,6))

        x = self.route_ranks
        y = np.zeros_like(self.route_ranks)

        # Draw horizontal line
        plt.axhline(0, color="black", linewidth=1)

        # Plot points
        plt.scatter(x, y, zorder=3)

        # Label each point by its index
        for idx, value in enumerate(x):
            plt.annotate(
                str(idx + 1),
                xy=(value, 0),
                xytext=(0, 10),          # offset label upward
                textcoords="offset points",
                ha="center",
                fontsize=12
            )

        # Make it look like a number line
        plt.yticks([])
        plt.xlabel("Value")
        plt.title("Ranking Each Route According to Comparrisons Recorded")

        # Add some padding around min/max
        padding = 0.1 * (x.max() - x.min())
        plt.xlim(x.min() - padding, x.max() + padding)

        plt.tight_layout()
        plt.savefig(figure_path)

def main():
    bt = BradleyTerry(10)
    bt.plot_comparison(DOCS_DIR / "before_update.svg")

    # Now add update
    winner_idx = 0
    loser_idx = 1
    bt.update_rankings(winner_idx,loser_idx)
    bt.plot_comparison(DOCS_DIR / "after_update.svg")

if __name__ == "__main__":
    main()