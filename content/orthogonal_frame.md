Title: Orthogonal coordinate frame
Date: 2024-02-25
Category: Blog
Slug: orthogonal-coordinate-frame
hidden: true
Summary: Properties of orthogonal coordinate frames

In this post we're going to derive some properties of orthogonal coordinate frames.  A frame is a set of vectors that spans a space and an orthogonal frame is a frame where the vectors are orthogonal to each other.  A coordinate frame is a frame where the vectors commute.  These are interesting because they can be used to represent a coordinate system.

# Coordinate frames
Let $(s^1, \dots, s^n)$ be a set of scalar valued functions and let $(U_1,\dots,U_n)$ be a frame with dual frame $(\upsilon^1,\dots,\upsilon^n)$ (for the moment, we do not assume that the frame is orthogonal).  We will assume that the frame $(s^1U_1,\dots,s^nU_n)$ is a coordinate frame, meaning that
$$
\begin{align}
  [s^iU_i,s^jU_j] = 0
\end{align}
$$
where $[A,B]$ is the Lie bracket of vector fields.  First, lets isolate the Lie bracket of $(U_1,\dots,U_n)$ in terms of $U_i$ and $s^i$:
$$
\begin{align}
  [s^iU_i,s^jU_j] &= s^is^j[U_i,U_j] + s^iU_i(s^j)U_j - s^jU_j(s^i)U_i \\
  &= s^is^j\left([U_i,U_j] + U_i(\log s^j)U_j - U_j(\log s^i)U_i \right) = 0
\end{align}
$$
$$
\begin{align}
  \implies [U_i,U_j] &= U_j(\log s^i)U_i - U_i(\log s^j)U_j \\
  &= \left(U_j(\log s^i)\delta_i^k - U_i(\log s^j)\delta_j^k\right)U_k \\
  &= \left(U_j(\log s^k)\delta_i^k - U_i(\log s^k)\delta_j^k\right)U_k \\
  &= U_j(\log s^i)U_i - U_i(\log s^j)U_j
\end{align}
$$

A consequence of this is that
$$
\begin{align}
  \langle [U_i,U_j], U_i \rangle &= U_j(\log s^i) \\
  \langle [U_i,U_j], U_j \rangle &= -U_i(\log s^j) \\
  \langle [U_i,U_j], U_{k\neq i,j} \rangle &= 0
\end{align}
$$

## Orthogonal coordinate frames
Now suppose that $(U_1,\dots,U_n)$ is an orthonormal frame, meaning that $\langle U_i, U_j \rangle = \delta_{ij}$.  We can use the Kozul formula to write the covariant derivative of vectors.  Suppose $X = X^i U_i$ and $Y = Y^j U_j$ are vector fields, where $(U_1,\dots,U_n)$ is an orthonormal frame with the bracket coefficients given above.  Then
$$
\begin{align}
  \nabla_X Y = X^i Y^j \nabla_{U_i} U_j = X^i Y^j \nabla_{U_i}U_j + X(Y^j)U_j
\end{align}
$$
So we need to compute the covariant derivative of these basis vectors.  The Kozul formula tells us how to find to torsion-free, and metric compatible, covariant derivative to do this.  The formula is given by:
$$
\begin{align}
  \langle \nabla_X Y, Z \rangle = \frac{1}{2}\left(X\langle Y, Z \rangle + Y\langle X, Z \rangle - Z\langle X, Y \rangle + \langle [X,Y], Z \rangle - \langle [X,Z], Y \rangle - \langle [Y,Z], X \rangle\right)
\end{align}
$$

Then to compute the covariant derivative of $U_i$ along $U_j$, we can start by noting that the first three terms in the expression for the covariant derivative are $0$ because $U_i$ and $U_j$ are orthogonal:
$$
\begin{align}
  \nabla_{U_i}U_j &= \langle \nabla_{U_i} U_j, U_k \rangle U_k \\
  &= \frac{1}{2}\left(\cancel{U_i\langle U_j, U_k \rangle} + \cancel{U_j\langle U_i, U_k \rangle} - \cancel{U_k\langle U_i, U_j \rangle} + \langle [U_i,U_j], U_k \rangle - \langle [U_i,U_k], U_j \rangle - \langle [U_j,U_k], U_i \rangle\right) U_k \\
  &= \frac{1}{2}\left(\langle [U_i,U_j], U_k \rangle - \langle [U_i,U_k], U_j \rangle - \langle [U_j,U_k], U_i \rangle\right) U_k
