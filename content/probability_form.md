Title: Probability measures using Riemannian densities
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
Tags: riemannian geometry, differential geometry
Slug: probability_measure
Summary: A connection between generative models and Riemannian geometry.

In this post, we'll look at how we can use the Riemannian volume form and Riemannian densities to measure probability on manifolds.

# Probability form
Let $(\mathcal{M},g)$ be a Riemannian manifold with volume form $dV_g$.  We can define the probability of a region $U$ using a positive function $\rho: \mathcal{M} \to \mathbb{R}_{+}$ (called a probability density function) as a function that satisfies:
$$
\begin{align}
  1 = \int_\mathcal{M} \rho dV_g
\end{align}
$$
as the integral of $\rho dV_g$ over $U$:
$$
\begin{align}
  \mathbb{P}(U) = \int_U \rho dV_g
\end{align}
$$
We will call the integrand $\rho dV_g$ a "probability n-form" with respect to the Riemannian metric $g$ and will denote it by:
$$
dP_g := \rho dV_g
$$
The "$d$" in front of $dP$ is not the exterior derivative, just a notation highlight the fact that $dP$ is closed $d(dP) = 0$ because $dV_g$ is closed.  In order to recover the probability density function $\rho$ from $dP$, we can evaluate $dP$ (locally) on an orthonormal frame:
$$
\begin{align}
  dP_g(E_1,\dots,E_n) &= \rho dV_g(E_1,\dots,E_n) \\
  &= \rho
\end{align}
$$
where $E_1,\dots,E_n$ is an orthonormal frame.  This is because $dV_g(E_1,\dots,E_n) = 1$.  It is important to note that $\rho$ is inherently dependent on the choice of $g$ because $g$ determines the coordinates of the orthonormal frame.

# Pullback of probability forms and normalizing flows
Normalizing flows use a diffemorphism $F:\mathcal{X} \to \mathcal{Z}$ to map between a data space $\mathcal{X}$ and base space $\mathcal{Z}$.  If we have a probability form $dP_{g_z}=\rho_z dV_{g_z}$ on $\mathcal{Z}$, we can induce a probability form on $\mathcal{X}$ via the pullback of $F$, denoted as $dP_{F^*g_z}=F^*dP_{g_z}$.  In order for this to be a valid probability form, we would need:
$$
\begin{align}
  1 &= \int_\mathcal{X} F^*dP_{g_z}
\end{align}
$$
This is satisfied if $F$ is a diffeomorphism because of the diffeomorphic invariance of the integral:
$$
\begin{align}
  \int_\mathcal{X} F^*dP_{g_z} &= \int_{F(\mathcal{X})} dP_{g_z} \\
  &= \int_{\mathcal{Z}} dP_{g_z} \\
  &= 1
\end{align}
$$
The probability density function associated with the pullback form can be found by applying $F^*dP_{g_z}$ to an orthonormal frame:
$$
\begin{align}
  F^*dP_{g_z}(E_1,\dots,E_n) &= dP_{g_z}(F_*E_1,\dots,F_*E_n) \\
  &= \rho_z dV_{g_z}(F_*E_1,\dots,F_*E_n) \\
  &= \rho_z \det(g_z(F_*E_i,F_*E_j))^\frac{1}{2} \\
  &= \rho_z \det(F^*g_z(E_i,E_j))^\frac{1}{2}
\end{align}
$$
In the Euclidean case, this is equivalent to the change of variables formula.

# Restricting to submanifolds
Probability forms can be restricted to submanifolds the same way that volume forms can be restricted to submanifolds.  Let $S\subset M$ be a k-dimensional submanifold of $\mathcal{M}$ and let $(E_1,\dots,E_k)$ and $(N_{k+1},\dots,N_n)$ be local orthonormal frames for the tangent space and normal space of $S$ respectively.  We can use the volume form on $\mathcal{M}$ to define a volume form on $S$ by filling $dV_g$ with the normal space frame and pulling back by the inclusion map:
$$
\begin{align}
  dV_{\tilde{g}} &= \iota_S^* (N_n\lrcorner \dots \lrcorner N_{k+1} dV_g) \\
  &= \epsilon^1 \wedge \cdots \wedge \epsilon^k
