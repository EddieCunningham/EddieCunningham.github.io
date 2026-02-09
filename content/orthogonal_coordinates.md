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

## Rotation coefficients
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

## Connection 1-forms
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
Note that ${\omega_{i}}^{i} = 0$ because $\beta_{ii} = 0$.

## Curvature 2-forms
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
  &= \left(U_i(\beta_{ij}) + \beta_{ij}^2\right) \nu^i \wedge \nu^j - \left(U_j(\beta_{ji}) + \beta_{ji}^2\right) \nu^j \wedge \nu^i + \sum_{k\neq i} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\neq j} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki}\right) \nu^k \wedge \nu^i \\
  &= \left(U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2\right) \nu^i \wedge \nu^j+ \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki}\right) \nu^k \wedge \nu^i
\end{align}
$$
The second term is given by:
$$
\begin{align}
  \sum_k {\omega_{i}}^{k} \wedge {\omega_{k}}^{j} &= \sum_k (\beta_{ik}\nu^k - \beta_{ki}\nu^i) \wedge (\beta_{kj}\nu^j - \beta_{jk}\nu^k) \\
  &= \sum_k \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_k \beta_{ik}\beta_{jk}\nu^k \wedge \nu^k - \sum_k \beta_{ki}\beta_{kj}\nu^i \wedge \nu^j + \sum_k \beta_{ki}\beta_{jk}\nu^i \wedge \nu^k \\
  &= \sum_k \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_k \beta_{ki}\beta_{jk}\nu^k \wedge \nu^i - \left(\sum_k \beta_{ki}\beta_{kj}
  \right)\nu^i \wedge \nu^j \\
  &= \sum_{k\notin\{i,j\}} \beta_{ik}\beta_{kj}\nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \beta_{ki}\beta_{jk}\nu^k \wedge \nu^i - \left(\sum_{k\notin\{i,j\}} \beta_{ki}\beta_{kj}\right)\nu^i \wedge \nu^j
\end{align}
$$
The last line follows from the fact that $\beta_{ii} = 0$.  Combining these two terms, and using Cartan II, we obtain the curvature 2-form explicitly:
$$
\begin{align}
  {\Omega_{i}}^{j}
    &= d{\omega_{i}}^{j} - \sum_k {\omega_{i}}^{k} \wedge {\omega_{k}}^{j} \\
    &= \left(U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2 + \left(\sum_{k\notin\{i,j\}} \beta_{ki}\beta_{kj}\right)\right) \nu^i \wedge \nu^j \\
    \qquad &+ \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) \nu^k \wedge \nu^i \\
\end{align}
$$

And so we are left with our final expression for the curvature 2-forms:
$$
\boxed{
\begin{align}
  {\Omega_{i}}^{j} &= \left(U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2 + \left(\sum_{k\notin\{i,j\}} \beta_{ki}\beta_{kj}\right)\right) \nu^i \wedge \nu^j \\
  &\qquad + \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj}\right) \nu^k \wedge \nu^j - \sum_{k\notin\{i,j\}} \left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) \nu^k \wedge \nu^i
\end{align}
}
$$
Note that ${\Omega_{i}}^{i} = 0$ because $\beta_{ii} = 0$ and because the non-zero terms cancel out.  With this expression, we can compute the entries of the Riemann curvature endomorphism using the equation ${\Omega_{i}}^{j} = \frac{1}{2}{R_{kli}}^j \nu^k \wedge \nu^l$.  Reading off the components, we obtain
$$
\boxed{
\begin{align}
  {R_{kli}}^j = 2\begin{cases}
    U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2 + \left(\sum_{m\notin\{i,j\}} \beta_{mi}\beta_{mj}\right) & \text{if } (k,l,i,j) = (i,j,i,j), \text{and } i \neq j \\
    U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj} & \text{if } (k,l,i,j) = (k,j,i,j), \text{and } k \neq i \neq j \\
    -\left(U_k(\beta_{ji}) + \beta_{ji}\beta_{ki} - \beta_{ki}\beta_{jk}\right) & \text{if } (k,l,i,j) = (k,i,i,j), \text{and } k \neq i \neq j \\
    0 & \text{if } k,l \notin \{i,j\} \text{ or } i = j \\
    -\, {R_{lki}}^{j} & \text{otherwise (by antisymmetry in $k,l$)}
  \end{cases}
\end{align}
}
$$

### Riemann tensor symmetries (component view)