\end{align}
$$
Let $i=j$.  Then we can simplify:
$$
\begin{align}
  \nabla_{U_i}U_i &= \frac{1}{2}\left(\cancel{\langle [U_i,U_i], U_k \rangle} - \langle [U_i,U_k], U_i \rangle - \langle [U_i,U_k], U_i \rangle\right) U_k \\
  &= -\langle [U_i,U_k], U_i \rangle U_k \\
  &= -\sum_{k\neq i}U_k(\log s^i)U_k
\end{align}
$$

Next, suppose that $i \neq j$.  Recalling that the inner product of $[U_i,U_j]$ and $U_k$ is nonzero when $k = i$ or $k = j$, summing over $k$ gives us:
$$
\begin{align}
  \nabla_{U_i}U_{j\neq i} &= \frac{1}{2}\langle [U_i,U_j], U_i \rangle U_i + \cancel{\frac{1}{2}\langle [U_i,U_j], U_j \rangle U_j} \\
  &\quad - \cancel{\frac{1}{2}\langle [U_i,U_i], U_j \rangle U_i} - \cancel{\frac{1}{2}\langle [U_i,U_j], U_j \rangle U_j} \\
  &\quad - \frac{1}{2}\langle [U_j,U_i], U_i \rangle U_i - \cancel{\frac{1}{2}\langle [U_j,U_j], U_i \rangle U_j} \\
  &= \langle [U_i,U_j], U_i \rangle U_i \\
  &= U_j(\log s^i)U_i
\end{align}
$$

And so, we are left with the general expression for the covariant derivative:
$$
\begin{align}
  \nabla_{U_i} U_j &= U_j(\log s^i)U_i - \sum_{k\neq i}U_k(\log s^i)\delta_{ij} U_k
\end{align}
$$
which implies that the Christoffel symbols, in this basis, are given by:
$$
\begin{align}
  \Gamma_{ij}^k &= U_j(\log s^i)\delta_i^k - U_k(\log s^i)\delta_{ij} \\
  &= \langle U_j, \nabla \log s^i\rangle \delta_i^k - \langle U_k, \nabla \log s^i\rangle \delta_{ij}
\end{align}
$$

### Non-standard properties of these Christoffel symbols
- **Strong sparsity**: $\Gamma_{ij}^k=0$ unless $k=i$ or $i=j$ (in particular, if $i,j,k$ are all distinct then $\Gamma_{ij}^k=0$).
- **Off-diagonal ($i\neq j$)**: $\nabla_{U_i}U_j = U_j(\log s^i)\,U_i$, so $\Gamma^i_{ij}=U_j(\log s^i)$ and $\Gamma^k_{ij}=0$ for $k\neq i$.
- **Diagonal ($i=j$)**: $\nabla_{U_i}U_i = -\sum_{k\neq i} U_k(\log s^i)\,U_k$, so $\Gamma^i_{ii}=0$ and $\Gamma^k_{ii}=-U_k(\log s^i)$ for $k\neq i$.
- **Metric-compatibility skew**: with $\Gamma_{ijk}:=\langle \nabla_{U_i}U_j, U_k\rangle$, one has $\Gamma_{ijk}=-\Gamma_{ikj}$.

### Divergence
We can use the covariant derivative to write the divergence of the frame vectors in a simple form.  Recall that the divergence of a vector field $X$ can be expressed using the covariant derivative, and a basis $(U_1,\dots,U_n)$ as:
$$
\begin{align}
  \text{Div}(U_j) &= \sum_i \langle \nabla_{U_i} U_j, U_i \rangle \\
  &= \sum_i \langle \sum_k \left( U_j(\log s^i)\delta_i^k - U_k(\log s^i)\delta_{ij} \right) U_k, U_i \rangle \\
  &= \sum_i \left( U_j(\log s^i)\delta_i^i - U_i(\log s^i)\delta_{ij} \right) \\
  &= U_j(\sum_i \log s^i) - U_j(\log s^j) \\
\end{align}
$$

## Implications for coframe
We can see that the distribution spanned by $(U_1,\dots,U_n)$ is involutive, so there is an integral manifold that is locally spanned by the frame.  We will use $\mathcal{S}_i$ to denote the integral manifold spanned by $U_i$.

