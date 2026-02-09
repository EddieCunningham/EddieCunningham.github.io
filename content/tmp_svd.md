Title: Singular value decomposition derivatives
Date: 2023-11-10
Category: Blog
<!-- status: published -->
Tags: svd
Slug: svd-derivatives
Summary: Derivatives of the singular value decomposition

The singular value decomposition (SVD) is a matrix decomposition that is used in many applications.  It is defined as:
$$
\begin{align}
  J &= U \Sigma V^T
\end{align}
$$
where $U$ and $V$ are orthogonal matrices and $\Sigma$ is a diagonal matrix with non-negative entries.  The diagonal entries of $\Sigma$ are called the singular values of $J$ and are denoted as $\sigma_1,\dots,\sigma_n$.  The singular values are the square roots of the eigenvalues of $J^TJ$.  In this post we're going to go over how to differentiate the elements of the SVD under the assumption that the singular values are all distinct and non-zero.

### Einstein notation
Before proceeding, we need to understand Einstein notation.  Einstein notation is an alternative way of writing matrix equations where we undo the matrix notation and remove the summation symbol.  For example, lets write the equation $Ax = b$ in Einstein notation.
  - Step 1: Undo the matrix notation
    - $Ax = b \to \sum_j J_{ij}x_j = b_i$
  - Step 2: Remove the summation symbol
    - $\sum_j J_{ij}x_j = b_i \to J_{ij}x_j = b_i$

And thats it!  All we did was remove the summation symbol.  When we see Einstein notation in practice, we implicitly assume that there is a summation over indices that only appear on one side of the equality.  Also in Einstein notation, we will make use of the Kronecker delta function $\delta_{ij}$ which is $1$ when $i=j$ and $0$ otherwise.

### Orthogonal matrices
Next, we need to know how to differentiate orthogonal matrices.  Let $Q$ be an orthogonal matrix, then by definition $Q_{ki}Q_{kj} = \delta_{ij}$.  Taking the derivative yields:
$$
\begin{align}
  \partial (Q_{ki}Q_{kj}) = \partial \delta_{ij} \\
  \implies \partial Q_{ki} Q_{kj} + Q_{ki} \partial Q_{kj} = 0 \\
  \implies \partial Q_{ki} Q_{kj} = -Q_{ki} \partial Q_{kj} \\
\end{align}
$$
To make this equations clearer, we can undo some of the Einstein notation by letting $q_i := Q_{:,i}$ be the $i$th column of $Q$.  Then we have:
$$
\begin{align}
  \partial q_i \cdot q_j = -\partial q_j \cdot q_i
\end{align}
$$
Note that when $i=j$, $\partial q_i \cdot q_i = 0$.  This will be useful when we differentiate the SVD.

# Singular value decomposition derivatives
Lets start by writing the SVD using Einstein notation
$$
\begin{align}
    J_{ij} &= U_{iu} \sigma_u V_{ju} \\
\end{align}
$$
with some term rearrangement, we can write two equations:
$$
\begin{align}
    J_{ij}U_{iu} &= \sigma_u V_{ju} \\
    J_{ij}V_{ju} &= \sigma_u U_{iu}
\end{align}
$$
by applying a derivative, we get
$$
\begin{align}
    \partial J_{ij}U_{iu} + J_{ij}\partial U_{iu} &= \partial \sigma_u V_{ju} + \sigma_u \partial V_{ju} \\
    \partial J_{ij}V_{ju} + J_{ij}\partial V_{ju} &= \partial \sigma_u U_{iu} + \sigma_u \partial U_{iu}
\end{align}
$$
We'll call the first equation, equation 1 and the second equation, equation 2.

## Singular value derivaties
To get the derivatives of the singular values, we can multiply both sides of equation 2 by $U_{iu}$ and summing over $i$:
$$
\begin{align}
    \partial J_{ij}V_{ju} U_{iu} + \underbrace{J_{ij}\partial V_{ju} U_{iu}}_{\sigma_u V_{ju} \partial V_{ju}=0} &= \partial \sigma_u \underbrace{U_{iu} U_{iu}}_{1} + \sigma_u \underbrace{\partial U_{iu} U_{iu}}_{0} \\
    \implies \partial \sigma_u &= \partial J_{ij}U_{iu} V_{ju}
