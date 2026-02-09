Title: Deterministic optimal control
Date: 2025-03-21
Category: Blog
Slug: deterministic_optimal_control
hidden: true
Summary: A derivation of the Hamilton-Jacobi-Bellman equation for deterministic optimal control

# Deterministic optimal control
Suppose $(\mathcal{M},g)$ is a Riemannian manifold and let $x(t): \mathcal{M} \to \mathcal{M}$ be a time dependent flow that starts at time $t=0$ and whose infinitesimal generator is $b_t = \frac{dx_t}{dt} \in \mathfrak{X}(\mathcal{M})$.  This flow transports an initial point, $x_0$, along the curve $x_t$ whose velocity is given by $\dot{x}_t = b_t(x_t)$.  In optimal control, we are interested in controlling this curve to minimize a cost function.  To do this, we can consider a control function for the velocity of the curve, $u_t \in \mathfrak{X}(\mathcal{M})$, and a matrix $L_t$, so that the new, controlled velocity curve is
$$
\dot{x}_t = b_t(x_t) + L_t(x_t)u_t(x_t)
$$

Without loss of generality, we can assume that the flow starts at time $t=0$ and ends at time $t=1$, in which case we define the cost function that we aim to minimize as follows:
$$
\begin{align}
  J_0[u](x_0) = \int_{0}^{1} \frac{1}{2}\|u_t(x_t)\|^2 + f_t(x_t) dt + \Phi(x_1),\\
  \text{where }\dot{x}_t = b_t(x_t) + L_t(x_t)u_t(x_t)\; \text{ and }\; x_{t=0} = x_0
\end{align}
$$
The cost is comprised of a running cost function, $f_t$, a terminal cost function, $\Phi$, and term that penalizes the norm of the control function, $u_t$ (with respect to the Riemannian metric $g$).  Our goal is to find the optimal control function, $u_t^*$, that minimizes the cost function.  Additionally, we will find the value function, which is defined as the value of the cost function, evaluated with the optimal control.  The value function is denoted by $V_0^*(x_0)$ and is defined as follows:
$$
\begin{align}
  V_0^*(x_0) = \min_{u} J_0[u](x_0)
\end{align}
$$

Skipping to the end, we will find that the optimal control is related to the gradient of the value function, and that the value function is the solution to the following system of equations:
$$
\begin{align}
  u_t^*(x_t) &= -L_t(x_t)^\top \nabla V_t^*(x_t) \\
  \frac{d V_t^*(x_t)}{dt} &= -\frac{1}{2}\|L_t(x_t)^\top \nabla V_t^*(x_t)\|^2 - f_t(x_t) \\
  V^*_1(x_1) &= \Phi(x_1)
\end{align}
$$
These expressions (after expanding the material derivative of the value function) are called the Hamilton-Jacobi-Bellman equations.


## Solving for the optimal control
To solve for the optimal control, we will use the method of Lagrange multipliers.  The constraint that the control must satisfy is the continuity equation, which relates the marginal distribution of $x_t$ to $\dot{x}_t$:
$$
\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t \dot{x}_t) = 0
$$
In this expression, and in the expression that follow, we have dropped the dependence of all of the functions on $x_t$ in order to simplify the notation.  The continuity equation follows directly from a conservation law for probability mass - if we assert that the probability mass within a region of space does not change when the entire space is shifted according to $\dot{x}_t$, then we get the continuity equation.

