Title: Adjoint method for ODEs
Date: 2025-07-18
Category: Blog
status: hidden
Slug: ode_adjoint
Summary: Derivation of the adjoint method for ODEs

# Motivation
Let $(\mathcal{M},g)$ be a Riemannian manifold and let $x_t$ be a curve on $\mathcal{M}$ that starts at $t=0$.  Furthermore, assume that the velocity of $x_t$ is given by the expression
$$
\begin{align}
  \dot{x}_t = u_t(x_t;\theta)
\end{align}
$$
where $u_t$ is a vector field with parameters $\theta$.  In applications such as optimal control, we are interested in seeing how a cost function changes as we change the control function $u_t$.  For example, consider the following cost function:
$$
\begin{align}
  J(x_t;u(\theta),\theta) = \int_t^1 L_s(x_s,u_s(\theta)) ds + \Phi(x_1;\theta), \quad \text{where} \quad \frac{dx_s}{ds} = u_s(x_s), \quad x_{s=t} = x_t
\end{align}
$$
where $L_t$ is a running cost function and $\Phi$ is a terminal cost function.  Note that although $x_s$, $u_s$ and $\Phi$ depend on $\theta$, we will not always explicitly write the dependence on $\theta$ for brevity.  Computing the derivative of $J$ with respect to $\theta$ is not straightforward because $x_t$ is a function of $\theta$.  The adjoint method is a technique that allows us to compute the gradient of $J$ with respect to $\theta$ by constructing a new value, called the adjoint.  This adjoint variable is introduced as an auxiliary variable and will ultimately be used to obtain a new expression for the cost that has no partial derivative terms that depend on $\theta$, and can be chosen so that the partial derivatives of $x_s$ with respect to $\theta$ will vanish.  We will define this adjoint function to satisfy a differential equation that can be solved back in time that will make the expression for the gradient very simple.  Additionally, we will be able to show that the adjoint is equal to the gradient of the original cost function with respect to the initial state.  We will derive both versions of the adjoint in this post.

# Derivative of the cost function with respect to the parameters
This derivation will only work if the running cost function $L_t$ is independent of the control function $u_t$.  To get this, we can note that the derivative of the cost function with respect to $\theta$ can be written as the sum of a term involving the derivative of $u$ with respect to $\theta$ and a term where $\theta$ is independent of $u$.  We can write this out as
$$
\begin{align}
  \frac{\partial J(x_t;u(\theta),\theta)}{\partial \theta} &= \int_t^1 \frac{\partial}{\partial \theta}L_s(x_s,u_s(\theta)) ds + \frac{\partial J(x_t;u,\theta)}{\partial \theta}
\end{align}
$$
where the second term has $u$ independent of $\theta$.  The first term is something that we can compute, so we now focus on the second term.   We can introduce an auxiliary function, $a_t$, to add a term that is equal to zero to the cost function.  Let $a(s)$ be the adjoint function $s \in [t,1]$.  Since $\frac{dx_s}{ds} = u_s(x_s)$, we have that
$$
\begin{align}
  J(x_t;u,\theta) = \int_t^1 L_s(x_s,u_s) ds + \Phi(x_1) + \int_t^1 \langle a_s, u_s - \frac{dx_s}{ds} \rangle ds, \quad \text{where }\quad x_{s=t} = x_t
\end{align}
$$
Using integration by parts, we have that
$$
\begin{align}
  \int_t^1 \langle a_s, \frac{dx_s}{ds}\rangle ds &= \langle a_1, x_1 \rangle - \langle a_t, x_t \rangle - \int_t^1 \langle \frac{d a_s}{ds}, x_s \rangle ds
\end{align}
$$
which gives us:
$$
\begin{align}
  J(x_t;u,\theta) = \int_t^1 L_s(x_s,u_s) ds + \Phi(x_1) - \langle a_1, x_1 \rangle + \langle a_t, x_t \rangle + \int_t^1 \langle \frac{d a_s}{ds}, x_s \rangle ds + \int_t^1 \langle a_s, u_s \rangle ds
