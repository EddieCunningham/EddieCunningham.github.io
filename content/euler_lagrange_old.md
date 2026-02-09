Title: Euler-Lagrange equations
Date: 2025-02-20
Category: Blog
Slug: euler_lagrange
hidden: true
Summary: Euler-Lagrange equations

### Lemma 1
$$
\begin{align}
  \frac{\partial}{\partial u} \int_{F_u(D)} \rho_u f_u dV_g = \int_{F_u(D)} \rho_u \frac{df_u}{du} dV_g, \quad \text{where } \rho_u = (F_u)_* \rho_0
\end{align}
$$
Proof:
$$
\begin{align}
  \frac{\partial}{\partial u} \int_{F_u(D)} \rho_u f_u dV_g &= \int_{D} \frac{\partial}{\partial u}F_u^* \left(\rho_u f_u dV_g \right) \\
  &= \int_{D} F_u^* \left[\underbrace{\mathcal{L}_{\Psi_u} \left(\rho_u f_u dV_g \right)}_{=d(\Psi_u \lrcorner \rho_u f_udV_g) + \cancel{\Psi_u \lrcorner d(\rho_u f_udV_g)}} + \frac{\partial}{\partial u} \left(\rho_u f_u\right) dV_g  \right] \\
  &= \int_{F_u(D)} \left[\text{Div}(\rho_u f_u\Psi_u) + \frac{\partial}{\partial u} \left(\rho_u f_u\right)\right] dV_g  \\
  &= \int_{F_u(D)} \left[f_u \text{Div}(\rho_u\Psi_u) + \langle \nabla f_u, \rho_u\Psi_u \rangle + \frac{\partial \rho_u}{\partial u} f_u + \rho_u \frac{\partial f_u}{\partial u}\right] dV_g \\
  &= \int_{F_u(D)} \left[f_u\underbrace{\left(\text{Div}(\rho_u\Psi_u)+ \frac{\partial \rho_u}{\partial u}\right)}_{=0\text{ by continuity equation}} + \rho_u\underbrace{\left(\langle \nabla f_u, \Psi_u \rangle  + \frac{\partial f_u}{\partial u}\right)}_{=\frac{df_u}{du}}\right] dV_g \\
  &= \int_{F_u(D)} \rho_u \frac{df_u}{du} dV_g
\end{align}
$$


### Lemma 2
$$
\begin{align}
  \frac{\partial}{\partial u} \int_1^0 L_t(x_{t,u}, \frac{dx_{t,u}}{dt})dt = \int_1^0 \langle \nabla_{x}L_t - \frac{d}{dt}\nabla_{\dot{x}}L_t, \Psi_u \rangle dt, \quad \text{where } \Psi_u = \frac{dx_{t,u}}{du}
\end{align}
$$
$$
\begin{align}
  \frac{\partial}{\partial u} \int_1^0 L_t(F_{t,u}, \frac{dF_{t,u}}{dt})dt = \int_1^0 \langle \nabla_{F}L_t - \frac{d}{dt}\nabla_{\dot{F}}L_t, \Psi_u \rangle dt, \quad \text{where } \Psi_u = \frac{dF_{t,u}}{du}
\end{align}
$$
Proof:
$$
\begin{align}
  \frac{\partial}{\partial u} \int_1^0 L_t(F_{t,u}, \frac{dF_{t,u}}{dt})dt &= \int_1^0 \frac{\partial}{\partial u} \left(L_t(F_{t,u}, \frac{dF_{t,u}}{dt})\right) dt \\
  &= \int_1^0 \langle \nabla_{F}L_t, \frac{dF_{t,u}}{du} \rangle + \underbrace{\langle \nabla_{\dot{F}}L_t, \frac{d^2F_{t,u}}{du dt} \rangle}_{\text{Integration by parts}} dt \\
  &= \int_1^0 \langle \nabla_{F}L_t, \Psi_u \rangle dt + \underbrace{\left.\langle \nabla_{\dot{F}}L_t, \Psi_u \rangle \right|_a^b}_{\Psi_u=0 \text{ at } t=a,b} - \int_1^0 \langle \frac{d}{dt}\nabla_{\dot{F}}L_t, \Psi_u \rangle dt \\
  &= \int_1^0 \langle \nabla_{F}L_t - \frac{d}{dt}\nabla_{\dot{F}}L_t, \Psi_u \rangle dt
