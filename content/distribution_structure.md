Title: On the structure of probability density functions
Date: 2025-03-01
Category: Blog
Slug: distribution_structure
hidden: true
Summary: A definition of the structure of probability density functions

In this document, we explore the structure of probability density functions by looking at the geometry of coordinate curves for flows whose pushforward distribution is fixed.  Let $\mathcal{X} = \mathbb{R}^n$ be the data space and let $\rho$ be the probability density function of the data and let $\mathcal{Z} = \mathbb{R}^n$ be a latent space, on which we define a probability density function with independent components, $\nu(z) = \prod_{i=1}^n \nu_i(z_i)$ where $z = (z_1, \ldots, z_n)$.  We consider the family of diffeomorphisms, $H: \mathcal{Z} \to \mathcal{X}$, that map $\nu$ to $\rho$ under the pushforward map, $(H)_* \nu = \rho$.  We will call the family of diffeomorphisms, $H$, a normalizing flow.  We then talk about the structure of $\rho$ using the coordinate curves of $H$, which are the curves given by pushing components $\mathcal{Z}_k = \mathbb{R} \subset \mathcal{Z}$ through $H$.  For example, the $k$'th coordinate curve is given by the 1d curve, $H(\mathcal{Z}_k)$.  Then we will look at the length of coordinate curves and see for which $H$ the coordinate curves have the shortest length.  To start, lets formally define the coordinate curves.

## Coordinate curves
Let $\mathcal{T} = \mathcal{Z}_k = \mathbb{R} \subset \mathcal{Z}$ be the $k$'th coordinate axes of the latent space and let $\pi: \mathcal{Z} \to \mathcal{T}$ be the standard projection map onto $\mathcal{T}$ and let $\pi^{-1}: \mathcal{T} \to \mathcal{Z}$ be a section (right inverse) of $\pi$.  Also let $\bar{\pi}: \mathcal{Z} \to \mathcal{Z} \setminus \mathcal{T}$ be the projection map onto the complement of $\mathcal{T}$ in $\mathcal{Z}$.  Note that we are using $\mathcal{T}$ to denote the $k$'th coordinate axes instead of $\mathcal{Z}_k$ to explicitly indicate that its parameter, $t \in \mathcal{T}$ should be interpreted as a time parameter that determines the position along the coordinate curve.  A coordinate curve is the map $\Phi: \mathcal{T} \times \mathcal{X} \to \mathcal{X}$ defined by
$$
\begin{equation}
  \Phi_t(x) = H\circ \pi_{\bar{z}}^{-1}\circ \gamma_t \circ \pi \circ H^{-1}(x)