Next, we can derive the expression for the exterior derivative of the dual frame.  We can use the following identity:
$$
\begin{align}
  d\upsilon^k &= -\sum_{i<j}c^k_{ij}\upsilon^i\wedge\upsilon^j \\
  \text{where }& [U_i,U_j] = \sum_k c^k_{ij}U_k \\
  \text{and }& c_{ij}^k = U_j(\log s^k)\delta_i^k - U_i(\log s^k)\delta_j^k \\
  &\qquad\;= \frac{1}{\sigma_k}\,(\delta_i^k\,\upsilon_{j\ell} - \delta_j^k\,\upsilon_{i\ell})\,(\partial_\ell J)_{p q}\,\upsilon_{k p}\, \omega_{q k}
\end{align}
$$
$$
\begin{align}
  d\upsilon^k &= -\sum_{i<j}c^k_{ij}\upsilon^i\wedge\upsilon^j \\
  &= -\sum_{i<j}\left(U_j(\log s^k)\delta_i^k - U_i(\log s^k)\delta_j^k\right)\upsilon^i\wedge\upsilon^j \\
  &= -\sum_{k<j}U_j(\log s^k)\upsilon^k\wedge \upsilon^j + \sum_{i<k}U_i(\log s^k)\upsilon^i \wedge \upsilon^k \\
  &= -\sum_{k<i}U_i(\log s^k)\upsilon^k\wedge \upsilon^i + \sum_{i<k}U_i(\log s^k)\upsilon^i \wedge \upsilon^k \\
  &= \sum_{k<i}U_i(\log s^k)\upsilon^i\wedge \upsilon^k + \sum_{i<k}U_i(\log s^k)\upsilon^i \wedge \upsilon^k \\
  &= \sum_{i\neq k}U_i(\log s^k)\upsilon^i\wedge \upsilon^k \\
  &= \sum_i U_i(\log s^k)\upsilon^i\wedge \upsilon^k
\end{align}
$$

A consequence of this is the following identity:
$$
\begin{align}
  d\upsilon^k \wedge \upsilon^k = 0, \quad \text{for all } k
\end{align}
$$

In coordinates, we have that:
$$
\begin{align}
\big(d\upsilon^k - \sum_i \upsilon_{i\ell}\,\partial_\ell(\log s^k)\,\upsilon^i \wedge \upsilon^k\big)
:= \sum_{i<j} \Big[\big(\partial_i \upsilon_{kj} - \partial_j \upsilon_{ki}\big)
- \upsilon_{i\ell}\,\partial_\ell(\log s^k)\,\delta_{jk} + \upsilon_{j\ell}\,\partial_\ell(\log s^k)\,\delta_{ik}\Big]\; dx^i \wedge dx^j.
\end{align}
$$

Ordered-basis coefficients (i<j): the coefficient of $dx^i \wedge dx^j$ equals
$$
\begin{align}
  C^{(k)}_{ij}
  &= (\partial_i \upsilon_{kj} - \partial_j \upsilon_{ki}) - \upsilon_{i\ell}\,\partial_\ell(\log s^k)\,\delta_{jk} + \upsilon_{j\ell}\,\partial_\ell(\log s^k)\,\delta_{ik}.
\end{align}
$$
This identity follows directly from the structure constants $c^k_{ij} = U_j(\log s^k)\delta_i^k - U_i(\log s^k)\delta_j^k$, and we verified numerically (see `notebooks/check_dv_identity.py`).
<!--
# Orthogonal coframes
Suppose we have a matrix, $J$, whose singular value decomposition is given by:
$$
\begin{align}
    J_{ij} &= U_{iu} \sigma_u V_{ju} \\
\end{align}
$$
Since $U$ and $V$ are orthogonal, we can write the components of their inverses as:
$$
\begin{align}
  U_{iu} = \upsilon_{ui} \\
  V_{ju} = \omega_{ju} \\
\end{align}
$$

and since we can write the derivatives of $U$ as:
$$
\begin{align}
  \partial U_{ku} U_{kv} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right), \quad u \neq v
\end{align}
$$
we can write the derivatives of $\upsilon$ as:
$$
\begin{align}
  \partial \upsilon_{uk} \upsilon_{vk} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_u \upsilon_{vi} \omega_{uj} + \sigma_v \upsilon_{ui} \omega_{vj}\right), \quad u \neq v
