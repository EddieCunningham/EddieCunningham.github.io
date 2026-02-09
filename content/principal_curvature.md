Title: Principal Curvature
Date: 2025-05-18
Category: Blog
Slug: principal_curvature
hidden: true
Summary: Principal Curvature

## Overview
The prinicpal curvatures of an embedded Riemannian submanifold can be used to construct a good, orthogonal coordinate system on the submanifold.  Let $F: \mathcal{Z}=\mathbb{R}^n \to \mathcal{X}$ be a diffeomorphism between an $n$-dimensional coordinate space and a Riemannian submanifold $(\mathcal{X}=\mathbb{R}^n, \bar{g})$, where $\bar{g}$ is the Euclidean metric on $\mathbb{R}^n$.  Let $z^i$ be the coordinates on $\mathcal{Z}$ and let $x^i$ be the coordinates on $\mathcal{X}$.  Consider setting the last coordinate, $n$, to be a constant value so that the image of the $\mathcal{Z}^{(1:n-1)}$ is an $(n-1)$-dimensional submanifold $\mathcal{M} \subset \mathcal{X}$.  Our goal will be to understand the principal curvatures of $\mathcal{M}$ in terms of the transformation $F$.  To begin, we will need to know various geometric quantities of $\mathcal{M}$ in terms of the coordinates $z^i$.

## Induced Metric
Suppose that $\pi_z: \mathcal{Z} \to \mathcal{Z}^{1:n-1}$ drops the last coordinate of $\mathcal{Z}$ and let $\pi_z^{-1}$ be a section of $\pi_z$.  Then we can define a corresponding projection map $\pi_x: \mathcal{X} \to \mathcal{X}^{1:n-1}$ by $\pi_x = F\circ \pi_z^{-1} \circ \pi_z \circ F^{-1}$.  The coordinates of the induced metric on $\mathcal{Z}^{1:n-1}$ are given by:
$$
\begin{align}
  g &:= \left(F\circ \pi_z^{-1}\right)^*\bar{g} \\
  &= \left(F\circ \pi_z^{-1}\right)^* \delta_{ij}dx^i \otimes dx^j, \quad i,j=1,\dots,n \\
  &= \delta_{ij}\left(\left(F\circ \pi_z^{-1}\right)^*dx^i \otimes \left(F\circ \pi_z^{-1}\right)^*dx^j\right) \\
  &= \delta_{ij}\left(J^i_u dz^u \otimes J^j_v dz^v\right), \quad u,v=1,\dots,n-1 \\
  &= (J^TJ)_{u,v} dz^u \otimes dz^v
\end{align}
$$

Similarly, the coordinates of the induced metric on $\mathcal{X}^{1:n-1}$ are given by summing over all of the dual basis elements:
$$
\begin{align}
  \bar{g} &= (J^TJ)_{u,v} dz^u \otimes dz^v, \quad u,v=1,\dots,n-1
\end{align}
$$

## Christoffel Symbols
Let $g$ be the metric on $\mathcal{Z}^{1:n-1}$.  We can compute the components of the Christoffel symbols of $g$ as follows:
$$
\begin{align}
  \Gamma_{ij}^k &= \frac{1}{2}{g}^{kl}\left(\partial_i {g}_{jl} + \partial_j {g}_{il} - \partial_l {g}_{ij}\right)
\end{align}
$$

To compute the Christoffel symbols, we need to expand the metric components in terms of $J$ to get the following expression:
$$
\begin{align}
  \partial_k g_{i,j} &= \partial_k (J^T J)_{i,j} \\
  &= \partial_k \left(J^m_i J^m_j \right) \\
  &= (\partial_k J^m_i) J^m_j + J^m_i (\partial_k J^m_j)
