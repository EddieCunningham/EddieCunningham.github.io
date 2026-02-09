Title: Lame coefficients
Date: 2025-09-11
Category: Blog
Slug: lame-coefficients
hidden: true
Summary: Lame coefficients

In this post we'll go over orthogonal coordinate systems and the constraints that they impose on the length of coordinate vectors, called the Lame coefficients.


# Orthogonal coordinates
Let $z = (z^1, \dots, z^n)$ be the coordinates defined by the commuting frame vectors themselves.  The Euclidean metric, written in these coordinates, is given by:
$$
\begin{align}
  g &= \delta_{ij} dx^i \otimes dx^j \\
  &= \delta_{ij} \left(\frac{\partial x^i}{\partial z^u}dz^u \otimes \frac{\partial x^j}{\partial z^v}dz^v\right) \\
  &= \frac{\partial x^i}{\partial z^u}\frac{\partial x^i}{\partial z^v}dz^u \otimes dz^v \\
  &= \left(J^TJ\right)_{uv}dz^u \otimes dz^v
\end{align}
$$
When $z$ is an orthogonal coordinate system, we have that $J^TJ = S^2$, where $S = \mathrm{diag}(s_1, \dots, s_n)$ is the diagonal matrix of singular values.  Therefore, we have that:
$$
\begin{align}
  g &= s_u^2 \delta_{uv} dz^u \otimes dz^v
\end{align}
$$
The values $s_u$ are called the Lame coefficients.  There are geometric constraints that are imposed on the Lame coefficients by the fact that the space is flat.  To derive these constraints, we need to compute the Christoffel symbols in these coordinates.

## Christoffel symbols
Since the space that these coordinates is flat, we can compute the elements of the Riemann curvature tensor in these coordinates in order to impose constraints on the Lame coefficients.  To do this, lets first compute the Christoffel symbols in these coordinates.
$$
\begin{align}
  \Gamma_{ij}^k &= \frac{1}{2}{g}^{kl}\left(\frac{\partial {g}_{li}}{\partial z^j} + \frac{\partial {g}_{lj}}{\partial z^i} - \frac{\partial {g}_{ij}}{\partial z^l}\right) \\
  &= \frac{1}{2}{s_k}^{-2}\delta^{kl}\left(\frac{\partial s_i^2}{\partial z^j}\delta_{li} + \frac{\partial s_j^2}{\partial z^i}\delta_{lj} - \frac{\partial s_i^2}{\partial z^l}\delta_{ij}\right) \\
  &= \frac{1}{2}{s_k}^{-2}\left(\frac{\partial s_i^2}{\partial z^j}\delta_{ki} + \frac{\partial s_j^2}{\partial z^i}\delta_{kj} - \frac{\partial s_i^2}{\partial z^k}\delta_{ij}\right) \\
  &= \frac{1}{2}{s_k}^{-2}\left(\frac{\partial s_k^2}{\partial z^j}\delta_{ki} + \frac{\partial s_k^2}{\partial z^i}\delta_{kj} - \frac{\partial s_i^2}{\partial z^k}\delta_{ij}\right) \\
  &= \frac{\partial \log s_k}{\partial z^j}\delta_{ki} + \frac{\partial \log s_k}{\partial z^i}\delta_{kj} - (\frac{s_i}{s_k})^{2}\frac{\partial \log s_i}{\partial z^k}\delta_{ij} \\
  &= \frac{\partial \log s_k}{\partial z^j}\delta_{ki} + \frac{\partial \log s_k}{\partial z^i}\delta_{kj} - s_k^{-2}\frac{\partial \frac{1}{2} s_i^2}{\partial z^k}\delta_{ij}
\end{align}
$$

The Christoffel symbols tell us how the coordinates change as we move along the coordinate curves, and give us the ability to compute the change of our position with respect to the coordinates:
$$
\begin{align}
  \boxed{\frac{\partial^2 x^a}{\partial z^i \partial z^j} = \Gamma_{ij}^k \frac{\partial x^a}{\partial z^k}
  = \frac{\partial \log s_i}{\partial z^j}\frac{\partial x^a}{\partial z^i} + \frac{\partial \log s_j}{\partial z^i}\frac{\partial x^a}{\partial z^j} - s_k^{-2}\frac{\partial \frac{1}{2} s_i^2}{\partial z^k}\delta_{ij}\frac{\partial x^a}{\partial z^k}}
