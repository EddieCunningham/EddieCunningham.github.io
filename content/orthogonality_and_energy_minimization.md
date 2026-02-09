Title: Orthogonality and energy minimization
Date: 2025-02-16
Category: Blog
Slug: orthogonality_and_energy_minimization
hidden: true
Summary: Orthogonal coordinates and energy minimization

# Abstract
We show that orthogonal coordinate transforms minimize the energy required to perform dimensionality reduction.

# Introduction
Dimensionality reduction is a key problem in machine learning that is focused on finding a low-dimensional embedding of data that preserves useful properties of the data.  Injective normalizing flows are one such method for performing dimensionality reduction while preserving the distribution of the data.  These models use an injective function $F: \mathcal{Z} = \mathbb{R}^k \to \mathcal{X} = \mathbb{R}^n$ to pushforward a prior distribution on $\mathcal{Z}$, denoted by $\nu$, onto an embedded submanifold $\mathcal{S} = F(\mathcal{Z}) \subset \mathcal{X}$.  Injective normalizing flows are trained to maximize the likelihood of projections of $x\sim \rho(x)$ onto $\mathcal{S}$, under the pushforward distribution $(F)_* \nu$, while ensuring that this projection minimizes some reconstruction error, such as the expected L2 reconstruction error between $x$ and its projection onto $\mathcal{S}$.  The choice of objective for the reconstruction error determines the shape that $\mathcal{S}$ takes in $\mathcal{X}$ and is what controls the dimensionality reduction, while the maximum likelihood objective ensures that the distribution of the learned embeddings is close to the data distribution.  We show that when the reconstruction error is chosen to be the energy required to transport a point $x$ to its projection onto $\mathcal{S}$, the minimizers of this reconstruction error are orthogonal coordinate transforms.

# Injective normalizing flows
Let $\rho(x)$ be the distribution of data in $\mathcal{X}$.  An injective normalizing flow is an injective map $F: \mathcal{Z} \to \mathcal{X}$ and a prior distribution $\nu$ on $\mathcal{Z}$ that is trained to maximize the likelihood of the data under the pushforward distribution $(F)_* \nu$, while ensuring that the image of $F$ is close to samples from $\rho(x)$.  A common objective function used to train an injective normalizing flow is the expected log likelihood of the data under the pushforward distribution,
$$
\begin{align}
  \mathcal{L}[F] = -\mathbb{E}_{x\sim \rho(x)} \left[ \underbrace{-\log \nu(z) + \frac{1}{2}\log|\det(J_F(z))|}_{\text{log likelihood}} + \lambda \underbrace{\left\| x - F(z) \right\|^2}_{\text{reconstruction error}} \right], \;\;\text{where } z = F^{-1}(x)
\end{align}
$$
where $J_F$ is the Jacobian matrix of $F$ and $\lambda$ is a hyperparameter that controls the trade-off between the log likelihood and the reconstruction error.  In order to ensure that $F$ is injective, it is typically implemented as a slice of a diffeomorphism $H: \mathbb{R}^n \to \mathbb{R}^n$ in the ambient space of $\mathcal{Z}$.  We first split the base space into two parts, $\mathcal{Z} = \mathbb{R}^k$ and $\bar{\mathcal{Z}} = \mathbb{R}^{n-k}$ so that $\mathbb{R}^n = \mathcal{Z} \oplus \bar{\mathcal{Z}}$.  We call $\mathcal{Z}$ and $\bar{\mathcal{Z}}$ the "on-manifold" and "off-manifold" coordinates respectively.  With this, we can take $H$ to be an invertible map from $(\mathcal{Z},\bar{\mathcal{Z}}) \to \mathcal{X}$ and then define $F$ and its inverse as follows:
$$
\begin{align}
  x &= F(z) = H(z, \bar{z}=0) \\
  z &= F^{-1}(x), \quad \text{where } (z, \bar{z}) = H^{-1}(x)
\end{align}
$$
This model constructs a low dimensional representation of $x$ by mapping $x$ to the latent space and dropping the off-manifold coordinates, and projections onto $F(\mathcal{Z})$ by replacing the dropped variables with a constant, such as $0$, and then applying $H$.

