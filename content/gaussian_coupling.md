Title: Gaussian coupling of distributions
Date: 2024-02-20
Category: Blog
Slug: gaussian-coupling
hidden: true
Summary: Gaussian coupling of distributions

Suppose that we want to find a transport map between two probability distributions, $p_0$ and $p_1$.  One way to do this is to construct the map as a flow of a time-dependent vector field such that the marginal density at time $t$ is given by:
$$
\begin{align}
  p_t(x_t) &= \int p_1(x_1)N(x_t|\mu_t(x_1),\Sigma_t(x_1)) dx_1 \\
  \text{ such that } p_{t=0} &= p_0 \text{ and } p_{t=1} = p_1
\end{align}
$$
$\mu_t$ and $\Sigma_t$ are chosen so that the marginal density at $t=0$ is $p_0$ and the marginal density at $t=1$ is $p_1$.



Suppose $\mathcal{S} \subset \mathbb{R}^N$ is a $k$ dimensional submanifold of Euclidean space and suppose $p_\mathcal{S}$ is a probability density function on $\mathcal{S}$.  Next, suppose that we observe the convolved probability distribution:
$$
\begin{align}
  p_\sigma(x) &= \int_{\mathcal{S}} p_\mathcal{S}(s) N(x|s,\sigma^2I) ds
\end{align}
$$

## Expected value under the posterior
Given $p_\sigma$, the expected value of the posterior is given by
$$
\begin{align}
  \mathbb{E}[s|x] &= \int_{\mathbb{R}^n} p_\sigma(s|x) s ds
\end{align}
$$
Note $\mathbb{E}[s|x]$ does not necessarily lie on $\mathcal{S}$.

We can use Tweedies formula to evaluate this.  It is easy to derive using the following identity:
$$
\begin{align}
  \nabla \log p(x) &= \int p(s|x) \nabla \log p(x|s) ds \\
  &= \int p(s|x) \frac{1}{\sigma^2}(s - x) ds \\
  &= \frac{1}{\sigma^2} \int p(s|x) s ds - x
\end{align}
$$
$$
\begin{align}
  \implies \mathbb{E}[s|x] &= \sigma^2 \nabla \log p(x) + x
\end{align}
$$

## Expected covariance
We can also compute the covariance matrix under the posterior distribution.  We'll derive this rearranging the expression for the projection to $x = \mathbb{E}[s|x] - \sigma^2 \nabla \log p(x)$ and then taking the derivative of both sides.  But before this, we need the following identity:
$$
\begin{align}
  \nabla \log p(s|x) &= \frac{1}{\sigma^2}(s - x) - \nabla \log p(x)
\end{align}
$$
Proof:
$$
\begin{align}
  \nabla \log p(s|x) &= \nabla \log p(x,s) - \nabla \log p(x) \\
  &= \nabla \log p(x|s) - \nabla \log p(x) \\
  &= \frac{1}{\sigma^2}(s - x) - \nabla \log p(x)
\end{align}
$$
Now we're ready to derive the covariance of the projection:
$$
\begin{align}
  \text{Var}[s|x] &= \sigma^2 I + \sigma^4 \nabla^2 \log p(x) \\
  &= \sigma^2 \nabla \mathbb{E}[s|x]
\end{align}
$$
Proof:
$$
\begin{align}
  I &= \nabla (\mathbb{E}[s|x] - \sigma^2 \nabla \log p(x)) \\
  &= \nabla \int p(s|x) s ds - \sigma^2 \nabla^2 \log p(x) \\
  &= \int p(s|x) s\nabla \log p(s|x)^T ds - \sigma^2 \nabla^2 \log p(x) \\
  &= \int p(s|x) s\left[ \frac{1}{\sigma^2}(s - x) - \nabla \log p(x)\right]^T ds - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\left(\int p(s|x)ss^Tds - \underbrace{\int p(s|x)s ds}_{x + \sigma^2 \nabla \log p(x)} x^T \right) - \underbrace{\int p(s|x)sds}_{x + \sigma^2 \nabla \log p(x)}\nabla \log p(x)^T  - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\mathbb{E}[ss^T|x] - \frac{1}{\sigma^2}xx^T - \nabla \log p(x)x^T - x\nabla \log p(x)^T - \sigma^2 \nabla \log p(x) \nabla \log p(x)^T - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\mathbb{E}[ss^T|x] - \frac{1}{\sigma^2}\left(xx^T + \sigma^2 \nabla \log p(x)x^T + \sigma^2 x \nabla \log p(x)^T + \sigma^4 \nabla \log p(x) \nabla \log p(x)^T\right) - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\mathbb{E}[ss^T|x] - \frac{1}{\sigma^2}\underbrace{\left(x + \sigma^2 \nabla \log p(x) \right)}_{\mathbb{E}[s
  |x]}\left(x + \sigma^2 \nabla \log p(x) \right)^T - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\mathbb{E}[ss^T|x] - \frac{1}{\sigma^2}\mathbb{E}[s
  |x]\mathbb{E}[s
  |x]^T - \sigma^2 \nabla^2 \log p(x) \\
  &= \frac{1}{\sigma^2}\text{Var}[s|x] - \sigma^2 \nabla^2 \log p(x)
