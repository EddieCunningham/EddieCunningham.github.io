Title: Flow matching
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
Tags: flows, matching, generative models
Slug: flow-matching
Summary: A tutorial on flow matching

Flow matching is probably the most important contribution to the field of normalizing flows in the last few years.  It allows us to train continuous normalizing flows in a simulation free way while also avoiding the pitfalls that comes with working with likelihoods.  In this tutorial, we'll go over what flow matching is and some of its practical properties.

# Overview
Say that we are trying to learn a parametric approximation of an unknown probability distribution that we can sample from.  The first [flow matching paper](https://arxiv.org/pdf/2210.02747.pdf) showed how we can **construct** a continuous normalizing flow that generates this target from any user specified prior.  Moreover, this flow that we can write down is something that we can use as a target to train a parametric model against.  This training algorithm does not suffer from the common pitfalls that maximum likelihood or score matching suffer from because it does not require us to compute likelihoods or score functions.  If you're not familiar with continuous normalizing flows, check out [my post]({filename}continuous_normalizing_flows.md) on them.

# CNF construction
Here, we'll show how we can **construct** the continuous normalizing flow that generates a target distribution from any user specified prior.  Let $p_1:=p_\text{data}$ be the target distribution that we want to learn and let $p_0$ be a user specified prior.  We'll start by assuming that there is a probability path between $p_0$ and $p_1$, denoted by $p_t$, that is generated by the flow of a time dependent vector field $V_t$.  Our goal will be to show what the equation of $V_t$ is.

To do this, we will assume that $p_t$ is actually a marginal probability distribution over $x_t$ and some random variable $y$:
$$
\begin{align}
  p_t(x_t) = \int p_y(y)p_{t|y}(x_t|y) dy
\end{align}
$$
where $p_y(y)$ and $p_{t|y}(x_t|y)$ are chosen so that $p_{t=0} = p_0$ and $p_{t=1} = p_\text{data}$.  Next, we assume that there is a CNF that generates $p_{t|y}(x_t|y)$ using a vector field $\tilde{V}_t(x_t|y)$ that takes $y$ as a parameter.  The key insight that the flow matching paper makes is that we can write $V_t(x_t)$ as the expected value of $\tilde{V}_t(x_t|y)$ over the posterior distribution of $y$ given $x_t$:
$$
\begin{align}
V_t(x_t) &= \int \frac{p_y(y)p_{t|y}(x_t|y)}{p_t(x_t)}\tilde{V}_t(x_t|y) dy \\
&= \mathbb{E}_{p_{t|y}(y|x_t)}[\tilde{V}_t(x_t|y)]
\end{align}
$$
We can check that this is true by checking that the continuity equation is satisfied:
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= \frac{d}{dt}\int p_y(y)p_{t|y}(x_t|y) dy \\
  &= \int p_y(y)\frac{d}{dt}p_{t|y}(x_t|y) dy \\
  &= -\int p_y(y)\text{Div}(p_{t|y}(x_t|y)\tilde{V}_t(x_t|y))dy \\
  &= -\text{Div}(\int p_y(y)p_{t|y}(x_t|y)\tilde{V}_t(x_t|y)dy) \\
  &= -\text{Div}(p_t \underbrace{\int \frac{1}{p_t}p_y(y)p_{t|y}(x_t|y)\tilde{V}_t(x_t|y)dy}_{V_t})
\end{align}
$$


Thus, we have constructed a continuous normalizing flow that takes $p_0$ to $p_1=p_\text{data}$.  So far this doesn't seem too useful, but there are two reasons main reasons that will lead us to a simulation free training algorithm:

1. We can get easy unbiased estimates of the expected vector field as follows:
  $$
  \begin{align}
  \mathbb{E}_{p_t(x_t)}[V_t(x_t)] &= \int p_t(x_t)V_t(x_t) dx_t \\
  &= \int p_t(x_t)\mathbb{E}_{p_{t|y}(y|x_t)}[\tilde{V}_t(x_t|y)] dx_t \\
  &= \int \int p_t(x_t)p_{t|y}(y|x_t)\tilde{V}_t(x_t|y) dx_t dy \\
  &= \int \int p_y(y)p_{t|y}(x_t|y)\tilde{V}_t(x_t|y) dx_t dy \\
  &= \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\tilde{V}_t(x_t|y)\right]
  \end{align}
  $$

2. There are easy choices of $p_y(y)$ and $p_t(x_t|y)$ that we can sample from and know in closed form.  Specifically, we will usually choose $p_y = p_\text{data}$ and $p_t(x_t|y)$ to be a Gaussian distribution with mean $\mu_t(y)$ and covariance $\Sigma_t(y)$ with conditions on $\mu_t$ and $\Sigma_t$ that ensure that $p_{t=0} = p_0$ and $p_{t=1} = p_\text{data}$.