### Problems with injective normalizing flows
- If we want to use the embeddings to be useful, we would hope that similar $x$ map to the same $z$.
- The usefulness of the embedding is determined by the reconstruction error because the likelihood part can be achieved using any arbitrary set of coordinates.
- The reconstruction error should be invariant to the choice of parameterization for $z$
- We propose a transport based reconstruction error that is
  1. Invariant to the choice of manifold coordinates
  2. Admits solutions that are OCT-ICs
  3. Offers a natural model for dimensionality reduction

# Transport maps for performing dimensionality reduction
In order to arrive at a model for dimensionality reduction, we need to first understand how exactly injective normalizing flows perform dimensionality reduction.  For an injective normalizing flow, defined above, we can write the projection map from $\mathcal{X}$ to $\mathcal{S}$ as follows:
$$
\begin{align}
  P_0(x) = H \circ \bar{\pi}_z^{-1} \circ \bar{\psi}_0 \circ \bar{\pi} \circ H^{-1}(x)
\end{align}
$$
where $\bar{\pi}: \mathbb{R}^n \to \bar{\mathcal{Z}} = \mathbb{R}^{n-k}$ is the standard projection map in Euclidean space and where $\bar{\psi}_0: \bar{z} \mapsto 0$ is the map that sets the off-manifold coordinates to $0$.  $\bar{\pi}_z^{-1}: \bar{\mathcal{Z}} \to \mathbb{R}^n$, defined by $\bar{\pi}_z^{-1} = (z,\bar{z})$, is the right inverse of $\bar{\pi}$ so that for a given $z \in \mathcal{Z}$, $\bar{\pi}\circ \bar{\pi}_z^{-1} = \mathrm{Id}_{\bar{\mathcal{Z}}}$.  This projection map is a simple and intuitive way to perform dimensionality reduction, because $H$ can be constructed using invertible deep neural networks, and the mechanism of setting the off-manifold coordinates to zero is striaghtforward.  (EXPOSITION).  We propose a different mechanism for performing dimensionality reduction where we smoothly change the off-manifold coordinates of data to zero.

Rather than performing dimensionality reduction by setting the off-manifold coordinates to zero, we can perform dimensionality reduction by smoothly changing the off-manifold coordinates of data to zero using a time-dependent flow map (see Lee Ch. 8,9) which we call the "transport map".  The transport map can be defined on the off-manifold coordinates as a smooth diffeomorphism $\bar{\psi}_t: \bar{\mathcal{Z}} \to \bar{\mathcal{Z}}$, with a scalar parameter $t\in [0,1]$, where $\bar{\psi}_{t=1}(\bar{z}) = \bar{z}$ and $\bar{\psi}_{t=0}(\bar{z}) = 0$.

An important property of $\bar{\psi}_t$ is that $\frac{d\bar{\psi}_t(0)}{dt} = 0$.  If it wasn't, then it would be able to find two times, $a,b$ and a value of $\bar{z}$ so that $\bar{\psi}_a(\bar{z}) = \bar{\psi}_b(\bar{z})$, which is not allowed?

### Properties of $\bar{\psi}_t$












This map can be applied in the data space by composing it with the ambient space diffeomorphism $H$ and the projection map $\bar{\pi}_z^{-1}$ as follows:
$$
\begin{align}
  P_t(x) = H \circ \bar{\pi}_z^{-1} \circ \bar{\psi}_t \circ \bar{\pi} \circ H^{-1}(x)
\end{align}
$$
As $t$ varies from $1$ to $0$, $P_t(x)$ transports $x$ to its projection $P_0(x)$.  The path that $P_t(x)$ takes in $\mathcal{X}$ depends on $H$, as defines the on- and off-manifold spaces, while $\bar{\psi}_t$ defines the path that $P_t(x)$ takes in the off-manifold space to transport samples in $\mathcal{X}$ onto the manifold.  This transport map lets us view dimensionality reduction from a physical perspective, and lets us measure how "difficult" it is to perform dimensionality reduction.  Rather than looking at the squared L2 norm of the difference between $x$ and $P_t(x)$, we can look at how much energy is required to move $x$ along the path $P_t(x)$ to $P_0(x)$.  This energy is given by
$$
\begin{align}
  E[H,\bar{\psi}_t](x) = \int_1^0 \frac{1}{2}\left\| \frac{dP_t(x)}{dt} \right\|^2 dt
