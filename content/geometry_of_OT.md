Title: Geometry of optimal transport
Date: 2024-05-13
Category: Blog
status: hidden
Slug: ot-geometry
Summary: Geometry of normalizing flows


# Problem statement
Let $\mathrm{Diff}(\mathbb{R}^n)$ denote the space of diffeomorphisms and $\mathrm{Dens}(\mathbb{R}^n)$ denote the space of probability densities on $\mathbb{R}^n$.  Given $\mu_0,\mu_1 \in \mathrm{Dens}(\mathbb{R}^n)$, our goal is to construct a principal bundle over $\mathrm{Dens}(\mathbb{R}^n)$ using the right action of $\mathrm{Diff}(\mathbb{R}^n)$.  This will give us a way to decompose the space diffeomorphisms into a "horizontal" space that is isomorphic to the space of densities and a "vertical" space that is orthogonal to it.  In the end, the horizontal space will correspond to gradient flows while the vertical space will correspond to measure preserving flows.  We will then use this decomposition to look at how the space of diffeomorphisms that have orthogonal Jacobians, $\mathcal{F}_{\text{OCT}}$.  This way of looking at $\mathcal{F}_{\text{OCT}}$ will allow us to directly relate the space of orthogonal coordinate transforms to the space of probability densities.


# Lie group structure of diffeomorphisms
In order to relate diffeomorphisms with probability density functions, we first need to look at how the set of diffeomorphisms forms a Lie group, and how to construct actions on the space of probability measures.
## Lie group definition
Let $\text{Diff}(\mathbb{R}^n)$ denote the set of diffeomorphisms on $\mathbb{R}^n$.  The set of diffeomorphisms is a Lie group because it has the following properties:
  1. **Identity**: The identity element, $e$ is the identity map $\text{Id}$.
  2. **Inverse**: The inverse of a diffeomorphism $g$ is the diffeomorphism $g^{-1}.
  3. **Composition**: The composition of two diffeomorphisms, $g$ and $h$, is the diffeomorphism $g\circ h$.

## Lie algebra
The Lie algebra associated with this Lie group is the set of vector fields $\mathfrak{X}(\mathbb{R}^n)$, which is also the space of functions from $\mathbb{R}^n \to \mathbb{R}^n$.  Its Lie bracket is given by
$$
\begin{align}
  [X,Y] &= X\partial_i Y - Y\partial_i X
\end{align}
$$


This corresponds to the tangent space at the identity element, $T_e\text{Diff}(\mathbb{R}^n)$, so any tangent vector $X$ at $g\in \text{Diff}$, can be written as the pushforward of an element of the Lie algebra at the identity element.  If $Y$ is a tangent vector at the identity element, then the pushforward of $Y$ to $g$ is given by:
$$
\begin{align}
  X &= g_* Y
\end{align}
$$

## Action on probability measures
Now suppose that $\mu = \rho dx$ is a probability measure on $\mathbb{R}^n$.  Then we can define a right action of $g\in \text{Diff}(\mathbb{R}^n)$ on $\mu \in \text{Dens}(\mathbb{R}^n)$ using the pullback operation:
$$
\begin{align}
  \mu \cdot g &= g^*\mu \\
  &= g^*(\rho dx) \\
  &= \rho \circ g\left|\det Dg\right| dx
\end{align}
$$

Similarly, a left action can be defined via the pushforward operation:
$$
\begin{align}
  g \cdot \mu &= \phi_* \mu \\
  &= (g^{-1})^*\mu \\
  &= \rho \circ g^{-1}\left|\det Dg^{-1}\right| dx
\end{align}
$$

## Lie subgroup of measure preserving diffeomorphisms
Suppose we are given $\mu_0,\mu_1 \in \text{Dens}(\mathbb{R}^n)$ and we want to find the set of diffeomorphisms such that push $\mu_0$ forward to $\mu_1$, $\phi_*\mu_0 = \mu_1$.  Denote this set by:
$$
\begin{align}
  C(\mu_0,\mu_1) = \{\phi | \phi_* \mu_0 = \mu_1\} \subset \text{Diff}(\mathbb{R}^n)
