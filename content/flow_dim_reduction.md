Title: Dimensionality reduction with flows
Date: 2024-05-06
Category: Blog
Slug: flow-dim-reduction
hidden: true
Summary: Dimensionality reduction with flows

# Dimensionality reduction with flows
Here we will see what happens when we use normalizing flows for dimensionality reduction.  Let $F: \mathcal{Z}=\mathbb{R}^n \to \mathcal{X}=\mathbb{R}^n$ be a diffeomorphism and let $p_z = \prod_i p_i$ be a prior over $\mathcal{Z}$.  We will perform dimensionality reduction by smoothly changing one of the components of the prior to be a dirac delta function.  This can be interpret as transporting samples from $F_\# p_z$ to the submanifold that is defined by setting the $i$'th latent variable to $0$.  We will measure how effective this dimensionality reduction is using something similar to the Wasserstein 2 distance.  Let $J_i = \frac{dF}{dz_i}$ be the Jacobian of $F$ with respect to the $i$'th component.  We will consider the value function:
$$
\begin{align}
  &\inf_{\rho_t,\phi_t} \int_0^1 \int \rho_t \frac{1}{2}\|V_t\|^2 dx_t dt \\
  &\text{where} \quad V_t = \phi_t J_i,\quad\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t V_t) = 0, \quad \text{and}\quad \rho_0 = F_\# p_z, \quad \rho_1 = F_\# p_z \delta_{z_i=0}
\end{align}
$$
We can solve for the optimality conditions by taking variations of $\rho_t$ and $\phi_t$ and setting them to $0$.  First, let $s_t$ be a lagrange multiplier.  Then
$$
\begin{align}
  &\inf_{\rho_t,\phi_t} \sup_{s_t}\int_0^1 \int \rho_t \frac{1}{2}\|V_t\|^2 dx_t dt + \int_0^1 \int s_t (\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t V_t))dx_t dt  \\
  &= \inf_{\rho_t,\phi_t} \sup_{s_t}\int_0^1 \int \rho_t \frac{1}{2}\|V_t\|^2 + s_t \text{Div}(\rho_t V_t) dx_t dt - \int_0^1 \int \frac{\partial s_t}{\partial t} \rho_t dx_t dt + \int \rho_1 s_1 - \rho_0 s_0 dx  \\
  &= \inf_{\rho_t,\phi_t} \sup_{s_t}\int_0^1 \int \rho_t (\frac{1}{2}\|V_t\|^2 - \langle \nabla s_t, V_t \rangle) dx_t dt - \int_0^1 \int \frac{\partial s_t}{\partial t} \rho_t dx_t dt + \int \rho_1 s_1 - \rho_0 s_0 dx
\end{align}
$$

## Optimal $\phi_t$
Next, isolate the terms that depend on $\phi_t$:
$$
\begin{align}
  \mathcal{L}(\phi_t) &= \int_0^1 \int \rho_t (\frac{1}{2}\|V_t\|^2 - \langle \nabla s_t, V_t \rangle) dx_t dt \\
  &= \int_0^1 \int \rho_t (\langle \phi_t J_i, \frac{1}{2}\phi_t J_i \rangle - \langle \nabla s_t, \phi_t J_i \rangle) dx_t dt \\
  &= \int_0^1 \int \rho_t \langle \frac{1}{2}\phi_t J_i - \nabla s_t, \phi_t J_i \rangle dx_t dt
\end{align}
$$
Now take a variation:
$$
\begin{align}
  \frac{d}{d \epsilon}|_{\epsilon = 0}\mathcal{L}(\phi_t + \epsilon \eta) &= \frac{d}{d \epsilon}|_{\epsilon = 0}\int_0^1 \int \rho_t \langle \frac{1}{2}(\phi_t + \epsilon \eta) J_i - \nabla s_t, (\phi_t + \epsilon \eta) J_i \rangle dx_t dt \\
  &= \int_0^1 \int \rho_t (\langle \frac{1}{2}\phi_t J_i - \nabla s_t, \eta J_i \rangle + \langle \frac{1}{2}\eta J_i, \phi_t J_i \rangle) dx_t dt \\
  &= \int_0^1 \int \rho_t \langle \phi_t J_i - \nabla s_t, \eta J_i \rangle dx_t dt \\
  &= \int_0^1 \int \rho_t \langle \phi_t J_i - \nabla s_t, J_i \rangle \eta dx_t dt \\