\end{align}
$$
Note that this energy depends on both $H$ and $\bar{\psi}_t$.  Since $H$ is the main object of interest, we can fix $\bar{\psi}_t$ to be the minimizer of the energy.  With this in mind, we can define a functional over $H$ that measures how "easy" it is to perform dimensionality reduction with $H$ over samples from $\rho(x)$.
$$
\begin{align}
  E[H] &= \min_{\bar{\psi}_t} \int_{\mathcal{X}} \rho(x) E[H,\bar{\psi}_t](x)dx \\
  &= \min_{\bar{\psi}_t} \int_1^0 \int_{\mathcal{X}} \rho_t(x_t) \frac{1}{2}\left\| \frac{dx_t}{dt} \right\|^2 dx_t \; dt, \quad \text{where } x_t = P_t(x) \text{ and } \rho_t = (P_t)_*\rho
\end{align}
$$
Our first result is that we can determine the form of the minimizer over $\bar{\psi}_t$.

## Gradient field for transport maps
First lets look at the expected energy over the data distribution $\rho(x)$ in terms of the base space.  Suppose that $\nu = H^{-1}_* \rho$ is the pushforward of the data distribution $\rho$ to the base space.  Then we can rewrite the expected energy as follows:
$$
\begin{align}
  E[H] &= \min_{\bar{\psi}_t} \int_1^0 \int_{\mathcal{X}} \rho_t(x_t) \frac{1}{2}\left\| \frac{dx_t}{dt} \right\|^2 dx_t \; dt, \quad \text{where } x_t = P_t(x) \text{ and } \rho_t = (P_t)_*\rho \\
  &= \min_{\bar{\psi}_t} \int\int \nu(z,\bar{z}) \int_1^0 \frac{1}{2} \left\| \frac{dP_t \circ H(z,\bar{z})}{dt}\right\|^2 dt\; d\bar{z}\; dz \\
  &\quad (P_t \circ H = H\circ \bar{\pi}_z^{-1} \circ \bar{\psi}_t \circ \bar{\pi}) \\
  &= \min_{\bar{\psi}_t} \int\int \nu(z,\bar{z}) \int_1^0 \frac{1}{2} \left\| \frac{dH\circ \bar{\pi}_z^{-1} \circ \bar{\psi}_t(\bar{z})}{dt}\right\|^2 dt\; d\bar{z}\; dz \\
  &\quad (\text{let }\bar{z}_t = \bar{\psi}_t(\bar{z}) \text{ and } \nu_t(\bar{\psi}_t(\bar{z})|z) = (\bar{\psi}_t)_* \nu(\bar{z}|z)) \\
  &= \min_{\bar{\psi}_t} \int \nu(z) \int_1^0 \int \nu_t(\bar{z}_t|z) \frac{1}{2} \left\| \frac{dH(z,\bar{z}_t)}{dt}\right\|^2 d\bar{z}_t\; dt\; dz \\
  &\quad \text{Since $\gamma_t$ is fixed at $t=0$ and $t=1$, we can solve for $\frac{d\bar{z}_t}{dt}$} \\
  &= \min_{\frac{d\bar{z}_t}{dt}} \int \nu(z) \int_1^0 \int \nu_t(\bar{z}_t|z) \frac{1}{2} \left\| \frac{dH(z,\bar{z}_t)}{dt}\right\|^2 d\bar{z}_t\; dt\; dz \\
  &= \min_{\frac{d\bar{z}_t}{dt}} \int \nu(z) \int_1^0 \int \nu_t(\bar{z}_t|z) \frac{1}{2}\langle \underbrace{DH(z,\bar{z}_t)^TDH(z,\bar{z}_t)}_{\Sigma_z(\bar{z}_t)}\frac{d\bar{z}_t}{dt}, \frac{d\bar{z}_t}{dt} \rangle d\bar{z}_t\; dt\; dz \\
  &= \min_{\frac{d\bar{z}_t}{dt}} \int \nu(z) \int_1^0 \int \nu_t(\bar{z}_t|z) \frac{1}{2}\langle \Sigma_z(\bar{z}_t)\frac{d\bar{z}_t}{dt}, \frac{d\bar{z}_t}{dt} \rangle d\bar{z}_t\; dt\; dz