# Flow matching
Now that we have a way to construct a target continuous normalizing flow whose generating vector field is $V_t$, we can train a model to match $V_t$.  Let $W_t$ be a vector field that is parametrized using a neural network whose flow corresponds to the probability density function $q_t(x_t)$.  We can train $W_t$ to match $V_t$ by minimizing the following loss function:
$$
\begin{align}
\mathcal{L}_{\text{FM}}(\theta) &= \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\left\|V_t(x_t) - W_t(x_t;\theta)\right\|^2\right] dt \\
&= \small{\underbrace{\int_0^1 \mathbb{E}_{p_t(x_t)}[\|V_t(x_t)\|^2]dt}_{C_1} - 2\int_0^1 \mathbb{E}_{p_t(x_t)}[V_t(x_t)^TW_t(x_t;\theta)]dt + \int_0^1 \mathbb{E}_{p_t(x_t)}[\|W_t(x_t;\theta)\|^2]dt} \\
&= C_1 - 2\int_0^1 \mathbb{E}_{p_t(x_t)}\left[V_t(x_t)\right]^TW_t(x_t;\theta)dt + \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\|W_t(x_t;\theta)\|^2\right]dt \\
&= C_1 - 2\int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\tilde{V}_t(x_t|y)\right]^TW_t(x_t;\theta)dt + \int_0^1 \mathbb{E}_{p_t(x_t)}\left[\|W_t(x_t;\theta)\|^2\right]dt \\
&= C_1 - C_2 + \underbrace{\int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|\tilde{V}_t(x_t|y) - W_t(x_t;\theta)\|^2\right]dt}_{\mathcal{L}_{\text{CFM}}(\theta)}
\end{align}
$$
where $C_2 = \int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|\tilde{V}_t(x_t|y)\|^2\right]dt$.  So we can minimize $\mathcal{L}_{\text{FM}}(\theta)$ by minimizing $\mathcal{L}_{\text{CFM}}(\theta)$ because $C_1$ and $C_2$ are constants.  $\mathcal{L}_{\text{CFM}}(\theta)$ is called the **conditional flow matching** loss.

We can also reparametrize $x_t$ with $f_t(x_t|y)$ to get the following loss function:
$$
\begin{align}
\mathcal{L}_{\text{CFM}}(\theta) &= \int_0^1 \mathbb{E}_{p_y(y)p_t(x_t|y)}\left[\|\tilde{V}_t(x_t|y) - W_t(x_t;\theta)\|^2\right]dt \\
&= \int_0^1 \mathbb{E}_{p_y(y)p_0(x_0)}\left[\left\|\tilde{V}_t(f_t(x_0)|y) - W_t(f_t(x_0);\theta)\right\|^2\right]dt
\end{align}
$$

In this form, we can see the algorithm needed to train $W_t(x_t;\theta)$:
1. Sample $y\sim p_y(y)$ and $x_0\sim p_0(x_0)$
2. Construct some path that starts at $x_0$ and ends at $y$
3. Sample any point on this path (to get $f_t(x_0)$) and get the tangent vector at that point (to get $\tilde{V}_t(f_t(x_0)|y)$)
4. Compute the loss between $\tilde{V}_t(f_t(x_0)|y)$ and $W_t(x_t;\theta)$

This training algorithm will be efficient so long as the path between $x_0$ and $x_1$ (which is given by $f_t(x_0)$) is easy to compute.  In the next section, we'll go over one possible example of how to do this.

# Conditional optimal transport
The easiest choice for that we could choose for a path between $x_0$ and $y$ is simply a straight line between the two.  This is called the **conditional optimal transport** path and is defined as follows:
$$
\begin{align}
  f_t(x_0;y) &= (1-t)x_0 + ty \\
  &= x_0 + t(y - x_0)
\end{align}
$$
The tangent vector to this curve is also trivial to compute:
$$
\begin{align}
  \frac{df_t(x_0;y)}{dt} &= y - x_0
\end{align}
$$
So the pseudo code to train a CNF using flow matching with the conditional optimal transport path looks like this
```python
def flow_matching_objective(data_batch):
  batch_size = data_batch.shape[0]
  t = uniform_sample(0, 1, batch_size)
  x0 = normal_sample(0, 1, batch_size)
  xt = x0 + t*(data_batch - x0)
  Vt = data_batch - x0
  Wt = model(t, xt)
  loss = (Vt - Wt)**2
  return loss.mean()
```
