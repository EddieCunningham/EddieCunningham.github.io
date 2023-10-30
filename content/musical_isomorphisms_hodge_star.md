Title: Musical isomorphisms and the Hodge star
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
Tags: riemannian geometry, differential geometry
Slug: musical_isomorphisms_and_hodge_star
Summary: Easy to understand explanation of the musical isomorphisms and the Hodge star operator.

One application of the Riemannian metric is for transforming vectors to covectors and vice versa.  We go from vector $X$ to some covector $\omega$ by filling the first argument of $g$ with $X$ so that $\omega(.) = g(X,.)$.  This is main property that we can use to construct the musical isomophisms - the operations that transform vectors to covectors and vice versa.  In this post, we'll go over an easy to understand interpretation of the musical isomorphisms and look at how they can be used to define the Hodge star operator.

# Riemannian metrics
Let $M$ be a smooth manifold and let $g$ be its Riemannian metric.  $g$ can be used to define the concept of orthogonality so that at each point on $M$, we can find an orthonormal frame $(E_1,\dots,E_n)$ locally around that point so that $g(E_i,E_j)=\delta_{ij}$.  A direct consequence is that $g$ can be written in terms of the coframe that is dual to the orthonormal frame, $\epsilon^1,\dots,\epsilon^n$ as:
$$
\begin{align}
  g = \epsilon^i \otimes \epsilon^i
\end{align}
$$
We can also write $g$ in terms of coordinates as :
$$
\begin{align}
  g = g_{ij}dx^i \otimes dx^j
\end{align}
$$



With this in mind, we'll define the musical isomorphisms $\flat: \mathfrak{X}(\mathcal{M}) \to \Omega(\mathcal{M})$ and $\sharp: \Omega(\mathcal{M}) \to \mathfrak{X}(\mathcal{M})$ as follows:
$$
\begin{align}
  X^\flat(.) = g(X,.) \\
  \omega(.) = g(\omega^\sharp,.)
\end{align}
$$
where $X \in \mathfrak{X}(\mathcal{M})$ and $\omega \in \Omega(\mathcal{M})$.  We can see that the $\flat$ operator and $\sharp$ operator are inverses of each other.  Also because $g(E_i,E_j)=\delta_{ij}$, we have that $E_i^\flat = ϵ^i$ because $E_i^\flat(E_j) = \delta_{ij}$.  With logic, we get that $(\epsilon^i)^\sharp = E_i$.  By linearity, we can write the sharp and flat operators as the operations to transform the components of a vector to the components of a covector:
$$
\begin{align}
  X^\flat &= (X^iE_i)^\flat = X^i\epsilon^i \\
  \omega^\sharp &= (\omega_i\epsilon^i)^\sharp = \omega_iE_i
\end{align}
$$

We can also look at how coordinate vectors transform.  Let $\frac{\partial}{\partial x^i}$ be the coordinate vector field associated with the coordinate $x^i$.  So say that $\frac{\partial}{\partial x^i} = A^j_iE_j$ and $E_j = B^i_j\frac{\partial}{\partial x^i}$ where $AB = I$.  Then we have that:

### Examples
Let's look at some examples of the musical isomorphisms in action.
$$
\begin{align}
  \text{grad}f = (df)^\sharp \\
  *X^\flat = X \lrcorner dV_g \\
  d*X^\flat = \text{div}(X)dV_g \\
  *d*X^\flat = \text{div}(X)
\end{align}
$$