\end{align}
$$

## Transport version
Next, we will transform slightly so that it becomes easier to solve.  To start, let $\bar{V}_t(\bar{z}_t) := \frac{d\bar{z}_t}{dt}$ and $\nu_{t,z}(\bar{z}_t) = \nu_t(\bar{z}|z)$.  A challenge of solving the above problem is that $\nu_{t,z}$ depends on $\bar{V}_t$.  However, since $\nu_{t,z}$ is a pushforward distribution, it is uniquely defined given $\bar{V}_t$, as the solution to the continuity equation $\frac{\partial \nu_{t,z}}{\partial t} + \text{Div}(\nu_{t,z} V_t) = 0$.  As a result, we can write the energy functional as a function of $\nu_{t,z}$, subject to the continuity equation:
$$
\begin{align}
  \min_{V_t,\nu_{t,z}}E[H,V_t,\nu_{t,z}] := \min_{V_t}E[H, V_t], \quad\text{s.t. }\frac{\partial \nu_{t,z}}{\partial t} + \text{Div}(\nu_{t,z} V_t) = 0
\end{align}
$$
This problem can be solved by introducing Lagrange multipliers $\bar{s}_{t,z}$ to add to $E[H,V_t,\nu_{t,z}]$.  The term that we add to $E[H,V_t,\nu_{t,z}]$ will have a Lagrange multiplier for each $t$ and $z$
$$
\begin{align}
  &\int \bar{s}_{t,z}\left( \frac{\partial \nu_{t,z}}{\partial t} + \text{Div}(\nu_{t,z} V_t) \right) d\bar{z}_t  \\
  &= \int s_{t,z} \frac{\partial \nu_{t,z}}{\partial t} d\bar{z}_t - \int \nu_{t,z} \langle \nabla_{\bar{z}} s_{t,z}, V_t \rangle d\bar{z}_t + \int_{\partial \bar{\mathcal{Z}}}\nu_{t,z} s_{t,z} \langle \underbrace{V_t}_{=0 \text{ when }\bar{\mathcal{Z}}=0}, N_z \rangle dV_{\tilde{g}},\quad \text{ where $N_z$ normal to $\partial \bar{\mathcal{Z}}$} \\
  &= \int s_{t,z} \frac{\partial \nu_{t,z}}{\partial t} d\bar{z}_t - \int \nu_{t,z} \langle \nabla_{\bar{z}} s_{t,z}, V_t \rangle d\bar{z}_t
\end{align}
$$
We used integration by parts to rewrite the experssion in a more convenient form.  Now, we can construct a Lagrangian by adding this term to the energy functional:
$$
\begin{align}
  &{E[H] = \max_{\bar{s}_{t,z}}\min_{V_t} \int \nu(z) \int_1^0 \left[\int \nu_{t,z} \langle \frac{1}{2}\Sigma_z V_t - \nabla_{\bar{z}} s_{t,z}, V_t \rangle d\bar{z}_t\; + \int s_{t,z} \frac{\partial \nu_{t,z}}{\partial t} d\bar{z}_t\right]dt\; dz} \\
  &{\quad\quad\;= \max_{\bar{s}_{t,z}}\min_{V_t} \int \nu(z) \left[\int_1^0 \int \nu_{t,z} \langle \frac{1}{2}\Sigma_z V_t - \nabla_{\bar{z}} s_{t,z}, V_t \rangle d\bar{z}_t\;dt + \int_1^0 \int s_{t,z} \frac{\partial \nu_{t,z}}{\partial t} d\bar{z}_t\; dt\right] dz}
