# Math Behind Ranking

## Colley Method

First, we are given $N$ routes. We can define vector $\underline{n} \in \mathbb{R}^N$ such that 
$$n_i = \text{number of recorded climbs of route } i$$
for $i, \dots, N$. We can also define $\underline{w}$ as the number of times each route is deemed harder than another route and $\underline{l}$ as the number of times the route is deemed easier than another route.

After having these terms defined, we will construct the Colley matrix $C \in \mathbb{R}^{N \times N}$.

$$
\begin{equation}
    C_{ii} = 2 + n_i
\end{equation}
$$
for $i = 1, \dots, N$.

$$
\begin{equation}
    C_{ij} = -(\text{number of trials between i and j})
\end{equation}
$$
for $i \not= j$.

$$
\begin{equation}
    b_{i} = 1 + \frac{ w_i - l_i}{2}
\end{equation}
$$
for $i = 1, \dots, N$.


After constructing matrix $C$ and $\underline{b}$, we can solve the following system to obtain ranking vector $\underline{r}$.
$$
\begin{equation}
    C \underline{r} = \underline{b}
\end{equation}
$$
