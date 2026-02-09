Title: Orthogonal coordinates
Date: 2025-09-14
Category: Blog
Slug: orthogonal-coordinates
hidden: true
Summary: Orthogonal coordinates

In this post we'll go over orthogonal coordinate systems and the restrictions that curvature imposes on them.

# Orthogonal coordinates
Let $z = (z^1, \dots, z^n)$ be a coordinate system in $\mathbb{R}^n$ that is associated with the chart $\phi: \mathcal{U} \to \mathbb{R}^n$.  This coordinate chart defines a mapping between the coordinates and $x \in \mathbb{R}^n$ via the equation $x = \phi(z)$.  The partial derivatives of $\phi$ with respect to each individual yields basis vectors, which we denote by $E_i$.  In terms of the coordinates, we have that:
$$
\begin{align}
  E_i = \frac{\partial}{\partial z^i}
\end{align}
$$
The coordinate system is said to be orthogonal if the basis vectors are orthogonal to each other, with respect to the Riemannian metric.  This is given by:
$$
\begin{align}
  g(E_i, E_j) = 0, \quad \text{where } i \neq j
\end{align}
$$
Note that this is not an orthonormal restriction because we allow $g(E_i, E_i) \neq 1$.  In this setting, the coordinate of the basis vectors can be written as the product of a column of an orthogonal matrix and a scalar:
$$
\begin{align}
  E_i = U_{ji}s_i \frac{\partial}{\partial x^j}
\end{align}
$$
Traditionally, each $s_i$ is called the Lamé coefficient and it is well known that there are constraints that the Lamé coefficients must satisfy in order for the coordinate system to be orthogonal.  We will derive these constraints in the next section.

# Curvature constraints on the Lamé coefficients
Since our space is flat, the Riemann curvature tensor must be zero.  However, if one derives out the components of the Riemann curvature tensor, we find non-zero entries that depend on the Lamé coefficients.  These restrictions are called the Lamé equations.  In this section, we will derive the Lamé equations.

### Rotation coefficients
The standard approach to deriving the Lamé equations is to compute the curvature 2-form, using the Levi-Civita connection, and setting it to zero.  To do this, we start by constructing an orthonormal frame and coframe from the basis vectors.  Let $(U_1,\dots,U_n)$ be an orthonormal frame, where $U_i = \frac{1}{s_i}E_i$ and $(\nu^1,\dots,\nu^n)$ be the corresponding coframe, where $\nu^i = s_i dz^i$.  In coordinates, these are given by:
$$
\begin{align}
  U_i = \frac{1}{s_i}\frac{\partial}{\partial z^i} = U_{ji}\frac{\partial}{\partial x^j} \\
  \nu^i = s_i dz^i = U_{ji}dx^j
\end{align}
$$

This orthonormal frame and coframe represent the directions that the coordinate system is aligned with.  The first item that we need is the exterior derivative of the coframe.
$$
\begin{align}
  d \nu^j &= d(s_j dz^j) \\
  &= ds_j \wedge dz^j \\
  &= \left(U_i(s_j)\nu^i\right) \wedge \left(\frac{1}{s_j}\nu^j\right) \\
  &= U_i(\log s_j)\nu^i \wedge \nu^j \\
  &=: \beta_{ij}\nu^i \wedge \nu^j
\end{align}
$$
The functions $\beta_{ij}$ are called the rotation coefficients.  We also have that $\beta_{ii} = 0$ because $\nu^i \wedge \nu^i = 0$.  In component form, we have that:
$$
\begin{align}
  \boxed{d\nu^j = \beta_{ij}\nu^i \wedge \nu^j, \quad \text{where } \beta_{ij} = \frac{1}{s_i}\frac{\partial \log s_j}{\partial z^i} = U_{ki}\frac{\partial \log s_j}{\partial x^k}}
\end{align}
$$