\end{align}
$$

# Curvature constraints
We will derive the constraints on the Lame coefficients by computing the Riemann curvature tensor in these coordinates.  Since we are constructing coordinates on a flat space, the Riemann curvature tensor must be zero.  Recall that the coordinates of the Riemann curvature tensor are given by:
$$
\begin{align}
  R_{ijk}^l &= \frac{\partial \Gamma_{jk}^l}{\partial z^i} - \frac{\partial \Gamma_{ik}^l}{\partial z^j} + \Gamma_{jk}^m \Gamma_{im}^l - \Gamma_{ik}^m \Gamma_{jm}^l
\end{align}
$$
This requires that we compute the derivatives of the Christoffel symbols.
$$
\begin{align}
  \frac{\partial \Gamma_{ij}^k}{\partial z^l} &= \frac{\partial^2 \log s_k}{\partial z^j \partial z^l}\delta_{ki} + \frac{\partial^2 \log s_k}{\partial z^i \partial z^l}\delta_{kj} - \frac{\partial (\frac{s_i}{s_k})^{2}}{\partial z^l}\frac{\partial \log s_i}{\partial z^k}\delta_{ij} - (\frac{s_i}{s_k})^{2}\frac{\partial^2 \log s_i}{\partial z^l \partial z^k}\delta_{ij}
\end{align}
$$
The intermediate derivative of $\frac{\partial (\frac{s_i}{s_k})^{2}}{\partial z^l}$ is given by:
$$
\begin{align}
  \frac{\partial (\frac{s_i}{s_k})^{2}}{\partial z^l}
  &= 2\left(\frac{s_i}{s_k}\right)^{2}\left(\frac{\partial \log s_i}{\partial z^l} - \frac{\partial \log s_k}{\partial z^l}\right)
\end{align}
$$
Plugging this back into the expression for the derivatives of the Christoffel symbols, we get:
$$
\begin{align}
  \frac{\partial \Gamma_{ij}^k}{\partial z^l}
  &= \frac{\partial^2 \log s_k}{\partial z^j \partial z^l}\delta_{ki}
   + \frac{\partial^2 \log s_k}{\partial z^i \partial z^l}\delta_{kj}
   - \left(\frac{s_i}{s_k}\right)^{2}\frac{\partial^2 \log s_i}{\partial z^l \partial z^k}\delta_{ij} \\
  &\quad - 2\left(\frac{s_i}{s_k}\right)^{2}\left(\frac{\partial \log s_i}{\partial z^l}-\frac{\partial \log s_k}{\partial z^l}\right)\frac{\partial \log s_i}{\partial z^k}\,\delta_{ij}
\end{align}
$$


# Lamé coefficients constraints
A classical result is that the Lame coefficients are subject to the following two systems of equations:
$$
\begin{align}
  \frac{\partial^2 s_i}{\partial z^j \partial z^k} = \frac{1}{s_j}\frac{\partial s_j}{\partial z^k}\frac{\partial s_i}{\partial z^j} + \frac{1}{s_k}\frac{\partial s_k}{\partial z^j}\frac{\partial s_i}{\partial z^k}, \quad \text{where } i\neq j \neq k
\end{align}
$$
and
$$
\begin{align}
  \frac{\partial}{\partial z^j}\left(s_j^{-1}\frac{\partial s_i}{\partial z^j}\right) + \frac{\partial}{\partial z^i}\left(s_i^{-1}\frac{\partial s_j}{\partial z^i}\right) + \sum_{k\neq i, k\neq j}s_k^{-2}\frac{\partial s_i}{\partial z^k}\frac{\partial s_j}{\partial z^k} = 0, \quad \text{where } i \neq j
