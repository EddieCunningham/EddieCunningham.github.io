Title: Volume form
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
Tags: riemannian geometry, volume form, differential geometry
Slug: volume-form
Summary: An intro to the Riemannian volume form

The Riemannian volume form is a way to define and measure "volume" on a Riemannian manifold.  In this doc we'll go over where the volume form comes from and how it is able to measure volume.


# Riemannian metrics
Let $\mathcal{M}$ be a smooth n-dimensional manifold.  A Riemannian metric is a choice of inner product that allows us to define geometric values on manifold, such as length, angles and distance.  Let $(U,(x^i))$ be a coordinate chart of $\mathcal{M}$.  Then a Riemannian metric is a contravariant 2-tensor written as
$$
\begin{align}
  g = g_{ij}dx^i\otimes dx^j
\end{align}
$$
where $g_{ij}$ is a symmetric positive definite matrix.  The Riemannian metric defines what an inner product means.  Let $X,Y \in \mathfrak{X}(\mathcal{M})$ be vector fields in the domain of a chart $(U,(x^i))$.  Then the inner product of $X$ and $Y$ is defined as
$$
\begin{align}
  \langle X, Y \rangle_g &= g(X, Y) \\
  &= \left(g_{ij}dx^i \otimes dx^j\right)(X, Y) \\
  &= g_{ij}dx^i(X)dx^j(Y) \\
  &= g_{ij}dx^i(X^a \frac{d}{dx^a})dx^j(Y^b \frac{d}{dx^b}) \\
  &= g_{ij}X^a dx^i(\frac{d}{dx^a})Y^b dx^j(\frac{d}{dx^b}) \\
  &= g_{ij}X^a \delta^i_a Y^b \delta^j_b \\
  &= g_{ij}X^i Y^j
\end{align}
$$
Note that $\langle X, Y \rangle_g: U \to \mathbb{R}$ is a function over $U$.  When we evaluate it at a point $p \in U$, we get a scalar value which represents the inner product between the tangent vectors $X_p$ and $Y_p$.

## Pullback metrics
Because the Riemannian metric is a covariant tensor, we can pull it back through any smooth map.  Let $F: \mathcal{N} \to \mathcal{M}$ be a smooth map and say that we have defined a Riemannian metric $g$ on $\mathcal{M}$.  Then the pullback metric of $g$ through $F$ is a Riemannian metric on $\mathcal{N}$ defined as $F^*g$.  In the domain of a chart $(V, (z^i))$ of $\mathcal{N}$ (and assuming that $(U,(x^i))$ is a chart on $\mathcal{M}$ so that $F(V)$ and $U$ overlap), we can write the pullback metric as
$$
\begin{align}
  F^* g &= (g_{ij}\circ F)d(x^i \circ F) \otimes d(x^j \circ F) \\
  &= (g_{ij}\circ F)\left(\frac{dF^i}{dz^u}dz^u \right)\otimes \left(\frac{dF^j}{dz^v}dz^v \right) \\
  &= \underbrace{(g_{ij}\circ F)\frac{dF^i}{dz^u}\frac{dF^j}{dz^v}}_{\hat{g}_{uv}}dz^u \otimes dz^v \\
  &= \hat{g}_{uv}dz^u \otimes dz^v
\end{align}
$$
So $F$ and $g$ define a new Riemannian metric $\hat{g}$ on $\mathcal{N}$ whose coordinates are given by $\hat{g}_{uv}$.

## Orthonormal frames
Riemannian metrics allow us to define the concept of orthogonality.  Two vectors $X$ and $Y$ are orthogonal if $\langle X, Y \rangle_g=0$.  An orthonormal frame is a frame $(E_1,\dots,E_n)$ where $\langle E_i, E_j \rangle_g = \delta_{ij}$.  There is a dual frame associated with every orthonormal frame, $(\epsilon^1,\dots,\epsilon^n)$, where $\epsilon^i(E_j) = \delta^i_j$.  Due to the definition that $g(E_i, E_j) = \delta_{ij}$, we can write the Riemannian metric in terms of the dual frame as:
$$
\begin{align}
  g = \epsilon^i \otimes \epsilon^i
\end{align}
$$

We can also see what the coordinates of the orthonormal frames are.  Let $E_j = E_j^k\frac{\partial}{\partial x^k}$ and $\epsilon^i = \epsilon^i_kdx^k$.  By definition of the dual frame, we get that
$$
\begin{align}
  \delta^i_j &= \epsilon^i(E_j) \\
  &= \epsilon^i_k E^k_j