\end{align}
$$
This implies that at optimality, $\phi_t$ is the scalar where $\langle \phi_t J_i - \nabla s_t, J_i \rangle = 0$.  This is obtained at:
$$
\begin{align}
  \phi_t^* &= \frac{1}{\|J_i\|^2}\langle J_i, \nabla s_t \rangle
\end{align}
$$
We also see that the optimal $V_t$ is:
$$
\begin{align}
  V_t^* &= \phi_t^* J_i \\
  &= \frac{1}{\|J_i\|^2}\langle J_i, \nabla s_t \rangle J_i \\
  &= J_i^\parallel \nabla s_t
\end{align}
$$
We see that the optimal $V_t$ is the projected gradient of $s_t$ (which might be the covariant derivative of $s_t$ in the direction of $J_i$).  At optimality, the value of $\mathcal{L}(\phi_t)$ is:
$$
\begin{align}
  \mathcal{L}(\phi_t^*) &= \int_0^1 \int \rho_t \langle \frac{1}{2}\phi_t^* J_i - \nabla s_t, \phi_t^* J_i \rangle dx_t dt \\
  &= \int_0^1 \int \rho_t \langle \frac{1}{2}J_i^\parallel \nabla s_t - \nabla s_t, J_i^\parallel \nabla s_t \rangle dx_t dt \\
  &= -\int_0^1 \int \rho_t \frac{1}{2}\|J_i^\parallel \nabla s_t\|^2 dx_t dt
\end{align}
$$

## Updated value function
Now we can update the value function:
$$
\begin{align}
  &\inf_{\rho_t,\phi_t} \sup_{s_t}\int_0^1 \int \rho_t (\frac{1}{2}\|V_t\|^2 - \langle \nabla s_t, V_t \rangle) dx_t dt - \int_0^1 \int \frac{\partial s_t}{\partial t} \rho_t dx_t dt + \int \rho_1 (s_1 + \log\frac{\rho_1}{\rho^*}) + \int \rho_1 s_1 - \rho_0 s_0 dx \\
  &= \inf_{\rho_t}\sup_{s_t}\int_0^1 \int \rho_t (-\frac{1}{2}\|J_i^\parallel \nabla s_t\|^2 - \frac{\partial s_t}{\partial t})dx_t dt + \int \rho_1 (s_1 + \log\frac{\rho_1}{\rho^*}) + \int \rho_1 s_1 - \rho_0 s_0 dx
\end{align}
$$
We can see that the optimality conditions are:
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t V_t^*) = 0 \\
  \frac{\partial s_t}{\partial t} + \frac{1}{2}\|V_t^* \|^2 = 0 \\
  V_t^* = J_i^\parallel \nabla s_t
\end{align}
$$

The second equation lets us interpret the $s_t$ as the value function itself

## Acceleration
We can see how the acceleration of particles changes along this flow:
$$
\begin{align}
  \frac{dx_t^2}{dt^2} &= \frac{d}{dt}V_t^* \\
  &= \frac{d}{dt}J_i^\parallel \nabla s_t \\
  &= (\frac{d}{dt}J_i^\parallel) \nabla s_t + J_i^\parallel \frac{d}{dt}\nabla s_t \\
  &= (\underbrace{\frac{\partial}{\partial t}J_i^\parallel}_{0} - {\nabla J_i^\parallel}^T V_t^*) \nabla s_t + J_i^\parallel \frac{d}{dt}\nabla s_t \\
  &= -({\nabla J_i^\parallel}^T J_i^\parallel \nabla s_t) \nabla s_t + J_i^\parallel \nabla(\frac{\partial s_t}{\partial t} + \frac{1}{2}\|\nabla s_t\|^2) \text{ because of how gradient fields evolve} \\