\end{align}
$$


# Variation of Expected Lagrangian
$$
\begin{align}
  &\frac{\partial}{\partial u} \int_1^0 \int_{X_{t,u}} \rho_{t,u}(x_{t,u}) L_t(x_{t,u}, \dot{x}_{t,u}) dV_g dt \\
  &= \int_1^0 \int_{X_{t,u}} \rho_{t,u}(x_{t,u}) \langle \nabla_{x}L_t(x_{t,u},\dot{x}_{t,u}) - \frac{d}{dt}\nabla_{\dot{x}}L_t(x_{t,u},\dot{x}_{t,u}), \Psi_u(x_{t,u}) \rangle dV_g dt \\
  &\text{where }\;\;\dot{x}_{t,u} = \frac{dx_{t,u}}{dt},\quad\text{and }\;\; \Psi_u(x_{t,u}) = \frac{dx_{t,u}}{du}
\end{align}
$$


$$
\begin{align}
  \frac{\partial}{\partial u} \int_1^0 \int_{F_{t,u}(D)} \rho_{t,u} L_t(F_{t,u}, \frac{dF_{t,u}}{dt}) dV_g dt = \int_1^0 \int_{F_t(D)} \rho_{t,u} \langle \nabla_{F}L_t - \frac{d}{dt}\nabla_{\dot{F}}L_t, \Psi_u \rangle dV_g dt
\end{align}
$$
Proof:
$$
\begin{align}
  \frac{\partial}{\partial u} \int_1^0 \int_{F_{t,u}(D)} \rho_{t,u} L_t(F_{t,u}, \frac{dF_{t,u}}{dt}) dV_g dt &= \int_1^0 \int_{F_{t,u}(D)} \rho_{t,u} \frac{d}{d u} L_t(F_{t,u}, \frac{dF_{t,u}}{dt}) dV_g dt\quad \because \text{Lemma 1} \\
  &= \int_1^0 \int_{F_t(D)} \rho_{t,u} \langle \nabla_{F}L_t - \frac{d}{dt}\nabla_{\dot{F}}L_t, \Psi_u \rangle dV_g dt\quad \because \text{Lemma 2}
\end{align}
$$

# Variation of our Lagrangian
Let $L_t(z_{t,u},\dot{z}_{t,u}) = \frac{1}{2}\langle J^TJ\dot{z}_{t,u}, \dot{z}_{t,u} \rangle$.  We are interested in evaluting the right hand side of the following equation:
$$
\begin{align}
  &\frac{\partial}{\partial u} \int_1^0 \int_{Z_{t,u}} \nu_{t,u}(z_{t,u},\bar{z}) L_t(z_{t,u}, \dot{z}_{t,u}) dV dt \\
  &= \int_1^0 \int_{Z_{t,u}} \nu_{t,u}(z_{t,u},\bar{z}) \langle \nabla_{z}L_t(z_{t,u},\dot{z}_{t,u}) - \frac{d}{dt}\nabla_{\dot{z}}L_t(z_{t,u},\dot{z}_{t,u}), \Psi_{t,u}(z_{t,u}) \rangle dV dt \\
  &\text{where }\;\;\dot{z}_{t,u} = \frac{dz_{t,u}}{dt},\quad\text{and }\;\; \Psi_{t,u}(z_{t,u}) = \frac{dz_{t,u}}{du}
\end{align}
$$

Note that $L_t$ is half of the pullback metric from $\mathcal{X}$ evaluated on $\dot{z}_{t,u}$, $\dot{z}_{t,u}$.
$$
\begin{align}
  L_t(z_{t,u},\dot{z}_{t,u}) = \frac{1}{2}\|\dot{z}_{t,u}\|_{(H\circ \pi_z^{-1})^*\bar{g}}
\end{align}
$$
Where $\bar{g}$ is the Euclidean metric on $\mathcal{X}$.  We will denote the pullback metric on $\mathcal{Z}$ by $g$ and define it as $g = (H\circ \pi_z^{-1})^*\bar{g}$.

