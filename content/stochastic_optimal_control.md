Title: Hamilton Jacobi equations derivation
Date: 2024-03-13
Category: Blog
Slug: bird-flow
hidden: true
Summary: How to derive the Hamilton Jacobi equations for stochastic optimal control

# Problem statement
Suppose we are given a joint density $\mu_{0,1}$ that we can sample from and can factor as $\mu_{0,1} = \mu_0\mu_{1|0}$.  We want to learn an SDE of the form
$$
\begin{align}
  dx_t = u_{t|0} dt + \sigma_t dW_t
\end{align}
$$
where $\sigma_t$ is a scalar that does not depend on $x_t$, whose transition density $\rho_{t|0}$ from $t=0$ to $t=1$ is equal to $\mu_{1|0}$.  Furthermore, we want to find the optimal $u_{t|0}$ that minimizes the cost
$$
\begin{align}
  \int_0^1 \int \mu_0 \int \rho_{t|0} \left[\frac{1}{2}\|u_{t|0}\|^2 + I_t \right]dx_t dx_0 dt
\end{align}
$$
where $I_t$ is a cost over the position $x_t$ at time $t$.  In order to solve this problem, we can decouple the transition density $\rho_{t|0}$ with the SDE and treat as another function that we will optimize over.  However, will then need to incorporate the constraint that $\rho_{t|0}$ satisfies the Kolmogorov forward equation for the SDE.  This leads us to the problem that we will solve:
$$
\begin{align}
  &\inf_{\rho_{t|0},u_{t|0}}\int_0^1 \int \mu_0 \int \rho_{t|0} \left[\frac{1}{2}\|u_{t|0}\|^2 + I_t \right]dx_t dx_0 dt \\
  &\text{s.t. } \frac{\partial \rho_{t|0}}{\partial t} + \text{Div}(\rho_{t|0}u_t) = \frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0}), \quad \rho_{0|0} = \delta_{x_0}, \quad \rho_{1|0} = \mu_{1|0}
\end{align}
$$
The first thing we need to do is incorporate the constraints using lagrange multipliers.  We will introduce a lagrange multiplier $s_{t|0}$ for the Kolmogorov forward equation associated with each $x_0\sim \mu_0$.  The optimization problem then becomes:
$$
\begin{align}
  &\inf_{\rho_{t|0},u_{t|0}}\sup_{s_{t|0}}\int_0^1 \int \mu_0 \int \rho_{t|0} \left[\frac{1}{2}\|u_{t|0}\|^2 + I_t \right]dx_t dx_0 dt \\
  &+ \int_0^1 \int \mu_0 \int s_{t|0}\left(\frac{\partial \rho_{t|0}}{\partial t} + \text{Div}(\rho_{t|0}u_t) - \frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0})\right)dx_t dx_0 dt \\
  &\quad\text{s.t.}\quad \rho_{0|0} = \delta_{x_0}, \quad \rho_{1|0} = \mu_{1|0}
\end{align}
$$

### Optimal $u_{t|0}$
Next, we can analytically solve for the optimal $u_{t|0}$ by taking the functional derivative of the cost with respect to $u_{t|0}$ and setting it to $0$.  To do this, lets isolate the terms with $u_{t|0}$ and simplify:
$$
\begin{align}
  \mathcal{L}(u_{t|0}) &= \int_0^1 \int \mu_0 \int \rho_{t|0} \underbrace{\frac{1}{2}\|u_{t|0}\|^2}_{\langle\frac{1}{2}u_t,u_t\rangle} dx_t dx_0 dt + \int_0^1 \int \mu_0 \underbrace{\int s_{t|0} \text{Div}(\rho_{t|0}u_t) dx_t}_{-\int \rho_{t|0}\langle \nabla s_{t|0}, u_t\rangle} dx_0 dt \\
  &= \int_0^1 \int \mu_0 \int \rho_{t|0} \langle \frac{1}{2}u_{t|0} - \nabla s_{t|0}, u_{t|0}\rangle dx_t dx_0 dt