\end{align}
$$
If we vary the part of the integrand that depends on $V_t$ and set the variation to zero, we can find the vector fields that are stationary points of the energy functional.  Let $V_t(\epsilon) = V_t + \epsilon \eta_t$ be a variation of $V_t$ where $\eta_t$ is a vector field on $\bar{\mathcal{Z}}$.  Then we can compute:
$$
\begin{aligned}
\frac{d}{d\epsilon}\Big|_{\epsilon=0} &\int \nu_{t,z} \Big\langle \frac{1}{2}\Sigma_z V_t(\epsilon) - \nabla_{\bar{z}} \bar{s}_{t,z}, V_t(\epsilon) \Big\rangle \, d\bar{z}_t \\
&= \int \nu_{t,z} \left[ \left\langle \frac{1}{2}\Sigma_z\, \eta_t, V_t \right\rangle + \left\langle \frac{1}{2}\Sigma_z V_t - \nabla_{\bar{z}} \bar{s}_{t,z}, \eta_t \right\rangle \right] \, d\bar{z}_t \\
&= \int \nu_{t,z} \left\langle \Sigma_z V_t - \nabla_{\bar{z}} \bar{s}_{t,z}, \eta_t \right\rangle \, d\bar{z}_t.
\end{aligned}
$$
Since $\eta_t$ is arbitrary, we must have that
$$
V_t = \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z}
$$
where $\nabla_{\bar{z}}$ is the gradient operator on $\bar{\mathcal{Z}}$.

### Plugging it back in
We can plug this back into the energy functional to get the following:
$$
\begin{align}
  &\small{E[H] = \max_{\bar{s}_{t,z}}\int \nu_z \left[\int_1^0 \int \nu_{t,z} \langle \frac{1}{2}\Sigma_z\Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} - \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle d\bar{z}_t\;dt + \int_1^0 \int \bar{s}_{t,z} \frac{\partial \nu_{t,z}}{\partial t} d\bar{z}_t\; dt\right] dz} \\
  &\small{\quad\quad \; = \max_{\bar{s}_{t,z}}\int \nu_z \left[\int_1^0 \int \nu_{t,z} -\frac{1}{2}\langle \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle d\bar{z}_t\;dt - \int_1^0 \int \nu_{t,z}\frac{\partial \bar{s}_{t,z}}{\partial t} d\bar{z}_t\; dt + \int \nu_{0,z} \bar{s}_{0,z} d\bar{z}_0 - \int \nu_{1,z} \bar{s}_{1,z} d\bar{z}_1\right] dz} \\
  &\small{\quad\quad \; = \max_{\bar{s}_{t,z}}\int \nu_z \left[\int_1^0 \int \nu_{t,z} \left(-\frac{1}{2}\langle \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle - \frac{\partial \bar{s}_{t,z}}{\partial t}\right) d\bar{z}_t\;dt  + \int \nu_{0,z} \bar{s}_{0,z} d\bar{z}_0 - \int \nu_{1,z} \bar{s}_{1,z} d\bar{z}_1\right] dz}
\end{align}
$$
Since $\bar{s}_{t,z}$ was nearly arbitrary, we can choose it to satisfy certain properties.  For example, we can assert that $-\frac{1}{2}\langle \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle - \frac{\partial \bar{s}_{t,z}}{\partial t} = 0$ for all $t$ and $z$ so that the energy functional is minimized.  This means that the energy functional can be written as:
$$
\begin{align}
  E[H] &= \max_{\bar{s}_{t,z}}\int \nu_z \left[\int \nu_{0,z} \bar{s}_{0,z} d\bar{z}_0 - \int \nu_{1,z} \bar{s}_{1,z} d\bar{z}_1\right] dz \\
  &\text{ s.t. }\frac{\partial \bar{s}_{t,z}}{\partial t} + \frac{1}{2}\langle \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle = 0 \text{ and }\bar{z}_t = \bar{z}_1 + \int_1^t \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{\tau,z} d\tau
\end{align}
$$

#### Note
I do not know if this is allowed because technically $\nu_{0,z}(\bar{z}) = \infty$.  To accomodate this, we can assume that $t \in [\epsilon, 1]$, solve for $\frac{\partial \bar{s}_{t,z}}{\partial t}$ and then show that $E[H,\epsilon]$ converges as $\epsilon \to 0$, and that $\frac{\partial \bar{s}_{t,z}}{\partial t}$ does not change.

