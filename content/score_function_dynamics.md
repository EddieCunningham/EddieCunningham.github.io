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

# Jacobian dynamics
$$
\begin{align}
    \frac{dJ(t)}{dt} = \lim_{\epsilon \to 0}\frac{J(t+\epsilon) - J(t)}{\epsilon}
\end{align}
$$
Also,
$$
\begin{align}
    J(t+\epsilon) &= \frac{dx(t+\epsilon)}{dx(0)} \\
                  &= \frac{dx(t+\epsilon)}{dx(t)}\underbrace{\frac{dx(t)}{dx(0)}}_{J(t)}
\end{align}
$$
and
$$
\begin{align}
    \frac{dx(t+\epsilon)}{dx(t)} &= \frac{d}{dx(t)}(x(t) + \int_{\epsilon}^{t+\epsilon}u_\tau(x(\tau))d\tau) \\
    &= \frac{d}{dx(t)}(x(t) + \epsilon u_t(x(t)) + O(\epsilon^2)) \\
    &= I + \epsilon \underbrace{\frac{du_t(x(t))}{dx(t)}}_{\Phi(t)} + O(\epsilon^2) \\
    &= I + \epsilon \Phi(t) + O(\epsilon^2)
\end{align}
$$
so we can continue:
$$
\begin{align}
    \frac{dJ(t)}{dt} &= \lim_{\epsilon \to 0}\frac{J(t+\epsilon) - J(t)}{\epsilon} \\
    &= \lim_{\epsilon \to 0}\frac{(I + \epsilon \Phi(t) + O(\epsilon^2))J(t) - J(t)}{\epsilon} \\
    &= \Phi(t) J(t)
\end{align}
$$
So our final result is:
$$
\begin{align}
    \frac{dJ(t)}{dt} = \Phi(t) J(t)
\end{align}
$$
We can also look at the inverse matrix, $G(t) = J(t)^{-1}$:
$$
\begin{align}
    \frac{dG(t)}{dt} &= \frac{d}{dt}J(t)^{-1} \\
    &= -J(t)^{-1}\frac{dJ(t)}{dt}J(t)^{-1} \\
    &= -G(t)\Phi(t)
\end{align}
$$

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

We can simplify this expression further by expanding the last term:
$$
\begin{align}
  \frac{d}{dt}f_t &= \frac{\partial f_t}{\partial t} + \frac{\partial f_t}{\partial x_t^i}V_t^i
\end{align}
$$
and so the gradient is
$$
\begin{align}
  \frac{\partial}{\partial x_t^k} \frac{d}{dt} f_t &=  \frac{\partial}{\partial x_t^k} \frac{\partial f_t}{\partial t}+ \frac{\partial^2 f_t}{\partial x_t^i \partial x_t^k}V_t^i + \frac{\partial V_t^i}{\partial x_t^k}\frac{\partial f_t}{\partial x_t^i}
\end{align}
$$
We can plug this back into the original equation and see that the $\frac{\partial V_t^i}{\partial x_t^k}\frac{\partial f_t}{\partial x_t^i}$ terms cancel, so we are left with:
$$
\begin{align}
    \frac{d}{dt}\frac{\partial f_t}{\partial x_t^i} &= \frac{\partial}{\partial x_t^k} \frac{\partial f_t}{\partial t}+ \frac{\partial^2 f_t}{\partial x_t^i \partial x_t^k}V_t^i
\end{align}
$$
which in matrix form is
$$
\begin{align}
  \frac{d}{dt}\nabla f_t &= \nabla\frac{\partial f_t}{\partial t} + \nabla^2 f_t V_t
\end{align}
$$
## Acceleration under gradient flow
In the special case that $V_t = \nabla f_t$, we can simplify the expression even more:
$$
\begin{align}
  \frac{d}{dt}\nabla f_t &= \nabla\frac{\partial f_t}{\partial t} + \nabla^2 f_t \nabla f_t \\
  &= \nabla\frac{\partial f_t}{\partial t} + \nabla(\frac{1}{2}\|\nabla f_t\|^2) \\
  &= \nabla\left(\frac{\partial f_t}{\partial t} + \frac{1}{2}\|\nabla f_t\|^2\right)
\end{align}
$$
So the acceleration is also a gradient flow.

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