\end{align}
$$
where $(\epsilon^1,\dots,\epsilon^k)$ is the dual frame for $(E_1,\dots,E_k)$.   Similarly, we can define a probability form on $S$ the same way and renormalizing:
$$
\begin{align}
  dP_{\tilde{g}} &= \frac{1}{Z}\epsilon^1 \wedge \cdots \wedge \epsilon^k \\
  \text{where }\quad Z &= \int_S \epsilon^1 \wedge \cdots \wedge \epsilon^k
\end{align}
$$
The normalization constant is necessary in order for $\int_S dP_{\tilde{g}} = 1$ so that $dP_{\tilde{g}}$ is a probability form on $S$.  The probability density function associated with $dP_{\tilde{g}}$ can be found by applying the $dP_{\tilde{g}}$ on an orthonormal frame on $S$:
$$
\begin{align}
  dP_{\tilde{g}}(E_1,\dots,E_k) &\propto \iota_S^* (N_n\lrcorner \dots \lrcorner N_{k+1} dP_g)(E_1,\dots,E_k) \\
   &\propto (N_n\lrcorner \dots \lrcorner N_{k+1} dP_g)({\iota_S}_* E_1,\dots,{\iota_S}_* E_k) \\
   &= dP_g(N_{k+1},\dots,N_n,E_1,\dots,E_k) \\
   &= \rho \\
   \implies dP_{\tilde{g}} &= \frac{1}{Z}\rho dV_{\tilde{g}}
\end{align}
$$
So the probability density function on any submanifold is proportional to the probability density function in the ambient space.

## Alternate probability forms on submanifolds
There is no unique probability form on $S$ induced by $dP_g$.  We can pullback the probability form on $\mathcal{M}$ and then restrict to $S$:
$$
\begin{align}
  dP_{F^*\tilde{g}_z} &= F^* \frac{1}{Z}\rho_z dV_{\tilde{g}_z} \\
  &= \frac{1}{Z} (\rho_z \circ F) F^* dV_{\tilde{g}_z} \\
  &= \frac{1}{Z} (\rho_z \circ F) dV_{F^*\tilde{g}_z}
\end{align}
$$
where $F:\mathcal{X} \to \mathcal{Z}$ is a diffeomorphism and $(\widetilde{N}_{k+1},\dots,\widetilde{N}_n)$ is a local orthonormal frame for the normal space of $F^{-1}(S)$.  The induced probability density function can be computed using an orthonormal frame on $S$, $(E_1,\dots,E_k)$:
$$
\begin{align}
  dP_{F^*\tilde{g}_z}(E_1,\dots,E_k) &= \frac{1}{Z} (\rho_z \circ F) dV_{F^*\tilde{g}_z}(E_1,\dots,E_k) \\
  &= \frac{1}{Z} (\rho_z \circ F)\det(F^*\tilde{g}_z(E_i,E_j))^\frac{1}{2} \\
  &= \frac{1}{Z} (\rho_z \circ F)\det(F^*g_z(E_i,E_j))^\frac{1}{2}
\end{align}
$$
If $F^{-1}(S)$ is aligned with the coordinate axes, then this expression is equivalent to the change of variables formula on manifolds.

# Probability form decomposition
Let $S\subset \mathcal{X}$ be a submanifold of $\mathcal{M}$ and let $F:\mathcal{X} \to \mathcal{Z}$ be a diffeomorphism.  Locally, let $S^\perp$ denote the submanifold with tangent space equal to the normal space of $S$.  Then we can decompose the probability form on $\mathcal{X}$ into a product of probability forms on $S$, $S^\perp$ and one other term.