\end{align}
$$
This is equivalent to the vanishing of the Riemann curvature tensor in these coordinates.  We can rewrite the first expression in a more familiar, log space form with some manipulation.  Recall the identity:
$$
\begin{align}
  \frac{\partial^2 \log s_i}{\partial z^j \partial z^k} &= \frac{\partial}{\partial z^j}\left(s_i^{-1}\frac{\partial s_i}{\partial z^k}\right) \\
  &= -s_i^{-2}\frac{\partial s_i}{\partial z^j}\frac{\partial s_i}{\partial z^k} + s_i^{-1}\frac{\partial^2 s_i}{\partial z^j \partial z^k} \\
  &= -\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k} + s_i^{-1}\frac{\partial^2 s_i}{\partial z^j \partial z^k}
\end{align}
$$
Multiplying the first expression by $s_i^{-1}$ gives:
$$
\begin{align}
  s_i^{-1}\frac{\partial^2 s_i}{\partial z^j \partial z^k} = \frac{\partial \log s_j}{\partial z^k}\frac{\partial \log s_i}{\partial z^j} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}
\end{align}
$$
This implies that the first expression can be rewritten as:
$$
\begin{align}
  \boxed{\frac{\partial^2 \log s_i}{\partial z^j \partial z^k} = \frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_j}{\partial z^k} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}-\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}, \quad \text{where } j \neq k}
\end{align}
$$

# Change of variables formula
Now suppose that we want to use an orthogonal coordinate system in a normalizing flow to model the distribution of data.  Suppose that $\nu(z)$ is a prior distribution over the coordinates $z$.  Then the log likelihood of a sample $x$ under the pushforward distribution through a diffeomorphism $F$ is given by:
$$
\begin{align}
  \log p(F(z)) = \log \nu(z) - \log \left| \frac{\partial F(z)}{\partial z} \right|
\end{align}
$$
When $F$ has a Jacobian matrix with orthogonal columns, $z$ is an orthogonal coordinate system, and so we can write the log likelihood as:
$$
\begin{align}
  \log p(F(z)) = \log \nu(z) - \sum_i\log s_i(z)
\end{align}
$$
where $s_i(z)$ are the singular values of the Jacobian matrix of $F$ and are also the Lame coefficients of the orthogonal coordinate system $z$.  To apply the constraints on the Lame coefficients, we can take the second derivative of the log likelihood.  First, let $\Lambda_{k}(z) = \frac{\partial \log p(F(z))}{\partial z^k} - \frac{\partial \log \nu(z)}{\partial z^k} = -\sum_i \frac{\partial \log s_i(z)}{\partial z^k}$.  Then we have
$$
\begin{align}
  \frac{\partial \Lambda_{j}(z)}{\partial z^k} &= -\sum_i \frac{\partial^2 \log s_i(z)}{\partial z^j \partial z^k} \\
  &= -\sum_i \left(\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_j}{\partial z^k} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}-\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}\right) \\
  &= \Lambda_j \frac{\partial \log s_j}{\partial z^k} + \frac{\partial \log s_k}{\partial z^j}\Lambda_k + \sum_i \left(\frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}\right) \\
  &= \left(\frac{\partial \log p(F(z))}{\partial z^j}-\frac{\partial \log \nu(z)}{\partial z^j}\right)\frac{\partial \log s_j}{\partial z^k} + \frac{\partial \log s_k}{\partial z^j}\left(\frac{\partial \log p(F(z))}{\partial z^k}-\frac{\partial \log \nu(z)}{\partial z^k}\right) + \sum_i \frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}
\end{align}
$$
and, recall the identity:
$$
\begin{align}
  \boxed{\frac{\partial^2 x^a}{\partial z^j \partial z^k} = \Gamma_{jk}^l \frac{\partial x^a}{\partial z^l}
  = \frac{\partial \log s_j}{\partial z^k}\frac{\partial x^a}{\partial z^j} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial x^a}{\partial z^k} - s_l^{-2}\frac{\partial \frac{1}{2} s_j^2}{\partial z^l}\delta_{jk}\frac{\partial x^a}{\partial z^l}}