So we need to be able to evaluate $\nabla_{z}L_t(z_{t,u},\dot{z}_{t,u})$ and $\frac{d}{dt}\nabla_{\dot{z}}L_t(z_{t,u},\dot{z}_{t,u})$.  We will drop the dependence on $t$ and $u$ for brevity and we will reuse $g$ to denote the coordinates of the pullback metric.  Also let $\partial_k = \frac{\partial}{\partial z^k}$ for brevity.
$$
\begin{align}
  \partial_k L(z,\dot{z}) &= \partial_k \frac{1}{2}\left(g_{i,j}\dot{z}^i\dot{z}^j\right) \\
  &= \frac{1}{2}\partial_k g_{i,j}\dot{z}^i\dot{z}^j
\end{align}
$$

Next, we need to evaluate $\frac{d}{dt}\nabla_{\dot{z}}L(z,\dot{z})$.  We can do this by taking the gradient of $L$ with respect to $\dot{z}$ and then taking the time derivative.  Let $\dot{\partial}_k = \frac{\partial}{\partial \dot{z}^k}$ for brevity.
$$
\begin{align}
  \dot{\partial}_k L(z,\dot{z}) &= \dot{\partial}_k \frac{1}{2}\left(g_{i,j}\dot{z}^i\dot{z}^j\right) \\
  &= g_{k,i}\dot{z}^i
\end{align}
$$
And next
$$
\begin{align}
  \frac{d}{dt}\dot{\partial}_k L(z,\dot{z}) &= \frac{d}{dt} g_{k,i}\dot{z}^i \\
  &= \frac{d}{dt}(g_{k,i})\dot{z}^i + g_{k,i}\frac{d}{dt}\dot{z}^i \\
  &= \partial_j g_{k,i}\dot{z}^j\dot{z}^i + g_{k,i}\ddot{z}^i \\
  &= \frac{1}{2}(\partial_j g_{k,i}\dot{z}^j\dot{z}^i) + \frac{1}{2}(\underbrace{\partial_j g_{i,k}}_{\text{swapped metric indices}}\dot{z}^j\dot{z}^i) + g_{k,i}\ddot{z}^i \\
  &= \frac{1}{2}(\partial_j g_{k,i}\underbrace{\dot{z}^i\dot{z}^j}_{\text{swapped order}}) + \frac{1}{2}\underbrace{(\partial_i g_{j,k}\dot{z}^i\dot{z}^j)}_{\text{swapped $i$ and $j$}} + g_{k,i}\ddot{z}^i \\
  &= \frac{1}{2}(\partial_j g_{k,i} + \partial_i g_{j,k})\dot{z}^i\dot{z}^j + g_{k,i}\ddot{z}^i \\
\end{align}
$$

Putting it all together, we get
$$
\begin{align}
  \nabla_{z}L_t(z_{t,u},\dot{z}_{t,u}) - \frac{d}{dt}\nabla_{\dot{z}}L_t(z_{t,u},\dot{z}_{t,u}) &= \frac{1}{2}\partial_k g_{i,j}\dot{z}^i\dot{z}^j - \frac{1}{2}(\partial_j g_{k,i} + \partial_i g_{j,k})\dot{z}^i\dot{z}^j - g_{k,i}\ddot{z}^i \\
  &= \frac{1}{2}\left(\partial_k g_{i,j} - \partial_j g_{k,i} - \partial_i g_{j,k}\right)\dot{z}^i\dot{z}^j - g_{k,i}\ddot{z}^i
\end{align}
$$
We can expand the metric components in terms of $J$ to get the following expression:
$$
\begin{align}
  \partial_k g_{i,j} &= \partial_k (J^T J)_{i,j} \\
  &= \partial_k \left(J^m_i J^m_j \right) \\
  &= \partial_k J^m_i J^m_j + J^m_i \partial_k J^m_j
\end{align}
$$
Since $J^i_j = \frac{\partial x^i}{\partial z^j}$ and $\partial_k = \frac{\partial}{\partial z^k}$, we have a symmetry in the indices of $\partial_k J^i_j$: $\partial_k J^i_j = \partial_j J^i_k$.  So we can also write:
$$
\begin{align}
  \partial_k g_{i,j} = \partial_i J^m_k J^m_j + J^m_i \partial_j J^m_k