\end{align}
$$
We want to isolate the term $\partial \upsilon_{uk}$ to fit the expression for the constraint on the dual frame.  To do this, we can multiply by $\upsilon_{v w}$ and sum over $\nu$:

$$
\begin{align}
  \partial \upsilon_{uw} &= \partial \upsilon_{uk} \upsilon_{vk} \upsilon_{v w} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_u \upsilon_{vi} \omega_{uj} + \sigma_v \upsilon_{ui} \omega_{vj}\right) \upsilon_{v w}
\end{align}
$$
Renaming the indices, we get:
$$
\begin{align}
  \partial_i \upsilon_{\ell j} &= \sum_{m \neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2}\; \partial_i J_{pq}\,\left( \sigma_\ell\, \upsilon_{m p}\, \omega_{\ell q} + \sigma_m\, \upsilon_{\ell p}\, \omega_{m q} \right)\, \upsilon_{m j}
\end{align}
$$

### Exanding constraints
Recall the constraint on the dual frame:
$$
\begin{align}
d\upsilon^l \wedge \upsilon^l = \sum_{i<j<k} \Big[
(\partial_i \upsilon_{lj} - \partial_j \upsilon_{li})\,\upsilon_{lk}
+ (\partial_j \upsilon_{lk} - \partial_k \upsilon_{lj})\,\upsilon_{li}
+ (\partial_k \upsilon_{li} - \partial_i \upsilon_{lk})\,\upsilon_{lj}
\Big]\; dx^i \wedge dx^j \wedge dx^k.
\end{align}
$$
we can now write the coordinates in terms of the expression that we derived above:
$$
\begin{align}
(\partial_i \upsilon_{lj} - \partial_j \upsilon_{li})\,\upsilon_{lk}
+ (\partial_j \upsilon_{lk} - \partial_k \upsilon_{lj})\,\upsilon_{li}
+ (\partial_k \upsilon_{li} - \partial_i \upsilon_{lk})\,\upsilon_{lj} &=
\sum_{m\neq \ell} \Big[
  (A^{(i)}_{\ell m}\, \upsilon_{m j} - A^{(j)}_{\ell m}\, \upsilon_{m i})\, \upsilon_{\ell k}
 + (A^{(j)}_{\ell m}\, \upsilon_{m k} - A^{(k)}_{\ell m}\, \upsilon_{m j})\, \upsilon_{\ell i}
 + (A^{(k)}_{\ell m}\, \upsilon_{m i} - A^{(i)}_{\ell m}\, \upsilon_{m k})\, \upsilon_{\ell j}
\Big]
\end{align}
$$

where, for an orthonormal coframe from the SVD of $J$,
$$
\begin{align}
  A^{(i)}_{\ell m} &= \frac{\sigma_\ell\, dS^{(i)}_{m\ell} + \sigma_m\, dS^{(i)}_{\ell m}}{\sigma_\ell^2 - \sigma_m^2},\quad m\neq \ell, \\
  dS^{(i)} &= \upsilon\, (\partial_i J)\, \omega,\quad dS^{(i)}_{ab} = \upsilon_{a p}\, (\partial_i J)_{p q}\, \omega_{q b}.
\end{align}
$$

Sub-problem 1 (derivative of the coframe row): Using the SVD identities,
$$
\begin{align}
  \partial_i \upsilon_{\ell j} = \sum_{m\neq \ell} A^{(i)}_{\ell m}\, \upsilon_{m j}.
\end{align}
$$
Numerically verified with JAX autodiff and `notebooks/svd.py` (custom SVD JVP), relative error ~ $10^{-5}$.

Equivalently, expanding the contractions without the $dS$ shorthand:
$$
\begin{align}
  \partial_i \upsilon_{\ell j}
  &= \sum_{m\neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2}\; \partial_i J_{pq}\,\left( \sigma_\ell\, \upsilon_{m p}\, \omega_{\ell q} + \sigma_m\, \upsilon_{\ell p}\, \omega_{m q} \right)\, \upsilon_{m j} \\
  &= \sum_{m\neq \ell} \frac{ \sigma_\ell\, \upsilon_{m p}\, (\partial_i J)_{p q}\, \omega_{q \ell} + \sigma_m\, \upsilon_{\ell p}\, (\partial_i J)_{p q}\, \omega_{q m} }{\sigma_\ell^2 - \sigma_m^2}\; \upsilon_{m j}.
