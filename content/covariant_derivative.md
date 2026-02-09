Title: Covariant Derivative
Date: 2025-03-02
Category: Blog
Slug: covariant_derivative
hidden: true
Summary: Covariant Derivative


In this doc we will give a normalizing flow based interpretation of the covariant derivative.

Let $\mathcal{X}$ be a Riemannian manifold with metric $g$ and suppose $F_\theta$ is a bijection between $\mathcal{Z}$ and $\mathcal{X}$ that depends on the scalar parameter $\theta$.  The


Suppose $\mathcal{Z} = \mathbb{R}^n$ is a Euclidean space and $F_{\theta}: \mathcal{Z} \to \mathcal{X}$ is a chart for a neighborhood of a point $x \in \mathcal{X}$.  Then the pullback metric on $\mathcal{Z}$ is given by $F_{\theta}^{*}g$.  Suppose we fix some $z \in \mathcal{Z}$ and consider the curve $\gamma^{(z)}(\theta): \mathbb{R} \to \mathcal{Z}$ given by $\gamma^{(z)}(\theta) = F_{\theta}(z)$.

$$
\begin{align}
\nabla_{\frac{d}{d\theta}} W_\theta &= (F_\theta^{-1})_* \frac{d}{d\theta} \left((F_\theta)_* W_\theta\right), \quad \text{where }\;\ V_\theta = \frac{dF_\theta}{d\theta} \\
&= \left(\frac{\partial x_\theta}{\partial z}^{-1}(z)\right)^i_j \frac{d}{d\theta} \left(\frac{\partial x^j_\theta}{\partial z^k}(z) (W_\theta(z))^k_l \right) \\
&= (\frac{\partial W_\theta}{\partial \theta})^i_j + \left(\frac{\partial x_\theta}{\partial z}^{-1}(z)\right)^i_j \frac{\partial^2 x^j_\theta}{\partial \theta \partial z^k}(z) (W_\theta(z))^k_l
\end{align}
$$

