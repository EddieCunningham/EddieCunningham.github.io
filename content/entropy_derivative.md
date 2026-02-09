Title: Optimal manifold
Date: 2024-01-27
Category: Blog
Slug: entropy-derivative
hidden: true
Summary: Functional derivatives of entropy

In this post we'll take a look at how the choice of normalizing flow affects the entropy of the distribution.

Suppose $f: \mathcal{Z}=\mathbb{R}^n \to \mathcal{X}=\mathbb{R}^n$ is a diffeomophism, $p_z$ be a prior, $\pi_1:\mathbb{R}^n \to \mathbb{R}$ denote the projection map onto the first coordinate, and $\iota_1: \mathbb{R} \to \mathbb{R}^n$ be $\iota_1(x) = (x,0,\dots,0)$.  We are interested in the entropy of the distribution of points projected onto the first coordinate of the base space.  Projection, in this case, is defined using $f$:
$$
\begin{align}
  \mathrm{proj}(x) := f\circ \iota_1 \circ \pi_1 \circ f^{-1}(x)
\end{align}
$$
We'll denote the curve that $\mathrm{proj}(x)$ lives on as $S=\mathrm{proj}(\mathbb{R}^n)$.

The entropy of the distribution of points projected onto the first coordinate is:
$$
\begin{align}
  \int_{S} p_1(x) \log p_1(x) dx &= \int_{\mathbb{R}} p_1(z_1)\left[\log p_1(z_1) - \frac{1}{2}\log \det{D_1F^T D_1F}\right]dz_1 \\
\end{align}
$$
We'll look at the functional derivative of this entropy with respect to $f$.  The derivative that we'll compute is
$$
\frac{d}{d\epsilon}\mathcal{L}[f+\epsilon \eta]_{\epsilon=0} = \lim_{\epsilon \to 0} \frac{\mathcal{L}[f+\epsilon \eta] - \mathcal{L}[f]}{\epsilon} = \eta
$$
where $\mathcal{L}$ is the entropy functional and $\eta$ is a vector field on $\mathbb{R}^n$.

In order to do this, we'll need a few identities.

## Derivative of log determinant
Let $A$ be a matrix and $A(\epsilon) = A + \epsilon B$ be a matrix that depends on $\epsilon$.  The derivative of the log determinant of $A(\epsilon)^TA(\epsilon)$ with respect to $\epsilon$ is:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}\frac{1}{2}\log \det A(\epsilon)^TA(\epsilon) &= \mathrm{tr}\left(A^{+}
\frac{dA(\epsilon)}{d\epsilon}|_{\epsilon=0}\right) \\
  &= \mathrm{tr}\left(A^{+}B\right)
\end{align}
$$
In the full context, we have $A = D_1f$ and $B = D_1\eta$, so the derivative is:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0}\frac{1}{2}\log \det D_1f(\epsilon)^TD_1f(\epsilon) &= \mathrm{tr}\left((D_1f)^{+}D_1\eta\right)
\end{align}
$$

# Likelihood constraint
We can also see which possible $\eta$ we can pick so that the likelihood under the model is still the same.  Let $p^*$ be the distribution of the data and $p_f$ be the distribution of the model.  Then we want the derivative of the KL divergence to be 0:
$$
\begin{align}
  \frac{d}{d\epsilon}|_{\epsilon=0} \mathrm{KL}(p_{f+\epsilon \eta}\|p^*) &= \frac{d}{d\epsilon}|_{\epsilon=0} \int_{\mathbb{R}^n} p_{f+\epsilon \eta}(x) \log \frac{p_{f+\epsilon \eta}(x)}{p^*(x)} dx \\
  &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_{\mathbb{R}^n} p(z)\left[- \log \det D(f + \epsilon \eta) - \log p^*((f+\epsilon \eta)(z)) \right] dz \\
  &= -\int_{\mathbb{R}^n} p(z)\left[\mathrm{tr}\left((Df)^{-1}D\eta\right) +
  \langle \nabla \log p^*(f(z)), \eta(z)\rangle\right]dz \\
  &= -\int_{\mathbb{R}^n} p(z)\left[\mathrm{tr}\left(GN\right) + \langle \nabla \log p^*(f(z)), \eta(z)\rangle\right]dz \\
  &= -\int_{\mathbb{R}^n} p(z)\left[ \mathrm{tr}\left(\begin{bmatrix} - & G_1  & - \\ - & G_2 & - \end{bmatrix}\begin{bmatrix} | & | \\ N_1 & N_2 \\  | & | \end{bmatrix}\right) + \langle \nabla \log p^*(f(z)), \eta(z)\rangle \right] dz \\
  &= -\int_{\mathbb{R}^n} p(z)\left[ \left(\mathrm{tr}\left(G_1N_1\right) + \mathrm{tr}\left(G_2N_2\right)\right) + \langle \nabla \log p^*(f(z)), \eta(z)\rangle \right] dz \\
  &= -\int_{\mathbb{R}^n} p(z)\left[ \left(\mathrm{tr}\left(J_1^+\Phi J_2^\perp N_1\right) + \mathrm{tr}\left(J_2^+\Phi^T J_1^\perp N_2\right)\right) + \langle \nabla \log p^*(f(z)), \eta(z)\rangle \right] dz
\end{align}
$$
where in the last line, we used the identity:
$$
\begin{align}
G_1 &= J_1^+\Phi J_2^\perp \\
G_2 &= J_2^+\Phi^T J_1^\perp \\
\text{where }\Phi &= \left(I - J_2^\parallel J_1^\parallel\right)^{-1}
\end{align}
$$

We can also rewrite the last line by using the expression for the log determinant:
$$
\begin{align}
  &= \frac{d}{d\epsilon}|_{\epsilon=0}\int_{\mathbb{R}^n} p(z)\left(\frac{1}{2}\log \det J_1(\epsilon)^TJ_1(\epsilon) + \frac{1}{2}\log \det J_2(\epsilon)^TJ_2(\epsilon)\right) dz \\
  &\text{where }J_1(\epsilon) = J_1 + \epsilon \underbrace{J_1^\parallel\Phi J_2^\perp}_{\Phi^TJ_1^\parallel J_2^\perp} N_1 \\
  &\quad\text{and }J_2(\epsilon) = J_2 + \epsilon \underbrace{J_2^\parallel\Phi^T J_1^\perp}_{\Phi J_2^\parallel J_1^\perp} N_2 \\
\end{align}
$$