\end{align}
$$
Next, we can take a variation and set it to $0$ to find the optimal $u_{t|0}$:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}\mathcal{L}(u_{t|0} + \epsilon \eta) &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_0^1 \int \mu_0 \int \rho_{t|0} \langle \frac{1}{2}(u_{t|0} + \epsilon \eta) - \nabla s_{t|0}, (u_{t|0} + \epsilon \eta)\rangle dx_t dx_0 dt \\
  &= \int_0^1 \int \mu_0 \int \rho_{t|0}\left[ \langle \frac{1}{2}u_{t|0}, \eta\rangle + \langle \frac{1}{2}\eta, u_{t|0}\rangle - \langle \nabla s_{t|0}, \eta \rangle \right]dx_t dx_0 dt \\
  &= \int_0^1 \int \mu_0 \int \rho_{t|0}\langle u_{t|0} - \nabla s_{t|0}, \eta\rangle dx_t dx_0 dt \\
  \implies u_{t|0}^* &= \nabla s_{t|0}
\end{align}
$$
So the optimal $u_{t|0}$ is the gradient of the lagrange multiplier $s_{t|0}$.  Plugging this back into the cost gives us:
$$
\mathcal{L}(u_{t|0}^*) = -\frac{1}{2}\int_0^1 \int \mu_0 \int \rho_{t|0}\|\nabla s_{t|0}\|^2 dx_t dx_0 dt
$$

We can plug this solution back into the original problem to get a dual version of the optimization problem:
$$
\begin{align}
  &\inf_{\rho_{t|0}}\sup_{s_{t|0}}\int_0^1 \int \mu_0 \int \rho_{t|0} \left[-\frac{1}{2}\|\nabla s_{t|0}\|^2 + I_t \right]dx_t dx_0 dt \\
  &+ \int_0^1 \int \mu_0 \int s_{t|0}\left(\frac{\partial \rho_{t|0}}{\partial t} - \frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0})\right)dx_t dx_0 dt \\
  &\quad\text{s.t.}\quad \rho_{0|0} = \delta_{x_0}, \quad \rho_{1|0} = \mu_{1|0}
\end{align}
$$

### Rewriting as an expectation
The next step is to simplify the second line of the equations above as an expectation:
$$
\begin{align}
  \int_0^1 \int s_{t|0}\left(\frac{\partial \rho_{t|0}}{\partial t} - \frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0})\right)dx_t dt &= \int \underbrace{\int_0^1 s_{t|0}\frac{\partial \rho_{t|0}}{\partial t}dt}_{\text{integration by parts}} dx_t - \int_0^1 \int s_{t|0}\frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0})dx_t dt \\
  &= \int \left[s_{1|0}\rho_{1|0} - s_{0|0}\rho_{0|0} - \int_0^1 \rho_{t|0}\frac{\partial s_{t|0}}{\partial t}dt\right]dx_t - \int_0^1 \frac{\sigma_t^2}{2} \int s_{t|0}\text{Div}(\nabla p_{t|0})dx_t dt \\
  &= \int \left[s_{1|0}\rho_{1|0} - s_{0|0}\rho_{0|0} - \int_0^1 \rho_{t|0}\frac{\partial s_{t|0}}{\partial t}dt\right]dx_t + \int_0^1 \frac{\sigma_t^2}{2} \int \langle \nabla s_{t|0}, \nabla p_{t|0}\rangle dx_t dt \\
  &= \int \left[s_{1|0}\rho_{1|0} - s_{0|0}\rho_{0|0} - \int_0^1 \rho_{t|0}\frac{\partial s_{t|0}}{\partial t}dt\right]dx_t - \int_0^1 \frac{\sigma_t^2}{2} \int p_{t|0} \text{Div}(\nabla s_{t|0}) dx_t dt \\
  &= \int \rho_{1|0}s_{1|0} dx_1 - \int \rho_{0|0}s_{0|0} dx_0 - \int_0^1 \int \rho_{t|0}\left(\frac{\partial s_{t|0}}{\partial t} + \frac{\sigma_t^2}{2} \text{Div}(\nabla s_{t|0}) \right)dx_t dt
\end{align}
$$

