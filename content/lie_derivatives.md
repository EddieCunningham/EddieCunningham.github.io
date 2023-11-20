Title: Lie derivatives
Date: 2023-11-10
Category: Blog
status: hidden
Tags: lie derivative
Slug: lie_derivatives
Summary: A practical introduction to Lie derivatives

Much of modern machine learning is based on ordinary differential equations.  For example, state of the art generative models generate samples "flowing" points along a vector field.  Continuous normalizing flows (and equivalently the probability flow associated with diffusion models) generate samples by solving the ODE:
$$
\begin{align}
  \frac{dx_t}{dt} &= V_t(x_t)
\end{align}
$$
where $V_t$ is a time dependent vector field (that we parametrize using a neural network).  Another way of thinking about this ODE is that it tells us how the space of points $x_t$ changes as we change the time $t$.