\end{align}
$$
This expanded form matches the analytic form above to a relative error of ~ $5\times 10^{-8}$ in numerical tests (`notebooks/dual_frame_constraint_check_jax.py`).

Sub-problem 2 (single-term coefficient):
$$
\begin{align}
  (\partial_i \upsilon_{\ell j} - \partial_j \upsilon_{\ell i})\, \upsilon_{\ell k}
  = \sum_{m\neq \ell} \left(A^{(i)}_{\ell m}\, \upsilon_{m j} - A^{(j)}_{\ell m}\, \upsilon_{m i}\right)\, \upsilon_{\ell k}.
\end{align}
$$
Matches autodiff to ~ $10^{-5}$ on random trials.

Expanded form (no $dS$ shorthand):
$$
\begin{align}
  (\partial_i \upsilon_{\ell j} - \partial_j \upsilon_{\ell i})\, \upsilon_{\ell k}
  &= \sum_{m\neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2} \Bigg[
     \sigma_\ell\, \upsilon_{m p}\, \omega_{q \ell} \Big( (\partial_i J)_{p q}\, \upsilon_{m j} - (\partial_j J)_{p q}\, \upsilon_{m i} \Big)
   + \sigma_m\, \upsilon_{\ell p}\, \omega_{q m} \Big( (\partial_i J)_{p q}\, \upsilon_{m j} - (\partial_j J)_{p q}\, \upsilon_{m i} \Big)
  \Bigg] \upsilon_{\ell k}.
\end{align}
$$

Sub-problem 3 (cyclic sum): summing the three cyclic permutations yields the coordinate expression above. Numerical check in `notebooks/dual_frame_constraint_check_jax.py` shows agreement with autodiff to ~ $10^{-5}$.

Fully expanded and grouped cyclic sum:
$$
\begin{align}
&\ (\partial_i \upsilon_{\ell j} - \partial_j \upsilon_{\ell i})\,\upsilon_{\ell k}
 + (\partial_j \upsilon_{\ell k} - \partial_k \upsilon_{\ell j})\,\upsilon_{\ell i}
 + (\partial_k \upsilon_{\ell i} - \partial_i \upsilon_{\ell k})\,\upsilon_{\ell j} \\
&= \sum_{m\neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2} \Bigg[\
  \sigma_\ell\, \upsilon_{m p}\,\omega_{q \ell}\,\Big(\
    (\partial_i J)_{p q}\, \upsilon_{m j}\, \upsilon_{\ell k}\
  - (\partial_j J)_{p q}\, \upsilon_{m i}\, \upsilon_{\ell k}\
  + (\partial_j J)_{p q}\, \upsilon_{m k}\, \upsilon_{\ell i}\
  - (\partial_k J)_{p q}\, \upsilon_{m j}\, \upsilon_{\ell i}\
  + (\partial_k J)_{p q}\, \upsilon_{m i}\, \upsilon_{\ell j}\
  - (\partial_i J)_{p q}\, \upsilon_{m k}\, \upsilon_{\ell j}\
  \Big) \\
&\qquad\qquad\qquad\ + \sigma_m\, \upsilon_{\ell p}\,\omega_{q m}\,\Big(\
    (\partial_i J)_{p q}\, \upsilon_{m j}\, \upsilon_{\ell k}\
  - (\partial_j J)_{p q}\, \upsilon_{m i}\, \upsilon_{\ell k}\
  + (\partial_j J)_{p q}\, \upsilon_{m k}\, \upsilon_{\ell i}\
  - (\partial_k J)_{p q}\, \upsilon_{m j}\, \upsilon_{\ell i}\
  + (\partial_k J)_{p q}\, \upsilon_{m i}\, \upsilon_{\ell j}\
  - (\partial_i J)_{p q}\, \upsilon_{m k}\, \upsilon_{\ell j}\
  \Big)
\Bigg].
\end{align}
$$

Cancellation note: in each bracket, terms pair with opposite signs across the three permutations; after grouping by $(\partial_r J)_{pq}$, all surviving terms are exactly those shown above. Grouped vs. ungrouped equality verified numerically with relative error ~ $6\times10^{-8}$ (see `notebooks/dual_frame_constraint_check_jax.py`).