Next, we will be able to directly solve for the optimal control by writing out the expected value of the cost functional, introducing the Lagrange multiplier, and then taking a variation and setting it to $0$.  Suppose that $\rho_0(x_0)$ is the initial distribution of $x_0$.  Then the expression for the optimal control is given by:
$$
\begin{align}
  u^* :=& \argmin_{u}\int_{\mathcal{M}} \rho_0 J_0[u] dV_g \quad \text{s.t. }\;\;\;\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t \dot{x}_t) = 0 \\
  =& \argmin_{u}\int_{\mathcal{M}} \rho_0 \int_{0}^{1} \frac{1}{2}\|u_t\|^2 + f_t dt + \Phi dV_g \\
  =& \argmin_{u}\int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(\frac{1}{2}\|u_t\|^2 + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 \Phi dV_g
\end{align}
$$
where $dV_g$ is the volume form of the manifold with respect to the Riemannian metric $g$.  Next, we can incorporate the constraint into the cost functional by introducing a Lagrange multiplier, $s_t: \mathcal{M} \to \mathbb{R}$, and then taking a variation and setting it to $0$.

## Solving for the optimal control
Let $s_t: \mathcal{M} \to \mathbb{R}$ be a Lagrange multiplier at each time and point in space that we use to enfore the continuity equation.  The Lagrangian for this problem depends now on both the control and the Lagrange multipler:
$$
\begin{align}
  u^* &= \max_{s}\argmin_{u}\int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(\frac{1}{2}\|u_t\|^2 + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 \Phi  dV_g \\
  &\quad\quad + \int_{0}^{1} \int_{\mathcal{M}} s_t\left(\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t \dot{x}_t)\right) dV_g dt
\end{align}
$$
We can begin by simplifying the constraint term and using integration by parts to simplify:
$$
\begin{align}
  &\int_{0}^{1} \int_{\mathcal{M}} s_t\left(\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t \dot{x}_t)\right) dV_g dt \\
  &= \int_{\mathcal{M}} \underbrace{\int_{0}^{1} s_t \frac{\partial \rho_t}{\partial t} dt}_{\text{integration by parts}} dV_g + \int_{0}^{1} \underbrace{\int_\mathcal{M} s_t\text{Div}(\rho_t \dot{x}_t) dV_g}_{\text{integration by parts}} dt \\
  &= \int_{\mathcal{M}} s_1 \rho_1 - s_0 \rho_0 dV_g - \int_{\mathcal{M}} \int_{0}^{1} \rho_t \frac{\partial s_t}{\partial t} dt - \int_{0}^{1} \int_{\mathcal{M}} \rho_t \langle \nabla s_t, \dot{x}_t \rangle dV_g dt \\
  &= \int_{\mathcal{M}} s_1 \rho_1 - s_0 \rho_0 dV_g - \int_{\mathcal{M}} \int_{0}^{1} \rho_t \frac{\partial s_t}{\partial t} dt - \int_{0}^{1} \int_{\mathcal{M}} \rho_t \langle \nabla s_t, b_t + L_t u_t \rangle dV_g dt
\end{align}
$$
Notice that only the last term of this expression depends on $u$ and that the first term in the cost functional depends on $u$.  Since all other terms are independent of $u$, they do not affect the solution to the optimal control.  Lets write out the parts of the cost functional and the Lagrange multiplier that depend on $u$:
$$
\begin{align}
  &\int_{0}^{1} \int_{\mathcal{M}} \rho_t \frac{1}{2}\|u_t(x_t)\|^2 - \rho_t \langle \nabla s_t, L_t u_t \rangle dV_g dt \\
  &=\int_{0}^{1} \int_{\mathcal{M}} \rho_t \langle \frac{1}{2}u_t - L_t^\top \nabla s_t, u_t \rangle dV_g dt
\end{align}
$$
Suppose $u$ depends on the scalar parameter $\theta$.  Clearly the state $x_t$ will then also depend on $\theta$, and so will the probability density function $\rho_t$.  We can take a derivative of this expression with respect to $\theta$ in order to identify the stationary conditions.  When we write in the dependence on $\theta$, we need to note that the probability density function also depends on $\theta$ because the pdf depends on $u$.
$$
\begin{align}
  \mathcal{L}(\theta) = \int_{0}^{1} \int_{\mathcal{M}} \rho_t(\theta) \langle \frac{1}{2}u_t(\theta) - L_t^\top \nabla s_t, u_t(\theta) \rangle dV_g dt
\end{align}
$$
The way derivatives of expectations work is that the derivative passes through the expectation and becomes a material derivative of the integrand with repsect to the variation direction, $\frac{dx_t(\theta)}{d\theta}$.  So we can write:
$$
\begin{align}
  \frac{\partial}{\partial\theta}\mathcal{L}(\theta) = \int_{0}^{1} \int_{\mathcal{M}} \rho_t(\theta) \frac{d}{d\theta}\langle \frac{1}{2}u_t(\theta) - L_t^\top \nabla s_t, u_t(\theta) \rangle dV_g dt
