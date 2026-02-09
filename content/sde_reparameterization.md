Title: Reparameterization of SDEs
Date: 2025-06-30
Modified: 2025-06-30
Category: Blog
status: hidden
Tags: SDE
Slug: SDE-reparameterization
Summary: Reparameterization of SDEs

# Reparameterization of SDEs
Flow-based generative models are the gold standard for generative modeling.  The key to their advance is their ability to represent any given marginal distribution.  For example, if $p_1(x_1)$ is the distribution of data and $p_0(x_0)$ is the distribution of a prior distribution, like a multivariate Gaussian, we are able to construct an SDE whose marginal distribution at time $t=0$ is $p_0(x_0)$ and at time $t=1$ is $p_1(x_1)$.  However, this SDE is not unique - in fact, there are an infinite number of SDEs that can achieve this.  In this post, we will explore the space of SDEs that transport samples from $p_0(x_0)$ to $p_1(x_1)$ and how to reparameterize them.

## Reparameterization of additive SDEs by their diffusion coefficient
Consider the additive SDE:
$$
\begin{align}
  dx_t = b_t(x_t) dt + L_t dW_t
\end{align}
$$
where $b_t(x_t)$ is the drift and $L_t$ is the diffusion coefficient.  This SDE is called additive because $L_t$ does not depend on $x_t$.  This class of SDEs is the most widely used class of SDEs in practice because it is highly tractable and admits a closed-form solution.  See [this post](???) for more details.  Let $p_t(x_t)$ be the marginal distribution of the SDE at time $t$, which is called its "probability path".  In the generative modeling problem, the probability path is the only quantity of interest as we are only interested in the marginal distribution at the end time because this corresponds to the distribution of data.  However, in other contexts, it is useful to know what the joint distribution of the SDE at different times.  For example, the joint distribution over the prior and data, $p_{0,1}(x_0, x_1)$, is a useful quantity in the context of paired generative modeling where the prior and data are presented in a paired manner.  In general, the joint distribution defines the "coupling" between the prior and data.

In the context of finetuning, it is necessary to ensure that the prior and data variables are not coupled at all in order to avoid the initial value function bias problem.  This presents a challenge for pretrained SDEs because the prior and data variables are coupled by the diffusion coefficient.  To counteract this, we can reparameterize the SDE by a new diffusion coefficient $L_t^*$ that changes the coupling of the prior and data variables without changing the probability path.  Suppose we have a new SDE of the form:
$$
\begin{align}
  dx_t = b_t^*(x_t) dt + L_t^* dW_t
\end{align}
$$
where $L_t^*$ is a new diffusion coefficient.  Our goal is to find a new drift function, $b_t^*(x_t)$, that ensures that this new SDE has the same probability path as the original SDE.  We can find one such $b_t^*(x_t)$ by simply rearranging terms in the Fokker-Planck equation for the original SDE.  For notational convenience, we will not write the dependence of $p_t$ and $b_t$ on $x_t$.  Recall that the Fokker-Planck equation is given by the following equation:
$$
\begin{align}
  \frac{\partial p_t}{\partial t} = -\mathrm{Div}(p_t b_t) + \mathrm{Div}(\frac{1}{2}L_tL_t^T \nabla p_t)
\end{align}
$$
To find the new drift function, we just need to introduce the new diffusion coefficient and then rearrange terms to get:
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= -\mathrm{Div}(p_t b_t) + \mathrm{Div}(\frac{1}{2}L_tL_t^T \nabla p_t) \\
  &= -\mathrm{Div}(p_t b_t) + \mathrm{Div}(\frac{1}{2}\left(L_tL_t^T - {L_t^*}{L_t^*}^T\right) \nabla p_t) + \mathrm{Div}(\frac{1}{2}{L_t^*}{L_t^*}^T \nabla p_t) \\
  &= -\mathrm{Div}(p_t \left(b_t + \frac{1}{2}\left({L_t^*}{L_t^*}^T - L_tL_t^T\right) \nabla \log p_t\right)) + \mathrm{Div}(\frac{1}{2}{L_t^*}{L_t^*}^T \nabla p_t) \\
\end{align}
$$
We can then see that the new drift function is given by:
$$
\begin{align}
  b_t^* = b_t + \frac{1}{2}\left({L_t^*}{L_t^*}^T - L_tL_t^T\right) \nabla \log p_t
\end{align}
$$