\end{align}
$$
The second part almost looks like the term in the optimality conditions.  We can simplify a bit as follows:
$$
\begin{align}
  \frac{1}{2}\|\nabla s_t\|^2 &= \frac{1}{2}\langle \nabla s_t, \nabla s_t \rangle \\
  &= \frac{1}{2}\langle (J_i^\parallel + J_i^\perp)\nabla s_t, \nabla s_t \rangle \\
  &= \frac{1}{2}\langle J_i^\parallel \nabla s_t, \nabla s_t \rangle + \frac{1}{2}\langle J_i^\perp \nabla s_t, \nabla s_t \rangle \\
  &= \frac{1}{2}\|J_i^\parallel \nabla s_t\|^2 + \frac{1}{2}\|J_i^\perp \nabla s_t\|^2
\end{align}
$$
Plugging this back into the acceleration equation and substituting the optimality conditions yields:
$$
\begin{align}
  \frac{dx_t^2}{dt^2} &= -({\nabla J_i^\parallel}^T J_i^\parallel \nabla s_t) \nabla s_t + J_i^\parallel \nabla(\frac{\partial s_t}{\partial t} + \frac{1}{2}\|\nabla s_t\|^2) \\
  &= -({\nabla J_i^\parallel}^T J_i^\parallel \nabla s_t) \nabla s_t + J_i^\parallel \nabla(\frac{\partial s_t}{\partial t} + \frac{1}{2}\|J_i^\parallel \nabla s_t\|^2 + \frac{1}{2}\|J_i^\perp \nabla s_t\|^2) \\
  &= -({\nabla J_i^\parallel}^T J_i^\parallel \nabla s_t) \nabla s_t + \frac{1}{2}J_i^\parallel \nabla \|J_i^\perp \nabla s_t \|^2
\end{align}
$$
### Simplifying assumption
If we assume that $J_i$ points in a straight line, then we'll have that $\frac{d}{dt}J_i^\parallel = 0$ and so we can simplify the acceleration equation to:
$$
\begin{align}
  \frac{dx_t^2}{dt^2} &= \frac{1}{2}J_i^\parallel \nabla \|J_i^\perp \nabla s_t \|^2
\end{align}
$$

# Variation of $J$
Now lets see what happens when we vary the Jacobian.  First, we need to know how the projection matrix changes when we vary the Jacobian.  Let $J(\epsilon) = J + \epsilon N$ be a Jacobian that depends on $\epsilon$.  We can expand $J^\parallel(\epsilon)$:
$$
\begin{align}
  J(\epsilon)^\parallel &= J(\epsilon)(J(\epsilon)^TJ(\epsilon))^{-1}J(\epsilon)^T
\end{align}
$$
Next, we can expand the inverse term using the identity $(A + \epsilon B)^{-1} = A^{-1} - \epsilon A^{-1}BA^{-1} + O(\epsilon^2)$:
$$
\begin{align}
  (J(\epsilon)^TJ(\epsilon))^{-1} &= (J^TJ + \epsilon J^TB + \epsilon N^TJ + \epsilon^2 N^TN)^{-1} \\
  &= (J^TJ + \epsilon (J^TN + N^TJ))^{-1} + O(\epsilon^2) \\
  &= (J^TJ)^{-1} - \epsilon (J^TJ)^{-1}(J^TN + N^TJ)(J^TJ)^{-1} + O(\epsilon^2) \\
\end{align}
$$