\end{align}
$$

## Conditional distributions and flows
We can use the above to learn something about the joint distribution of


Suppose we approximate $p_\sigma(x)$ with $q(x)$.  We can construct a flow between $p_\sigma(x)$ and $q(x)$ using conditional probability paths in order to be able to evaluate the expected value of a variable in $p_\sigma$ conditioned on a value from $q(x)$.

Let $p_t(x_t)$ be a time dependent probability distribution with $t=0,\dots,1$.

## Construction of optimal coordinates
Next, we can start building a coordinate system that admits $\mathbb{E}[s|x]$ as a coordinate.  First, lets look at the kernel of $\pi_\sigma$ in order to determine the normal space on $\mathcal{S}$.  Let $V = V^i \frac{\partial}{\partial x^i}$ be a vector field on $\mathcal{M}$.  The normal space of $\mathcal{S}$
$$
\begin{align}
  \frac{d\pi(x)^j}{dx^i} &= \frac{d}{dx^i}\left(\sigma^2 \nabla \log p(x)^j + x^j\right) \\
  &= \sigma^2 \frac{d}{dx^i}\nabla \log p(x)^j + \delta_{ij} \\
  &= \sigma^2 \nabla^2 \log p(x)^{ij} + \delta_{ij}
\end{align}
$$

## Evaluation
We can evaluate the quality of the projection by computing the expected value of the squared distance between the optimal projection and the projection under $f$.  This is given by
$$
\begin{align}
  \mathbb{E}[\|\mathbb{E}[s|x] - \pi_f(x)\|^2] &= \int_{\mathbb{R}^n} p_\sigma(x) \|\mathbb{E}[s|x] - \pi_f(x)\|^2 dx \\
  &= \int_{\mathbb{R}^n} p_\sigma(x) \|\sigma^2 \nabla \log p(x) + x - f(f^{-1}(x)_1, 0)\|^2 dx \\
  &= \int_{[-\frac{1}{2}, \frac{1}{2}]}\int_{[-\frac{1}{2}, \frac{1}{2}]} \|\sigma^2 \nabla_x \log p(f(z_1,z_2)) + f(z_1,z_2) - f(z_1, 0)\|^2 dz_1 dz_2
\end{align}
$$
where we have used the change of variables $x = f(z_1,z_2)$.  Next, lets use the triangle inequality to bound the above integral:

$$
\begin{align}
  \leq \sigma \int_{[-\frac{1}{2}, \frac{1}{2}]}\int_{[-\frac{1}{2}, \frac{1}{2}]} \|\nabla_x \log p(f(z_1,z_2))\|^2 dz_1 dz_2 + \int_{[-\frac{1}{2}, \frac{1}{2}]}\int_{[-\frac{1}{2}, \frac{1}{2}]} \|f(z_1,z_2) - f(z_1, 0)\|^2 dz_1 dz_2
\end{align}
$$
The first term is $0$ as $\sigma \to 0$, so we'll focus on the second term.
$$
\begin{align}
  \int_{[-\frac{1}{2}, \frac{1}{2}]}\int_{[-\frac{1}{2}, \frac{1}{2}]} \|f(z_1,z_2) - f(z_1, 0)\|^2 dz_1 dz_2 &\leq \int_{[-\frac{1}{2}, \frac{1}{2}]}\int_{[-\frac{1}{2}, \frac{1}{2}]} \int_0^{z_2} \|\frac{df(z_1,z_2')}{dz_2'}\| dz_1 dz_2
\end{align}
$$
If we can show that $\|\frac{df(z_1,z_2')}{dz_2'}\| \to 0$ as $\sigma \to 0$, then we can show that the optimal projection is recovered by the orthogonal coordinate transform.