The Riemann tensor satisfies
$$
  R_{abcd} = -R_{bacd} = -R_{abdc},\qquad R_{abcd} = R_{cdab},\qquad R_{a[bcd]}=0.
$$
In particular, for distinct indices:
- For $(i,j,i,j)$ with $i\ne j$:
$$
  R_{ijij} = -R_{jiij} = -R_{ijji} = R_{jiji}.
$$
- For $(k,j,i,j)$ with $k\ne i\ne j$ (and $k$ arbitrary relative to $j$):
$$
\begin{aligned}
  &\{\,R_{kjij},\; -R_{jkij},\; -R_{kjji},\; R_{jkji},\; R_{ijkj},\; -R_{jikj},\; -R_{ijjk},\; R_{jijk}\,\}
\end{aligned}
$$
are all related by the above symmetries (no further independent identities beyond these and Bianchi).
- For $(k,i,i,j)$ with $k\ne i\ne j$:
$$
\begin{aligned}
  &\{\,R_{kiij},\; -R_{ikij},\; -R_{kiji},\; R_{ikji},\; R_{ijki},\; -R_{jiki},\; -R_{ijik},\; R_{jiik}\,\}
\end{aligned}
$$
are likewise related.

The Lamé equation constraints are simply given by the fact that the Riemann curvature tensor must be zero.  Therefore, our final constraints on the orthogonal frame are given by:
$$
\boxed{
\begin{align}
  U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2 + \left(\sum_{m\notin\{i,j\}} \beta_{mi}\beta_{mj}\right) &= 0, \quad \text{for } i \neq j \\
  U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj} &= 0, \quad \text{for } k \neq i \neq j
\end{align}
}
$$


## Lamé equations
We are finally ready to derive the Lamé equations.  The Lamé equations come directly from noting that in flat space, the Riemann curvature tensor must be zero.  Therefore, the following expressions hold:
$$
\begin{align}
  U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2 + \left(\sum_{m\notin\{i,j\}} \beta_{mi}\beta_{mj}\right) &= 0, \quad \text{for } i \neq j \\
  U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj} &= 0, \quad \text{for } k \neq i \neq j
\end{align}
$$
While these expressions can be reduced to the classical Lamé equations, we adopt a slightly different notation to make the connection to log likelihoods more obvious.  Lets take the second equation and rewrite it in terms of the basis $(E_1,\dots,E_n)$.  Term by term, we have:
$$
\begin{align}
  U_k(\beta_{ij}) &= s_k^{-1}\frac{\partial}{\partial z^k}\left(s_i^{-1} \frac{\partial \log s_j}{\partial z^i}\right) \\
  &= s_k^{-1}s_i^{-1}\left(-\frac{\partial \log s_i}{\partial z^k} \frac{\partial \log s_j}{\partial z^i} + \frac{\partial^2 \log s_j}{\partial z^k \partial z^i}\right) \\
\end{align}
$$
$$
\begin{align}
  \beta_{ij}\beta_{kj} &= s_i^{-1}s_k^{-1}\frac{\partial \log s_j}{\partial z^i}\frac{\partial \log s_j}{\partial z^k}
\end{align}
$$
$$
\begin{align}
  \beta_{ik}\beta_{kj} &= s_i^{-1}s_k^{-1}\frac{\partial \log s_k}{\partial z^i}\frac{\partial \log s_j}{\partial z^k}
\end{align}
$$
Putting the terms together, we obtain:
$$
\begin{align}
  U_k(\beta_{ij}) + \beta_{ij}\beta_{kj} - \beta_{ik}\beta_{kj} &= s_k^{-1}s_i^{-1}\left(-\frac{\partial \log s_i}{\partial z^k} \frac{\partial \log s_j}{\partial z^i} + \frac{\partial^2 \log s_j}{\partial z^k \partial z^i} + \frac{\partial \log s_j}{\partial z^i}\frac{\partial \log s_j}{\partial z^k} - \frac{\partial \log s_k}{\partial z^i}\frac{\partial \log s_j}{\partial z^k}\right)
\end{align}
$$
This gives us the following expression for the second Lamé equation:
$$
\boxed{
\begin{align}
  \frac{\partial^2 \log s_j}{\partial z^k \partial z^i} = \frac{\partial \log s_i}{\partial z^k} \frac{\partial \log s_j}{\partial z^i} + \frac{\partial \log s_k}{\partial z^i}\frac{\partial \log s_j}{\partial z^k} - \frac{\partial \log s_j}{\partial z^i}\frac{\partial \log s_j}{\partial z^k}, \quad \text{where } k \neq i \neq j
\end{align}
}
$$