\end{align}
$$
Plugging this into the expression for the second derivative of the log likelihood, we get:
$$
\begin{align}
  \frac{\partial \Lambda_{j}(z)}{\partial z^k} &= \frac{\partial^2 \log p(F(z))}{\partial z^j \partial z^k} - \frac{\partial^2 \log \nu(z)}{\partial z^j \partial z^k} \\
  &= \frac{\partial^2 \log p(x)}{\partial x^a \partial x^b}\frac{\partial x^a}{\partial z^j}\frac{\partial x^b}{\partial z^k}
     + \frac{\partial \log p(x)}{\partial x^a}\frac{\partial^2 x^a}{\partial z^j \partial z^k}
     - \frac{\partial^2 \log \nu(z)}{\partial z^j \partial z^k} \\
  &= \frac{\partial^2 \log p(x)}{\partial x^a \partial x^b}\frac{\partial x^a}{\partial z^j}\frac{\partial x^b}{\partial z^k}
     + \frac{\partial \log p(x)}{\partial x^a}\left(\frac{\partial \log s_j}{\partial z^k}\frac{\partial x^a}{\partial z^j} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial x^a}{\partial z^k} - s_l^{-2}\frac{\partial \frac{1}{2} s_j^2}{\partial z^l}\delta_{jk}\frac{\partial x^a}{\partial z^l}\right)
     - \frac{\partial^2 \log \nu(z)}{\partial z^j \partial z^k} \\
  &= \frac{\partial^2 \log p(x)}{\partial x^a \partial x^b}\frac{\partial x^a}{\partial z^j}\frac{\partial x^b}{\partial z^k}
     + \left(\frac{\partial \log p(F(z))}{\partial z^j}\frac{\partial \log s_j}{\partial z^k} + \frac{\partial \log s_k}{\partial z^j}\frac{\partial \log p(F(z))}{\partial z^k} - s_l^{-2}\frac{\partial \frac{1}{2} s_j^2}{\partial z^l}\delta_{jk}\frac{\partial \log p(F(z))}{\partial z^l}\right)
     - \frac{\partial^2 \log \nu(z)}{\partial z^j \partial z^k}
\end{align}
$$

### Equating the two expressions
We can equate the two expressions for the second derivative of the log likelihood, and cancel the terms that are the same on both sides.  This gives us the following equation:
$$
\begin{align}
  \frac{\partial^2 \log p(x)}{\partial x^a \partial x^b}\frac{\partial x^a}{\partial z^j}\frac{\partial x^b}{\partial z^k}&
     - s_l^{-2}\frac{\partial \frac{1}{2} s_j^2}{\partial z^l}\delta_{jk}\frac{\partial \log p(F(z))}{\partial z^l}
     - \frac{\partial^2 \log \nu(z)}{\partial z^j \partial z^k} \\
     \quad \quad \quad \quad &= -\frac{\partial \log \nu(z)}{\partial z^j}\frac{\partial \log s_j}{\partial z^k} - \frac{\partial \log s_k}{\partial z^j}\frac{\partial \log \nu(z)}{\partial z^k} + \sum_i \frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k}
\end{align}
$$
For simplicity, we'll assume that $\nu$ is a uniform prior, so $\frac{\partial \log \nu(z)}{\partial z^j} = 0$.  This gives us the following equation:
$$
\begin{align}
\frac{\partial^2 \log p(x)}{\partial x^a \partial x^b}\frac{\partial x^a}{\partial z^j}\frac{\partial x^b}{\partial z^k} &= \sum_i \frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k} + s_l^{-2}\frac{\partial \frac{1}{2} s_j^2}{\partial z^l}\delta_{jk}\frac{\partial \log p(F(z))}{\partial z^l} \\
&= \sum_i \frac{\partial \log s_i}{\partial z^j}\frac{\partial \log s_i}{\partial z^k} + \frac{1}{2} \langle \nabla s_j^2, \nabla \log p \rangle \delta_{jk}
\end{align}
$$
Changing coordinates to $x$ gives:
$$
\begin{align}
  \frac{\partial^2 \log p(x)}{\partial x^a \partial x^b} &= \sum_i \frac{\partial \log s_i}{\partial x^a}\frac{\partial \log s_i}{\partial x^b} + \frac{1}{2} \langle \nabla s_j^2, \nabla \log p \rangle \frac{\partial z^j}{\partial x^a}\frac{\partial z^j}{\partial x^b} \\
  &= \sum_i \frac{\partial \log s_i}{\partial x^a}\frac{\partial \log s_i}{\partial x^b} - \langle \nabla \log s_j, \nabla \log p \rangle U_{ja}U_{jb}
\end{align}
$$