\end{align}
$$

Using these symmetries, we can simplify the expression for $\frac{1}{2}\left(\partial_k g_{i,j} - \partial_j g_{k,i} - \partial_i g_{j,k}\right)$ as follows:
$$
\begin{align}
  \frac{1}{2}\left(\partial_k g_{i,j} - \partial_j g_{k,i} - \partial_i g_{j,k}\right) &= \frac{1}{2}\left(\partial_i J^m_k J^m_j + J^m_i \partial_j J^m_k - \partial_j J^m_k J^m_i - J^m_j \partial_i J^m_k\right) \\
  &= \frac{1}{2}\left(\partial_i J^m_k J^m_j - \partial_j J^m_k J^m_i\right) \\
  &= \frac{1}{2}\left(\partial_i J^m_k J^m_j - \partial_j J^m_k J^m_i\right)
\end{align}
$$

$$
\begin{align}
  \frac{1}{2}\left(\partial_k g_{i,j} - \partial_j g_{k,i} - \partial_i g_{j,k}\right)
  &=\frac{1}{2}\left[\cancel{\partial_iJ^m_k\,J^m_j} + \cancel{J^m_i\,\partial_jJ^m_k}\right] \\
  &\quad -\frac{1}{2}\left[\cancel{\partial_jJ^m_k\,J^m_i} + J^m_k\,\partial_jJ^m_i \right] \\
  &\quad -\frac{1}{2}\left[\partial_iJ^m_j\,J^m_k + \cancel{J^m_j\,\partial_iJ^m_k}\right] \\
  &= -J^m_k\,\partial_iJ^m_j \\
  &= -\frac{dx^m}{dz^k}\frac{d^2x^m}{dz^i dz^j}
\end{align}
$$ safari



Plugging this back into our expression for the variation of the Lagrangian, we get:
$$
\begin{align}
  \nabla_{z}L_t(z_{t,u},\dot{z}_{t,u}) - \frac{d}{dt}\nabla_{\dot{z}}L_t(z_{t,u},\dot{z}_{t,u}) &= -J^m_k\,\partial_iJ^m_j\dot{z}^i\dot{z}^j - g_{k,i}\ddot{z}^i \\
  &= -J^m_k\left(\partial_iJ^m_j\dot{z}^i\dot{z}^j + J^m_i\ddot{z}^i\right)
\end{align}
$$
So we find our condition for $\dot{z}_{t,u}$ to be a minimizer of the Lagrangian:
$$
\begin{align}
  J^m_k\left(\partial_iJ^m_j\dot{z}^i\dot{z}^j + J^m_i\ddot{z}^i\right) = 0 \\
  \frac{dx^m}{dz^k}\left(\frac{d^2x^m}{dz^i dz^j}\dot{z}^i\dot{z}^j + \frac{dx^m}{dz^i}\ddot{z}^i\right) = 0
\end{align}
$$
If we multiply on the right by $(J^TJ)^{-1}$, we get:
$$
\begin{align}
  \ddot{z}^k + \Gamma_{ij}^k\dot{z}^i\dot{z}^j = 0
\end{align}
$$
where
$$
\begin{align}
  \Gamma_{ij}^k &= (J^+)^k_m \partial_i(J^m_j), \quad J^i_j = \frac{\partial x^i}{\partial z^j}
\end{align}
$$


# Properties of the energy functional
So now we can write the energy functional with uniquely defined transport maps as:
$$
\begin{align}
  E[H] &= \int_1^0 \int_{\bar{\mathcal{Z}}} \int_{Z_{t}} \nu_t \frac{1}{2}\|\dot{z}_t\|^2_{g_{H_{\bar{z}}}} dV dt, \quad \text{s.t. }\; \forall k, \;\; \sum_{i,j,m}\ddot{z}_t^k + \Gamma_{ij}^k\dot{z}_t^i\dot{z}_t^j = 0
\end{align}
$$
where $H_{\bar{z}} = H\circ \pi_{\bar{z}}$ is the map from $\mathcal{Z}$ to $\mathcal{X}$ and $g_{H_{\bar{z}}} = (H\circ \pi_{\bar{z}})^* \bar{g}$ is the pullback metric on $\mathcal{Z}$ and $\Gamma_{ij}^k$ is the Christoffel symbol of the pullback metric.  There are a couple of properties of this functional that we can prove.

