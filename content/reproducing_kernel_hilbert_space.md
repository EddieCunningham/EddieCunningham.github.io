Title: Reproducing Kernel Hilbert Space
Date: 2023-07-16
Modified: 2023-07-16
Category: Blog
<!-- status: hidden -->
Tags: rkhs, mercer representation, kernels
Slug: reproducing-kernel-hilbert-space
Summary: A quick practical introduction into RKHS

We'll go over the basics of RKHS and how to use them in practice using the [Mercer representation](https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space#Integral_operators_and_Mercer's_theorem).

# Square integrable functions
The kinds of functions that we will care about are square integrable functions.  Let $X$ be a compact space.  A function $f$ is square integrable (meaning $f \in L_2(X)$) if it has a bounded norm with repspect to the inner product
$$
\begin{align}
  \langle f, g \rangle_{L_2} = \int_X f(x)g(x)dx
\end{align}
$$
In other words, the space of integrable functions is defined as
$$
\begin{align}
  L_2(X) = \left\{f \mid \langle f, f \rangle_{L_2} < \infty \right\}
\end{align}
$$
If we have a basis of functions $\{e_i\}_{i=1}^{\infty}$ for $L_2(X)$, then we can write any function $f\in L_2(X)$ in terms of the basis functions as
$$
\begin{align}
   f(x) &= \sum_{i=1}^{\infty} \langle f, e_i \rangle_{L_2} e_i(x) \\
   &= \sum_{i=1}^{\infty} \underbrace{\int_X f(y)e_i(y)dy}_{f_i} e_i(x) \\
   &= \sum_{i=1}^{\infty} f_i e_i(x)
\end{align}
$$
where $f_i$ is defined as the component of $f$ in the $e_i$ basis.  By our assumption that $f\in L_2(X)$, we have that $f_i < \infty$ for all $i$.

# Kernels
A kernel function $K: X\times X \to \mathbb{R}$ is a symmetric, positive definite function.  We can think of a kernel function as a way to "smooth" out functions by integrating them with respect to the kernel function.  We will define this "smoothing operation" as $T_K: L_2(X) \to L_2(X)$:
$$
\begin{align}
  T_Kf(x) &= \int_X K(x,y)f(y)dy \\
  &= \langle K_x, f \rangle_{L_2}, \text{ where }K_x(y) = K(x,y)
\end{align}
$$
Notice that $T_K$ is a self-adjoint linear operator, so by the Mercer theorem it has an eigendecomposition.  This means that there exists scalars $\{\lambda_i\}_{i=1}^{\infty}$ and orthonormal functions $\{e_i\}_{i=1}^{\infty}$ (where $\int_{\infty}^{\infty} e_i(x)e_j(x) dx = \delta_{ij}$) so that
$$
\begin{align}
  T_K e_i(x) = \lambda_i e_i(x), \quad \forall i
\end{align}
$$
This implies that we can write $K$ in terms of its eigendecomposition as
$$
\begin{align}
  K(x,y) = \sum_{i=1}^{\infty} \lambda_i e_i(x)e_i(y)
\end{align}
$$
This is similar to how We can verify this easily because
$$
\begin{align}
  T_K e_i(x) &= \int_X K(x,y)e_i(y)dy \\
  &= \int_X \sum_{j=1}^{\infty} \lambda_j e_j(x)e_j(y)e_i(y)dy \\
  &= \sum_{j=1}^{\infty} \lambda_j e_j(x) \int_X e_j(y)e_i(y)dy \\
  &= \sum_{j=1}^{\infty} \lambda_j e_j(x) \delta_{ij} \\
  &= \lambda_i e_i(x)
\end{align}
$$


Using these definitions, we can relate $K$ to its eigenfunctions in a more linear algabraic way as
$$
\begin{align}
  \langle K_x, e_i \rangle_{L_2} = \lambda_i e_i(x)
