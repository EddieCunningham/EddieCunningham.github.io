Title: Flow matching
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
Tags: flows, matching, generative models
Slug: flow-matching
Summary: A tutorial on flow matching

Flow matching is probably the most important contribution to the field of normalizing flows in the last few years.  It allows us to train continuous normalizing flows in a simulation free way while also avoiding the pitfalls that comes with working with likelihoods.  In this tutorial, we'll go over what flow matching is and some of its practical properties.

# Overview
Say that we are trying to learn a parametric approximation of an unknown probability distribution that we can sample from.  The first [flow matching paper](https://arxiv.org/pdf/2210.02747.pdf) showed how we can **construct** a continuous normalizing flow that generates this target from any user specified prior.  Moreover, this flow that we can write down is something that we can use as a target to train a parametric model against.  This training algorithm does not suffer from the common pitfalls that maximum likelihood or score matching suffer from because it does not require us to compute likelihoods or score functions.  If you're not familiar with continuous normalizing flows, check out [my post]({static}/continuous_normalizing_flows.md) on them.

# Optimal continuous normalizing flow
Next, we'll show how to construct $u_t$ so that $\log p_1(x_1;\theta) = \log p_\text{data}(x_1)$.  Assume that $p_t(x_t)$ is a marginal probability distribution over $x_t$ and some random variable $y$ so that
$$
\begin{align}
  p_t(x_t) = \int p_y(y)p_{t|y}(x_t|y) dy
\end{align}
$$
We need to choose $p_y(y)$ and $p_{t|y}(x_t|y)$ so that the conditions at $t=0$ and $t=1$ are satisfied: $p_{t=0} = p_0$ and $p_{t=1} = p_\text{data}$.  Notice that $p_{t|y}(x_t|y)$ is time dependent, so it can also be written as the likelihood of $x_t$ under the flow of a conditional vector field, $u_t(x_t|y)$.  It turns out that $u_t(x)$ can be written as the expected value of conditional vector fields over the posterior distribution of $y$ given $x_t$:
$$
\begin{align}
u_t(x_t) = \mathbb{E}_{p_{t|y}(y|x_t)}[u_t(x_t|y)]
\end{align}
$$
Thus, we have constructed a continuous normalizing flow that satisfies our conditions.  To summarize, we can build a continuous normalizing flow that generates samples on $p_\text{data}$ by:
1. Choose $p_y(y)$ and $p_{t|y}(x_t|y)$ so that $p_{t=0} = p_0$ and $p_{t=1} = p_\text{data}$
2. Find a flow $u_t(x_t|y)$ for $p_{t|y}(x_t|y)$
3. Compute $u_t(x_t) = \mathbb{E}_{p_{t|y}(y|x_t)}[u_t(x_t|y)]$

The point of introducing $u_t(x_t|y)$ is not to estimate $u_t(x_t)$, but to estimate its **expectation** as follows:
$$
\begin{align}
\mathbb{E}_{p_t(x_t)}[u_t(x_t)] &= \int p_t(x_t)u_t(x_t) dx_t \\
&= \int p_t(x_t)\mathbb{E}_{p_{t|y}(y|x_t)}[u_t(x_t|y)] dx_t \\
&= \int \int p_t(x_t)p_{t|y}(y|x_t)u_t(x_t|y) dx_t dy \\
&= \int \int p_y(y)p_{t|y}(x_t|y)u_t(x_t|y) dx_t dy \\
&= \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[u_t(x_t|y)\right]
\end{align}
$$

Thus if we can sample from $p_y(y)$ and $p_t(x_t|y)$, then we can compute an unbiased estimate of $\mathbb{E}_{p_t(x_t)}[u_t(x_t)]$.  Before we see how this is useful for learning $u_t(x_t)$, we'll show an example of how to choose $p_y(y)$ and $p_{t|y}(x_t|y)$.

# Gaussian conditional flows
Let $p_y = p_\text{data}$ and $p_{t|y}(x_t|y) = \mathcal{N}(x_t; \mu_t(y), \Sigma_t(y))$ and let $(\mu_0(y), \Sigma_0(y)) = (0, I)$ and $(\mu_1(y), \Sigma_1(y)) = (y, 0)$ so that $p_0(x_0) = N(x_0|0,I)$ and $p_{1|y}(x_1|y) = \delta(x_1 - y)$.  We have that $p_1(x_1) = p_\text{data}(x_1)$ because
$$
\begin{align}
  p_1(x_1) &= \int p_y(y)p_{t=1|y}(x_1|y) dy \\
  &= \int p_\text{data}(y)\mathcal{N}(x_1; \mu_1(y), \Sigma_1(y)) dy \\
  &= \mathcal{N}(x_1; \mu_1, \Sigma_1) \\
  &= p_\text{data}(x_1)
\end{align}
$$

Notice that we can sample $x_t \sim p_{t|y}(x_t|y)$ using the model:
$$
\begin{align}
x_0 &\sim N(0,I) \\
x_t &= \mu_t(y) + \Sigma_t(y)^{1/2}x_0
\end{align}
$$
So we can differentiate $x_t$ to get the conditional vector field:
$$
\begin{align}
u_t(x_t|y) &= \frac{dx_t}{dt} \\
&= \frac{d}{dt}\left[\mu_t(y) + \Sigma_t(y)^{1/2}x_0\right] \\
&= \frac{d \mu_t(y)}{dt} + \frac{d \Sigma_t(y)^{1/2}}{dt}\underbrace{x_0}_{\Sigma_t^{\frac{-1}{2}}(x_t - \mu_t(y))} \\
&= \frac{d \mu_t(y)}{dt} + \frac{d \Sigma_t(y)^{1/2}}{dt}\Sigma_t^{\frac{-1}{2}}(x_t - \mu_t(y))
\end{align}
$$


# Flow matching
Now that we have a way to construct a target continuous normalizing flow whose generating vector field is $u_t(x_t)$, we can train a model to match $u_t(x_t)$.  Let $v_t(x_t;\theta)$ be a parametric neural network whose flow corresponds to the probability density function $q_t(x_t)$.  We can train $v_t(x_t;\theta)$ to match $u_t(x_t)$ by minimizing the following loss function:
$$
\begin{align}
\mathcal{L}_{\text{FM}}(\theta) &= \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\left\|u_t(x_t) - v_t(x_t;\theta)\right\|^2\right] dt \\
&= \small{\underbrace{\int_0^1 \mathbb{E}_{p_t(x_t)}[\|u_t(x_t)\|^2]dt}_{C_1} - 2\int_0^1 \mathbb{E}_{p_t(x_t)}[u_t(x_t)^Tv_t(x_t;\theta)]dt + \int_0^1 \mathbb{E}_{p_t(x_t)}[\|v_t(x_t;\theta)\|^2]dt} \\
&= C_1 - 2\int_0^1 \mathbb{E}_{p_t(x_t)}\left[u_t(x_t)\right]^Tv_t(x_t;\theta)dt + \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\|v_t(x_t;\theta)\|^2\right]dt \\
&= C_1 - 2\int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[u_t(x_t|y)\right]^Tv_t(x_t;\theta)dt + \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\|v_t(x_t;\theta)\|^2\right]dt \\
&= C_1 - C_2 + \underbrace{\int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|u_t(x_t|y) - v_t(x_t;\theta)\|^2\right]dt}_{\mathcal{L}_{\text{CFM}}(\theta)}
\end{align}
$$
where $C_2 = \int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|u_t(x_t|y)\|^2\right]dt$.  So we can minimize $\mathcal{L}_{\text{FM}}(\theta)$ by minimizing $\mathcal{L}_{\text{CFM}}(\theta)$ because $C_1$ and $C_2$ are constants.  $\mathcal{L}_{\text{CFM}}(\theta)$ is called the **conditional flow matching** loss.

