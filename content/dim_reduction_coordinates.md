Title: Coordinate systems for dimension reduction
Date: 2025-04-05
Category: Blog
Slug: dim_reduction_coordinates
hidden: true
Summary: A construction of coordinate systems for dimension reduction


Consider a non-degenerate probability density function, $\rho$, defined on Euclidean space $\mathbb{R}^n$.  We will call this Euclidean space the **data space** and denote it by $\mathcal{X}$.  We are interested in understanding the shape of $\rho$ by finding a coordinate system on $\mathcal{X}$ that captures the "structure" of $\rho$.  At a high level, this means that we want to be able to find a coordinate system (chart) for $\mathcal{X}$ such that "dropping" some coordinates of a point $\mathbf{x} \in \mathcal{X}$ has the least amount of impact on the shape of $\rho$.  In this document, we will construct this coordinate system as the solution to a constrained optimal control problem.

## Overview
To summarize what is to come, we will construct a cost function over $F$ that measures how much energy is needed to transport a sample $\mathbf{x} \sim \rho$ onto an embedded submanifold of $\mathcal{X}$.  This submanifold will be constructed as the set of points on $\mathcal{X}$ that whose $k$-th coordinate is zero.  This cost function will depend on $F$, $k$ and also the "transport map" that actually transports the point $\mathbf{x}$ onto the submanifold.  We will optimize this cost function over the transport map to find get a value function that measures the energy needed to transport a point $\mathbf{x}$ onto the submanifold.  We will show that this value function is itsself a coordinate map on $\mathcal{X}$ with some nice properties, namely that its value is the total distance that a point $\mathbf{x}$ needs to travel to reach the submanifold.  Finally, we will examine the expected value of this value function over $\rho$ to see how much distance a point $\mathbf{x}$ needs to travel on average to reach the submanifold.  We will vary this average distance over all possible $F$ and identify the properties of the optimal $F$ that minimizes this average distance.

# Problem setup
Let $\rho$ be a non-degenerate probability density function defined on the data space $\mathcal{X} = \mathbb{R}^n$, let $\mathcal{Z} = \mathbb{R}^n$ be the coordinate space (which we will refer to as either the **latent space** or the **base space**), and $F: \mathcal{Z} \to \mathcal{X}$ be a diffeomorphism.  We say that the inverse of $F$ is a coordinate map on $\mathcal{X}$ because it maps points in $\mathcal{X}$ to points in the coordinate space.  Our mechanism for "dropping" coordinates is to project onto a coordinate axis by setting the corresponding coordinate to zero.  We need to be careful about how exactly we define this projection operator because later we will construct a dynamical formulation of this dropping process that we will use in an optimal control problem.

## Coordinate dropping and dimensionality reduction
Our first ingredient for dimensionality reduction is the dropping operator, $\Pi_0: \mathcal{Z} \to \mathcal{Z}$, that sets an index of a coordinate to $0$.  We carefully introduce this operator in order to ensure that our notation later is clear.  We use bold letters to denote vectors and normal letters to denote scalars.  Let $\mathbf{z} \in \mathcal{Z}$ be a point in the coordinate space.  We will use the projection operators $\pi: \mathbb{R}^n \to \mathbb{R}$ and $\bar{\pi}: \mathbb{R}^n \to \mathbb{R}^{n-1}$ to denote the projection operators onto a one dimensional coordinate axis and the projection operator onto its complement, respectively.  Without loss of generality, we can assume that $\pi$ is the projection onto the $k$-th coordinate axis and $\bar{\pi}$ is the projection onto the complement of the $k$-th coordinate axis.  For example, for any $\mathbf{z} \in \mathcal{Z}$, we can split the vector into two components as
$$
\begin{align}
  \mathbf{z} &= \left(\pi(\mathbf{z}), \bar{\pi}(\mathbf{z})\right) \\
  &=: (z, \bar{\mathbf{z}})