\end{align}
$$

## Singular vector derivatives
Next, to isolate the derivatives of the singular vecotrs, we'll first multiply both sides of equation 1 by $V_{jv}$, where $v \neq u$ and sum over $j$:

$$
\begin{align}
    \partial J_{ij}U_{iu} V_{jv} + \underbrace{J_{ij}\partial U_{iu} V_{jv}}_{\sigma_v \partial U_{iu} U_{iv}} &= \partial \sigma_u \underbrace{V_{ju} V_{jv}}_{0} + \sigma_u \partial V_{ju} V_{jv} \\
    \partial J_{ij}U_{iu} V_{jv} &= -\sigma_v \partial U_{iu} U_{iv} + \sigma_u \partial V_{ju} V_{jv}
\end{align}
$$
Similarly we can do the same with equation 2 but multiply by $U_{iv}$ where $v\neq u$ and sum over $i$:
$$
\begin{align}
    \partial J_{ij}V_{ju} U_{iv} + \underbrace{J_{ij}\partial V_{ju} U_{iv}}_{\sigma_v \partial V_{ju} V_{jv}} &= \partial \sigma_u \underbrace{U_{iu} U_{iv}}_{0} + \sigma_u \partial U_{iu} U_{iv} \\
    \partial J_{ij}U_{iv} V_{ju} &= \sigma_u \partial U_{iu} U_{iv} - \sigma_v \partial V_{ju} V_{jv}
\end{align}
$$

So we're left with the equation
$$
\begin{align}
  \partial J_{ij}U_{iu} V_{jv} &= -\sigma_v \partial U_{iu} U_{iv} + \sigma_u \partial V_{ju} V_{jv} \\
  \partial J_{ij}U_{iv} V_{ju} &= \sigma_u \partial U_{iu} U_{iv} - \sigma_v \partial V_{ju} V_{jv}
\end{align}
$$

### Left singular vectors
Lets multiply the above equations by $\sigma_v$ and $\sigma_u$ respectively:
$$
\begin{align}
    \sigma_v \partial J_{ij}U_{iu} V_{jv} &= -{\sigma_v}^2 \partial U_{iu} U_{iv} + \sigma_v \sigma_u \partial V_{ju} V_{jv} \\
    \sigma_u \partial J_{ij}U_{iv} V_{ju} &= {\sigma_u}^2 \partial U_{iu} U_{iv} - \sigma_v \sigma_u \partial V_{ju} V_{jv}
\end{align}
$$
If we sum the equations, the last terms cancel and we're left with
$$
\begin{align}
    \partial J_{ij}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right) = ({\sigma_u}^2 - {\sigma_v}^2) \partial U_{iu} U_{iv} \\
    \implies \partial U_{iu} U_{iv} = \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right)
\end{align}
$$

### Right singular vectors
Similarly, if we multiplied by $\sigma_u$ and $\sigma_v$ respectively, we get
$$
\begin{align}
    \sigma_u \partial J_{ij}U_{iu} V_{jv} &= -{\sigma_v} \sigma_u \partial U_{iu} U_{iv} + {\sigma_u}^2 \partial V_{ju} V_{jv} \\
    \sigma_v\partial J_{ij}U_{iv} V_{ju} &= \sigma_v\sigma_u \partial U_{iu} U_{iv} - {\sigma_v}^2 \partial V_{ju} V_{jv}
\end{align}
$$
If we sum the equations, the first terms on the RHS cancel and we're left with
$$
\begin{align}
    \partial J_{ij}\left(\sigma_v U_{iv} V_{ju} + \sigma_u U_{iu} V_{jv}\right) = ({\sigma_u}^2 - {\sigma_v}^2) \partial V_{ju} V_{jv} \\
    \implies \partial V_{ju} V_{jv} = \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_v U_{iv} V_{ju} + \sigma_u U_{iu} V_{jv}\right)
\end{align}
$$

## Summary
To simplify the expressions, we'll use the notation $U_i := U_{:,i}$ and $V_i := V_{:,i}$ to denote the $i$th column of $U$ and $V$ respectively.  Then returning to matrix notation yields:
$$
\begin{align}
  \partial \sigma_u &= \partial J_{ij}U_{iu} V_{ju} \\
  \partial U_u \cdot U_{v\neq u} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right) \\
  \partial V_u \cdot V_v &= \frac{1}{\sigma_u^2 - \sigma_v^2} \partial J_{ij}\left(\sigma_v U_{iv} V_{ju} + \sigma_u U_{iu} V_{jv}\right)