\end{align}
$$
This set is nonempty because you can always find a diffeomorphism that pushes $\mu_0$ forward to $\mu_1$ (Darmois construction or Moser's theorem).  Suppose we fix an element of this set, $\zeta \in C(\mu_0,\mu_1)$.  Then we can arrive at any other element of this set by composing $\zeta$ with a measure preserving map, $\phi \in \text{Diff}_{\mu_0}(\mathbb{R}^n)$ where
$$
\begin{align}
  \mathrm{Diff}_{\mu_0}(\mathbb{R}^n) = \{\phi \in \mathrm{Diff}(\mathbb{R}^n) | \phi_*\mu_0 = \mu_0\} \subset \text{Diff}(\mathbb{R}^n)
\end{align}
$$

# Principal bundle structure
Now, lets connect the set of diffeomorphisms with the set of probability densities.  We will define a principal $\mathrm{Diff}_{\mu_0}(\mathbb{R}^n)$-bundle over $\mathrm{Dens}(\mathbb{R}^n)$ using the right action of $\mathrm{Diff}_{\mu_0}(\mathbb{R}^n)$ on $\mathrm{Dens}(\mathbb{R}^n)$.

Fix $\mu_0 \in \mathrm{Dens}(\mathbb{R}^n)$ and let $(E,\pi,M)$ be a principal $\mathrm{Diff}_{\mu_0}(\mathbb{R}^n)$ bundle over $\mathrm{Dens}(\mathbb{R}^n)$ where
$$
\begin{align}
  \text{Total space }E &= \mathrm{Diff}(\mathbb{R}^n) \\
  \text{Lie group }G &= \mathrm{Diff}_{\mu_0}(\mathbb{R}^n) \\
  \text{Projection map }\pi_{\mu_0}&: \mathrm{Diff}(\mathbb{R}^n) \ni \phi \mapsto \phi_* \mu_0 \in \mathrm{Dens}(\mathbb{R}^n) \\
  \text{Base space }M &= \mathrm{Dens}(\mathbb{R}^n)
\end{align}
$$
The fibers of this principal bundles, denoted by $E_\mu = \pi_{\mu_0}^{-1}(\mu)$, is the orbit of the right action of $G$ on $M=\mathrm{Dens}(\mathbb{R}^n)$, which is the set of measure preserving flows.  We can also check that every $\mu \in M$ has a neighborhood $U$ and a diffeomorphism (local trivialization) $f: \pi_{\mu_0}^{-1}(U) \to U\times G$ that is $G$ equivariant.  Let $\mu \in U$ and $\phi \in \pi_{\mu_0}^{-1}(\mu)$.  Let $\zeta_{\mu} \in C(\mu_0,\mu)$ be the Darmois map from $\mu_0$ to $\mu$.  Then $\zeta_{\mu} \circ \phi$ is measure preserving, so the local trivialization map can be defined as $f: \phi \mapsto (\mu,\phi \circ \zeta_{\mu}^{-1})$, where $\mu = \pi_{\mu_0}(\phi)$.

The principal bundle construction lets us identify the space of diffeomorphisms that are homeomorphic to the space of probability densities as the quotient space $\mathrm{Diff}(\mathbb{R}^n)/\mathrm{Diff}_{\mu_0}(\mathbb{R}^n)$.  Next, we will look more closely at what this space is by looking at the tangent space of the fibers of the principal bundle, which will be spanned by "vertical vectors" and its orthogonal complement, which will be spanned by "horizontal vectors".

# Horizontal and vertical vectors
We can decompose the total space of diffeomorphisms into a "horizontal space" that spans the space of probability densities and a "vertical space" that is orthogonal to it.  First we'll define the vertical vectors.

The vertical tangent vectors of $P$ are those whose flow at $\phi \in \mathrm{Diff}(\mathbb{R}^n)$ leaves $\pi(\phi)$ unchanged.  Recall that a definition of the principal bundle is that the right action of $G$ leaves $\pi$ unchanged, i.e. $\pi(\phi\cdot g) = \pi(\phi)$.  If we parametrize this as a curve $\gamma(t) = \phi \exp(tX)$ where $X \in \mathfrak{g}$ is the Lie algebra of $\mathrm{Diff}(\mathbb{R}^n)$, then a vertical vector at $\phi$ is the tangent vector to the curve at $t=0$:
$$
\begin{align}
  \frac{d}{dt}|_{t=0} (\phi \cdot g(t)) &= \frac{d}{dt}|_{t=0} (\phi \cdot g(t))
  &= D(\phi)_{Id}X
\end{align}
$$

Alternatively, we can look at the kernel of $\pi$:
$$
\begin{align}
  \frac{d}{dt}|_{t=0} \gamma(t)^* \mu &= \gamma(t)^* \mathcal{L}_u \mu \\
  &= \gamma(t)^* \mathcal{L}_u (\gamma(t)^*\mu_0) \\
\end{align}
$$