### Putting it all together
With this simplification, we can rewrite the optimization problem as:
$$
\begin{align}
  &\inf_{\rho_{t|0}}\sup_{s_{t|0}}\int_0^1 \int \mu_0 \int \rho_{t|0} \left[-\frac{1}{2}\|\nabla s_{t|0}\|^2 - \frac{\partial s_{t|0}}{\partial t} - \frac{\sigma_t^2}{2} \text{Div}(\nabla s_{t|0}) + I_t \right]dx_t dx_0 dt \\
  &+ \int \mu_0 \left(\int \rho_{1|0}s_{1|0} dx_1  - \int \rho_{0|0}s_{0|0} dx_0\right)dx_0 \quad\text{s.t.}\quad \rho_{0|0} = \delta_{x_0}, \quad \rho_{1|0} = \mu_{1|0} \\
  &= \inf_{\rho_{t|0}}\sup_{s_{t|0}}\int_0^1 \int \mu_0 \int \rho_{t|0} \left[-\frac{1}{2}\|\nabla s_{t|0}\|^2 - \frac{\partial s_{t|0}}{\partial t} - \frac{\sigma_t^2}{2} \text{Div}(\nabla s_{t|0}) + I_t \right]dx_t dx_0 dt + \int\int \mu_{0,1} s_{1|0}dx_1dx_0 - \int \mu_0 s_{0|0}dx_0
\end{align}
$$
We already know that the optimality condition for $s_{t|0}$ is the Kolmogorov forward equation (evaluated with the optimal drift $u_{t|0}^* = \nabla s_{t|0}$) because it was introduced as a Lagrange multiplier.  The last thing we need to know is the optimality condition for $\rho_{t|0}$  We can find this by taking the functional derivative of the cost with respect to $\rho_{t|0}$ and setting it to $0$, which gives us that the integrand of first term must be 0.  This gives us the Hamilton Jacobi equations:
$$
\begin{align}
  \frac{\partial \rho_{t|0}}{\partial t} + \text{Div}(\rho_{t|0}\nabla s_{t|0}) = \frac{\sigma_t^2}{2} \text{Div}(\nabla \rho_{t|0}) \\
  \frac{1}{2}\|\nabla s_{t|0}\|^2 + \frac{\partial s_{t|0}}{\partial t} + \frac{\sigma_t^2}{2} \text{Div}(\nabla s_{t|0}) = I_t
\end{align}
$$

When these equations are satisfied, the optimization problem is at a stationary point.

# Value function interpretation
It turns out that we can interpret the dual variables as the value function of the problem.  Lets define the value of the problem that starts at $t=0$ with $x_0$ as $\Phi_0(x_0)$:
$$
\begin{align}
  \Phi_0(x_0) &= \inf_{u_t}\int_0^1 \int \rho_{t|0} \left[\frac{1}{2}\|u_{t|0}\|^2 + I_t \right]dx_t dt \\
  &= \inf_{u_t}\int_0^1 \mathbb{E}_{t|0}\left [\frac{1}{2}\|u_{t|0}\|^2 + I_t \right]dt
\end{align}
$$
Bellman's principal of optimality tells us that the value function can be decomposed into the value of the problem at the next time step plus the cost of the current time step:
$$
\begin{align}
  \Phi_t(x_t) &= \inf_{u_{t|0}}\left[\mathbb{E}_{t+h|0,t}\left[\Phi_{t+h}(x_{t+h})\right] + \int_t^{t+h} \mathbb{E}_{t+h|0,t}\left [\frac{1}{2}\|u_{t|0}\|^2 + I_t \right] dt\right]
\end{align}
$$
where $h>0$.  Next, we can subtract both sides by $\Phi_t(x_t)$, divide by $h$ and take a limit as $h\to 0$ to simplify:
$$
\begin{align}
  0 &= \inf_{u_{t|0}}\lim_{h\to 0}\left[\frac{\mathbb{E}_{t+h|0,t}\left[\Phi_{t+h}(x_{t+h})\right] - \Phi_t(x_t)}{h} + \frac{1}{h}\int_t^{t+h} \mathbb{E}_{t+h|0,t}\left [\frac{1}{2}\|u_{t|0}\|^2 + I_t \right] dt\right] \\
  &= \inf_{u_{t|0}}\left[\mathcal{A}\Phi_t + \frac{1}{2}\|u_{t|0}\|^2 + I_t \right] \\
  &= \inf_{u_{t|0}}\left[\frac{\partial \Phi_t}{\partial t} + \langle u_{t|0},\nabla \Phi_t \rangle + \frac{\sigma_t^2}{2}\text{Div}(\nabla \Phi_t) + \frac{1}{2}\|u_{t|0}\|^2 + I_t \right]
\end{align}
$$