### 1) Expression in data space
We can push this expression through $H_{\bar{z}}$ to get an expression in data space:
$$
\begin{align}
  E[H] &= \int_1^0 \int_{\bar{\mathcal{Z}}} \int_{Z_{t}} \nu_t \frac{1}{2}\|\dot{z}_t\|^2_{g_{H_{\bar{z}}}} dV dt, \quad \text{s.t. }\; \forall k, \;\; \sum_{i,j,m}\ddot{z}_t^k + \Gamma_{ij}^k\dot{z}_t^i\dot{z}_t^j = 0 \\
  &= \int_1^0 \int_{H(\bar{\mathcal{Z}},Z_{t})} (H_{\bar{z}}^{-1})^* \left[ \frac{1}{2}\|\dot{z}_t\|^2_{g_{H_{\bar{z}}}} \nu_t dV\right] dt, \quad \text{s.t. }\; (H_{\bar{z}})_*\left[\sum_{i,j,m}\ddot{z}_t + \Gamma_{ij}\dot{z}_t^i\dot{z}_t^j\right] = 0
\end{align}
$$
where the first term is the pullback of the energy functional under $H_{\bar{z}}$ and the second term is the pushforward of the constraint under $H_{\bar{z}}$.  Let's look at each term separately.

First, we can write the energy functional in data space as:
$$
\begin{align}
  \int_{H(\bar{\mathcal{Z}},Z_{t})} (H_{\bar{z}}^{-1})^* \left[ \frac{1}{2}\|\dot{z}_t\|^2_{g_{H_{\bar{z}}}} \nu_t dV\right] &= \int_{\mathcal{X}_t} \frac{1}{2} \|(H_{\bar{z}})_* \dot{z}_t\|^2_{(H_{\bar{z}}^{-1})^* g_{H_{\bar{z}}}} \rho_t dV
\end{align}
$$
The pullback of the metric is given by:
$$
\begin{align}
  (H_{\bar{z}}^{-1})^*_{(z_t)}g_{H_{\bar{z}}} &= (H_{\bar{z}}^{-1})^*_{(z_t)}(H\circ \pi_{\bar{z}})^*_{(x_t)} \bar{g} \\
  &= (H\circ \pi_{\bar{z}} \circ \pi \circ  H^{-1})^*_{(x_t)} \bar{g} \\
  &= (H_{\pi})^*_{(x_t)} \bar{g}
\end{align}
$$
where $H_{\pi}$ is the projection map from $\mathcal{X}$ to $\mathcal{X}$ onto $F(\bar{\mathcal{Z}})$.  To find the coordinates of the projection metric, we can evaluate it on a basis of $\mathcal{X}$:
$$
\begin{align}
  (H_{\pi})^*_{(x_t)} \bar{g} \left(\frac{\partial}{\partial x^i}, \frac{\partial}{\partial x^j}\right) &= \bar{g}_{(x_t)} \left(d(H_{\pi})_{(x_t)}\frac{\partial}{\partial x^i}, d(H_{\pi})_{(x_t)}\frac{\partial}{\partial x^j}\right) \\
  &= dx^u \otimes dx^v \left(d(H_{\pi})_{(x_t)}\frac{\partial}{\partial x^i}, d(H_{\pi})_{(x_t)}\frac{\partial}{\partial x^j}\right) \\
  &= (J^\parallel)^i_j
\end{align}
$$
The pushforward of $\dot{z}_t$ is given by:
$$
\begin{align}
  d(H_{\bar{z}})_{(z_t)} \dot{z}_t \Big|_{z_t} &= \dot{z}_t^k(z_t) d(H_{\bar{z}})_{(z_t)} \frac{\partial}{\partial z^k} \Big|_{z_t} \\
  &= \underbrace{(J\dot{z}_t)(z_t)^k}_{\dot{x}_t^k} \frac{\partial}{\partial x^i} \Big|_{x_t} \\
  &= \dot{x}_t^k \frac{\partial}{\partial x^i} \Big|_{x_t} \\
  &= \dot{x}_t
