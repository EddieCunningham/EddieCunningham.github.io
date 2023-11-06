Title: Equations for SDEs
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
status: hidden
Tags: SDE
Slug: SDE-equations
Summary: Some equations for SDEs

# Ito formula
Let $x(t)$ be an Ito process and consider a scalar function $\phi(x(t))$.  Then the Ito differential of $\phi$ is given by:
$$
\begin{align}
  d\phi &= \frac{\partial \phi}{\partial x_i}dx_i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_i \partial x_j}dx_i dx_j
\end{align}
$$
where mixed differentials are combined according to
$$
\begin{align}
    d\beta dt &= 0 \\
    dt d\beta &= 0 \\
    d\beta d\beta^T &= Qdt
\end{align}
$$

We can go further with this expression by recalling that $dx_i = f_i dt + L_{ij}d\beta_j$.  We can compute $dx_i dx_j$ as
$$
\begin{align}
  dx_i dx_j &= (f_i dt + L_{ik}d\beta_k)(f_j dt + L_{jl}d\beta_l) \\
  &= f_i f_j \underbrace{dt^2}_{0?} + f_i L_{jl}\underbrace{dt d\beta_l}_{0} + f_j L_{ik}\underbrace{d\beta_k dt}_{0} + L_{ik}d\beta_k L_{jl}d\beta_l \\
  &= L_{ik}L_{jl}d\beta_k d\beta_l \\
  &= L_{ik}L_{jl}Q_{kl}dt \quad \text{(somehow?)}
\end{align}
$$
Plugging this into the Ito formula yields:
$$
\begin{align}
  d\phi &= \frac{\partial \phi}{\partial x_i}(f_i dt + L_{ij}d\beta_j) + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_i \partial x_j}L_{ik}L_{jl}Q_{kl}dt \\
\end{align}
$$
Because the above equation is shorthand for an integral, we can "divide" by $dt$ to get to simplify terms:
$$
\begin{align}
  \frac{d\phi}{dt} &= \frac{\partial \phi}{\partial x_i}f_i + L_{ij}\frac{d\beta_j}{dt} + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_i \partial x_j}L_{ik}L_{jl}Q_{kl}
\end{align}
$$
Finally, taking the expectation of both sides removes the stochastic term because $\mathbb{E}\left[\frac{d\beta_j}{dt}\right] = 0$:
$$
\begin{align}
  \frac{d\mathbb{E}\left[\phi\right]}{dt} &= \mathbb{E}\left[\frac{\partial \phi}{\partial x_i}f_i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_i \partial x_j}L_{ik}L_{jl}Q_{kl}\right]
\end{align}
$$

# Infinitesmal generator
The generalized infinitesmal generator of a stochastic process $x(t)$ for a function $\phi(x)$ is defined as
$$
\begin{align}
  \mathcal{A}\phi(x) = \lim_{s\to 0+}\frac{\mathbb{E}\left[\phi(x(t+s))\right] - \phi(x(t))}{s}
\end{align}
$$
for which the solution of the time dependent SDE
$$
\begin{align}
  dx = f(x,t)dt + L(x,t)d\beta
\end{align}
$$
is given as
$$
\begin{align}
  \mathcal{A}\phi = f_i\frac{\partial\phi}{\partial x_i} + \frac{1}{2}L_{iu}Q_{uv}L_{jv}\frac{\partial^2\phi}{\partial x_i \partial x_j}
\end{align}
$$
where $Q$ is the diffusion matrix for $\beta$.  Note the similarity between this and the expected value of the derivative of the Ito formula from before.  We can see that
$$
\begin{align}
  \frac{d\mathbb{E}\left[\phi\right]}{dt} &= \mathbb{E}\left[ \mathcal{A}\phi \right]
\end{align}
$$