We can also reparametrize $x_t$ with $f_t(x_t|y)$ to get the following loss function:
$$
\begin{align}
\mathcal{L}_{\text{CFM}}(\theta) &= \int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|u_t(x_t|y) - v_t(x_t;\theta)\|^2\right]dt \\
&= \int_0^1 \mathbb{E}_{p_y(y)p_0(x_0)}\left[\left\|u_t(f_t(x_0)|y) - v_t(x_t;\theta)\right\|^2\right]dt
\end{align}
$$

In this form, we see a new recipe for what we need to do to train $v_t(x_t;\theta)$:
1. Sample $y\sim p_y(y)$ and $x_0\sim p_0(x_0)$
2. Construct some path that starts at $x_0$ and ends at $y$
3. Sample any point on this path (to get $f_t(x_0)$) and get the tangent vector at that point (to get $u_t(f_t(x_0)|y)$)
4. Compute the loss between $u_t(f_t(x_0)|y)$ and $v_t(x_t;\theta)$

As we saw in the Gaussian flow matching section, we will often choose $p_y(y) = p_\text{data}(y)$ and $p_0(x_0) = \mathcal{N}(x_0; 0, I)$, so we are free to choose any path that starts at $x_0$ and ends at $y$.  The simplest choice is a straight line between $x_0$ and $y$, but we can also choose a more complicated path.

# Riemannian flow matching
Riemannian flow matching chooses the path between $x_0$ and $y$ using a gradient flow.