\end{align}
$$
Notice that $(H_\pi)_* \dot{x}_t = \dot{x}_t$, and so we can rewrite the energy functional as:
$$
\begin{align}
  \int_{\mathcal{X}_t} \frac{1}{2} \|(H_{\bar{z}})_* \dot{z}_t\|^2_{(H_{\bar{z}}^{-1})^* g_{H_{\bar{z}}}} \rho_t dV &= \int_{\mathcal{X}_t} \frac{1}{2} \|(H_\pi)_* \dot{x}_t\|^2_{(H_\pi)^* g} \rho_t dV
\end{align}
$$

# Geodesic equation derivation from data space
Next we need to push the geodesic equation through $H_{\bar{z}}$ to get the geodesic equation in data space:
$$
\begin{align}
  (H_{\bar{z}})_*\left[\sum_{i,j,m}\ddot{z}_t + \Gamma_{ij}\dot{z}_t^i\dot{z}_t^j\right] = 0
\end{align}
$$
To do this, it will help to first look at what the coordinates of the second derivative of $x_t$ are.  We can compute:
$$
\begin{align}
  \ddot{x}_t &= \frac{d}{dt}\dot{x}_t \\
  &= \frac{d}{dt}\left(J\dot{z}_t\right) \\
  &= \dot{x}_t(J)\dot{z}_t + J\ddot{z}_t \\
  &= \dot{z}_t(J)\dot{z}_t + J\ddot{z}_t,\quad \because \text{ $\dot{z}_t$ and $\dot{x}_t$ are the same vector field} \\
  &= \frac{\partial x^2}{\partial z^i \partial z^j}\dot{z}_t^i \dot{z}_t^j + J\ddot{z}_t
\end{align}
$$
If we multiply on the right by $J^+$, we get:
$$
\begin{align}
  J^+\ddot{x}_t &= J^+\left(J\ddot{z}_t + \frac{\partial x^2}{\partial z^i \partial z^j}\dot{z}_t^i \dot{z}_t^j\right) \\
  &= \ddot{z}_t + J^+\frac{\partial x^2}{\partial z^i \partial z^j}\dot{z}_t^i \dot{z}_t^j \\
  &= \ddot{z}_t + \Gamma_{ij}\dot{z}_t^i\dot{z}_t^j
\end{align}
$$
This is exactly the geodesic equation, and so by multiplying on the right by $J$, we get the geodesic equation in data space:
$$
\begin{align}
  d(H_\pi)_{(x_t)} \ddot{X}_t = 0 = J^\parallel\ddot{x}_t
\end{align}
$$

# Implications for the value function
An implication of the geodesic equation is that the speed of the transport map is constant along the geodesic.  We can see this by taking the time derivative of the integrand:
$$
\begin{align}
  \frac{d}{dt}\frac{1}{2} \|(H_\pi)_* \dot{X}_t\|^2_{(H_\pi)^* g} &= \frac{d}{dt}\frac{1}{2} \langle J^\parallel \dot{x}_t, J^\parallel \dot{x}_t \rangle \\
  &= \langle \frac{dJ^\parallel}{dt} \dot{x}_t + \underbrace{J^\parallel \ddot{x}_t}_{=0}, J^\parallel \dot{x}_t \rangle \\
  &= \langle \left(\cancel{J^\perp \frac{dJ}{dt}J^+} + (J^\perp \frac{dJ}{dt}J^+)^T\right) \dot{x}_t, J^\parallel \dot{x}_t \rangle \\
  &= \langle \cancel{{J^+}^T \frac{dJ^T}{dt}J^\perp J\dot{z}_t}, J^\parallel \dot{x}_t \rangle \\
  &= 0
\end{align}
$$
And so we have that
$$
\begin{align}
  \frac{d}{dt}E[H] = \frac{1}{2} \|(H_\pi)_* \dot{X}_t\|^2_{(H_\pi)^* g} = \text{const}
\end{align}
$$