For the first Lamé equation, we can also go term by term:

#### Term 1
$$
\begin{align}
  U_i(\beta_{ij}) &= s_i^{-1}\frac{\partial}{\partial z^i}\left(s_i^{-1} \frac{\partial \log s_j}{\partial z^i}\right) \\
  &= s_i^{-1}\frac{\partial s_i^{-1}}{\partial z^i}\frac{\partial \log s_j}{\partial z^i} + s_i^{-2}\frac{\partial^2 \log s_j}{\partial z^i\partial z^i} \\
  &= s_i^{-2}\left(-\frac{\partial \log s_i}{\partial z^i}\frac{\partial \log s_j}{\partial z^i} + \frac{\partial^2 \log s_j}{\partial z^i\partial z^i}\right)
\end{align}
$$
#### Term 2
$$
\begin{align}
  U_j(\beta_{ji}) &= s_j^{-2}\left(-\frac{\partial \log s_j}{\partial z^j}\frac{\partial \log s_i}{\partial z^j} + \frac{\partial^2 \log s_i}{\partial z^j\partial z^j}\right)
\end{align}
$$
#### Term 3
$$
\begin{align}
  \beta_{ij}^2 &= s_i^{-2}\frac{\partial \log s_j}{\partial z^i}\frac{\partial \log s_j}{\partial z^i}
\end{align}
$$
#### Term 4
$$
\begin{align}
  \beta_{ji}^2 &= s_j^{-2}\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^j}
\end{align}
$$
#### Term 5
$$
\begin{align}
  \sum_{m\notin\{i,j\}} \beta_{mi}\beta_{mj} &= \sum_{m\notin\{i,j\}} s_m^{-2}\frac{\partial \log s_i}{\partial z^m}\frac{\partial \log s_j}{\partial z^m}
\end{align}
$$

Collecting the five terms of the first Lamé equation and simplifying, we obtain the component form
that depends only on derivatives of the Lamé coefficients
$$
\begin{aligned}
s_i^{-2}\Big( \frac{\partial^2 \log s_j}{\partial z^i \partial z^i}
      - \frac{\partial \log s_i}{\partial z^i}\frac{\partial \log s_j}{\partial z^i}
      + \left(\frac{\partial \log s_j}{\partial z^i}\right)^2 \Big)
     + s_j^{-2}\Big( \frac{\partial^2 \log s_i}{\partial z^j \partial z^j}
      - \frac{\partial \log s_j}{\partial z^j}\frac{\partial \log s_i}{\partial z^j}
      + \left(\frac{\partial \log s_i}{\partial z^j}\right)^2 \Big) + \sum_{m\notin\{i,j\}} s_m^{-2}\frac{\partial \log s_i}{\partial z^m}\frac{\partial \log s_j}{\partial z^m} \,=\, 0,\qquad i\ne j
\end{aligned}
$$
which is gives us the following expression for the first Lamé equation:
$$
\boxed{
\begin{aligned}
  s_i^{-2}\Big( \frac{\partial^2 \log s_j}{\partial z^i \partial z^i}
      + \left(\frac{\partial \log s_j}{\partial z^i}\right)^2 \Big)
     + s_j^{-2}\Big( \frac{\partial^2 \log s_i}{\partial z^j \partial z^j}
      + \left(\frac{\partial \log s_i}{\partial z^j}\right)^2 \Big) + \sum_{m} s_m^{-2}\frac{\partial \log s_i}{\partial z^m}\frac{\partial \log s_j}{\partial z^m} \,=\, 0,\qquad i\ne j
\end{aligned}
}
$$

## Sectional curvature

Sectional curvature measures how a chosen 2‑plane bends. Given the orthonormal frame
$\{U_1,\dots,U_n\}$, the sectional curvature of the plane spanned by $U_i$ and $U_j$ ($i\ne j$)
is read directly from the curvature 2‑form $\Omega_i{}^{\,j}$ as the coefficient of
$\nu^i\wedge\nu^j$:
$$
  \boxed{\;K_{ij} = U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2
  + \sum_{m\notin\{i,j\}} \beta_{mi}\,\beta_{mj}\;},\quad i\ne j.