\end{align}
$$

But we also have that
$$
\begin{align}
  \delta_{ij} &= g(E_i, E_j) \\
  &= g_{lk}dx^l \otimes dx^k(E_i^a\frac{\partial}{\partial x^a}, E_j^b\frac{\partial}{\partial x^b}) \\
  &= E_i^lg_{lk}E_j^k
\end{align}
$$
Comparing the two, we see that $\epsilon^i_k = E_i^lg_{lk}$.  Multiplying by the inverse, we also have that $E_i^l = \epsilon^i_kg^{kl}$.  So
$$
\begin{align}
  E_j &= E_j^k \frac{\partial}{\partial x^k} \\
      &= \epsilon^j_l g^{lk} \frac{\partial}{\partial x^k} \\
  \epsilon^i &= E_i^lg_{lk} dx^k \\
             &= \epsilon^i_k dx^k
\end{align}
$$

## Riemannian submanifolds
Let $g$ be a Riemannian metric on an n-dimensional smooth manifold $\mathcal{M}$ and let $S\subset \mathcal{M}$ be a k-dimensional embedded submanifold.  If $\iota: S \to \mathcal{M}$ is the inclusion map, then we can define a Riemannian metric on $S$ as the pullback metric of $g$ through $\iota$,
$$
  \tilde{g} = \iota^*g
$$
Let $E_1,\dots,E_k$ be a local orthonormal frame on $S$ with respect to $\tilde{g}$ and let $(\epsilon^1,\dots,\epsilon^k)$ be the dual coframe.  Then we can see that
$$
\begin{align}
  \tilde{g}(E_i,E_j) &= \iota^*g(E_i,E_j) \\
  &= g(\iota_*E_i,\iota_*E_j)
\end{align}
$$
Furthermore, we can write the coordinates of $\tilde{g}$ in the ambient space by pulling back through the projection map $\pi: \mathcal{M} \to S$:

$$
\begin{align}
  \pi^*\tilde{g} &= \pi^* \left(\sum_{i=1}^k \epsilon^i \otimes \epsilon^i\right) \\
  &= \sum_{i=1}^k \epsilon^i \otimes \epsilon^i \\
  &= \epsilon_i^k \epsilon_j^k dx^i \otimes dx^j
\end{align}
$$

# Riemannian volume form
A Riemannian volume form is a top form $dV_g \in \Omega^n(\mathcal{M})$ with the property that for every orthonormal frame $(E_1, \dots, E_n)$ over $\mathcal{M}$, we have that
$$
\begin{align}
  dV_g(E_1, \dots, E_n) = 1
\end{align}
$$
It turns out that this property alone **defines** a unique $n$-form, which we denote by $dV_g$, on $\mathcal{M}$.  First we'll show how to construct $dV_g$ and show its uniqueness and then we'll show how to define volume.  The $d$ at the front of $dV_g$ is not the exterior derivative, just a notation highlight the fact that $dV_g$ is closed $d(dV_g) = 0$ because $dV_g$ is a top form.  But it is not necessarily true that $dV_g$ is exact.

## Construction and uniqueness
Let $(E_1, \dots, E_n)$ be an orthonormal frame over $\mathcal{M}$ and let $(\epsilon^1, \dots, \epsilon^n)$ be the dual coframe.  If we let $dV_g = \epsilon^1 \wedge \dots \wedge \epsilon^n$, then $dV_g$ clearly satisfies our definition.  Futhermore, let $(\tilde{E_1}, \dots, \tilde{E_n})$ and $\tilde{\epsilon}^1, \dots, \tilde{\epsilon}^n$ be another orthogonal frame/coframe pair that we use to construct another form $\tilde{w}_g$ that satisfies our definition of a volume form.  Then we have that
$$
\begin{align}
  dV_g(\tilde{E_1}, \dots, \tilde{E_n}) &= dV_g(\tilde{E_1}, \dots, \tilde{E_n}) \\
  &= \epsilon^1 \wedge \dots \wedge \epsilon^n(\tilde{E_1}, \dots, \tilde{E_n}) \\
  &= \det(\epsilon^i(\tilde{E}_j)) \\
  &= \det(\epsilon^i(Q^k_j E_k)) \\
  &= \det(Q^i_j) \\
  &= 1 \\
  &= \tilde{w}_g(\tilde{E_1}, \dots, \tilde{E_n})