# Full form of energy functional
We can now write the full form of the energy functional:
$$
\begin{align}
  E[H] &= \int_1^0 \int_{\mathcal{X}_t} \rho_t \frac{1}{2}\|(H_\pi)_* \dot{X}_t\|^2_{(H_\pi)^* g} dV dt, \quad \text{s.t. } \;\; d(H_\pi)_{(x_t)} \ddot{X}_t = 0 \\
  &= \int_1^0 \int_{\mathcal{X}_t} \rho_t(x_t) \frac{1}{2}\|J^\parallel(x_t) \dot{x}_t(x_t)\|^2 dV dt, \quad \text{s.t. } \;\; J^\parallel(x_t) \ddot{x}_t(x_t) = 0
\end{align}
$$

# Variation of energy functional
We can now vary the energy functional by incorporating a Lagrange multiplier, ${\lambda_t}$, for the constraint:
$$
\begin{align}
  \frac{d}{du}E_{\lambda_t}[H_u] = \frac{d}{du} \int_1^0 \int_{\mathcal{X}_{t,u}} \rho_{t,u}(x_{t,u}) \frac{1}{2}\left(\|J_u^\parallel(x_{t,u}) \dot{x}_{t,u}(x_{t,u})\|^2 + \langle {\lambda_t}(x_{t,u}), J_u^\parallel(x_{t,u}) \ddot{x}_{t,u}(x_{t,u})\rangle\right) dV dt
\end{align}
$$
From Lemma 1, we have that:
$$
\begin{align}
  \frac{d}{du}E_{\lambda_t}[H_u] = \int_1^0 \int_{\mathcal{X}_{t,u}} \rho_{t,u}(x_{t,u}) \frac{d}{du}\frac{1}{2}\left(\|J_u^\parallel(x_{t,u}) \dot{x}_{t,u}(x_{t,u})\|^2 + \langle {\lambda_t}(x_{t,u}), J_u^\parallel(x_{t,u}) \ddot{x}_{t,u}(x_{t,u})\rangle\right) dV dt
\end{align}
$$
Suppose that $\frac{dH_u}{du} = \Phi_u$.  A lemma that we will need is the following:
$$
\begin{align}
  \frac{d}{du}J_u^{\parallel} = (J_u^\perp \nabla \Phi_u J_u^\parallel) + (J_u^\perp \nabla \Phi_u J_u^\parallel)^T
\end{align}
$$
Then the first term in the variation of the energy functional is:
$$
\begin{align}
  \frac{d}{du}\frac{1}{2}\|J_u^\parallel \dot{x}_{t,u}\|^2 &= \langle \frac{d}{du}\left(J_u^\parallel \dot{x}_{t,u}\right), J_u^\parallel \dot{x}_{t,u}\rangle \\
  &= \langle (J_u^\perp \nabla \Phi_u J_u^\parallel)\dot{x}_{t,u} + (J_u^\perp \nabla \Phi_u J_u^\parallel)^T\dot{x}_{t,u} + \frac{d\dot{x}_{t,u}}{du}, J_u^\parallel \dot{x}_{t,u}\rangle \\
  &= \langle \frac{d\dot{x}_{t,u}}{du}, J_u^\parallel \dot{x}_{t,u}\rangle , \because \text{ $\dot{x}_{t,u} = J^\parallel \dot{x}_{t,u}$}
\end{align}
$$

Next, the second term in the variation of the energy functional is:
$$
\begin{align}
  \frac{d}{du}\langle {\lambda_t}, J_u^\parallel \ddot{x}_{t,u}\rangle &= \langle \Phi_u({\lambda_t}), J_u^\parallel \ddot{x}_{t,u}\rangle + \langle {\lambda_t}, \frac{d}{du}J_u^\parallel \ddot{x}_{t,u}\rangle \\
  &= \langle \Phi_u({\lambda_t}), J_u^\parallel \ddot{x}_{t,u}\rangle + \langle {\lambda_t},(J_u^\perp \nabla \Phi_u J_u^\parallel)\ddot{x}_{t,u} + (J_u^\perp \nabla \Phi_u J_u^\parallel)^T\ddot{x}_{t,u} + \frac{d\ddot{x}_{t,u}}{du} \rangle \\
  &= \langle \Phi_u({\lambda_t}), J_u^\parallel \ddot{x}_{t,u}\rangle + \langle {\lambda_t},J_u^\parallel \nabla \Phi_u^T J_u^\perp \ddot{x}_{t,u} + \frac{d\ddot{x}_{t,u}}{du} \rangle
\end{align}
$$

