Final simplified form (cyclic sum):
$$
\begin{align}
& (\partial_i \upsilon_{\ell j} - \partial_j \upsilon_{\ell i})\,\upsilon_{\ell k}
 + (\partial_j \upsilon_{\ell k} - \partial_k \upsilon_{\ell j})\,\upsilon_{\ell i}
 + (\partial_k \upsilon_{\ell i} - \partial_i \upsilon_{\ell k})\,\upsilon_{\ell j} \\
&= \sum_{m\neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2}\; H^{(m,\ell)}_{p q}\,\left(
  (\partial_i J)_{p q}\, G_i^{(m,\ell)}
- (\partial_j J)_{p q}\, G_j^{(m,\ell)}
+ (\partial_k J)_{p q}\, G_k^{(m,\ell)}
\right).
\end{align}
$$

where
$$
\begin{align}
  H^{(m,\ell)}_{p q} &:= \sigma_\ell\, \upsilon_{m p}\, \omega_{q \ell} + \sigma_m\, \upsilon_{\ell p}\, \omega_{q m}, \\
  G_i^{(m,\ell)} &:= \upsilon_{m j}\, \upsilon_{\ell k} - \upsilon_{m k}\, \upsilon_{\ell j}, \\
  G_j^{(m,\ell)} &:= \upsilon_{m k}\, \upsilon_{\ell i} - \upsilon_{m i}\, \upsilon_{\ell k}, \\
  G_k^{(m,\ell)} &:= \upsilon_{m i}\, \upsilon_{\ell j} - \upsilon_{m j}\, \upsilon_{\ell i}.
\end{align}
$$

Cancellation note: this compact \partial J-based cyclic form is algebraically equivalent to the fully expanded grouped expression; numerical checks confirm equality to ~ $6\times10^{-8}$ (see `notebooks/dual_frame_constraint_check_jax.py`).

Specialization when $\omega = I$:
$$
\begin{align}
& (\partial_i \upsilon_{\ell j} - \partial_j \upsilon_{\ell i})\,\upsilon_{\ell k}
 + (\partial_j \upsilon_{\ell k} - \partial_k \upsilon_{\ell j})\,\upsilon_{\ell i}
 + (\partial_k \upsilon_{\ell i} - \partial_i \upsilon_{\ell k})\,\upsilon_{\ell j} \\
&= \sum_{m\neq \ell} \frac{1}{\sigma_\ell^2 - \sigma_m^2}\;\Big[\
  \sigma_\ell\, \upsilon_{m p}\Big( (\partial_i J)_{p \ell}\, G_i^{(m,\ell)} - (\partial_j J)_{p \ell}\, G_j^{(m,\ell)} + (\partial_k J)_{p \ell}\, G_k^{(m,\ell)} \Big) \\
&\qquad\qquad\qquad\qquad\ \ + \sigma_m\, \upsilon_{\ell p}\Big( (\partial_i J)_{p m}\, G_i^{(m,\ell)} - (\partial_j J)_{p m}\, G_j^{(m,\ell)} + (\partial_k J)_{p m}\, G_k^{(m,\ell)} \Big)\Big].
\end{align}
$$
This follows from replacing $\omega_{q\ell}$ and $\omega_{q m}$ by $\delta_{q\ell}$ and $\delta_{q m}$, i.e., selecting the $\ell$-th and $m$-th columns of $\partial J$. The identity has been validated numerically in `notebooks/dual_frame_constraint_check_jax.py`.

# Orthogonal frames
Suppose that we have a Riemannian metric $g$ and suppose that the frame is orthogonal, meaning that $U_i$ is orthogonal to $U_j$ for $i\neq j$:
$$
\begin{align}
  g(U_i,U_j) = 0, \quad \text{for all } i\neq j
\end{align}
$$
Furthermore, taking the Lie derivative of this equation along a vector field $X$ should also be zero:
$$
\begin{align}
  \mathcal{L}_X g(U_i,U_j) = 0, \quad \text{for all } i\neq j
\end{align}
$$
We can use the identity for the Lie derivative from Lee Proposition 12.32 to expand the Lie derivative of the metric:
$$
\begin{align}
  \mathcal{L}_X g(U_i,U_j) = (\mathcal{L}_X g)(U_i,U_j) + g([X,U_i],U_j) + g(U_i,[X,U_j])
\end{align}
$$
Lets write out the coordinate expression for each term.  Suppose that $g = g_{uv}dx^u\otimes dx^v$.
### Term 1
From Lee Example 12.35, we have that:
$$
\begin{align}
  \mathcal{L}_X g = (X(g_{uv}) + g_{kv}\frac{\partial X^k}{\partial x^u} + g_{uk}\frac{\partial X^k}{\partial x^v})dx^u\otimes dx^v