\end{align}
$$
Notably, this expression does not contain any partial derivative terms involving $x_s$ or $u_s$, and so taking the derivative is now straightforward.  We can directly compute the derivative of the cost function with respect to $\theta$ and then group terms by the derivative terms with respect to $\theta$.  For clarity, we'll expand each term separately and then combine the result:
$$
\begin{align}
\frac{\partial}{\partial \theta}\int_t^1 L_s(x_s,u_s) ds &= \int_t^1 \langle \nabla_x L_s(x_s,u_s),\frac{\partial x_s}{\partial \theta} \rangle ds \\
\frac{\partial}{\partial \theta}\Phi(x_1) &= \frac{\partial \Phi(x_1)}{\partial \theta} + \langle \nabla \Phi, \frac{\partial x_1}{\partial \theta} \rangle \\
\frac{\partial}{\partial \theta} -\langle a_1, x_1 \rangle &= - \langle a_1, \frac{\partial x_1}{\partial \theta} \rangle \\
\frac{\partial}{\partial \theta} \langle a_t, x_t \rangle &= 0 \\
\frac{\partial}{\partial \theta} \int_t^1 \langle \frac{d a_s}{ds}, x_s \rangle ds &= \int_t^1 \langle \frac{d a_s}{ds}, \frac{\partial x_s}{\partial \theta} \rangle ds \\
\frac{\partial}{\partial \theta} \int_t^1 \langle a_s, u_s \rangle ds &= \int_t^1 \langle a_s, \nabla u_s \frac{\partial x_s}{\partial \theta} + \frac{\partial u_s}{\partial \theta} \rangle ds \\
\end{align}
$$
Putting it all together, we have that
$$
\begin{align}
  \frac{\partial J(x_t;u,\theta)}{\partial \theta} &= \int_t^1 \langle \nabla_x L_s(x_s,u_s) + \frac{d a_s}{ds} + \nabla u_s^T a_s,\frac{\partial x_s}{\partial \theta} \rangle + \langle a_s,\frac{\partial u_s}{\partial \theta} \rangle ds + \frac{\partial \Phi(x_1)}{\partial \theta} + \langle \nabla \Phi - a_1, \frac{\partial x_1}{\partial \theta} \rangle
\end{align}
$$


If we choose $a_t$ such that
$$
\begin{align}
  \frac{d a_s}{ds} = -\nabla_x L_s(x_s,u_s) - \nabla u_s^T a_s, \quad \text{and} \quad a_1 = \nabla \Phi(x_1)
\end{align}
$$
then all of the partial derivatives of $x_s$ with respect to $\theta$ will vanish, and we are left with the following expression for the gradient of the cost function with respect to $\theta$:
$$
\begin{align}
  \frac{\partial J(x_t;u,\theta)}{\partial \theta} = \int_t^1\langle a_s,\frac{\partial u_s}{\partial \theta} \rangle ds + \frac{\partial \Phi(x_1)}{\partial \theta}
\end{align}
$$

So the full expression for the gradient of the cost function with respect to $\theta$ is
$$
\begin{align}
  \frac{\partial J(x_t;u(\theta),\theta)}{\partial \theta} &= \int_t^1 \frac{\partial}{\partial \theta}L_s(x_s,u_s(\theta)) ds + \int_t^1\langle a_s,\frac{\partial u_s}{\partial \theta} \rangle ds + \frac{\partial \Phi(x_1)}{\partial \theta}
\end{align}
$$

# Derivative of the cost function with respect to the state
Let $a_{t}(x_t) = \nabla J[u_t](x_t)$ be the gradient of the cost function $J$ with respect to $x_t$.  We can compute the material derivative of $a_t$ in the direction of the velocity field, $\dot{x}_t$, using the limit definition of the material derivative:
$$
\begin{align}
  \frac{d a_t(x_t)}{dt} &= \lim_{\epsilon \to 0^+} \frac{a_{t+\epsilon}(x_{t+\epsilon}) - a_t(x_t)}{\epsilon}
\end{align}
$$
We can write $a_t(x_t)$ using the chain rule as follows:
$$
\begin{align}
  a_t(x_t) &= \frac{\partial J_t(x_t)}{\partial x_t} = \frac{\partial J_t(x_t)}{\partial x_{t+\epsilon}^k} \frac{\partial x_{t+\epsilon}^k}{\partial x_t}
\end{align}
$$
where $x_{t+\epsilon}^k$ is the $k$-th component of $x_{t+\epsilon}$.  Then, we can take the derivative of the Taylor expansion of $x_{t+\epsilon}$ around $x_t$ to get the following expression:
$$
\begin{align}
  \frac{\partial x_{t+\epsilon}}{\partial x_t} &= \frac{\partial}{\partial x_t} \left(x_t + \epsilon u_t(x_t) + O(\epsilon^2)\right) \\
  &= I + \epsilon \frac{\partial u_t(x_t)}{\partial x_t} + O(\epsilon^2)