\end{align}
$$
where $Q^i_j = \epsilon^i(\tilde{E}_j)$ is the change of basis matrix from $(E_1, \dots, E_n)$ to $(\tilde{E_1}, \dots, \tilde{E_n})$.  It has a determinant of 1 because both bases are orthonormal.  Thus we have that $dV_g = \tilde{w}_g$, so $dV_g$ can be defined using any orthonormal frame.  In this setup, $g$ played a role in the construction of the orthonormal frames.

To make the relation clearer, we can write the volume form in terms of the Riemannian metric $g$.  Let $(X_1,\dots,X^n)$ be a frame.  Then
$$
\begin{align}
  dV_g(X_1,\dots,X_n) &= \epsilon^1 \wedge \dots \wedge \epsilon^n(X_1,\dots,X_n) \\
  &= \det(\epsilon^i(X_j)) \\
  &= \det(\epsilon^k(X_i)\epsilon^k(X_j))^\frac{1}{2} \quad (\det(A)=\det(A^TA)^\frac{1}{2}) \\
  &= \det(\epsilon^k\otimes \epsilon^k(X_i,X_j))^\frac{1}{2} \\
  &= \det(g(X_i,X_j))^\frac{1}{2} \\
\end{align}
$$
Therefore if $(\omega^1,\dots,\omega^n)$ is the coframe for $(X_1,\dots,X_n)$, then
$$
\begin{align}
  dV_g &= \det(g(X_i,X_j))^\frac{1}{2} \omega^1 \wedge \dots \wedge \omega^n
\end{align}
$$

## Induced volume form on submanifolds
The volume form on $\mathcal{M}$ induces a volume form on any k-dimensional submanifold $\mathcal{S} \subset \mathcal{M}$.  Let $\iota_{\mathcal{S}}: \mathcal{S} \to \mathcal{M}$ be the inclusion map and let $(E_1,\dots,E_{n-k})$ be an orthonormal frame on the normal bundle of $\mathcal{S}$.  Then the induced volume form on $\mathcal{S}$ is defined as
$$
\begin{align}
  \omega_{\tilde{g}} = \iota_{\mathcal{S}}^*(i_{E_{n-k}}\circ \dots \circ i_{E_1}dV_g)
\end{align}
$$
where $i_{E_i}$ is the interior product with respect to $E_i$.  We can check that this is a volume form by applying it to an orthonormal frame $(E_{n-k}, \dots, E_n)$ on $\mathcal{S}$:
$$
\begin{align}
  \omega_{\tilde{g}}(E_{n-k}, \dots, E_n) &= \iota_{\mathcal{S}}^*(i_{E_{n-k}}\circ \dots \circ i_{E_1}dV_g)(E_{n-k}, \dots, E_n) \\
  &= (i_{E_{n-k}}\circ \dots \circ i_{E_1}dV_g)(\iota_{\mathcal{S}}(E_{n-k}), \dots, \iota_{\mathcal{S}}(E_n)) \\
  &= (i_{E_{n-k}}\circ \dots \circ i_{E_1}dV_g)(E_{n-k}, \dots, E_n) \\
  &= dV_g(E_1, \dots, E_n) \\
  &= 1
\end{align}
$$
where the last equality follows from the fact that $dV_g$ is a volume form on $\mathcal{M}$.

## Pullback volume forms
Let $F: \mathcal{N} \to \mathcal{M}$ be a diffeomorphism and $dV_g$ be a volume form on $\mathcal{M}$.  Then the volume form on $\mathcal{N}$ induced by $F$ and $dV_g$ is:
$$
\begin{align}
  F^*dV_g = \omega_{F^*g}
\end{align}
$$
where $F^*g$ is the pullback metric of $g$ through $F$.  We can see this by checking that $F^*dV_g$ is a volume form on $\mathcal{N}$ with respect to the pullback metric $F^*g$.  Let $(E_1, \dots, E_n)$ be an orthonormal frame on $\mathcal{M}$.  Then we can see that $(F^{-1}_*E_1, \dots, F^{-1}_*E_n)$ is an orthonormal frame on $\mathcal{N}$ with respect to $F^*g$ because
$$
\begin{align}
  \langle F^{-1}_*E_i, F^{-1}_*E_j \rangle_{F^*g} &= F^*g(F^{-1}_*E_i, F^{-1}_*E_j) \\
  &= g(F_*F^{-1}_*E_i, F_*F^{-1}_*E_j) \\
  &= g(E_i, E_j) \\
  &= \delta_{ij}