## Adjoint infinitesmal generator
Let $\langle \phi, \theta \rangle := \int \phi(x) \varphi(x) dx$.  The adjoint of $\mathcal{A}$, denoted by $\mathcal{A}^*$, is defined as the operator such that $\langle \mathcal{A}\phi, \theta \rangle = \langle \phi, \mathcal{A}^*\theta \rangle$.  Lets derive $\mathcal{A}^\theta$:
$$
\begin{align}
  \langle \mathcal{A}\phi, \theta \rangle &= \int \mathcal{A}\phi(x) \theta(x) dx \\
  &= \int \left(f_i\frac{\partial \phi}{\partial x_i} + \frac{1}{2}L_{iu}Q_{uv}L_{jv}\frac{\partial^2 \phi}{\partial x_i \partial x_j}\right)\theta dx \\
  &= \int \frac{\partial \phi}{\partial x_i}(f_i\theta) dx + \frac{1}{2}\int \frac{\partial}{\partial x_i}\frac{\partial \phi}{\partial x_j}L_{iu}Q_{uv}L_{jv}\theta dx \\
  &= -\int \phi \frac{\partial}{\partial x_i}(f_i\theta) dx - \frac{1}{2}\int \frac{\partial \phi}{\partial x_j}\frac{\partial}{\partial x_i}(L_{iu}Q_{uv}L_{jv}\theta) dx \quad \text{ (integration by parts)}\\
  &= -\langle \phi, \frac{\partial f_i\theta}{\partial x_i} \rangle + \frac{1}{2}\int \phi \frac{\partial^2}{\partial x_i \partial x_j}(L_{iu}Q_{uv}L_{jv}\theta) dx \\
  &= -\langle \phi, \frac{\partial f_i\theta}{\partial x_i} \rangle + \langle \phi,\frac{1}{2} \frac{\partial^2}{\partial x_i \partial x_j}(L_{iu}Q_{uv}L_{jv}\theta) \rangle \\
  &= \langle \phi, -\frac{\partial f_i\theta}{\partial x_i} + \frac{1}{2} \frac{\partial^2}{\partial x_i \partial x_j}(L_{iu}Q_{uv}L_{jv}\theta) \rangle \\
  &:= \langle \phi, \mathcal{A}^*\theta \rangle
\end{align}
$$
So we have that
$$
\begin{align}
  \mathcal{A}^*\theta &= -\frac{\partial f_i\theta}{\partial x_i} + \frac{1}{2} \frac{\partial^2}{\partial x_i \partial x_j}(L_{iu}Q_{uv}L_{jv}\theta)
\end{align}
$$

# Fokker-Planck equation (Kolmogorov forward equation)

Next, lets look at how we can write expectations using the infinitesmal generator.
$$
\begin{align}
  \mathbb{E}\left[\phi(x(t)) \right] &= \int p(x,t)\phi(x(t))dx \\
  &= \langle p, \phi \rangle
\end{align}
$$

From earlier, we saw that $\frac{d\mathbb{E}\left[\phi\right]}{dt} = \mathbb{E}\left[ \mathcal{A}\phi \right]$.  So we can see that
$$
\begin{align}
  \langle \frac{\partial p}{\partial t}, \phi \rangle &= \langle p_t, \mathcal{A}\phi \rangle \\
  &= \langle \mathcal{A}^*p_t, \phi \rangle
\end{align}
$$
So we're left with the final result:
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= \mathcal{A}^*p_t \\
  &= -\frac{\partial f_ip_t}{\partial x_i} + \frac{1}{2} \frac{\partial^2}{\partial x_i \partial x_j}(L_{iu}Q_{uv}L_{jv}p_t)
\end{align}
$$

Note that $p_t(x)$ is technically a conditional distribution conditioned on a starting state $x_0$ at time $t=0$.

We can also see how the vector field looks like for SDEs by pulling out $\frac{\partial}{\partial x^i}$ (and letting $Q=I$ for simplicity):
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= -\frac{\partial}{\partial x_i}\left[f_ip_t - \frac{1}{2} \frac{\partial}{\partial x_j}(L_{ik}L_{jk}p_t) \right] \\
  &= -\frac{\partial}{\partial x_i}\left[p_t \left(f_i - \frac{1}{2} \frac{\partial}{\partial x_j}(L_{ik}L_{jk}\log p_t) \right) \right] \\
  &= -\frac{\partial}{\partial x_i}\left[p_t \left(f_i - \frac{1}{2} L_{ik}L_{jk}\frac{\partial \log p_t}{\partial x_j} \right) \right] \quad \text{if $L$ doesn't depend on $x$}
\end{align}
$$

# Kolmogorov backward equation
The Kolmogorov backward equation is given by
$$
\begin{align}
  -\frac{\partial p(x,t|x_0,t_0)}{\partial t_0} &= \mathcal{A}p(x,t|x_0,t_0) \\
  &= f_i\frac{\partial p(x,t|x_0,t_0)}{\partial {x_0}_i} + \frac{1}{2}L_{iu}Q_{uv}L_{jv}\frac{\partial^2 p(x,t|x_0,t_0)}{\partial {x_0}_i \partial {x_0}_j}
\end{align}
$$

*** HOW DO WE DERIVE THIS?

*** HOW CAN THE DRIFT AND DIFFUSION COEFFICIENTS BE WRITTEN AS EXPECTED VALUES?