Now we can plug this back into the expression for $J^\parallel(\epsilon)$:
$$
\begin{align}
  J(\epsilon)^\parallel &= J(\epsilon)(J(\epsilon)^TJ(\epsilon))^{-1}J(\epsilon)^T \\
  &= (J + \epsilon N)((J^TJ)^{-1} - \epsilon (J^TJ)^{-1}(J^TN + N^TJ)(J^TJ)^{-1})(J + \epsilon N)^T + O(\epsilon^2) \\
  &= J^\parallel + \epsilon(NJ^+ + {J^+}^TN^T - {J^+}^T(J^TN + N^TJ)J^+) + O(\epsilon^2) \\
  &= J^\parallel + \epsilon(NJ^+ + {J^+}^TN^T - J^\parallel N J^+ - {J^+}^T N^T J^\parallel) + O(\epsilon^2) \\
  &= J^\parallel + \epsilon((I - J^\parallel)NJ^+ + {J^+}^TN^T(I - J^\parallel)) + O(\epsilon^2) \\
  &= J^\parallel + \epsilon(J^\perp NJ^+ + {J^+}^TN^TJ^\perp) + O(\epsilon^2)
\end{align}
$$
So we can compute the Gateaux derivative of $J^\parallel$ as:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}(J + \epsilon N)^\parallel &= \lim_{\epsilon \to 0}\frac{1}{\epsilon}((J + \epsilon N)^\parallel - J^\parallel) \\
  &= J^\perp NJ^+ + {J^+}^TN^TJ^\perp
\end{align}
$$

### Projected square norm
We need this derivative to compute the derivative of the projected square norm of the Jacobian.  The projected square norm is given by:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}\frac{1}{2}\|J(\epsilon)^\parallel \nabla s_t\|^2 &= \frac{1}{2}\frac{d}{d\epsilon}|_{\epsilon=0}\langle J(\epsilon)^\parallel \nabla s_t, \nabla s_t \rangle \\
  &= \frac{1}{2}\langle (J^\perp NJ^+ + {J^+}^TN^TJ^\perp) \nabla s_t, \nabla s_t \rangle \\
  &= \langle J^\perp NJ^+ \nabla s_t, \nabla s_t \rangle \\
  &= \langle NJ^+ \nabla s_t, J^\perp \nabla s_t \rangle \\
  &= \mathrm{tr}\left(NJ^+ \nabla s_t \nabla s_t^T J^\perp \right)
\end{align}
$$

We will also need the derivative of the log determinant of $J(\epsilon)^TJ(\epsilon)$, which is given by:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}\frac{1}{2}\log \det J(\epsilon)^TJ(\epsilon) &= \mathrm{tr}\left(J^{+}
\frac{dJ(\epsilon)}{d\epsilon}|_{\epsilon=0}\right) \\
  &= \mathrm{tr}\left(J^{+}N\right) \\
  &= \mathrm{tr}\left(NJ^{+}\right)
\end{align}
$$

# Variation of the value function
Now, lets vary $J$ with a fixed $s_t$ and see what conditions are needed for it to be $0$:
$$
\begin{align}
  &\frac{d}{d\epsilon}|_{\epsilon=0}\mathcal{L}(J_i(\epsilon), s_t) \\
  &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_0^1 \int \rho_t(\epsilon) (-\frac{1}{2}\|J_i(\epsilon)^\parallel \nabla {s_t}\|^2 - \frac{\partial {s_t}}{\partial t})dx_t dt + \int \rho_1(\epsilon) s_1 - \rho_0 s_0 dx \\
  &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_0^1 \int \rho_t(\epsilon) (-\frac{1}{2}\|J_i(\epsilon)^\parallel \nabla {s_t}\|^2 - \frac{\partial {s_t}}{\partial t})dx_t dt + \int \pi_1 s_1 dx \\
  &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_0^1 \int \pi_t (-\frac{1}{2}\|J_i(\epsilon)^\parallel \nabla {s_t}\|^2 - \frac{\partial {s_t}}{\partial t})dx_t dt \\
  &= \int \mathrm{tr}\left(-N_iJ_i^+ \left[\int_0^1 \pi_t \nabla {s_t} \nabla {s_t}^T dt \right]J_i^\perp \right)dx
\end{align}
$$