\end{align}
$$
Since $J^i_j = \frac{\partial x^i}{\partial z^j}$ and $\partial_k = \frac{\partial}{\partial z^k}$ we get the symmetry $\partial_k J^i_j = \partial_j J^i_k$, and so we can simplify the Christoffel symbols as follows:
$$
\begin{align}
\Gamma_{ij}^k &= \frac{1}{2}{g}^{kl}\left(\partial_i {g}_{jl} + \partial_j {g}_{il} - \partial_l {g}_{ij}\right) \\
&= \frac{1}{2}{g}^{kl}\left((\partial_i J^m_j J^m_l + \cancel{J^m_j \partial_i J^m_l}) + (\partial_j J^m_i J^m_l + \cancel{J^m_i \partial_j J^m_l}) - (\cancel{\partial_l J^m_i J^m_j} + \cancel{J^m_i \partial_l J^m_j})\right) \\
&= {g}^{kl}J^m_l \partial_i J^m_j \\
&= \left((J^TJ)^{-1}J\right)^k_m \partial_i J^m_j \\
&= \left(J^+\right)^k_m \partial_i J^m_j
\end{align}
$$

Therefore, the Christoffel symbols for the Levi-Civita connection on $\mathcal{Z}^{1:n-1}$ are given by:
$$
\begin{align}
  \Gamma_{ij}^k &= \sum_{m=1}^{n} \left(J^+\right)^k_m \partial_i J^m_j, \quad i,j,k=1,\dots,n-1
\end{align}
$$

## Covariant Derivative
Using the Christoffel symbols, we can compute the covariant derivative with respect to the manifold.  Suppose $\partial_i$ denotes the $i$'th standard basis vector of $\mathcal{Z}=\mathbb{R}^n$ and suppose that $X=X^i \partial_i$ and $Y=Y^j \partial_j$ are two vector fields on $\mathcal{Z}^{1:n-1}$.  Then the covariant derivative of $Y$ along $X$ is given by:
$$
\begin{align}
  \nabla_X Y &= \left(X^i \partial_i Y^k + \Gamma_{ij}^k X^i Y^j\right) \partial_k \\
  &= \left(X^i \partial_i Y^k + \left(J^+\right)^k_m \partial_i J^m_j X^i Y^j\right) \partial_k \\
  &= X^i \partial_i Y^k \partial_k + \left(\partial_i J^m_j X^i Y^j\right) \left(J^+\right)^k_m \partial_k, \quad k=1,\dots,n-1
\end{align}
$$
<!-- From here, because $\nabla_X Y$ is a tensor, we can compute its coordinates in the data space.  Suppose that $X=X^j \frac{\partial}{\partial z^j} = X^j J^i_j \frac{\partial}{\partial x^i}$ and $Y=Y^j \frac{\partial}{\partial z^j} = Y^j J^i_j \frac{\partial}{\partial x^i}$.  Then $\nabla_X Y$ is given by:
$$
\begin{align}
  \nabla_X Y &= \left(X^i \frac{\partial Y^k}{\partial z^i} + \left(J^+\right)^k_m \frac{\partial J^m_j}{\partial z^i} X^i Y^j\right) \frac{\partial}{\partial z^k} \\
  &= \left(X^i \frac{\partial Y^k}{\partial z^i} + \left(J^+\right)^k_m \frac{\partial J^m_j}{\partial z^i} X^i Y^j\right) J^l_k \frac{\partial}{\partial x^l} \\
  &= \left(\tilde{X}^i \frac{\partial Y^k}{\partial x^i} J^l_k + \left(J^\parallel\right)^l_m \frac{\partial J^m_j}{\partial z^i} X^i Y^j\right) \frac{\partial}{\partial x^l}
\end{align}
$$ -->

