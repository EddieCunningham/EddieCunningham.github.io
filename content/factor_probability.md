Title: Probability form factorization
Date: 2024-02-06
Category: Blog
Tags: probability form
Slug: probability-form-factorization
Summary: A look at how probability forms can be factorized using normalizing flows.

We are interested in studying how to induce probability measures on submanifolds using a probability measure in the ambient space.  In general, there is no unique way to induce a probability measure on a submanifold.  However, we will investigate if it is possible to do so if we place certain restrictions on the induced probability measure.

# Space of flows that induce a probability measure
Let $P$ be a probability distribution on a Riemannian manifold $(\mathcal{M},g)$ with non-degenerate density function $\rho$.  Let $dP_\rho = \rho dV$ denote the probability form associated with $\rho$ the density $\rho$.  Let $\mathcal{F}_\rho$ be the family of diffeomorphisms that induce $\rho$ by pulling back a prior probability form $dP_0 = \rho_0 dV$:
$$
\begin{align}
  \mathcal{F_\rho} = \{F: dP_\rho = F^*dP_0\}
\end{align}
$$
Each $F\in \mathcal{F}_\rho$ can be thought of as a normalizing flow whose output density is equal to $\rho$.  In general $\mathcal{F}_\rho$ has an infinite number of elements because any measure preserving transformation takes an element in $\mathcal{F}$ to another element in $\mathcal{F}$.

The reason that we are interested in $\mathcal{F}_\rho$ is that we are interested in looking at how to induce probability measures on embedded submanifolds of $\mathcal{M}$ that can be obtained by pushing forward a coordinate submanifold in the base space of some $F\in \mathcal{F}_\rho$.  If $S \subset \mathcal{M}$ is a k-dimensional submanifold, we assume that there is a $F\in \mathcal{F}_\rho$ such that $F(B) = S$ for some coordinate submanifold $B \subset \mathbb{R}^n$.  This means that the tangent space of $S$ is spanned by the vectors $F_*\frac{\partial}{\partial z_1},\dots,F_*\frac{\partial}{\partial z_k}$ where $F_*\frac{\partial}{\partial z_i}$ is the pushforward of the coordinate basis vector $\frac{\partial}{\partial z_i}$.

TODO: Characterize which submanifolds can be obtained by pushing forward a coordinate submanifold using a flow in $\mathcal{F}_\rho$.

# Restriction to submanifolds
Let $\mathcal{S}$ be a k-dimensional submanifold of $\mathcal{M}$ and $x\in \mathcal{M}$.  Then the map $r_S = \hookrightarrow \circ \pi$ restricts any $x \in \mathcal{M}$ to $\mathcal{S}$.  For any $x\in \mathcal{M}$ that lies in $\mathcal{S}$, $r_S(x) = x$, however the pushforward of tangent vectors through $r_S$ projects them onto the tangent space of $\mathcal{S}$.

Let $V \in T_x\mathcal{M}$ be a tangent vector at $x$ and suppose that the tangent space of $\mathcal{S}$ is spanned by the vectors $\frac{\partial}{\partial z_1},\dots, \frac{\partial}{\partial z_k}$ where $z_1,\dots,z_k$ are coordinates for a chart.  If $V = \sum_{i=1}^n v^i \frac{\partial}{\partial z^i}$, then the pushforward of $V$ through $r_S$ is $r_{S*}V = \sum_{i=1}^k v^i \frac{\partial}{\partial z^i}$.  So pushing forward through $r_S$ projects the tangent vectors onto the tangent space of $\mathcal{S}$.

# Induced probability forms
The way that we will induce probability forms on submanifolds is by inducing a volume form on a coordinate submanifold and pulling back through a diffeomorphism.  Suppose $S = F(B)$ is a k-dimensional submanifold of $\mathcal{M}$ and $B$ is a coordinate submanifold of the base space for some $F\in \mathcal{F}_\rho$.  Let $dV$ be the volume form on $\mathcal{M}$.  If $\frac{\partial}{\partial z_1},\dots,\frac{\partial}{\partial z_k}$ is a local orthonormal frame for the tangent space of $B$, then the induced volume form on $B$ is $dV_B = \frac{\partial}{\partial z^{k+1}}\lrcorner\dots\lrcorner\frac{\partial}{\partial z^n}\lrcorner dV$.  The the induced probability form on $B$ is $dP_B = \rho_0 dV_B$.

Finally, we can pullback $dP_B$ through $F$ to get the induced probability form on $S$:
$$
\begin{align}
  dP_S = F^*dP_B
\end{align}
$$
This is a valid probability form if $F$ is a diffeomorphism because of the diffeomorphic invariance of the integral:
$$
\begin{align}
  \int_S dP_S &= \int_{F(B)} F^*dP_B \\
  &= \int_B dP_B \\
  &= 1
\end{align}
$$


# Factorization of probability forms
Suppose that we want to factor $\rho$ into a product of two densities, $\rho_1$ and $\rho_2$, along submanifolds $\mathcal{S}_1$ and $\mathcal{S}_2$ respectively.  What this means is that we want to construct a map $\rho \to (\rho_1,\rho_2)$ such that $\rho_1$ and $\rho_2$ are valid probability densities, i.e. $\int \rho_1 dS_1 = \int \rho_2 dS_2 = 1$.

We assume that there is an $F \in \mathcal{F}_\rho$ such that $F(B_1) = \mathcal{S}_1$ and $F(B_2) = \mathcal{S}_2$ where $B_1$ and $B_2$ are coordinate submanifolds of $\mathbb{R}^n$.  Then we can pull back the probability form on $B_1$ and $B_2$ to get the induced probability forms on $\mathcal{S}_1$ and $\mathcal{S}_2$:
$$
\begin{align}
  dP_{\rho_1} &= F^*dP_{B_1} \\
  dP_{\rho_2} &= F^*dP_{B_2}
\end{align}
$$
We can compute $\rho_1$ and $\rho_2$ by evaluating $dP_{\rho_1}$ and $dP_{\rho_2}$ on an orthonormal frame of $S_1$ and $S_2$ respectively.  Here is the derivation for $\rho_1$:
$$
\begin{align}
  dP_{\rho_1}(E_1,\dots,E_k) &= \rho_1 dV_{\mathcal{S}_1}(E_1,\dots,E_k) \\
  &= \rho_1
\end{align}
$$
where $E_1,\dots,E_k$ is an orthonormal frame for $\mathcal{S}_1$.  This is because $dV_{\mathcal{S}_1}(E_1,\dots,E_k) = 1$.  The derivation for $\rho_2$ is similar.

# Properties of induced probability forms


# Restricting family of induced probability forms
Place functional restrictions on $\rho_1$ and $\rho_2$.
