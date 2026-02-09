Title: Linear Stochastic Interpolation
Date: 2025-02-11
Category: Blog
status: hidden
Slug: linear-stochastic-interpolation
Summary: Notes on linear stochastic interpolation

# Linear stochastic interpolants
The goal of stochastic interpolants is to construct a stochastic process that has a given joint distribution at a given set of times.
Let $X_t$ be a stochastic process with transition distribution $\phi(x_{t+s}|x_t)$.  We can condition this process on potential functions at a given set of times $\mathcal{R} = \{t_1, \ldots, t_n\}$, which we denote by $\{\phi_k\}_{k=1}^n$, to obtain a new process $X_t$ whose joint distribution at times $\mathcal{T} \supset \mathcal{R}$ is given by
$$
\begin{align}
  p(X_\mathcal{T}) = \frac{1}{Z} \prod_{t_k \in \mathcal{T}} \phi(x_{t_k}|x_{t_{k-1}})\prod_{t_k \in \mathcal{R}} \phi_k(x_{t_k})
\end{align}
$$

Suppose that the potential functions are Gaussians, with natural parameters denoted by $\{\eta_k\}_{k=1}^n$.  Then the joint distribution can be written as
$$
\begin{align}
  p(X_\mathcal{T}) = \frac{1}{Z} \prod_{t_k \in \mathcal{T}} \phi(x_{t_k}|x_{t_{k-1}})\prod_{t_k \in \mathcal{R}} \mathcal{N}(x_{t_k}; \eta_k)
\end{align}
$$
where $\mathcal{N}(x; \eta)$ denotes the Gaussian distribution with natural parameters $\eta$, i.e. $\eta = (J, h)$ where $J = -\frac{1}{2}\Sigma^{-1}$ and $h = \Sigma^{-1} \mu$ and
$$
\begin{align}
  \mathcal{N}(x; \eta) \propto \exp\left\{x^\top J x + h^\top x\right\}
\end{align}
$$

## Transition distribution
The transition distribution of $X_t$, given the potential functions at times $\mathcal{R}$, is given by the conditional distribution $p(x_{t_k}|X_{t_{1:k-1}})$.  We can compute this distribution by performing message passing to integrate out the variables at times greater than $t$ from the joint distribution $p(X_\mathcal{T})$:
$$
\begin{align}
  p(x_{t_k}|X_{t_{1:k-1}}) &= p(x_{t_k}|x_{t_{k-1}}) \\
  &\propto \phi(x_{t_k}|x_{t_{k-1}}) \mathcal{N}(x_{t_k}; \eta_k + \eta^\beta_{k})
\end{align}
$$
where $\eta^\beta_{k}$ are the natural parameters of the backward messages.  If we use $x_k$ as shorthand for $x_{t_k}$ and $\eta_k$ as shorthand for $\eta_{t_k}$, then we can define these parameters recursively as the natural parameters of the backward messages:
$$
\begin{align}
    \mathcal{N}(x_{k};\eta^\beta_k) &= \int \phi(x_{k}|x_{k+1})\mathcal{N}(x_{k+1};\eta_{k+1} + \eta^\beta_{k+1}) dx_{k+1},\quad \eta^\beta_N = 0
\end{align}
$$
Note that the transition distribution is Markovian because it only depends on the previous time step.

## Stochastic interpolants
Stochastic interpolants are constructed by letting the natural parameters of the potential functions be the random variables $\eta_k = \eta_k(Y)$ where $Y\sim \mu(Y)$.  Doing this gives us a new distribution for $X_T$ given by
$$
\begin{align}
  p_\mu(X_\mathcal{T}) = \underset{Y \sim \mu(Y)}{\mathbb{E}}\left[ \frac{1}{Z(Y)} \prod_{t_k \in \mathcal{T}} \phi(x_{t_k}|x_{t_{k-1}}) \prod_{t_k \in \mathcal{R}} \mathcal{N}(x_{t_k}; \eta_k(Y)) \right]
\end{align}
$$

The transition distribution of $X_t$ is not autoregressive because the terms in $X_{t_{1:k-1}}$ are conditionally dependent on $Y$, furthermore it is not tractable.  To address this issue, we propose a mean field approximation of $p_\mu(x_{t_k}|X_{t_{1:k-1}})$.

