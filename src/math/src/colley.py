import numpy as np

def get_colley_matrix(route_comparisons: np.array) -> np.array:
    """
    # Get Colley Matrix

    ## Input
    Given a matrix of dimensions MxN where M is the number of route comparisons and N is the number of routes.

    Each row of the matrix contains -1s, 0s, and 1s, where -1 indicates that the route in that column lost the comparison, 0 indicates the route not compared, and 1 indicates a win.

    ## Output
    The function returns the Colley matrix, which is an NxN SPD matrix used in the Colley Method for ranking
    """
    N = route_comparisons.shape[1]
    C = np.zeros((N, N))
    for i in range(N):
        C[i, i] = 2 + route_comparisons[:, i].sum()
        for j in range(i + 1, N):
            C[i, j] = -route_comparisons[:, i].sum() * route_comparisons[:, j].sum() / (route_comparisons[:, i].sum() + route_comparisons[:, j].sum())
            C[j, i] = C[i, j]

    return C