First, consider the matrix $M = \begin{bmatrix}A^TA & A^TB \\ B^TA & B^TB\end{bmatrix}$.  We can decompose $\det(M)$ into a product of matrices:
$$
\begin{align}
  \det(M) &= \det\begin{bmatrix}A^TA & A^TB \\ B^TA & B^TB\end{bmatrix}^\frac{1}{2} \\
  &= \det(A^TA)^\frac{1}{2}\det(B^TB - B^T\underbrace{A(A^TA)^{-1}A^T}_{A^\parallel}B)^\frac{1}{2} \\
  &= \det(A^TA)^\frac{1}{2}\det(B^TB)^\frac{1}{2}\det(I - A^\parallel \underbrace{B(B^TB)^{-1}B^T}_{B^\parallel})^\frac{1}{2} \\
  &= \det(A^TA)^\frac{1}{2}\det(B^TB)^\frac{1}{2}\det(I - A^\parallel B^\parallel)^\frac{1}{2}
\end{align}
$$
In log space, we can write this decomposition as:
$$
\begin{align}
  \log\det(M) &= \frac{1}{2}\log\det(A^TA) + \frac{1}{2}\log\det(B^TB) + \frac{1}{2}\underbrace{\log\det(I - A^\parallel B^\parallel)}_{\mathcal{I}}
\end{align}
$$
We can show that $\mathcal{I} \geq 0$ and equals $0$ if and only if $A^TB=0$.

Next, let $E_1,\dots,E_k$ be a local orthonormal frame for $S$ and let $N_{k+1},\dots,N_n$ be a local orthonormal frame for $S^\perp$ that completes the basis for $E_1,\dots,E_k$.  A probability form on $dP_{g_z}$ on $\mathcal{Z}$ can be used to induce probability forms on $S$ and $S^\perp$ using the pullback and restriction operations:
$$
\begin{align}
  dP_{F^*\tilde{g}_z^\parallel} &= \frac{1}{Z^\parallel}\iota_S^* (N_n\lrcorner \dots \lrcorner N_{k+1} dP_{\tilde{g}}) \\
  dP_{F^*\tilde{g}_z^\perp} &= \frac{1}{Z^\perp}\iota_{S^\perp}^* (E_k\lrcorner \dots \lrcorner E_{1} dP_{\tilde{g}})
\end{align}
$$
The probability densities associated with the probability forms can be computed be evaluating the forms on the orthonormal frames which yields:
$$
  \log\rho^\parallel = \log(\rho_z \circ F) + \frac{1}{2}\log\det(F^*g_z(E_i,E_j)) - \log Z^\parallel \\
  \log\rho^\perp = \log(\rho_z \circ F) + \frac{1}{2}\log\det(F^*g_z(N_i,N_j)) - \log Z^\perp
$$
Now, notice that we can factor the ambient space probability density in block form:
$$
\begin{align}
  \log\rho &= \log(\rho_z \circ F) + \frac{1}{2}\log\det\begin{bmatrix}F^*g_z(E_i,E_j) & F^*g_z(E_i,N_j) \\ F^*g_z(N_i,E_j) & F^*g_z(N_i,N_j)\end{bmatrix} \\
       &= \log(\rho_z \circ F) + \frac{1}{2}\log\det(F^*g_z(E_i,E_j)) + \frac{1}{2}\log\det(F^*g_z(N_i,N_j)) + \mathcal{I} \\
       &= \log \rho^\parallel + \log \rho^\perp + (\mathcal{I} + \log Z^\parallel + \log Z^\perp - \log(\rho_z \circ F))
\end{align}
$$

# Incorporating geometric information into generative models
Our goal is to learn the mapping $F: \mathcal{X} \to \mathcal{Z}$ so that we maximize the probability density of the data under the pullback metric $F^*g_z$, with the additional constraint that the the likelihood on $S$ and $S^\perp$ are maximized.