### Connection 1-forms
To understand the geometry of the space, we need to compute the Levi-Civita connection 1-forms, which we will denote by ${\omega_{i}}^{j}$.  These one-forms define the covariant derivative with respect to the orthonormal frame via the equation:
$$
\begin{align}
  \nabla_{X} U_i = {\omega_{i}}^{j}(X)U_j
\end{align}
$$
for all vector fields $X$.  The connection 1-forms are uniquely defined using the Levi-Civita connection, which says that the connection should be torsion-free, and metric-compatible.  The torsion-free condition is given by Cartan's first structure equation, which says that:
$$
\begin{align}
  d\nu^j = \nu^i \wedge {\omega_{i}}^{j}
\end{align}
$$
While metric compatibility implies that ${\omega_{i}}^{j} = -{\omega_{j}}^{i}$ because
$$
\begin{align}
  0 &= \nabla_X g(U_i, U_j) \\
  &= g(\nabla_X U_i, U_j) + g(U_i, \nabla_X U_j) \\
  &= g({\omega_{i}}^{k}(X)U_k, U_j) + g(U_i, {\omega_{j}}^{l}(X)U_l) \\
  &= {\omega_{i}}^{j}(X) + {\omega_{j}}^{i}(X)
\end{align}
$$

Using these two equations, and the expression that we derived for $d\nu^j$ using the rotation coefficients, we can solve for the connection 1-forms.  Suppose that ${\omega_{i}}^{j} = {\omega_{ik}}^{j}\nu^k$.  Then we have that:
$$
\begin{align}
  \beta_{ij}\nu^i \wedge \nu^j &= \nu^i \wedge {\omega_{i}}^{j} = -\nu^i \wedge {\omega_{j}}^{i} \\
  &= {\omega_{ik}}^{j}\nu^i \wedge \nu^k \\
  &= -{\omega_{jk}}^{i}\nu^i \wedge \nu^k
\end{align}
$$
From these expressions, we have that
$$
\begin{align}
  {\omega_{ik}}^{j} = -{\omega_{jk}}^{i} = \beta_{ij}\delta_k^j
\end{align}
$$
from which we derive
$$
\begin{align}
  {\omega_{ik}}^{j} = \beta_{ij}\delta_k^j = -\beta_{ji}\delta_k^i
\end{align}
$$
so the connection 1-forms are given by:
$$
\begin{align}
  \boxed{{\omega_{i}}^{j} = \beta_{ij}\nu^j - \beta_{ji}\nu^i}
\end{align}
$$

### Curvature 2-forms
The last step is to compute the curvature 2-forms, which we will denote by ${\Omega_{i}}^{j}$, defined by:
$$
\begin{align}
  {\Omega_{i}}^{j} = \frac{1}{2}{R_{kli}}^j \nu^k \wedge \nu^l
\end{align}
$$
where ${R_{kli}}^j$ are the components of the Riemann curvature endomorphism.  Cartan's second structure equation gives us a way to compute the curvature 2-forms.  It says that:
$$
\begin{align}
  {\Omega_{i}}^{j} = d{\omega_{i}}^{j} - \sum_k {\omega_{i}}^{k} \wedge {\omega_{k}}^{j}
\end{align}
$$
We can do a direct computation of the curvature 2-forms using the connection 1-forms.  First, the exterior derivative of the connection 1-form is given by:
$$
\begin{align}
  d{\omega_{i}}^{j} &= d(\beta_{ij}\nu^j - \beta_{ji}\nu^i) \\
  &= d\beta_{ij} \wedge \nu^j + \beta_{ij}d\nu^j - d\beta_{ji} \wedge \nu^i - \beta_{ji}d\nu^i \\
  &= \sum_k \left(U_k(\beta_{ij})\nu^k \wedge \nu^j\right) + \beta_{ij}\sum_k \left(\beta_{kj}\nu^k \wedge \nu^j\right) - \sum_k \left(U_k(\beta_{ji})\nu^k \wedge \nu^i\right) - \beta_{ji}\sum_k \left(\beta_{ki}\nu^k \wedge \nu^i\right) \\
  &= \sum_k \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_k \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki}\right) \nu^k \wedge \nu^i \\
  &= \left(U_i(\beta_{ij}) + \beta_{ij}\beta_{ij}\right) \nu^i \wedge \nu^j - \left(U_j(\beta_{ji}) + \beta_{ji}\beta_{ji}\right) \nu^j \wedge \nu^i + \sum_{k\neq i} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\neq j} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki}\right) \nu^k \wedge \nu^i \\
  &= \left(U_i(\beta_{ij}) - U_j(\beta_{ji}) + \beta_{ij}\beta_{ij} - \beta_{ji}\beta_{ji}\right) \nu^i \wedge \nu^j+ \sum_{k\neq i} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\neq j} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki}\right) \nu^k \wedge \nu^i \\
