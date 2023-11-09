Title: The Dynamics of SDE based MCMC
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
<!-- status: hidden -->
Tags: mcmc, differential equations
Slug: mcmc_dynamics
Summary: A look at the probability path of MCMC

In this post we'll be looking at the dynamics of MCMC following [Ma et al. 2015](https://arxiv.org/pdf/1506.04696.pdf) by looking at how to construct stationary distributions for MCMC using stochastic differential equations.

# MCMC and SGMCMC
Markov chain monte carlo (MCMC) is an algorithm to samples from a target probability density function $p^*(x)$.  Assume that we can evaluate $p^*(x)$ up to a normalizing constant, there are a variety of MCMC algorithms that can be used to sample from $p^*(x)$.  The one that we'll look at is stochastic gradient MCMC (SGMCMC).  These algorithms access the score function, $\nabla \log p^*(x)$, and use it to construct a stochastic differential equation (SDE) that has $p^*(x)$ as its stationary distribution.  The SDE is then discretized and run until it reaches a stationary distribution which will be constructed to be $p^*(x)$.  In this post, we'll go through how to come up with SGMCMC from first principals.

Consider the multivariate Ito SDE:
$$
\begin{align}
  dx_t = \mu(x_t,t) dt + \sigma(x_t,t) dW_t
\end{align}
$$
Our goal will be to figure out how to choose $\mu$ so that the stationary distribution is $p^*(x)$.  In order to do so, we first need to look at the marginal distribution of the SDE at any time $t$, $p_t(x)$.  This is given by the Fokker-Planck equation.  Let $D_{ij}
 = \sigma_{ik}\sigma_{jk}$.  Then the Fokker-Planck equation is:
$$
\begin{align}
  \frac{\partial p_t}{\partial t} = -\frac{\partial p_t \mu_i}{\partial x_i} + \frac{1}{2} \frac{\partial^2 p_t D_{ij}}{\partial x_i \partial x_j}
\end{align}
$$
It is also true that if $Q_{ij}(x,t)$ is a skew symmetric matrix $(Q=-Q^T)$, then $\frac{\partial^2 f Q_{ij}}{\partial x^i \partial x^j} = 0$ for any function $f$, so we also have that
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= -\frac{\partial p_t \mu_i}{\partial x_i} + \frac{1}{2} \frac{\partial^2 p_t D_{ij}}{\partial x_i \partial x_j}  + \frac{1}{2} \frac{\partial^2 p_t Q_{ij}}{\partial x_i \partial x_j} \\
  &= -\frac{\partial p_t \mu_i}{\partial x_i} + \frac{1}{2} \frac{\partial^2 p_t (D_{ij} + Q_{ij})}{\partial x_i \partial x_j} \\
  &= \frac{\partial p_t}{\partial x_i}(-\mu_i + \frac{1}{2} \frac{1}{p_t}\frac{\partial p_t(D_{ij} + Q_{ij})}{\partial x_j}) \\
  &= \frac{\partial p_t}{\partial x_i}(-\mu_i + \frac{1}{2}\left[\frac{\partial \log p_t}{\partial x_j}(D_{ij} + Q_{ij}) + \frac{\partial D_{ij} + Q_{ij}}{\partial x_j}\right]) \\
\end{align}
$$
Notice that this equation now resembles the continuity equation, $\frac{\partial p_t}{\partial t} + \frac{\partial p_tV_i}{\partial x_i} = 0$ where $V$ is the vector field that determines how particles evolve.  So in the case of the SDE, we have that:
$$
\begin{align}
  V_i = \mu_i - \frac{1}{2}\left[\frac{\partial \log p_t}{\partial x_j}(D_{ij} + Q_{ij}) + \frac{\partial D_{ij} + Q_{ij}}{\partial x_j}\right]
\end{align}
$$
The stationary distribution of the SDE is achieved when $V=0$ (which leaves $p_t$ constant) which will clearly be equal to our target when we set
$$
  \mu_i = \frac{1}{2}\left[\frac{\partial \log p^*}{\partial x_j}(D_{ij} + Q_{ij}) + \frac{\partial D_{ij} + Q_{ij}}{\partial x_j}\right]
$$
This is the "complete recipe" described in [Ma et al.](https://arxiv.org/pdf/1506.04696.pdf) for constructing SGMCMC algorithms.  The proof that this is complete (describes all MCMC algorithms) is given in the appendix of the paper and basically shows how to construct $Q$.  Now we can take a lookg at the dynamics of MCMC.

# MCMC dynamics
In the first part we saw that the SDE with the form
$$
\begin{align}
  dx_t &= \mu(x_t,t) dt + \sigma(x_t,t) dW_t
\end{align}
$$
where
$$
\begin{align}
  \mu_i &= \frac{1}{2}\left[\frac{\partial \log p^*}{\partial x_j}(D_{ij} + Q_{ij}) + \frac{\partial D_{ij} + Q_{ij}}{\partial x_j}\right]
\end{align}
$$
will have $p^*(x)$ as its stationary distribution and that the dynamics of the SDE are given by
$$
\begin{align}
  V_i &= \mu_i - \frac{1}{2}\left[\frac{\partial \log p_t}{\partial x_j}(D_{ij} + Q_{ij}) + \frac{\partial D_{ij} + Q_{ij}}{\partial x_j}\right] \\
  &= \frac{1}{2}(\frac{\partial \log p^*}{\partial x_j} - \frac{\partial \log p_t}{\partial x_j})(D_{ij} + Q_{ij}) \\
\end{align}
$$
where $p_t$ is the marginal distribution of the SDE at time $t$.