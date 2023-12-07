Title: Likelihood gradient dynamics
Date: 2023-11-25
Category: Blog
status: hidden
Slug: score-matching-cnf
Summary: The dynamics of the score function

# Motivation
From another post, we saw that the vector field
$$
\begin{align}
  V_t &= A(\nabla \log p^* - \nabla \log p_t), \text{ where }A \in \mathbb{R}^{d\times d}
\end{align}
$$
generates a flow whose probability path is the same as that of stochastic gradient MCMC.  So a sample $x_t$ that evolves under $V_t$ will slowly become more distributed like $p^*$.  However in order to do this in practice, we need to know the score function $\nabla \log p_t$ at every time.  In this post we'll show how to keep track of the score function dynamics.

# Gradient dynamics
First we need to know how the gradient function changes over time.  Recall that the gradient $\nabla_{x_t}$ depends on the time $t$.  Let $f_t$ be a time-dependent function.  Then
$$
\begin{align}
  \frac{d}{dt}\frac{\partial f_t}{\partial x_t^i} &= \frac{d}{dt}\frac{\partial x_0^j}{\partial x_t^i}\frac{\partial f_t}{\partial x_0^j} \\
  &= \left(\frac{d}{dt}\frac{\partial x_0^j}{\partial x_t^i}\right)\frac{\partial f_t}{\partial x_0^j} + \frac{\partial x_0^j}{\partial x_t^i}\left(\frac{d}{dt}\frac{\partial f_t}{\partial x_0^j}\right) \\
  &= \left( -\frac{\partial x_0^j}{\partial x_t^k} \frac{\partial V_t^k}{\partial x_t^i} \right)\frac{\partial f_t}{\partial x_0^j} + \frac{\partial x_0^j}{\partial x_t^i}\left(\frac{\partial}{\partial x_0^j}\frac{d f_t}{dt}\right) \\
  &= -\frac{\partial V_t^k}{\partial x_t^i}\frac{\partial f_t}{\partial x_t^k} + \frac{\partial}{\partial x_t^i}\frac{d f_t}{dt}
\end{align}
$$
In matrix form, we have
$$
\frac{d}{dt}\nabla f_t = -\nabla V_t^T\nabla f_t + \nabla\frac{d}{dt} f_t
$$

# Likelihood dynamics
Next lets see how the dynamics of derivatives of the likelihood function.  Also we'll take a look at what these values using $V_t$ from above with $A=I$.

### Likelihood
$$
\begin{align}
\frac{d\log p_t}{dt} &= -\text{Div}(V_t)
\end{align}
$$

### Score function
$$
\begin{align}
\frac{d\nabla \log p_t}{dt} &= -\nabla V_t^T\nabla \log p_t + \nabla \frac{d\log p_t}{dt}
\end{align}
$$

### Hessian
$$
\begin{align}
\frac{d\nabla^2 \log p_t}{dt} &= -\nabla V_t^T\nabla^2 \log p_t + \nabla \frac{d\nabla \log p_t}{dt} \\
&= -\nabla V_t^T\nabla^2 \log p_t + \nabla (-\nabla V_t^T\nabla \log p_t + \nabla \frac{d\log p_t}{dt}) \\
&= -\nabla V_t^T\nabla^2 \log p_t - \nabla^2 V_t^T\nabla \log p_t - \nabla^2 \log p_t \nabla V_t + \nabla^2 \frac{d\log p_t}{dt} \\
&= -\nabla V_t^T\nabla^2 \log p_t - \nabla^2 \log p_t \nabla V_t - \nabla^2 V_t^T\nabla \log p_t + \nabla^2 \frac{d\log p_t}{dt} \\
\end{align}
$$

## Plugging in values for $V_t$
$$
\begin{align}
\frac{d\log p_t}{dt} &= -\text{Div}(\nabla \log p^* - \nabla \log p_t)
\end{align}
$$

$$
\begin{align}
\frac{d\nabla \log p_t}{dt} &= -(\nabla^2 \log p^* - \nabla^2 \log p_t)^T\nabla \log p_t + \nabla \frac{d\log p_t}{dt} \\
&= (\nabla^2 \log p_t - \nabla^2 \log p^*)^T\nabla \log p_t + \nabla \frac{d\log p_t}{dt}
\end{align}
$$

$$
\begin{align}
\frac{d\nabla^2 \log p_t}{dt} &= -(\nabla^2 \log p^* - \nabla^2 \log p_t)^T\nabla^2 \log p_t - \nabla^2 \log p_t (\nabla^2 \log p^* - \nabla^2 \log p_t) - (\nabla^3 \log p^* - \nabla^3 \log p_t)^T\nabla \log p_t + \nabla^2 \frac{d\log p_t}{dt} \\
\end{align}
$$