## Expression in data space
We can also push this expression back into the data space to get some intuition for the form of the transport map.  First, we can push the transport vector, $V_t$, to $\mathcal{X}$ to see how samples move in the data space:
$$
\begin{align}
  \frac{dx_t}{dt} &= (dH_z)_{\bar{z}_t}V_t \\
  &= DH_z(DH_z^TDH_z)^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \\
  &= DH_z(DH_z^TDH_z)^{-1}DH_z^T \nabla_x \underbrace{(\bar{s}_{t,z}\circ \pi \circ H^{-1})}_{\bar{s}_{t,x}} \\
  &= (DH_{F^{-1}(x)})^\parallel \nabla_x \bar{s}_{t,x}
\end{align}
$$
We can see that the transport vector is the projected gradient of $\bar{s}_{t,x}$ pulled back to $\mathcal{X}$.  The condition that we imposed on $\bar{s}_{t,z}$ can be rewritten as:
$$
\begin{align}
  0 = \frac{\partial \bar{s}_{t,z}}{\partial t} + \frac{1}{2}\langle \nabla_{\bar{z}} \bar{s}_{t,z}, \Sigma_z^{-1} \nabla_{\bar{z}} \bar{s}_{t,z} \rangle
  \implies 0 &= \frac{\partial \bar{s}_{t,x}}{\partial t} + \frac{1}{2}\langle DH_z^T \nabla_x \bar{s}_{t,x}, \Sigma_x^{-1} DH_z^T \nabla_x \bar{s}_{t,x} \rangle \\
  &= \frac{\partial \bar{s}_{t,x}}{\partial t} + \frac{1}{2}\langle DH_z^\parallel \nabla_x \bar{s}_{t,x}, \nabla_x \bar{s}_{t,x} \rangle \\
  &= \frac{\partial \bar{s}_{t,x}}{\partial t} + \frac{1}{2}\|(DH_z)^\parallel \nabla_x \bar{s}_{t,x}\|^2
\end{align}
$$
and so the energy functional can be written as:
$$
\begin{align}
  E[H] &= \int \nu_z \left[\int \nu_{0,z} \bar{s}_{0,z} d\bar{z}_0 - \int \nu_{1,z} \bar{s}_{1,z} d\bar{z}_1\right] dz \\
  &= \int \nu(z) \left[\int \nu_{0}(\bar{z}|z) \bar{s}_{0}(\bar{z};z) d\bar{z} - \int \nu_{1}(\bar{z}|z) \bar{s}_{1}(\bar{z};z) d\bar{z}\right] dz \\
  &= \int \int \nu_{0}(\bar{z},z) \bar{s}_{0}(\bar{z};z) d\bar{z} dz - \int \int \nu_{1}(\bar{z},z) \bar{s}_{1}(\bar{z};z) d\bar{z} dz \\
  &= \int \rho_0(x) \bar{s}_{0}(x) dx - \int \rho_1(x) \bar{s}_{1}(x) dx
\end{align}
$$
Notice that we also have, from before, that
$$
\begin{align}
  E[H] &= \min_{\bar{\psi}_t} \int_1^0 \int_{\mathcal{X}} \rho_t(x_t) \frac{1}{2}\left\| \frac{dx_t}{dt} \right\|^2 dx_t \; dt, \quad \text{where } x_t = P_t(x) \text{ and } \rho_t = (P_t)_*\rho \\
  &= \int_1^0 \int_{\mathcal{X}} \rho_t(x_t) \frac{1}{2}\|(DH_z)^\parallel \nabla_x \bar{s}_{t,x}\|^2 dx_t \; dt
\end{align}
$$

