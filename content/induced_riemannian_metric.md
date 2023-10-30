Title: Geometry on submanifolds
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
Tags: riemannian metric
Slug: submanifolds
Summary: A look at how the Riemannian metric on a manifold can be used to define a Riemannian metric on a submanifold.

Riemannian metrics give us a way to measure angles and lengths on smooth manifolds.  Furthermore, they can be used to define a Riemannian metric on submanifolds.  In this post, we'll look at the coordinate representations of these induced metrics and show how to compute quantities that depend on the metric such as the gradient of a function and divergence of a vector field.

# Restriction to a submanifold
Let $(M,g)$ be an n-dimensional Riemannian manifold and let $S\subset M$ be a k-dimensional immersed submanifold.  We can construct a map that restricts to $S$ using the projection map onto $S$, $\pi: M \to S$, and the inclusion map to the ambient space, $\iota: S\to M$.  Lets call the restriction map, $r = \iota \circ \pi$.  While $r$ may seem trivially defined because for $p\in M$ that also lies on $S$, we have that $p=r(p)$.  However the differential of $r$ tells us how tangent vectors on $T_pM$ change when pushed through the restriction map.

Let $E_1,\dots,E_k$ be a frame that spans the tangent space of $S$ at $\pi(p)$.  We can extend this frame to a frame $E_1,\dots,E_n$ that spans $T_pM$ by adding $n-k$ vectors that are orthogonal to $S$, $(N_{k+1},\dots,N_n)$.  If we write $X = X_1^iE_i + X_2^iN_i$ for some $X\in T_pM$, then we have that $dr_p X = X_1^iE_i$.  So restricting to a submanifold has the effect of removing the components of a vector that are orthogonal to the submanifold.

## Restriction of the metric
Similarly, we can restrict the Riemannian metric to $S$.  We can write the ambient space Riemannian metric in terms of $(\epsilon^1,\dots,\epsilon^k, \eta^{k+1},\dots,\eta^n)$, which is the dual frame for $(E_1,\dots,E_k,N_{k+1},\dots,N_n)$:
$$
\begin{align}
  g &= \epsilon^i \otimes \epsilon^i + \eta^i \otimes \eta^i
\end{align}
$$
Then the restriction of the metric to $S$ is given by:
$$
\begin{align}
  \tilde{g} &= (\iota\circ \pi)^* g \\
  &= (\iota\circ \pi)^*(\epsilon^i \otimes \epsilon^i + \eta^i \otimes \eta^i) \\
  &= \epsilon^i \otimes \epsilon^i \\
  &= (E_i^u g_{ua}dx^a) \otimes (E_i^v g_{vb}dx^b) \\
  &= g_{bv} E_i^v E_i^u g_{ua} dx^a \otimes dx^b
\end{align}
$$

# Gradient on submanifolds
$$
\begin{align}
    \text{grad}_{\tilde{g}} f &= \tilde{g}^{ij} \frac{\partial f}{\partial x^i} E_j \\
\end{align}
$$