\end{align}
$$
where $I$ is the identity matrix.  Plugging this back into the material derivative of $a_t$ gives:
$$
\begin{align}
  \frac{d a_t(x_t)}{dt} &= \lim_{\epsilon \to 0^+} \frac{1}{\epsilon} \left(a_{t+\epsilon}(x_{t+\epsilon}) - a_t(x_t)\right) \\
  &= \lim_{\epsilon \to 0^+} \frac{1}{\epsilon} \left(\frac{\partial J_{t+\epsilon}(x_{t+\epsilon})}{\partial x_{t+\epsilon}} - \frac{\partial J_t(x_t)}{\partial x_{t+\epsilon}}\left(I + \epsilon \frac{\partial u_t(x_t)}{\partial x_t} + O(\epsilon^2)\right)\right) \\
  &= \lim_{\epsilon \to 0^+} \frac{1}{\epsilon} \left(\frac{\partial J_{t+\epsilon}(x_{t+\epsilon})}{\partial x_{t+\epsilon}} - \frac{\partial J_t(x_t)}{\partial x_{t+\epsilon}}\right) - \lim_{\epsilon \to 0^+}\frac{\partial J_t(x_t)}{\partial x_{t+\epsilon}}\frac{\partial u_t(x_t)}{\partial x_t} + \lim_{\epsilon \to 0^+} O(\epsilon) \\
  &= \lim_{\epsilon \to 0^+} \frac{1}{\epsilon} \frac{\partial}{\partial x_{t+\epsilon}}\left(J_{t+\epsilon}(x_{t+\epsilon}) - J_t(x_t)\right) - a_t(x_t)\frac{\partial u_t(x_t)}{\partial x_t}
\end{align}
$$
To simplify this last expression, we can use the fact that $J_{t}$ decomposes as the sum of the running cost to time $t+\epsilon$ and the cost at time $t+\epsilon$:
$$
\begin{align}
  J_{t}(x_t) &= \int_t^{t+\epsilon} L_s(x_s) ds + J_{t+\epsilon}(x_{t+\epsilon}) \\
  &\approx \epsilon L_t(x_t) + J_{t+\epsilon}(x_{t+\epsilon}) + O(\epsilon^2)
\end{align}
$$
Plugging this back in gives our final expression for the material derivative of $a_t$:
$$
\begin{align}
  \frac{d a_t(x_t)}{dt} &= \lim_{\epsilon \to 0^+} \frac{1}{\epsilon} \frac{\partial}{\partial x_{t+\epsilon}}\left(-\epsilon L_t(x_t) + O(\epsilon^2)\right) - a_t(x_t)\frac{\partial u_t(x_t)}{\partial x_t} \\
  &= -\frac{\partial L_t(x_t)}{\partial x_{t}} - a_t(x_t)\frac{\partial u_t(x_t)}{\partial x_t}
\end{align}
$$
with $a_1(x_1) = \frac{\partial \Phi(x_1)}{\partial x_1}$.  Written more compactly, we have that
$$
\begin{align}
  \frac{d a_t}{dt} = -\nabla_x L_t - \nabla u_t^T a_t, \quad \text{and} \quad a_1 = \nabla \Phi
\end{align}
$$

We can see that this is the exact ODE governing the adjoint function $a_t$ that we derived in the previous section, which means that they are the same function.

# Summary
Given the cost function
$$
\begin{align}
  J(x_t;u(\theta),\theta) = \int_t^1 L_s(x_s,u_s(\theta)) ds + \Phi(x_1;\theta), \quad \text{where} \quad \frac{dx_s}{ds} = u_s(x_s), \quad x_{s=t} = x_t
\end{align}
$$
we showed that the gradient of the cost function with respect to the parameters is given by
$$
\begin{align}
  \frac{\partial J(x_t;u(\theta),\theta)}{\partial \theta} &= \int_t^1 \frac{\partial}{\partial \theta}L_s(x_s,u_s(\theta)) ds + \int_t^1\langle a_s,\frac{\partial u_s}{\partial \theta} \rangle ds + \frac{\partial \Phi(x_1)}{\partial \theta}
\end{align}
$$
where $a_t$ is the adjoint function that satisfies the ODE
$$
\begin{align}
  \frac{d a_t}{dt} = -\nabla_x L_t - \nabla u_t^T a_t, \quad \text{and} \quad a_1 = \nabla \Phi
\end{align}
$$
Furthermore, the adjoint is equal to the gradient of the cost function with respect to the state, when the vector field is independent of the parameters.
$$
\begin{align}
  a_t = \nabla J(x_t;u)(x_t)
\end{align}
$$