$$
This is the classical expression in orthogonal coordinates (via Lamé coefficients). Positive $K_{ij}$
indicates locally sphere‑like bending of the $ij$‑plane; negative values indicate saddle‑like bending.
The $\beta$’s package all dependence on the Lamé coefficients and their derivatives.

Sectional curvature is the most local, plane‑wise notion of curvature. Aggregating these over all
planes through a direction produces Ricci curvature.

Convention. We use the sign convention (consistent with $\Omega_i{}^{\,j} = \tfrac12 R_{k\,l\,i}{}^{j}\, \nu^k \wedge \nu^l$):
$$
  K(U_i,U_j) \,=\, Rm(U_i,U_j,U_j,U_i) \,=\, -\,Rm(U_i,U_j,U_i,U_j).
$$
With this normalization, the coefficient of $\nu^i\wedge\nu^j$ displayed above equals $K_{ij}$.
Equivalently,
$$
  R_{ijij} \,=\, -2\,K_{ij}.
$$

## Ricci curvature

Ricci curvature summarizes how volumes deform: it is the trace (over the plane directions) of the
curvature endomorphism. Equivalently, it averages sectional curvatures through a given direction.
Let $\{U_i\}$ be the orthonormal frame and $\{\nu^i\}$ its dual. With $\Omega_i{}^{\,j} = \tfrac12 R_{k\,l\,i}{}^{j} \, \nu^k \wedge \nu^l$,
the Ricci tensor is the trace on the first and last indices:
$$
  \operatorname{Ric}(U_i, U_j) = \sum_{m=1}^n \big\langle R(U_m, U_i)U_j, U_m\big\rangle
  = \sum_{m=1}^n R_{m\,i\,j}{}^{m}.
$$
In particular, by antisymmetry in the first two indices, the diagonal components are sums of
sectional curvatures through $U_i$:
$$
  \boxed{\operatorname{Ric}_{ii} = \sum_{j\ne i} K_{ij}},\quad\text{where } K_{ij} = \big\langle R(U_i,U_j)U_j, U_i\big\rangle.
$$
Using the explicit expression for the curvature 2-forms from above, the sectional curvature of the
plane spanned by $U_i, U_j$ (with $i\ne j$) equals the coefficient of $\nu^i \wedge \nu^j$ in
$\Omega_i{}^{\,j}$:
$$
  K_{ij} \,=\, U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2
  + \sum_{m\notin\{i,j\}} \beta_{mi}\,\beta_{mj}.
$$
Consequently, the diagonal Ricci components are given explicitly by
$$
  \boxed{\operatorname{Ric}_{ii}
    = \sum_{j\ne i} \Big( U_i(\beta_{ij}) + U_j(\beta_{ji}) + \beta_{ij}^2 + \beta_{ji}^2
      + \sum_{m\notin\{i,j\}} \beta_{mi}\,\beta_{mj} \Big)}.
$$
The scalar curvature is then
$$
  \boxed{\mathrm{Scal} = \sum_{i=1}^n \operatorname{Ric}_{ii} = 2 \sum_{1\le i<j\le n} K_{ij}}.
$$

For completeness, the off-diagonal Ricci components can be obtained from
$\operatorname{Ric}_{ij} = \sum_{m} R_{m\,i\,j}{}^{m}$. Using the decomposition of
$\Omega_i{}^{\,j}$ into $\nu^k\wedge\nu^j$ and $\nu^k\wedge\nu^i$ parts above, this becomes
$$
  \operatorname{Ric}_{ij} = \sum_{k\notin\{i,j\}}
    \Big( U_k(\beta_{ij}) + \beta_{ij}\,\beta_{kj} - \beta_{ik}\,\beta_{kj}
          - U_k(\beta_{ji}) - \beta_{ji}\,\beta_{ki} + \beta_{ki}\,\beta_{jk} \Big),\quad i\ne j,
$$
which is symmetric in $i,j$ after applying the identities satisfied by the rotation coefficients.

## Conceptual clarifications

- Coordinates vs curvature.
  - Existence of (even global) coordinates $z$ makes the manifold diffeomorphic to $\mathbb{R}^n$; it does not determine curvature. Curvature is a property of the metric/connection, not the topology.