\end{align}
$$
Applying this to $U_i$ and $U_j$, we get:
$$
\begin{align}
  \mathcal{L}_X g(U_i,U_j) &= (X(g_{uv}) + g_{kv}\frac{\partial X^k}{\partial x^u} + g_{ku}\frac{\partial X^k}{\partial x^v})U_i^uU_j^v \\
  &= U_i^uU_j^vX(g_{uv}) + g_{kv}U_i(X^k)U^v_j + g_{ku}U_j(X^k)U^u_i \\
  &= U_i^uU_j^vX(g_{uv}) + g_{uv}U_i(X^u)U^v_j + g_{uv}U_j(X^u)U^v_i \\
  &= U_i^uU_j^vX(g_{uv}) + g_{uv}\left(U_i(X^u)U^v_j + U_j(X^u)U^v_i\right)
\end{align}
$$

### Term 2
$$
\begin{align}
  g(\mathcal{L}_X U_i,U_j) &= g([X, U_i],U_j) \\
  &= g_{uv}\left(X(U_i^u) - U_i(X^u)\right)U_j^v
\end{align}
$$

### Term 3
$$
\begin{align}
  g(U_i,\mathcal{L}_X U_j) &= g(U_i,[X, U_j]) \\
  &= g_{uv}\left(X(U_j^u) - U_j(X^u)\right)U_i^v
\end{align}
$$
We can see that the second parts of terms 2 and 3 cancel out with the last 2 terms of term 1, so we get:
$$
\begin{align}
  0 = \mathcal{L}_X g(U_i,U_j) &= U_i^uU_j^vX(g_{uv}) + g_{uv}\left(X(U_i^u)U_j^v + U_i^uX(U_j^v)\right) \\
  &= U_i^uU_j^vX(g_{uv}) + g_{uv}X(U_i^u U_j^v) \\
  &= X(g_{uv}U_i^u U_j^v)
\end{align}
$$


 -->


# Mass preserving functions
Given this coordinate system, we need to see which kinds of functions can be integrated on $(\upsilon^1,\dots,\upsilon^n)$.  Let $p_i: \mathcal{C}^\infty(\mathcal{S_i})$.  We will interpret each $p_i$ as the probability density function on the manifold spanned by $U_i$.  The condition that we want to enforce is that the densities integrate to 1:
$$
\begin{align}
  \int_{S_i}p_i \upsilon^i = 1
\end{align}
$$
To enforce this constraint, we need to ensure that the flow of the vector field $U_{j\neq i}$ preserves the mass on $S_i$:
$$
\begin{align}
  \frac{d}{dt}_{t=0}\mathbb{P}(\Theta_t(S_i)) &= \frac{d}{dt}_{t=0}\int_{\Theta_t(S_i)}\Theta^{-1}_t p_i \upsilon^i \\
  &= \int_{S_i}\mathcal{L}_{U_{j\neq i}}(p_i\upsilon^i) \\
\end{align}
$$
So we assert that
$$
\begin{align}
  0 &= \mathcal{L}_{U_{j\neq i}}(p_i\upsilon^i) \\
  &= d(\underbrace{U_{j\neq i} \lrcorner p_i\upsilon^i}_{0}) + U_{j\neq i} \lrcorner d(p_i\upsilon^i) \\
  &= U_{j\neq i} \lrcorner d(p_i\upsilon^i) \\
  &= U_{j\neq i} \lrcorner \left(dp_i \wedge \upsilon^i + p_id\upsilon^i \right) \\
  &= dp_i(U_j)\upsilon^i - \underbrace{\upsilon^i(U_j)}_{0}dp_i + p_i d\upsilon^i(U_j) \\
  &= U_j(p_i)\upsilon^i + p_i \sum_{k\neq i}U_k(\log s^i)\left(\upsilon^k(U_j)\upsilon^i + \underbrace{\upsilon^i(U_j)}_{0}\upsilon^k\right) \\
  &= \left(U_j(p_i) + p_i U_j(\log s^i)\right)\upsilon^i \\
  &= \frac{1}{p_i}\left(U_j(\log p_i) + U_j(\log s^i)\right)\upsilon^i \\
  &= \frac{1}{p_i}\left(U_j(\log p_i + \log s^i)\right)\upsilon^i \\