## Constrained mean field approximation
We propose approximating $p_\mu(x_{t_k}|X_{t_{1:k-1}})$ using the solution to a mean field variational inference problem:
$$
\begin{align}
  q^*(x_{t_k} | X_{t_{1:k-1}}) &= \underset{q(x_{t_k} | X_{t_{1:k-1}})}{\mathrm{argmin}}\; \mathrm{KL}\left[q(x_{t_k} | X_{t_{1:k-1}}) p_\mu(Y|X_{t_{1:k-1}}) \| p_\mu(x_{t_k}, Y | X_{t_{1:k-1}})\right] \\
  &\propto \phi(x_{t_{k}}|x_{t_{k-1}})\mathcal{N}(x_{t_k}; [\eta_k + \eta^\beta_{k}](X_{t_{1:k-1}})),\quad \text{where }\eta(X_{t_{1:k-1}}) := \underset{Y \sim p_\mu(Y|X_{t_{1:k-1}})}{\mathbb{E}}\left[\eta(Y)\right]
\end{align}
$$

#### Proof
Recall that the mean field variational inference problem is to find the distributions $q(X)$ and $q(Y)$ that minimize the KL divergence between $q(X)q(Y)$ and $p(X,Y)$:
$$
\begin{align}
    q^*(X)q^*(Y) &= \argmin_{q(X),q(Y)} \mathrm{KL}(q(X)q(Y) | p(X,Y))
\end{align}
$$
where
$$
\begin{align}
    q^*(X) \propto \exp\{\mathbb{E}_{q(Y)}\left[\log p(X,Y)\right] \} \quad \text{and} \quad q^*(Y) \propto \exp\{\mathbb{E}_{q(X)}\left[\log p(X,Y)\right] \}
\end{align}
$$

The result follows directly by fixing $q^*(Y) = p_\mu(Y|X_{t_{1:k-1}})$
$$
\begin{align}
    q^*(x_{t_k} | X_{t_{1:k-1}}) &= \argmin_{q(x_{t_k} | X_{t_{1:k-1}})}\; \mathrm{KL}\left[q(x_{t_k} | X_{t_{1:k-1}}) p_\mu(Y|X_{t_{1:k-1}}) \| p_\mu(x_{t_k}, Y | X_{t_{1:k-1}})\right] \\
    &\propto \exp\left\{\underset{Y \sim p_\mu(Y|X_{t_{1:k-1}})}{\mathbb{E}}\left[\;\log p_\mu(x_{t_k}, Y | X_{t_{1:k-1}})\;\right] \right\} \propto \exp\left\{\underset{Y \sim p_\mu(Y|X_{t_{1:k-1}})}{\mathbb{E}}\left[\;\log p_\mu(x_{t_k}| Y, X_{t_{1:k-1}})\;\right] \right\} \\
    &\propto \exp\left\{\underset{Y \sim p_\mu(Y|X_{t_{1:k-1}})}{\mathbb{E}}\left[\;\log \phi(x_{t_k}|x_{t_{k-1}}) + \log \mathcal{N}(x_{t_k}; \eta_k(Y) + \eta^\beta_{k}(Y))\;\right] \right\} \\
    &\propto \exp\left\{\log \phi(x_{t_k}|x_{t_{k-1}}) + \log \mathcal{N}(x_{t_k}; \underset{Y \sim p_\mu(Y|X_{t_{1:k-1}})}{\mathbb{E}}\left[\;\eta_k(Y) + \eta^\beta_{k}(Y)\;\right]) \right\} \\
    &= \phi(x_{t_k}|x_{t_{k-1}})\mathcal{N}(x_{t_k}; \eta_k(X_{t_{1:k-1}}) + \eta^\beta_{k}(X_{t_{1:k-1}}))
\end{align}
$$
$\blacksquare$


We can then use the mean field approximation to construct an approximation of the forecasting distribution $p_\mu(X_\mathcal{T} | X_\mathcal{C})$:
$$
\begin{align}
  q^*(X_\mathcal{T} | X_\mathcal{C}) &= \prod_{t_k \in \mathcal{T}}q^*(x_{t_k}|X_{t_{1:k-1} \cup \mathcal{C}})
\end{align}
$$

# Fine partition autoregressive proof
Next, we will show that the finer the partition $\mathcal{T}$ is, the closer the mean field approximation $q^*(X_\mathcal{T} | X_\mathcal{C})$ is to the true distribution $p_\mu(X_\mathcal{T} | X_\mathcal{C})$.