- What metric are we using?
  - Declaring an orthonormal frame $\{U_i\}$ with dual coframe $\{\nu^i\}$ defines the metric by
    $$g = \sum_i \nu^i \otimes \nu^i.$$
    In orthogonal coordinates with $\nu^i = s_i\,dz^i$, this is the diagonal metric
    $$g = \sum_i s_i(z)^2\,(dz^i)^2.$$
    This is not a convenience choice; it is the unique metric that makes $\{U_i\}$ orthonormal.

- Scaled commutation vs commuting orthonormal frame.
  - The condition $[s_i U_i, s_j U_j]=0$ (for $i\ne j$) is precisely Frobenius integrability of the diagonal coframe: $\nu^i = s_i\,dz^i$ for some coordinates $z$ and $\beta_{ij} = U_i(\log s_j)$.
  - A commuting orthonormal frame $[U_i, U_j]=0$ is stronger; it yields orthonormal coordinates (so $s_i\equiv 1$) and hence flatness.

- Recovering Euclidean coordinates $x$ from orthogonal $z$.
  - Write $dx = Q\,\nu$ with $Q:U\to O(n)$. Exactness $d(dx)=0$ is equivalent to $dQ + Q\,\omega = 0$.
  - Integrability is $\Omega = d\omega - \omega\wedge\omega \equiv 0$. On simply connected domains, $\Omega\equiv 0$ (the Lamé system) $\iff$ there exist Euclidean coordinates $x$ (unique up to rigid motion).

- Why scaled commutation is weaker than Lamé.
  - Scaled commutation enforces first‑order integrability (orthogonal coordinates) but does not impose the second‑order compatibility among rotation coefficients required by $\Omega\equiv 0$.
  - Example in $n=2$: $s_1\equiv 1$, $s_2(z)=e^{a z^1}$ gives $[s_1U_1, s_2U_2]=0$ while $K_{12}=a^2>0$.

- Rule of thumb.
  - “Integrable orthogonal coframe” $\Rightarrow$ you have $z$ and $s_i$.
  - “Flatness (Lamé)” $\Rightarrow$ you can solve for Euclidean $x$ via $dx = Q\,\nu$.

Setup
-----
Let (E_1, …, E_n) be a local orthonormal frame (column vector E),
and let ω = (ω^i_j) be the Levi–Civita connection 1-form, defined by
    ∇E_i = ω^k_i E_k .
In matrix form this is  ∇E = E ω.

Change of frame
---------------
Rotate the frame by a point-dependent A(x) ∈ SO(n):
    Ē = E A            (A is an n×n matrix of functions)
Define the new connection 1-form ω̃ by  ∇Ē = Ē ω̃.

Gauge-transformation law
------------------------
∇Ē
 = ∇(E A)
 = (∇E) A + E (dA)                (Leibniz rule; dA is the matrix of 1-forms of the entries of A)
 = (E ω) A + E (dA)
 = E (ω A + dA).

But also  ∇Ē = Ē ω̃ = E A ω̃.
Left-multiply by A⁻¹:
    ω̃ = A⁻¹ ω A + A⁻¹ dA.         (1)

Infinitesimal version (variation)
---------------------------------
Write A = I + a + O(a²) with a(x) ∈ so(n) a skew-symmetric 0-form (matrix of functions).
Then A⁻¹ = I − a + O(a²), and dA = da + O(a²).
Plug into (1) and keep terms linear in a:
    ω̃ = (I − a) ω (I + a) + (I − a) da + O(a²)
        = ω + [ω, a] + da + O(a²).

Therefore the first-order variation is
    δω = da + [ω, a].              (2)

Meaning of [ω, a]
-----------------
a is a 0-form (matrix of functions), ω is a matrix of 1-forms.
The bracket is the usual Lie-algebra commutator (ordinary matrix product since a is a 0-form):
    [ω, a] = ω a − a ω.

Component form
--------------
If ω = (ω^i_j) and a = (a^i_j), then
    (δω)^i_j = d a^i_j + ω^i_k a^k_j − a^i_k ω^k_j.

If you further expand each 1-form ω^i_j in a coframe {θ^α},
    ω^i_j = ω^i_{jα} θ^α,
then
    (δω)^i_{jα} = E_α(a^i_j) + ω^i_{kα} a^k_j − a^i_k ω^k_{jα}.

Checks
------
• a_{ij} = −a_{ji} and ω_{ij} = −ω_{ji}, so δω stays skew-symmetric as required.
• If a ≡ 0 there is no change: δω = 0.
• At a point where ω ≡ 0 (normal frame), δω = da at that point.