\end{align}
$$
To identifty the stationary conditions, we need to see for what $u$ the material derivative of the inner product is zero.
$$
\begin{align}
  \frac{d}{d\theta}\langle \frac{1}{2}u_t(\theta) - L_t^\top \nabla s_t, u_t(\theta) \rangle &= \langle \frac{1}{2}\frac{d u_t(\theta)}{d\theta}, u_t(\theta) \rangle + \langle \frac{1}{2}u_t(\theta) - L_t^\top \nabla s_t, \frac{d u_t(\theta)}{d\theta} \rangle \\
  &= \langle u_t(\theta) - L_t^\top \nabla s_t, \frac{du_t(\theta)}{d\theta} \rangle
\end{align}
$$
Since $\frac{du_t(\theta)}{d\theta}$ is arbitrary, we get that the optimal control is $u_t^*(\theta) = L_t^\top \nabla s_t$.  Plugging this back into the original expression that only depended on $u$, we get
$$
\begin{align}
\int_{0}^{1} \int_{\mathcal{M}} \rho_t \frac{1}{2}\|u^*_t(x_t)\|^2 - \rho_t \langle \nabla s_t, L_t u^*_t \rangle dV_g dt = -\int_{0}^{1} \int_{\mathcal{M}} \rho_t \frac{1}{2}\|L_t^\top \nabla s_t\|^2 dV_g dt
\end{align}
$$

