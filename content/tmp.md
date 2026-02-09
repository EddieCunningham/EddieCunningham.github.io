Title: Lamé coefficients (clean revision)
Date: 2025-09-12
Category: Notes
Slug: lame-coefficients-clean
hidden: true
Summary: Orthogonal coordinates with corrected Lamé equations, curvature components, and Hessian change-of-variables.

# Orthogonal coordinates
Let $z=(z^1,\dots,z^n)$ be an **orthogonal** coordinate chart on Euclidean space with Lamé (scale) factors $s_i(z)>0$ so that
$$
 g \;=\; \sum_{i=1}^n s_i(z)^2\,(dz^i)^2.
$$
Equivalently, if $x=F(z)$ and $J=\partial x/\partial z$ is the Jacobian, then
$$
 J^{\top}J \;=\; \operatorname{diag}(s_1^2,\dots,s_n^2).
$$
Introduce the orthonormal coframe $\theta^i := s_i\,dz^i$ with dual frame $e_i := s_i^{-1}\,\partial_{z^i}$.

# Christoffel symbols (diagonal metric)
For $g_{ij}=s_i^2\,\delta_{ij}$ the nonzero Christoffel symbols are
$$
\Gamma^i_{ii}=\partial_{z^i}\!\ln s_i,\qquad
\Gamma^i_{ij}=\partial_{z^j}\!\ln s_i\ (i\ne j),\qquad
\Gamma^i_{jj}=-\Big(\tfrac{s_j}{s_i}\Big)^{\!2}\partial_{z^i}\!\ln s_j\ (i\ne j),
$$
with all others zero when the three indices are pairwise distinct.

# Rotation coefficients and connection (orthonormal frame)
Define the (dimensionless) rotation coefficients
$$
\beta_{ij}:=e_j(\ln s_i)=\frac{1}{s_j}\,\partial_{z^j}\!\ln s_i\quad (i\ne j),\qquad \beta_{ii}=0.
$$
Then the Levi–Civita connection 1-forms are
$$
\omega_{ij}=\beta_{ij}\,\theta^i-\beta_{ji}\,\theta^j\qquad(\omega_{ij}=-\omega_{ji}).
$$

# Flatness and the Lamé equations (correct index conditions)
In Euclidean space written in orthogonal coordinates, the curvature tensor vanishes. This yields the Lamé system.

## First Lamé equation (from $R_{ijik}=0$)
For **pairwise distinct** indices $i,j,k$:
$$
\boxed{\ \partial_{z^k}\!\big( s_j^{-1}\,\partial_{z^j}s_i\big)
= s_k^{-1}\,\partial_{z^k}s_j\;\cdot\; s_j^{-1}\,\partial_{z^j}s_i
\;+ \;
 s_k^{-1}\,\partial_{z^k}s_i\;\cdot\; s_i^{-1}\,\partial_{z^i}s_j\ }.
$$
Equivalently, in logarithmic form (same distinctness requirement):
$$
\boxed{\ \partial_{z^j}\partial_{z^k}\ln s_i
= (\partial_{z^j}\!\ln s_i)(\partial_{z^k}\!\ln s_j)
+ (\partial_{z^j}\!\ln s_k)(\partial_{z^k}\!\ln s_i)
- (\partial_{z^j}\!\ln s_i)(\partial_{z^k}\!\ln s_i)\ }.
$$

## Second Lamé equation (from $R_{ijij}=0$)
For $i\ne j$:
$$
\boxed{\ \partial_{z^j}\!\big( s_j^{-1}\,\partial_{z^j}s_i\big)
+\partial_{z^i}\!\big( s_i^{-1}\,\partial_{z^i}s_j\big)
+\sum_{k\ne i,\,k\ne j} s_k^{-2}\,\partial_{z^k}s_i\,\partial_{z^k}s_j=0\ }.
$$

# Curvature components (for reference)
In the orthonormal frame $\{e_i\}$ with $\beta_{ij}=e_j\ln s_i$, the only independent nonzero components for distinct indices are
$$
R_{ijik}= e_k\beta_{ij}-\beta_{ik}\,\beta_{kj},\qquad
R_{ijij}= -\big(e_i\beta_{ij}+e_j\beta_{ji}\big)-\sum_{k\ne i,j}\beta_{ik}\,\beta_{jk},
$$
and all components with four distinct indices vanish. Setting these to zero reproduces the Lamé equations above.

# Change of variables for the Hessian of $\log p$
Let $x=F(z)$ be a diffeomorphism with Jacobian $J=\partial x/\partial z$. The $x$-Hessian of $\log p$ relates to $z$ by
$$
J^{\top} H_x J
= H_z\big(\log p(F(z))\big)
\; -\; \sum_{j=1}^n \big(\partial_{z^j}\log p(F(z))\big)\, H_z(x^j).
$$
In orthogonal coordinates, this identity simplifies to the decomposition
$$
\boxed{\ H_x
= \sum_{i=1}^n (\nabla_x\!\ln s_i)(\nabla_x\!\ln s_i)^{\top}
\; + \; \sum_{j=1}^n (J^{-\top}e_j)(J^{-\top}e_j)^{\top}\,\Big\langle \nabla_z \Big(\tfrac12 s_j^2\Big),\ \nabla_z \log p(F)\Big\rangle_{g^{-1}}\ }.
$$
Here $e_j$ is the $j$-th standard basis vector in $\mathbb{R}^n$, $\nabla_x\!\ln s_i = J^{-\top}\,\nabla_z\!\ln s_i$, and the co-metric inner product is
$$
\langle u,v\rangle_{g^{-1}} := \sum_{\ell=1}^n s_\ell^{-2}\,u_\ell v_\ell.
$$
This form makes explicit (i) the contribution from coordinate scaling via the gradients of $\ln s_i$, and (ii) the anisotropic contraction (with $g^{-1}$) of the interaction between $\nabla_z(\tfrac12 s_j^2)$ and $\nabla_z\log p(F)$, transported to $x$-space by $J^{-\top}$.

# Conventions cross-walk (rotation coefficients)
Some references define $\beta^{\mathrm{src}}_{ij}:=\partial_{z^i} s_j / s_i$ for $i\ne j$. Our convention $\beta_{ij}= e_j\ln s_i = s_j^{-1}\partial_{z^j}\ln s_i$ satisfies
$$
\beta_{ij} = \frac{\beta^{\mathrm{src}}_{ji}}{s_i},
$$
so curvature and the Lamé equations agree after converting conventions.

---

**Summary:** We use consistent Lamé factors $s_i$, impose the correct distinctness conditions in the Lamé equations, and express the Hessian change-of-variables with the co-metric contraction and $J^{-1}$/$J^{-\top}$ explicitly.