We can see that these expressions are in fact equivalent because $\frac{d\bar{s}_{t,x}}{dt} = \frac{1}{2}\|(DH_z)^\parallel \nabla_x \bar{s}_{t,x}\|^2$:
$$
\begin{align}
  \frac{d\bar{s}_{t,x}}{dt} &= \frac{\partial \bar{s}_{t,x}}{\partial t} + \langle\frac{dx_t}{dt}, \nabla_x \bar{s}_{t,x} \rangle \\
  &= \frac{\partial \bar{s}_{t,x}}{\partial t} + \langle (DH_z)^\parallel \nabla_x \bar{s}_{t,x}, \nabla_x \bar{s}_{t,x} \rangle \\
  &= \underbrace{\frac{\partial \bar{s}_{t,x}}{\partial t} + \frac{1}{2}\langle (DH_z)^\parallel \nabla_x \bar{s}_{t,x}, \nabla_x \bar{s}_{t,x} \rangle}_{0} + \frac{1}{2}\langle (DH_z)^\parallel \nabla_x \bar{s}_{t,x}, \nabla_x \bar{s}_{t,x} \rangle \\
  &= \frac{1}{2}\|(DH_z)^\parallel \nabla_x \bar{s}_{t,x}\|^2
\end{align}
$$

We can also relate $\rho_t$ to the transport map directly using the continuity equation:
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t (DH_z)^\parallel \nabla_x \bar{s}_{t,x}) = 0
\end{align}
$$

So to summarize, we can define the energy functional in the data space as follows:
$$
\begin{align}
  E[H] &= \int \rho_0 \bar{s}_{0} dx - \int \rho_1 \bar{s}_{1} dx \\
  &= \int_1^0 \int_{\mathcal{X}_t} \rho_t \frac{1}{2}\|(DH_{F^{-1}(x)})^\parallel \nabla_x \bar{s}_{t}\|^2 dx_t \; dt \\
  &= \int_1^0 \int_{\mathcal{X}_t} \rho_t \frac{d\bar{s}_{t}}{dt} dx_t \; dt \\
  &\quad\quad\quad\quad\quad\quad\quad\quad\quad \text{s.t. } \frac{\partial \bar{s}_{t}}{\partial t} + \frac{1}{2}\langle (DH_{F^{-1}(x)})^\parallel \nabla_x \bar{s}_{t}, \nabla_x \bar{s}_{t} \rangle = 0, \\
  &\quad\quad\quad\quad\quad\quad\quad\quad\quad\text{and}\quad\frac{\partial \rho_t}{\partial t} + \text{Div}(\rho_t (DH_{F^{-1}(x)})^\parallel \nabla_x \bar{s}_{t}) = 0
\end{align}
$$

# Stationary points of the energy functional
Now, we will find the stationary points of the energy functional with respect to $H$ in order to find optimal dimensionality reduction maps for a given data distribution.  We will do this by letting $H$ depend on a parameter $u$ and then taking a derivative with respect to $u$ and examining when it is zero.  To make notation easier, we will denote write the Jacobian matrix of $H$ at $x$, $DH_{F^{-1}(x)}$, as $J_u$.  Then we can write the energy functional as follows:
$$
\begin{align}
  \frac{\partial}{\partial u} E[H_u] &= \frac{\partial}{\partial u}\int_1^0 \int_{P_{t,u}(\mathcal{X})} \rho_{t,u} \frac{d\bar{s}_{t,u}}{dt} dV \; dt \\
  &= \int_1^0 \frac{\partial}{\partial u}\int_{\mathcal{X}} P_{t,u}^* \left(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt} dV\right) \; dt \\
  &\text{use Cartan's magic formula} \\
  &= \int_1^0 \int_{\mathcal{X}_t} \underbrace{\mathcal{L}_{\frac{dP_{t,u}}{du}}\left(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt}dV\right)}_{\text{Term A}} + \underbrace{\frac{\partial}{\partial u}\left(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt}\right)}_{\text{Term B}} dV \; dt
\end{align}
$$

Next, we'll simplify each expression in this equation separately.  Let $X_{t,u} := \frac{dP_{t,u}}{du}$.

#### Term A
$$
\begin{align}
  \mathcal{L}_{X_{t,u}}\left(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt}dV\right) &= X_{t,u} \lrcorner \underbrace{d(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt}dV)}_{0} + d(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt} X_{t,u} \lrcorner dV) \\
  &= \text{Div}(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt} X_{t,u})dV \\
  &= \left(\frac{d\bar{s}_{t,u}}{dt}\text{Div}(\rho_{t,u}X_{t,u}) + \langle \nabla_x \frac{d\bar{s}_{t,u}}{dt}, \rho_{t,u}X_{t,u} \rangle\right)dV \\
  &= \left(-\frac{d\bar{s}_{t,u}}{dt}\frac{\partial \rho_{t,u}}{\partial u} + \langle \nabla_x \frac{d\bar{s}_{t,u}}{dt}, \rho_{t,u}X_{t,u} \rangle\right)dV \\