\end{align}
$$
In order for the flow of $U_{j\neq i}$ to preserve the mass on $S_i$, we need to enforce that $\log p_i + \log s^i = 0$, so we get $p_i = \frac{1}{s^i}$.


<!--
$$
\begin{align}
  \delta c_{ij}^k &= \big(\delta_i^k\,\delta U_j - \delta_j^k\,\delta U_i\big)(\log \sigma_k)
  + (\delta_i^k U_j - \delta_j^k U_i)\Big(\tfrac{\langle U_{:k},\, \delta J\, V_{:k}\rangle}{\sigma_k}\Big),\\
  \delta \sigma_k &= \big(U^T\,\delta J\,V\big)_{kk}, \\
  \delta U &= U\,\Omega_U,\quad (\Omega_U)_{m k} = \frac{\sigma_k\, (U^T\,\delta J\,V)_{m k} + \sigma_m\, (U^T\,\delta J\,V)_{k m}}{\sigma_k^2 - \sigma_m^2},\; m\neq k,\\
  \delta V &= V\,\Omega_V,\quad (\Omega_V)_{m k} = \frac{\sigma_m\, (U^T\,\delta J\,V)_{m k} + \sigma_k\, (U^T\,\delta J\,V)_{k m}}{\sigma_k^2 - \sigma_m^2},\; m\neq k.
\end{align}
$$
Numerically verified against JAX JVP to ~ $7\times 10^{-8}$ (see `notebooks/vary_cijk_jax.py`).

### Single-entry variation (\delta J = E_{ab})
$$
\begin{align}
  \delta c_{ij}^k
  &= \delta_i^k\,\Omega_{m j}\,U_m(\log \sigma_k)
   \, - \, \delta_j^k\,\Omega_{m i}\,U_m(\log \sigma_k)
   \, + \, (\delta_i^k U_j - \delta_j^k U_i)\Big(\tfrac{U_{a k} V_{b k}}{\sigma_k}\Big),\\
  \Omega_{m j} &= \frac{\sigma_j\, U_{a m} V_{b j} + \sigma_m\, U_{a j} V_{b m}}{\sigma_j^2 - \sigma_m^2},\quad m\neq j,\qquad \Omega_{j j}=0,\\
  U_m(\log \sigma_k) &= \frac{1}{\sigma_k}\,\upsilon_{m\ell}\,\upsilon_{k p}\,(\partial_\ell J)_{p q}\,\omega_{q k},\qquad \frac{\delta \sigma_k}{\sigma_k} = \frac{U_{a k} V_{b k}}{\sigma_k}.
\end{align}
$$
This specialized form matches the JAX JVP with a single-entry perturbation to ~ $5\times 10^{-8}$ (see `notebooks/vary_cijk_jax.py`).

#### Single-entry variation with $\omega = I$
$$
\begin{align}
  U_m(\log \sigma_k) &= \frac{1}{\sigma_k}\,\upsilon_{m\ell}\,(\partial_\ell J)_{p k}\,\upsilon_{k p},\\
  \frac{\delta \sigma_k}{\sigma_k} &= \frac{U_{a k}\,\delta_{b k}}{\sigma_k},\\
  (\Omega_U)_{m j} &= \frac{\sigma_j\, U_{a m}\,\delta_{b j} + \sigma_m\, U_{a j}\,\delta_{b m}}{\sigma_j^2 - \sigma_m^2},\quad m\neq j,\ \Omega_{j j}=0.
\end{align}
$$
These replacements (with $\omega=I$) are the only safe simplifications; further cancellations (e.g., dropping $\delta V$-induced contributions) are not valid in general. Numerically validated in `notebooks/vary_cijk_jax.py`. -->


# Change of variables formula in ambient space vs on coordinate curve
Ambient space:
$$
\begin{align}
  x = f(z), \quad z\sim p_z(z) \\
  \log p_x(x) = \log p_z(z) - \log \det J(z), \quad J = \frac{\partial f(z)}{\partial z}
\end{align}
$$
Coordinate curve:
$$
\begin{align}
  x = f(z_1,0), \quad z_1\sim p_z(z_1) \\
  \log p_x(x) = \log p_{z_1}(z_1) - \log \det J_1(z_1), \quad J_1 = \frac{\partial f(z_1,0)}{\partial z_1}
\end{align}
$$