\end{align}
$$

Note that to isolate the derivatives of $U$ and $V$, we can write them as a linear combination of the singular vectors:
$$
\begin{align}
  \partial U_u = (\partial U_u \cdot U_{v\neq u}) U_u \\
  \partial V_u = (\partial V_u \cdot V_{v\neq u}) V_u
\end{align}
$$
Because $U$ and $V$ are orthogonal, $\partial U_u \cdot U_u = \partial V_u \cdot V_u = 0$.


# Time derivative
We can also see how the singular vectors and singular values evolve when we flow on the vector field:
$$
\begin{align}
  \frac{dx_t}{dt} = X_t(x_t)
\end{align}
$$
To do this, recall that we can write the time derivative of the components of $J$ as:
$$
\begin{align}
  \frac{dJ}{dt} = \nabla X_t J
\end{align}
$$
Then we can look at the time derivative of the SVD derivatives.

### Singular value derivatives
$$
\begin{align}
  \frac{d\sigma_u}{dt} &= \frac{dJ_{ij}}{dt}U_{iu} V_{ju} \\
  &= (\nabla X_t)_{ik} J_{kj} U_{iu} V_{ju} \\
  &= (\nabla X_t)_{ik} U_{iu} \sigma_u U_{ku} \\
\end{align}
$$
This is more simply expressed using the log of the singular values:
$$
\begin{align}
  \frac{d\log \sigma_u}{dt} = (\nabla X_t)_{ik} U_{iu} U_{ku}
\end{align}
$$

### Left singular vector derivatives
$$
\begin{align}
  \frac{dU_u}{dt} \cdot U_{v\neq u} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \frac{dJ_{ij}}{dt}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right) \\
  &= \frac{1}{\sigma_u^2 - \sigma_v^2} (\nabla X_t)_{ik} J_{kj}\left(\sigma_u U_{iv} V_{ju} + \sigma_v U_{iu} V_{jv}\right) \\
  &= \frac{1}{\sigma_u^2 - \sigma_v^2} (\nabla X_t)_{ik}\left(\sigma_u^2 U_{iv} U_{ku} + \sigma_v^2 U_{iu} U_{kv}\right) \\
  &= \frac{\sigma_u^2}{\sigma_u^2 - \sigma_v^2} U_v^T(\nabla X_t)U_u + \frac{\sigma_v^2}{\sigma_u^2 - \sigma_v^2} U_u^T(\nabla X_t)U_v \\
  &= U_v^T(\frac{\sigma_u^2}{\sigma_u^2 - \sigma_v^2}\nabla X_t + \frac{\sigma_v^2}{\sigma_u^2 - \sigma_v^2} \nabla X_t^T)U_u
\end{align}
$$

### Right singular vector derivatives
$$
\begin{align}
  \frac{dV_u}{dt} \cdot V_{v\neq u} &= \frac{1}{\sigma_u^2 - \sigma_v^2} \frac{dJ_{ij}}{dt}\left(\sigma_v U_{iv} V_{ju} + \sigma_u U_{iu} V_{jv}\right) \\
  &= \frac{1}{\sigma_u^2 - \sigma_v^2} (\nabla X_t)_{ik} J_{kj}\left(\sigma_v U_{iv} V_{ju} + \sigma_u U_{iu} V_{jv}\right) \\
  &= \frac{1}{\sigma_u^2 - \sigma_v^2} (\nabla X_t)_{ik}\left(\sigma_u\sigma_v U_{iv} U_{ku} + \sigma_u\sigma_v U_{iu} U_{kv}\right) \\
  &= \frac{\sigma_u \sigma_v}{\sigma_u^2 - \sigma_v^2}\left( U_v^T(\nabla X_t)U_u + U_u^T(\nabla X_t)U_v \right) \\
  &= \frac{\sigma_u \sigma_v}{\sigma_u^2 - \sigma_v^2} U_v^T(\nabla X_t + \nabla X_t^T)U_u
\end{align}
$$