## Second Fundamental Form
The second fundamental form is defined as follows:
$$
\begin{align}
  II(X,Y) &:= \bar{\nabla}_X Y - \nabla_X Y \\
  &= \left(\left(\bar{\Gamma}_{ij}^k - \Gamma_{ij}^k\right) X^i Y^j\right) \partial_k + \left(\bar{\Gamma}_{ij}^{k'} X^i Y^j\right) \partial_{k'}, \quad k\in [1,n-1], \quad k'\in [n,n] \\
  &= \begin{cases}
    \left(\bar{\Gamma}_{ij}^k - \Gamma_{ij}^k\right) X^i Y^j \partial_k, & k=1,\dots,n-1 \\
    \bar{\Gamma}_{ij}^{k} X^i Y^j \partial_k, & k=n
  \end{cases} \\
  &= \begin{cases}
    \left(\partial_i J^m_j\left[\left(J^{-1}\right)^k_m - \left(J^{+}\right)^k_m\right]\right) X^i Y^j \partial_k, & k=1,\dots,n-1 \\
    \left(\partial_i J^m_j\left(J^{-1}\right)^n_m\right) X^i Y^j \partial_n, & \text{otherwise}
  \end{cases} \\
  &= \begin{cases}
    \left(\partial_i J^m_j\left[G^k_m - \left(J^{+}\right)^k_m\right]\right) X^i Y^j \partial_k, & k=1,\dots,n-1 \\
    \left(\partial_i J^m_jG^n_m\right) X^i Y^j \partial_n, & \text{otherwise}
  \end{cases}
\end{align}
$$

$$
\begin{align}
G_1 &= J_1^+\Phi J_2^\perp  \\
G_2 &= J_2^+\Phi^T J_1^\perp  \\
\text{where }\Phi &= \left(I - J_2^\parallel J_1^\parallel\right)^{-1} \\
\text{ and }\Phi^T &= \left(I - J_1^\parallel J_2^\parallel\right)^{-1}
\end{align}
$$

## Scalar Second Fundamental Form
Suppose that $\dim(\mathcal{M}) = n - 1$.  Then the scalar second fundamental form is defined as follows:
$$
\begin{align}
  h(X,Y) &:= \langle II(X,Y),N\rangle
\end{align}
$$
where $N$ is the unit normal vector to $\mathcal{M}$, which is given by:
$$
\begin{align}
  N &= \frac{1}{\sqrt{g^\perp(V, V)}}J^\perp V, \quad\text{where } J^\perp = I - J^\parallel \quad \text{and} \quad V \notin T\mathcal{M}
\end{align}
$$
Suppose that $N = N^i \partial_i$ is a unit normal vector to $\mathcal{M}$.  Then the scalar second fundamental form is given by:
$$
\begin{align}
  h(X,Y) &:= \begin{cases}
    \left(\partial_i J^m_j\left[\left(J^{-1}\right)^k_m - \left(J^{+}\right)^k_m\right] N^k \right) X^i Y^j, & k=1,\dots,n-1 \\
    \left(\partial_i J^m_j\left(J^{-1}\right)^n_m N^n \right) X^i Y^j, & \text{otherwise}
  \end{cases}
\end{align}
$$

## Shape Operator
The shape operator is defined as the linear operator $s: T\mathcal{M} \to T\mathcal{M}$ that satisfies:
$$
\begin{align}
  \langle sX, Y\rangle &= h(X,Y) = h_{ij}X^i Y^j
\end{align}
$$
We can see directly from the definition of the scalar second fundamental form that the coordinates of the shape operator tensor are given by:
$$
\begin{align}
  h_{ij} &= \begin{cases}
    \partial_i J^m_j\left[\left(J^{-1}\right)^k_m - \left(J^{+}\right)^k_m\right] N^k, & k=1,\dots,n-1 \\
    \partial_i J^m_j\left(J^{-1}\right)^n_m N^n, & \text{otherwise}
  \end{cases}
\end{align}
$$

## Principal Curvatures
The principal curvatures of $\mathcal{M}$ are the eigenvalues of the shape operator.  This is the eigenvalues, $(\kappa_1,\dots,\kappa_{\text{dim}(\mathcal{M})})$, that corresponds to a frame $(W_1,\dots,W_{\text{dim}(\mathcal{M})})$ of $T\mathcal{M}$ such that $sW_i = \kappa_i W_i$.  This can be computed by taking the eigendecomposition of the shape operator.

# Orthogonal coordinate transforms
Suppose that $N$ is proportional to a basis vector on $\mathcal{Z}$, say $N=\partial_k$.  Then the shape operator is given by:
$$
\begin{align}
  h_{ij} &= \partial_i J^m_j\left(J^{-1}\right)^k_m
\end{align}
$$
We can interpret $N$ as determining $\mathcal{M}$ in this setting because $\mathcal{M}$ corresponds to the image of $\mathcal{Z}^{-k}$ under the diffeomorphism $F$.  We should verify if this is true for different values of $k$.