This leaves us with the following SDE:
$$
\begin{align}
  dx_t = \left(b_t(x_t) + \frac{1}{2}\left({L_t^*}{L_t^*}^T - L_tL_t^T\right) \nabla \log p_t(x_t)\right) dt + L_t^* dW_t
\end{align}
$$
This SDE has the same probability path as the original SDE, but has a different coupling between the prior and data variables.

## Reparameterization of markovian projection SDEs by their base SDE
Consider following linear SDE:
$$
\begin{align}
  dx_t = (F_t x_t + u_t) dt + L_t dW_t
\end{align}
$$
where $(F_t, u_t, L_t)$ are variables that do not depend on $x_t$.  Next, let $p(y)$ be the distribution of data and suppose that we construct potential functions at the times $t_1, \ldots, t_n$ using the parameters $\{\theta_{t_k}(y)\}_{k=1}^n$, where each $\theta_{t_k}(y) = (\mu_{t_k}(y), \Sigma_{t_k})$ are the mean and covariance of a Gaussian distribution.  Using the linear SDE and the potential functions, we can construct a joint distribution over $x_{t_{1:n}}$, given $y$, as
$$
\begin{align}
  p(x_{t_{1:n}}|y) \propto \prod_{k=1}^{n-1}p(x_{t_{k+1}}|x_{t_k})\prod_{k=1}^n \phi(x_{t_k}|\theta_{t_k}(y))
\end{align}
$$
where $p(x_{t_{k+1}}|x_{t_k})$ is the transition probability of the linear SDE and $\phi(x_{t_k}|\theta_{t_k}(y))$ is the (unnormalized) Gaussian potential function.  The Markovian projection SDE is the SDE whose marginal distribution is equal to that of the joint distribution above.  This is given by
$$
\begin{align}
  dx_t = (F_t x_t + u_t + L_tL_t^T \nabla \log \phi(x_t|\beta_t^*(x_t))) dt + L_t dW_t
\end{align}
$$
where $\beta_t^*(x_t) = \mathbb{E}_{p(y|x_t)}[\beta_{t}(y)]$ is the Bayes estimate of the backward message associated with the graphical model above.

Now suppose that we have a different linear SDE:
$$
\begin{align}
  d\bar{x}_t = (\bar{F}_t \bar{x}_t + \bar{u}_t) dt + \bar{L}_t dW_t
\end{align}
$$
Given $(F_t, u_t, L_t)$, $\beta_t^*(x_t)$ and $(\bar{F}_t, \bar{u}_t, \bar{L}_t)$, we will show that how to compute $\bar{\beta}_t^*(\bar{x}_t)$.  To do this, we make use of useful properties of Bayes estimators.

## Bayes estimators
Let $\theta(y)$ be a random variable where $y\sim p(y)$ is the data, and let $x$ be another random variable where $p(x,y)$ is the joint distribution of $x$ and $y$.  The Bayes estimator of $\theta(y)$, given $x$, is given by the posterior estimate of $\theta(y)$ given $x$:
$$
\begin{align}
  \theta^*(x) = \mathbb{E}_{p(y|x)}[\theta(y)]
\end{align}
$$
It is well known that the Bayes estimator has a variational form that is given by the minimum of a mean squared error loss:
$$
\begin{align}
  \theta^*(x) = \argmin_{f(x)} \mathbb{E}_{p(x,y)}[\|\theta(y) - f(x)\|^2]
\end{align}
$$
where $f(x)$ is a function of $x$.  From this definition, we can see that the Bayes estimator is invariant to reparameterization of $x$.  Suppose that $\bar{x} = T(x)$ is a transformation of $x$ and let $\bar{p}(\bar{x},y)$ be the joint distribution of $\bar{x}$ and $y$.  Then we can also compute the Bayes estimator of $\theta(y)$, given $\bar{x}$, as
$$
\begin{align}
  \bar{\theta}^*(\bar{x}) &= \argmin_{f(\bar{x})} \mathbb{E}_{\bar{p}(\bar{x},y)}[\|\theta(y) - f(\bar{x})\|^2] \\
  &= \argmin_{f(T(x))} \mathbb{E}_{\bar{p}(T(x),y)}[\|\theta(y) - f(T(x))\|^2] \\
  &= \argmin_{f\circ T(x)} \mathbb{E}_{p(x,y)}[\|\theta(y) - f\circ T(x)\|^2] \\
  &= \theta^*(x)
\end{align}
$$
What we have shown is that $\bar{\theta}^*\circ T = \theta^*$, which shows that the Bayes estimator is invariant to reparameterization.