\end{align}
$$

#### Term B
$$
\begin{align}
  \frac{\partial}{\partial u}\left(\rho_{t,u} \frac{d\bar{s}_{t,u}}{dt}\right) &= \frac{\partial \rho_{t,u}}{\partial u}\frac{d\bar{s}_{t,u}}{dt} + \rho_{t,u}\frac{\partial}{\partial u}\frac{d\bar{s}_{t,u}}{dt}
\end{align}
$$

The first terms in each expression cancel, and so we are left with
$$
\begin{align}
  &= \int_1^0 \int_{\mathcal{X}_t}\rho_{t,u}\left(\langle \nabla_x \frac{d\bar{s}_{t,u}}{dt}, X_{t,u} \rangle + \frac{\partial}{\partial u}\frac{d\bar{s}_{t,u}}{dt}\right)dV dt \\
  &= \int_1^0 \int_{\mathcal{X}_t}\rho_{t,u}\frac{d}{d u}\frac{d\bar{s}_{t,u}}{dt}dV dt
\end{align}
$$

Next we will expand the integrand.   For notational convenience, we will write $J = DH_z$
$$
\begin{align}
  \frac{d}{du}\frac{d\bar{s}_{t,u}}{dt} &= \frac{d}{du}\frac{1}{2}\|{J_u}^\parallel \nabla_x \bar{s}_{t,u}\|^2 \\
  &= \left\langle \frac{d}{du}({J_u}^\parallel \nabla_x \bar{s}_{t,u}), {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle \\
  &= \left\langle \frac{d {J_u}^\parallel}{du} \nabla_x \bar{s}_{t,u}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle + \left\langle {J_u}^\parallel \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle \\
  &= \left\langle \frac{d {J_u}^\parallel}{du} \nabla_x \bar{s}_{t,u}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle + \left\langle \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle
\end{align}
$$

We have a corollary that shows that
$$
\begin{align}
  \frac{d {J_u}^\parallel}{du} &= ({J_u}^\perp \frac{d J_u}{du} {J_u}^+) + ({J_u}^\perp \frac{d J_u}{du} {J_u}^+)^T \\
  &= ({J_u}^\perp\nabla_x X_u {J_u}^\parallel) + ({J_u}^\perp\nabla_x X_u {J_u}^\parallel)^T
\end{align}
$$
Since ${J_u}^\perp {J_u}^\parallel = 0$, we can simplify:
$$
\begin{align}
  &= \left\langle {J_u}^\perp \nabla_x \bar{s}_{t,u}, \frac{d J_u}{du} {J_u}^+{J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle + \left\langle \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle \\
  &= \left\langle {J_u}^\perp \nabla_x \bar{s}_{t,u}, \frac{d J_u}{du} {J_u}^+ \nabla_x \bar{s}_{t,u}
  \right\rangle + \left\langle \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle \\
  &= \left\langle {J_u}^\perp \nabla_x \bar{s}_{t,u}, \nabla_x X_u \;{J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle + \left\langle \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle \\
\end{align}
$$

So we are left with the following expression:
$$
\begin{align}
  \frac{\partial}{\partial u} E[H_u] &= \int_1^0 \int_{\mathcal{X}_t} \rho_{t,u}\left(\left\langle {J_u}^\perp \nabla_x \bar{s}_{t,u}, \nabla_x X_u \;{J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle + \left\langle \frac{d \nabla_x \bar{s}_{t,u}}{du}, {J_u}^\parallel \nabla_x \bar{s}_{t,u}\right\rangle\right)dV dt
\end{align}
$$

# OCT-IC
Next, we will show what happeens when $H \in \mathcal{F}_{\text{OCT-IC}}$.  This means that the Jacobian matrix of $H$ has orthogonal columns.