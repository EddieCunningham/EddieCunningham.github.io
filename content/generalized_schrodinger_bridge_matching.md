Title: Generalized Schrodinger bridge matching
Date: 2024-03-23
Modified: 2024-03-23
Category: Blog
status: hidden
Tags: SDE
Slug: gsbm
Summary: An overview of generalized schrodinger bridge matching


In this post we'll go over the generalized Schrodinger bridge matching problem as done in [this paper](https://arxiv.org/pdf/2310.02233.pdf).

Let $\mu$ and $\nu$ be probability distributions.  We want to find a parametric SDE that transports samples from $\mu$ to $\nu$ in a way that minimizes some cost.  For example, in generative modeling we pick $\mu$ to be a prior distribution like a Gaussian and $\nu$ to be our data's distribution.  We can impose a cost on the SDE that will transport samples from $\mu$ to $\nu$ in an efficient way, i.e., uses as few neural network evaluations as possible.


# Problem setup
We will consider SDEs of the following form:
$$
\begin{align}
  dx_t = u_t(x_t)dt + \sigma_t dW_t
\end{align}
$$
where $u_t$ is the drift and $\sigma_t$ is the diffusion coefficient and does not depend on $x_t$.  The distribution of samples that are simulated by this SDE is given by the Fokker-Planck equation:
$$
\begin{align}
  \partial_t \rho_t + \nabla \cdot (\rho_t u_t) = \frac{1}{2}\sigma_t^2 \Delta \rho_t
\end{align}
$$
where $\rho_t$ is the probability density of the samples at time $t$.

We will want to learn $u_t$ that minimizes the following problem:
$$
\begin{align}
  \inf_{\rho_t,u_t}\int_0^1 \int \rho_t(x_t)\left[\frac{1}{2}\|u_t(x_t)\|^2 + V_t(x_t)\right]dx_t dt \\
  \text{s.t.} \quad \partial_t \rho_t + \nabla \cdot (\rho_t u_t) = \frac{1}{2}\sigma_t^2 \Delta \rho_t, \quad \rho_0 = \mu, \rho_1 = \nu
\end{align}
$$
where $V_t(x_t)$ is some potential energy function.  For example, $V_t(x_t)$ could represent a physical obstruction that the particles must avoid.  The optimization over $\rho_t$ and $u_t$ is difficult in general and typically requires introducing Lagrange multipliers to solve, however we can simplify the problem considerably by assuming that $\rho_t$ is a conditional distribution, conditioned on the initial and final distributions.

### Conditional SDE
The key insight in the paper is to consider a conditional SDE that is conditioned on the initial and final distributions by writing
$$
\begin{align}
  \rho_t(x_t) = \int \int \rho_{0,1}(x_0,x_1) \rho_{t|0,1}(x_t|x_0,x_1)dx_0dx_1
\end{align}
$$
where $\rho_{0,1}$ is some joint distribution of the initial and final states and $\rho_{t|0,1}(x_t|x_0,x_1)$ is the conditional distribution of the state at time $t$ given the initial and final states.  In particular, $\rho_{t|0,1}(x_t|x_0,x_1)$ is the probability density function of a conditional SDE that starts at $x_0$ and ends at $x_1$:
$$
\begin{align}
  dx_t = u_t(x_t|x_0,x_1)dt + \sigma_t dW_t, \quad x_0 = x_0, x_1 = x_1
\end{align}
$$
This definition of $\rho_t(x_t)$ implies a specific form of the marginal drift $u_t(x_t)$:
$$
\begin{align}
  u_t(x_t) = \int \int \rho_{0,1|t}(x_0,x_1|x_t)u_t(x_t|x_0,x_1)dx_0dx_1 \\
  \text{where}\quad \rho_{0,1|t}(x_0,x_1|x_t) = \frac{\rho_{0,1}(x_0,x_1)\rho_{t|0,1}(x_t|x_0,x_1)}{\rho_t(x_t)}
\end{align}
$$
Note that this is identical to the marginal vector field definition in flow matching.  This relationship can be checked easily by checking that the Fokker-planck equation holds:
$$
\begin{align}
  \frac{\partial \rho_t(x_t)}{\partial t} &= \int\int \rho_{0,1}(x_0,x_1)\frac{\partial \rho_{t|0,1}(x_t|x_0,x_1)}{\partial t}dx_0dx_1 \\
  &= \int\int \rho_{0,1}(x_0,x_1)\left(-\nabla\cdot (\rho_{t|0,1}(x_t|x_0,x_1)u_t(x_t|x_0,x_1) + \frac{1}{2}\sigma_t^2 \Delta \rho_{t|0,1}(x_t|x_0,x_1)\right)dx_0dx_1 \\
  &= -\nabla\cdot \int\int \underbrace{\rho_{0,1}(x_0,x_1)\rho_{t|0,1}(x_t|x_0,x_1)}_{\rho_t(x_t)\rho_{0,1|t}(x_0,x_1|x_t)}u_t(x_t|x_0,x_1)dx_0dx_1 + \frac{1}{2}\sigma_t^2 \Delta \underbrace{\int\int \rho_{0,1}(x_0,x_1)\rho_{t|0,1}(x_t|x_0,x_1)dx_0dx_1}_{\rho_t(x_t)} \\
  &= -\nabla\cdot \rho_t(x_t)\underbrace{\int\int \rho_{0,1|t}(x_0,x_1|x_t)u_t(x_t|x_0,x_1)dx_0dx_1}_{=: u_t(x_t)} + \frac{1}{2}\sigma_t^2 \Delta \rho_t(x_t) \\
  &= -\nabla\cdot \rho_t(x_t)u_t(x_t) + \frac{1}{2}\sigma_t^2 \Delta \rho_t(x_t)
\end{align}
$$

With all of this in mind, we can return our attention to our optimization problem.

## Conditional optimization problem
Since $p_0$ and $p_1$ are fixed, we can rewrite the optimization problem using the conditional distribution:
$$
\begin{align}
  &\inf_{\rho_t,u_t}\int_0^1 \int \rho_t(x_t)\left[\frac{1}{2}\|u_t(x_t)\|^2 + V_t(x_t)\right]dx_t dt \\
  &= \inf_{\rho_t,u_t}\int_0^1 \int \left[\frac{1}{2}\langle \rho_t(x_t) u_t(x_t), u_t(x_t) \rangle + \rho_t(x_t)V_t(x_t)\right]dx_t dt \\
  &\text{restrict to vector fields that can be defined above}\\
  &= \inf_{\rho_{t|0,1},u_t}\int_0^1 \int\int p_{0,1}(x_0,x_1)\int \rho_{t|0,1}(x_t|x_0,x_1)\left[\frac{1}{2}\langle u_t(x_t|x_0,x_1), u_t(x_t) \rangle + V_t(x_t)\right]dx_t dx_0 dx_1 dt \\
  &= \inf_{u_t} \int\int p_{0,1}(x_0,x_1) \inf_{\rho_{t|0,1}}\int_0^1\int \rho_{t|0,1}(x_t|x_0,x_1)\left[\frac{1}{2}\langle u_t(x_t|x_0,x_1), u_t(x_t) \rangle + V_t(x_t)\right]dx_t dt dx_0 dx_1 \\
\end{align}
$$
Notice that we have not replaced the expression of $u_t(x_t)$ in the cost function with its conditional version.