\end{align}
$$
Furthermore, the dual basis for $(F^{-1}_*E_1, \dots, F^{-1}_*E_n)$ is $(F^*\epsilon^1, \dots, F^*\epsilon^n)$ where $(\epsilon^1, \dots, \epsilon^n)$ is the dual basis for $(E_1, \dots, E_n)$ because
$$
\begin{align}
  F^*\epsilon^i(F^{-1}_*E_j) &= \epsilon^i(F_*F^{-1}_*E_j) \\
  &= \epsilon^i(E_j) \\
  &= \delta^i_j
\end{align}
$$
So now that we know that $(F^*\epsilon^1, \dots, F^*\epsilon^n)$ forms an orthonormal dual frame on $\mathcal{N}$ with respect to $F^*g$, and we know that volume forms can be written as the wedge product of any orthonormal dual frame, we can immediately see that $F^*dV_g$ is a volume form on $\mathcal{N}$ with respect to $F^*g$:
$$
\begin{align}
  F^*dV_g &= F^*(\epsilon^1 \wedge \dots \wedge \epsilon^n) \\
  &= (F^*\epsilon^1) \wedge \dots \wedge (F^*\epsilon^n)
\end{align}
$$

## Volume
The volume form can be used to define the **signed** volume of a region on a manifold using integration.  Let $(U, \phi)$ be a chart on $\mathcal{M}$ and let $(x^i)$ be a set of coordinates for $\phi(U)$.  Then the volume of a region $D \subseteq U$ can be defined as
$$
\begin{align}
  \text{Vol}(D) &= \int_D dV_g \\
  &= \pm \int_{\phi(D)}(\phi^{-1})^*dV_g \\
  &= \pm \int_{\phi(D)}\underbrace{dV_{(\phi^{-1})^*g}}_{dV_{\bar{g}}} \\
  &= \pm \int_{\phi(D)}\det(\bar{g}_{ij})^\frac{1}{2} dx^1 \wedge \dots \wedge dx^n \\
  &= \pm \int_{\phi(D)}\det(\bar{g}_{ij})^\frac{1}{2} dx^1 \dots dx^n
\end{align}
$$
So the volume of $D$ is defined as the integral of volume form and we can evaluate it by pulling back the volume form to a coordinate chart and integrating over the chart.

The plus or minus sign appears due to the orientation of the chart.  If the chart is orientation preserving, then the sign is positive and if the chart is orientation reversing, then the sign is negative.  This can be an issue for non-orientable manifolds.  For example if we wanted to find the volume of a Mobius strip, we would need to use two charts to cover the strip.  One chart would be orientation preserving and the other would be orientation reversing, so the volumes we compute on each chart would cancel.  A way to get around this is to use a Riemannian density instead of a volume form.

# Riemannian densities
A Riemannian density is an object that is like the absolute value of a volume form and can be used to define an unsigned volume on a manifold.  See Chapter 16 of [Lee 2013](https://math.berkeley.edu/~jchaidez/materials/reu/lee_smooth_manifolds.pdf) for a reference.

Let $dV_g$ be a volume form over a Riemannian manifold $(\mathcal{M},g)$.  Then a Riemmanian density, $\mu_g$ can be constructed as the absolute value of $dV_g$:
$$
\begin{align}
  \mu_g = |dV_g|
\end{align}
$$
where the absolute value sign means that we take the absolute value of the evaluation of the volume form
$$
\begin{align}
  \mu_g(E_1,\dots,D_n) &= |dV_g|(E_1,\dots,D_n) \\
  &= |dV_g(E_1,\dots,D_n)|
\end{align}
$$
The Riemannian density, although they aren't tensors, have many of the same properties as the volume form like the ability to pullback through immersions and define volume.  If $(U, \phi)$ is a chart on $\mathcal{M}$, then the volume of a region $D \subseteq U$ can be defined as
$$
\begin{align}
  \text{Vol}(D) &= \int_D \mu_g \\
  &= \int_D |dV_g| \\
  &= \int_{\phi(D)} (\phi^{-1})^*|dV_g| \\
  &= \int_{\phi(D)} |(\phi^{-1})^*dV_g| \\
\end{align}
$$
The absolute value sign will cancel out the sign ambiguity that we had with the volume form, so we don't need to worry about orientation.  So we can use the Riemannian density to measure volume on non-orientable manifolds.