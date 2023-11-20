Title: VI with CNFs
Date: 2023-11-17
Modified: 2023-11-17
Category: Blog
status: hidden
Slug: vi-cnf
Summary: How to do variational inference with continuous normalizing flows

# Motivation
Consider the task of minimizing the reverse KL divergence between a target distribution $p$ and a model distribution $q$ over a Riemannian manifold $(\mathcal{M},g)$.  If we have a probability path as the solution where $q_t(z)$ where $q_0$ is arbitrary and $q_1 = p$, then we could be interested in seeing how the reverse KL divergence between $q_t(z)$ and $p$ changes as $t$ changes.

Let $(q_t(z), V_t(z))$ be a probability path between $q_0$ and $q_1$ where $V_t(z)\in \mathfrak{X}(\mathcal{M})$ is the vector field that generates the flow of $q_t(z)$ and let $dz$ be the volume form on $\mathcal{M}$.  Then the time derivative of the reverse KL divergence is:
$$
\begin{align}
  \frac{d}{dt}\text{KL}\left[q_t(z_t)||p(z_t|x)\right] &= \int \frac{d}{dt}q_t(z_t)\log \frac{q_t(z_t)}{p(z_t|x)}dz_t \\
  &= \int \left((\frac{d q_t(z_t)}{dt})\log \frac{q_t(z_t)}{p(z_t|x)} + q_t(z_t)\frac{d \log q_t(z_t)}{dt}\right)dz_t \\
  &= \int \left(-\text{Div}(q_t(z_t) V_t(z_t)) \log \frac{q_t(z_t)}{p(z_t|x)} + \underbrace{\frac{d q(z_t)}{dt}}_{\text{$0$ in expectation}}\right)dz_t \\
  &= \int \langle \text{grad } \log \frac{q_t(z_t)}{p(z_t|x)} , q_t(z_t) V_t(z_t)\rangle dz \\
  &= \int q_t(z_t)\left( \langle \text{grad } \log q_t(z_t) , V_t(z_t)\rangle  - \langle \text{grad } \log p(z_t|x), V_t(z_t)\rangle  \right)dz_t \\
  &= \int \langle \text{grad } q_t(z_t) , V_t(z_t)\rangle  dz_t - \int q_t(z_t)\langle \text{grad } \log p(z_t|x), V_t(z_t)\rangle  dz_t \\
  &= -\int q_t(z_t) \text{Div}(V_t(z_t)) dz_t - \int q_t(z_t)\langle \text{grad } \log p(z_t|x), V_t(z_t)\rangle  dz_t \\
  &= -\mathbb{E}_{q_t(z_t)}\left[\langle \text{grad } \log p(z_t|x), V_t(z_t) \rangle  + \text{Div}(V_t(z_t))\right]
\end{align}
$$

So the full KL divergence is
$$
\begin{align}
  \text{KL}\left[q_1(z_1)||p(z_1|x)\right] &= \text{KL}\left[q_0(z_0)||p(z_0|x)\right] + \int_0^1 \frac{d}{dt}\text{KL}\left[q_t(z_t)||p(z_t|x)\right]dt \\
  &= \text{KL}\left[q_0(z_0)||p(z_0|x)\right] - \int_0^1 \mathbb{E}_{q_t(z_t)}\left[\langle \text{grad } \log p(z_t|x), V_t(z_t) \rangle  + \text{Div}(V_t(z_t))\right]dt
\end{align}
$$

# Comparison to ELBO maximization
Lets see how this compares to maximizing the ELBO
$$
\begin{align}
  -\log p(x) &= \int q_1(z_1)\log \frac{q_1(z_1)}{p(x,z_1)}dz_1 - \text{KL}\left[q_1(z_1)||p(z_1|x)\right] \\
  &\leq \int q_1(z_1)\log \frac{q_1(z_1)}{p(x,z_1)}dz_1 \\
  &= \int q_0(z_0)\log q_1(F_1(z_0))dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
  &= \int q_0(z_0)\left[\log q_0(z_0) + \int_0^1 \frac{d\log q_t(z_t)}{dt}dt\right]dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
  &= \int q_0(z_0)\left[\log q_0(z_0) - \int_0^1 \text{Div}(V_t(z_t))\right]dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
\end{align}
$$