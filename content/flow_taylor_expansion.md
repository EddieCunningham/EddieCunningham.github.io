Title: Flows Taylor Expansion
Date: 2025-10-01
Category: Blog
Slug: flow_taylor_expansion
hidden: true
Summary: Flows Taylor Expansion

# Flows Taylor Expansion

We will first write the Taylor expansion of the $i$'th element of $x'=f(z+\sigma \epsilon)$.
$$
\begin{align}
    f(z+\sigma\epsilon)_i = x_i + \sigma \sum_u \nabla f_{iu}\epsilon_u + \frac{\sigma^2}{2}\sum_u \sum_v \nabla^2 f_{iuv}\epsilon_u\epsilon_v + \frac{\sigma^3}{6}\sum_u \sum_v \sum_w \nabla^3 f_{iuvw}\epsilon_u\epsilon_v\epsilon_w + O(\sigma^4)
\end{align}
$$
The $(i,j)$ element of the covariance matrix of $x'$ is equal to $\mathbb{E}[x'_ix'_j] - \mathbb{E}[x']_i\mathbb{E}[x']_j$.  The next step is to compute each term.  In each equation we absorb the terms of order $\sigma^4$ together because they will be negligible in the limit of $\sigma \to 0$.  Furthermore expectations with an odd number of $\epsilon$ terms will be 0 because Gaussian random variables have odd moments equal to 0.
$$
\begin{align}
    \mathbb{E}[x']_i &= x_i + \frac{\sigma^2}{2}\mathrm{Tr}(\nabla^2 f_i) + O(\sigma^4) \\
    \mathbb{E}[x']_i\mathbb{E}[x']_j &= x_ix_j + \frac{x_i\sigma^2}{2}\mathrm{Tr}(\nabla^2 f_j) + \frac{x_j\sigma^2}{2}\mathrm{Tr}(\nabla^2 f_i) + O(\sigma^4) \\
    \mathbb{E}[x'_ix'_j] &= x_ix_j + \sigma^2\nabla f_i^T \nabla f_j + \frac{x_i\sigma^2}{2}\mathrm{Tr}(\nabla^2 f_j) + \frac{x_j\sigma^2}{2}\mathrm{Tr}(\nabla^2 f_i) + O(\sigma^4)
\end{align}
$$
Plugging the terms into the equation for covariance yields
$$
\begin{align}
    \text{Cov}[x']_{ij} &= \sigma^2\nabla f_i^T \nabla f_j + O(\sigma^4) \\
    \text{Cov}[x] &= \sigma^2JJ^T + O(\sigma^4)
\end{align}
$$

As $\sigma\to 0$ we can simplify to
$$
\begin{align}
    \text{Cov}[x] \overset{\sigma\to 0}{=} \sigma^2JJ^T
\end{align}
$$
$\sigma^2$ is a scalar value so $\sigma^2JJ^T$ has the same eigenvectors as $JJ^T$, so the principal components of the flow at $x$ are equal to the eigenvectors of $JJ^T$.