\end{equation}
$$
where $\gamma_t: \mathbb{R} \times \mathcal{T} \to \mathcal{T}$ is a diffeomorphism that parameterizes the coordinate curve.  We can understand what the coordinate curve is doing by explicitly writing out the computations
$$
\begin{align*}
  z &= H^{-1}(x) \\
  t', \bar{z} &= (\pi(z), \bar{\pi}(z)) \\
  t &= \gamma_t(t') \\
  z_t &= \pi_{\bar{z}}^{-1}(t) \\
  \Phi_t(x) &= H(z_t)
\end{align*}
$$
We can see that $\Phi_t$ moves $x$ along the coordinate curve in $\mathcal{X}$ by transporting $x$, in the latent space, along the $k$'th coordinate axis for $t$ seconds and then projecting the result back to the data space.  The curve, $\gamma_t$, controls how fast we move along the coordinate curve while the diffeomorphism, $H$, controls the shape of the curve.  For convenience, we will use $H_{\bar{z}}$ to denote the injective map from the $k$'th coordinate axis to the corresponding coordinate curve by $H_{\bar{z}} = H \circ \bar{\pi}_{\bar{z}}^{-1}$,


We denote the tangent vector to the coordinate curve by $\mathbf{V}_t \in \mathfrak{X}(\mathcal{X})$ and is given by $\mathbf{V}_t = \frac{d\Phi_t}{dt}$.  This vector field is defined by pushing forward the vector field on the latent space, $\mathbf{W}_t \in \mathfrak{X}(\mathcal{Z}_k)$, that is defined by the time derivative, $\mathbf{W}_t = \frac{d\gamma_t}{dt}$, through $H_{\bar{z}}$.
$$
\begin{align}
  \mathbf{V}_t\Big|_{x_t} &= (dH_{\bar{z}})_{z_t}W_t\Big|_{z_t}, \quad \text{where} \quad x_t = H(z_t,\bar{z})
\end{align}
$$
where $dH_{\bar{z}}$ is the differential of $H_{\bar{z}}$ at $z_t$ and $W_t$ is the vector field on the latent space.

#### Data space at time $t$
$$
\begin{align}
  \mathbf{V}_t(x_t) &= V_t(x_t)^i E_i
\end{align}
$$
#### Data space at time $0$
$$
\begin{align}
  \mathbf{V}_t(x_0) &= DH(z_t)^i W_t(z_t) E_i
\end{align}
$$





### Derivative with respect to $f$
Assume that $f$ depends on the scalar parameter $\theta$ so that $f_\theta: \mathcal{Z} \to \mathcal{X}$ is a diffeomorphism.  Then we have the following derivative:
$$
\begin{align}
  \frac{d}{d\theta} \Phi_t(x) &= X_\theta \circ \Phi_{\theta,t}(x) + d(\Phi_{\theta,t})_x X_\theta(x), \quad \text{where} \quad X_\theta = \frac{df_\theta}{d\theta}
\end{align}
$$
Proof:
$$
\begin{align}
  \frac{d}{d\theta} \Phi_{\theta,t}(x) &= \frac{d}{d\theta} f_\theta\circ \pi_{\bar{z}}^{-1}\circ \gamma_t \circ \pi \circ f_\theta^{-1}(x) \\
  &= \left(\frac{d f_\theta}{d\theta} \right)(\pi_{\bar{z}}^{-1}( \gamma_t ( \pi ( f_\theta^{-1}(x))))) + d(f_\theta\circ \pi_{\bar{z}}^{-1}\circ \gamma_t \circ \pi \circ f_\theta^{-1})_z \frac{df_\theta^{-1}}{d\theta}(x)
\end{align}
$$
Notice that $\frac{df_\theta}{d\theta} = \frac{dx_\theta}{d\theta}$ is a vector field on $\mathcal{X}$ and $\frac{df_\theta^{-1}}{d\theta} = \frac{dz_\theta}{d\theta}$ is the same vector field, pushed forward to $\mathcal{Z}$.  We will denote this vector field on $\mathcal{X}$ as $X_\theta$.  Then we can simplify our expression:
$$
\begin{align}
  &= X_\theta(\pi_{\bar{z}}^{-1}( \gamma_t ( \pi ( f_\theta^{-1}(x))))) + d(f_\theta\circ \pi_{\bar{z}}^{-1}\circ \gamma_t \circ \pi \circ f_\theta^{-1} \circ f_\theta^{-1})_x V_\theta(x) \\
  &= X_\theta \circ \Phi_{\theta,t}(x) + d(\Phi_{\theta,t})_x X_\theta(x)
\end{align}
$$
$\blacksquare$

### Derivative with respect to $\gamma_t$
The derivative of the projection map with respect to $t$ yields the tangent vector to the coordinate curve.  This is given by:
$$
\begin{align}
  \frac{d}{dt} \Phi_{\theta,t}(x) &= d(f_{\theta}\circ \pi_{\bar{z}}^{-1})_{\gamma_t(t)} V_t(t'), \quad \text{where} \quad V_t = \frac{d\gamma_t}{dt}|_{t'} \text{ and } t' = \pi(f_{\theta}^{-1}(x))
\end{align}
$$
We can evaluate this expression using the covariant derivative.

### Second derivatives
Suppose we want to see how the tangent vector to the coordinate curve changes as we change the parameter $\theta$.  Then we have the following second derivative:
$$
\begin{align}
  \frac{d}{d\theta}\frac{d}{dt} \Phi_{\theta,t}(x) &= \frac{d}{d\theta}d(f_{\theta}\circ \pi_{\bar{z}}^{-1})_{\gamma_t(t)} V_t(t')
\end{align}
$$




### Weighted length
We will examine the length of the tangent vector to the coordinate curve, weighted by the probability density function $\rho$.  This weighted length is defined as follows:
$$
\begin{align}
  D(x_0) = \int_{-\infty}^{\infty} \rho(\Phi_t(x_0)) \|\frac{d \Phi_t}{dt}(x_0)\|_g dt
\end{align}
$$
where $\|\cdot\|_g$ is the norm induced by the Riemannian metric $g$ on $\mathcal{X}$.

### Weighted energy

### Probability density constraint