\end{align}
$$
This expression highlights the interpretation that a Hilbert space is an infinite dimensional vector space because $x$ is analagous to a row index.  For example, if we have a matrix symmetric PSD $\Sigma \in \mathbb{R}^{n\times n}$ with eigenvectors $\{v_i \in \mathbb{R}^n\}_{i=1}^{n}$ and eigenvalues $\{\lambda_i \in \mathbb{R}\}_{i=1}^{n}$, we can write the j'th index of the scaled i'th eigenvector is $\langle \Sigma_j, v_i \rangle_2 = \lambda_i (v_i)_j$.

# Reproducing Kernel Hilbert Space
Now that we've seen how to relate the kernel function with its eigenfunctions, we can define the RKHS.  An RKHS associated with a kernel $K$ is a Hilbert space with an inner product that resembles the inner product weighted by a symmetric matrix $\Sigma$ on $R^n$, $\langle x, y \rangle_\Sigma = x^T\Sigma^{-1} y$.

Recall that $K(x,y) = \sum_{i=1}^{\infty} \lambda_i e_i(x)e_i(y)$.  We define the inner product of an RKHS as follows:
$$
\begin{align}
  \langle f, g \rangle_{\mathcal{H}_K} = \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2}\langle g, e_i \rangle_{L_2}
\end{align}
$$
This is similar to the inner product weighted by $\Sigma^{-1}$ on $\mathbb{R}^n$ because if the eigendecomposition of $\Sigma^{-1}$ is $\Sigma^{-1}=\frac{1}{\lambda_i}v_i v_i^T$, then $\langle x, y \rangle_{\Sigma^{-1}} = x^T\Sigma^{-1} y = \sum_{i=1}^n \frac{1}{\lambda_i} (x^Tv_i)(y^Tv_i) = \sum_{i=1}^n \frac{1}{\lambda_i} \langle x, v_i \rangle_2 \langle y, v_i \rangle_2$.  Finally, an RKHS is defined as the collection of functions with finite norm under this inner product:
$$
\begin{align}
  \mathcal{H}_K = \left\{f\in L_2(X) \mid \langle f, f \rangle_{\mathcal{H}_K} < \infty \right\}
\end{align}
$$

## Reproducing property
The "reproducing" part of RKHS comes from the following property:
$$
\begin{align}
  \langle f, K_x \rangle_{\mathcal{H}_K} &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2}\langle K_x, e_i \rangle_{L_2} \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\underbrace{\langle f, e_i \rangle_{L_2}}_{f_i} \int_X K(x,y)e_i(y)dy \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}f_i \int_X \sum_{j=1}^{\infty} \lambda_j e_j(x)e_j(y)e_i(y)dy \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}f_i \sum_{j=1}^{\infty} \lambda_j e_j(x) \delta_{ij} \\
  &= \sum_{i=1}^{\infty} f_i e_i(x) \\
  &= f(x)
\end{align}
$$
This is called the reproducing property because it means that the evaluation of a function $f$ at $x$ can be "reproduced" by the inner product of $f$ with $K_x$. We get another nice property if we take the inner product with the partially filled kernel functions:
$$
\begin{align}
  \langle K_x, K_y \rangle_{\mathcal{H}_K} &= K_x(y) \\
  &= K(x, y)
\end{align}
$$

Finally, we can also push linear operators on $x$ through the inner product.  For example, let $\text{grad }$ be the gradient function on $x$.  Then
$$
\begin{align}
  \langle f, \text{grad } K_x \rangle_{\mathcal{H}_K} &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2}\langle \text{grad } K_x, e_i \rangle_{L_2} \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2} \int_X \text{grad } K(x,y)e_i(y)dy \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2} \sum_{j=1}^{\infty} \lambda_j \text{grad } e_j(x) \delta_{ij} \\
  &= \sum_{i=1}^{\infty} \frac{1}{\lambda_i}\langle f, e_i \rangle_{L_2} \lambda_i \text{grad } e_i(x) \\
  &= \text{grad } \sum_{i=1}^{\infty} \langle f, e_i \rangle_{L_2} e_i(x) \\
  &= \text{grad } f(x)
\end{align}
$$