\end{align}
$$
The second term is given by:
$$
\begin{align}
  \sum_k {\omega_{i}}^{k} \wedge {\omega_{k}}^{j} &= \sum_k (\beta_{ik}\nu^k - \beta_{ki}\nu^i) \wedge (\beta_{kj}\nu^j - \beta_{jk}\nu^k) \\
  &= \sum_k \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_k \beta_{ik}\beta_{jk}\nu^k \wedge \nu^k - \sum_k \beta_{ki}\beta_{kj}\nu^i \wedge \nu^j + \sum_k \beta_{ki}\beta_{jk}\nu^i \wedge \nu^k \\
  &= \sum_k \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_k \beta_{ki}\beta_{jk}\nu^k \wedge \nu^i - \left(\sum_k \beta_{ki}\beta_{kj}
  \right)\nu^i \wedge \nu^j \\
  &= \sum_{k\neq i} \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_{k\neq i} \beta_{ki}\beta_{jk}\nu^k \wedge \nu^i - \left(\left(\sum_k \beta_{ki}\beta_{kj}\right) - \beta_{ii}\beta_{ij} - \beta_{ji}\beta_{jj}\right)\nu^i \wedge \nu^j \\
\end{align}
$$
Combining these two terms, and using Cartan II, we obtain the curvature 2-form explicitly:
$$
\begin{align}
  {\Omega_{i}}^{j}
    &= d{\omega_{i}}^{j} - \sum_k {\omega_{i}}^{k} \wedge {\omega_{k}}^{j} \\
    &= \left(U_i(\beta_{ij}) - U_j(\beta_{ji}) + \beta_{ij}\beta_{ij} - \beta_{ji}\beta_{ji} + \left(\sum_k \beta_{ki}\beta_{kj}\right) - \beta_{ii}\beta_{ij} - \beta_{ji}\beta_{jj}\right) \nu^i \wedge \nu^j \\
    \qquad &+ \sum_{k\neq i} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\neq j} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) \nu^k \wedge \nu^i \\
    &= \left(U_i(\beta_{ij}) - U_j(\beta_{ji}) + \underbrace{\beta_{ij}\beta_{ij} - \beta_{ji}\beta_{ji}}_{=0} + \left(\sum_{k\notin\{i,j\}} \beta_{ki}\beta_{kj}\right)\right) \nu^i \wedge \nu^j \\
    \qquad &+ \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) \nu^k \wedge \nu^i \\
\end{align}
$$
The squared beta terms cancel because $\beta_{ij}\beta_{ij} = U_{ai}U_{bi}\frac{\partial \log s_j}{\partial x^a}\frac{\partial \log s_j}{\partial x^b} = \beta_{ji}\beta_{ji}$.

And so we are left with our final expression for the curvature 2-forms:
$$
\boxed{
\begin{align}
  {\Omega_{i}}^{j} &= \left(U_i(\beta_{ij}) - U_j(\beta_{ji}) + \left(\sum_{k\notin\{i,j\}} \beta_{ki}\beta_{kj}\right)\right) \nu^i \wedge \nu^j \\
  &\qquad + \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) \nu^k \wedge \nu^i
\end{align}
}
$$

### Ricci curvature