\end{align}
$$
$z$ denotes the one dimensional coordinate that $\pi$ projects onto and $\bar{\mathbf{z}}$ denotes the $n-1$ dimensional vector of coordinates that $\bar{\pi}$ projects onto.

We use the notation $\pi^{-1}$ to denote a section of $\pi$ (Lee Thm. 4.26), meaning that $\pi^{-1}$ is a right inverse of $\pi$.  Clearly, $\pi$ is not an invertible map, and so reasoning about $\pi^{-1}$ requires a bit of care.  A practical way to interpret this inverse map is that for any time one performs a projection $\pi(\mathbf{z})$, an inverse map $\pi^{-1}$ is created that "remembers" the part of $\mathbf{z}$ that is removed by $\pi$.  For example, if $\mathbf{z} = \left(\pi(\mathbf{z}), \bar{\pi}(\mathbf{z})\right) = (z, \bar{\mathbf{z}})$, then $\pi^{-1}(.) = \left(., \bar{\mathbf{z}}\right)$.

With this notation in mind, we can now define the "dropping" operation.  Let $\gamma_0: \mathbb{R} \to \{0\}$ be the constant function that maps every point in $\mathbb{R}$ to $0$.  We denote the "dropping" operation with $\Pi_0: \mathcal{Z} \to \mathcal{Z}$ and define it as the following composition:
$$
\begin{align}
  \Pi_0 = \pi^{-1} \circ \gamma_0 \circ \pi
\end{align}
$$
When applied to a point $\mathbf{z} = (z_1, \ldots, z_n) \in \mathcal{Z}$, the operation $\Pi_0$ returns the point $\Pi_0(\mathbf{z}) = (z_1, \ldots, z_{k-1}, 0, z_{k+1}, \ldots, z_n) \in \mathcal{Z}$.

## Dynamical formulation of coordinate dropping
Rather than using $\gamma_0$ to set the $k$-th coordinate to $0$, we can consider a time-indexed family of maps $\gamma_t: \mathbb{R} \to \mathbb{R}$ that at time $t=0$ sets the $k$-th coordinate to $0$ and at time $t=1$ is the identity map.  So $\gamma_{t=1}(z) = z$ and $\gamma_{t=0}(z) = 0$ for all $z \in \mathbb{R}$.  We can then define a time dependent dropping operator $\Pi_t: \mathcal{Z} \to \mathcal{Z}$ as the following composition:
$$
\begin{align}
  \Pi_t = \pi^{-1} \circ \gamma_t \circ \pi
\end{align}
$$

## Dynamical formulation of dimensionality reduction
We will use the dropping operator $\Pi_t$ to construct our mechanism for dimensionality reduction by applying it to points in the data space.  For any point $\mathbf{x} \in \mathcal{X}$, we define the dimensionality reduction operator, $P_t: \mathcal{X} \to \mathcal{X}$ as:
$$
\begin{align}
  P_t = F \circ \Pi_t \circ F^{-1}
\end{align}
$$
This map first moves $\mathbf{x}$ to the coordinate space via $F^{-1}$, tranports the point along the $k$-th coordinate curve of $F$ in the coordinate space, and then moves the point back to the data space via $F$.

We will use this map to measure how much energy it takes to transport a point $\mathbf{x}$ along the $k$-th coordinate curve of $F$ in the coordinate space.  To do so, consider the following cost function:
$$
\begin{align}
  J_t[\gamma](x_t) = \int_0^t \left\| \frac{dP_s(x_s)}{ds} \right\|^2 ds, \quad x_s = P_s(x_0)
\end{align}
$$
This cost function measures the energy needed to transport a point $\mathbf{x}$ along the $k$-th coordinate curve of $F$ in the coordinate space when we transport it with a time-indexed family of maps $\gamma_t$.  We can define a cost function that does not depend on the choice of $\gamma_t$ by taking the infimum of $J_t$ over all possible $\gamma_t$:
$$
\begin{align}
  v_t^*(x_t) = \inf_{\gamma} J_t[\gamma](x_t)
\end{align}
$$