## Solving for the Lagrange multiplier
Plugging the optimal control back into the Lagrangian, we get:
$$
\begin{align}
  &\max_{s}\int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(-\frac{1}{2}\|L_t^\top \nabla s_t\|^2 - \langle \nabla s_t, b_t \rangle + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 \Phi  dV_g + \int_{\mathcal{M}} s_1\rho_1 - s_0 \rho_0 dV_g - \int_{\mathcal{M}} \int_{0}^{1} \rho_t \frac{\partial s_t}{\partial t} dt \\
  &= \max_{s}\int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(-\frac{1}{2}\|L_t^\top \nabla s_t\|^2 - \frac{\partial s_t}{\partial t} - \langle \nabla s_t, b_t \rangle + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 (\Phi + s_1)  - \rho_0 s_0 dV_g
\end{align}
$$
To complete the derivation, we need to find the stationary conditions for $s$.  We can do this in the same way as before by assuming that $s$ depends on the scalar parameter $\phi$ and taking a derivative with respect to $\phi$.  Since this is again a conditional expectation, the derivative passes through the expectation and becomes the material derivative of the integrand with respect to the variation direction, $X_\phi = \frac{dx_t(\phi)}{d\phi}$.
First, we can see that the boundary terms do not simplify significantly:
$$
\begin{align}
  \frac{\partial}{\partial\phi}\int_{\mathcal{M}} \rho_1 (\Phi + s_1(\phi))  - \rho_0 s_0(\phi) dV_g &= \int_{\mathcal{M}} \rho_1 \frac{d}{d\phi}(\Phi + s_1(\phi))  - \rho_0 \frac{d}{d\phi}s_0(\phi) dV_g \\
  &= \int_{\mathcal{M}} \rho_1 \frac{\partial s_1(\phi)}{\partial \phi} - \rho_0 \frac{\partial s_0(\phi)}{\partial \phi} dV_g \nonumber \\ &\quad+ \int_{\mathcal{M}} \rho_1 \langle X_\phi, \nabla (\Phi + s_1(\phi)) \rangle - \underbrace{\rho_0 \langle X_\phi, \nabla s_0(\phi) \rangle}_{0} dV_g
\end{align}
$$
The last term is $0$ because the initial distribution, $\rho_0$ is fixed with respect to $\phi$, and so integrating it and using integration by parts gives $0$:
$$
\begin{align}
  \int_{\mathcal{M}} \rho_0 \langle X_\phi, \nabla s_0(\phi) \rangle dV_g &= -\int_{\mathcal{M}} \text{Div}(\rho_0 X_\phi) s_0(\phi)dV_g \\
  &= \int_{\mathcal{M}} \frac{\partial \rho_0}{\partial \phi} s_0(\phi)dV_g \\
  &= 0
\end{align}
$$

Let's take a look at the integrand of the first term and expand the definition of the material derivative:
$$
\begin{align}
  &\frac{d}{d\phi}\left(-\frac{1}{2}\|L_t^\top \nabla s_t(\phi)\|^2 - \frac{\partial s_t(\phi)}{\partial t} - \langle \nabla s_t(\phi), b_t \rangle + f_t\right) \\
  &= \underbrace{\frac{\partial}{\partial\phi}\left(-\frac{1}{2}\|L_t^\top \nabla s_t(\phi)\|^2 - \frac{\partial s_t(\phi)}{\partial t} - \langle \nabla s_t(\phi), b_t \rangle\right)}_{\text{simplify this term next}} + \underbrace{\langle X_\phi, \nabla\left(-\frac{1}{2}\|L_t^\top \nabla s_t(\phi)\|^2 - \frac{\partial s_t(\phi)}{\partial t} - \langle \nabla s_t(\phi), b_t \rangle + f_t \right)\rangle}_{\text{Not going to simplify further}}
\end{align}
$$
The first part of this expression ends up simplifying significantly when we integrate and apply integration by parts:
$$
\begin{align}
  &\int_{0}^{1} \int_{\mathcal{M}} \rho_t \frac{\partial}{\partial\phi}\left(-\frac{1}{2}\|L_t^\top \nabla s_t(\phi)\|^2 - \frac{\partial s_t(\phi)}{\partial t} - \langle \nabla s_t(\phi), b_t \rangle\right) dV_g dt \\
  &= \int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(-\langle \underbrace{b_t + L_t L_t^\top \nabla s_t}_{= \dot{x}_t^*}, \nabla \frac{\partial s_t(\phi)}{\partial \phi} \rangle  - \frac{\partial}{\partial t}\frac{\partial s_t(\phi)}{\partial \phi} \right) dV_g dt \\
  &= \int_{0}^{1} \int_{\mathcal{M}} \left(-\langle \rho_t \dot{x}_t^*, \nabla \frac{\partial s_t(\phi)}{\partial \phi} \rangle  - \rho_t \frac{\partial}{\partial t}\frac{\partial s_t(\phi)}{\partial \phi} \right) dV_g dt
\end{align}
$$
Next, we can apply integration by parts with respect to the space and time for the above two expressions.
$$
\begin{align}
  &= \int_{0}^{1}\int \underbrace{\text{Div}(\rho_t \dot{x}_t^*)}_{\text{continuity equation}}\frac{\partial s_t(\phi)}{\partial \phi}dV_g dt + \int_\mathcal{M} \left(-\rho_1 \frac{\partial s_1(\phi)}{\partial \phi} + \rho_0 \frac{\partial s_0(\phi)}{\partial \phi} + \int_{0}^{1} \frac{\partial \rho_t}{\partial t}\frac{\partial s_t(\phi)}{\partial \phi} dt \right) dV_g \\
  &= -\int_{0}^{1}\int \cancel{\frac{\partial \rho_t}{\partial t}\frac{\partial s_t(\phi)}{\partial \phi}}dV_g dt + \int_\mathcal{M} \left(-\rho_1 \frac{\partial s_1(\phi)}{\partial \phi} + \rho_0 \frac{\partial s_0(\phi)}{\partial \phi} + \int_{0}^{1} \cancel{\frac{\partial \rho_t}{\partial t}\frac{\partial s_t(\phi)}{\partial \phi} dt} \right) dV_g \\
  &= \int_\mathcal{M} -\rho_1 \frac{\partial s_1(\phi)}{\partial \phi} + \rho_0 \frac{\partial s_0(\phi)}{\partial \phi} dV_g
\end{align}
$$
We can see that we are left with the the derivative of the boundary terms, which cancel with the terms from the boundary terms in the first expression.  So we get the final expression for the variation of the Lagrangian:
$$
\begin{align}
  &\frac{\partial}{\partial\phi}\left(\int_{0}^{1} \int_{\mathcal{M}} \rho_t(\phi) \left(-\frac{1}{2}\|L_t^\top \nabla s_t(\phi)\|^2 - \frac{\partial s_t(\phi)}{\partial t} - \langle \nabla s_t(\phi), b_t \rangle + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 (\Phi + s_1(\phi))  - \rho_0 s_0(\phi) dV_g\right) \\
  &= \int_{0}^{1} \int_{\mathcal{M}} \rho_t \langle X_\phi, \nabla\left(-\frac{1}{2}\|L_t^\top \nabla s_t\|^2 - \frac{\partial s_t}{\partial t} - \langle \nabla s_t, b_t \rangle + f_t \right)\rangle dV_g dt + \int_{\mathcal{M}} \rho_1 \langle X_\phi, \nabla (\Phi + s_1) \rangle dV_g
\end{align}
$$
Since $X_\phi$ is arbitrary, we get the conditions on $s$ that make it a stationary point of the Lagrangian:
$$
\begin{align}
  -\frac{1}{2}\|L_t^\top \nabla s_t\|^2 - \frac{\partial s_t}{\partial t} - \langle \nabla s_t, b_t \rangle + f_t = 0 \\
  \Phi + s_1 = 0
\end{align}
$$

### Putting the pieces together
To the Hamilton-Jacobi-Bellman equation is expand out the expression for the material derivative of $s_t$ in the direction of the optimal velocity field, $\dot{x}_t^*$.  We can do this by using the chain rule and the fact that $\dot{x}_t^* = L_t^\top \nabla s_t$.
$$
\begin{align}
  \frac{d s_t}{dt} &= \frac{\partial s_t}{\partial t} + \langle \nabla s_t, \dot{x}_t^* \rangle \\
  &= \frac{\partial s_t}{\partial t} + \langle \nabla s_t, b_t + L_t L_t^\top \nabla s_t \rangle \\
  &= \frac{\partial s_t}{\partial t} + \langle \nabla s_t, b_t \rangle + \|L_t^\top \nabla s_t\|^2 \\
  &= \frac{1}{2}\|L_t^\top \nabla s_t\|^2 + f_t
\end{align}
$$
where the last line follows from the constraint that derived.  To summarize, we found that the solution to the problem:
$$
\begin{align}
u^* :=& \argmin_{u}\int_{0}^{1} \int_{\mathcal{M}} \rho_t \left(\frac{1}{2}\|u_t\|^2 + f_t\right) dt dV_g + \int_{\mathcal{M}} \rho_1 \Phi dV_g \nonumber \\ &\text{s.t. }\;\;\;\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t \dot{x}_t) = 0 \;\;\text{ and }\;\;\dot{x}_t = b_t + L_t u_t
\end{align}
$$
is given by $u^*_t(x_t) = L_t^\top \nabla s_t(x_t)$ where $s_t$ satisfies the following system of equations:
$$
\begin{align}
    \frac{d s_t(x_t)}{dt} &= \frac{1}{2}\|L_t(x_t)^\top \nabla s_t(x_t)\|^2 + f_t \\
    s_1(x_1) &= -\Phi(x_1)
\end{align}
$$

# Solving for the value function
We can plug the optimal control back into the cost functional to get the value function:
$$
\begin{align}
  V_0^*(x_0) &= J_0[L_t^\top \nabla s_t](x_0) \\
  &= \int_{0}^{1} \frac{1}{2}\|u_t(x_t)\|^2 + f_t(x_t) dt + \Phi(x_1) \\
  &= \int_{0}^{1} \frac{d s_t}{dt} dt - s_1(x_1) \\
  &= -s_0(x_0)
\end{align}
$$
Since the starting point $t=0$ was arbitrary, we get that the value function is the negative Lagrange multiplier.  This completes the derivation of the Hamilton-Jacobi-Bellman equations and we are left with the following system of equations:
$$
\begin{align}
    \frac{d V_t^*(x_t)}{dt} &= -\frac{1}{2}\|L_t(x_t)^\top \nabla V_t^*(x_t)\|^2 - f_t \\
    V_1^*(x_1) &= \Phi(x_1)
\end{align}
$$
where the optimal control is given by $u^*_t(x_t) = -L_t(x_t)^\top \nabla V_t^*(x_t)$.
