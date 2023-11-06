Title: KL-Divergence, Score Matching, and Flow Matching
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
status: hidden
Tags: probability paths, KL-divergence, score matching, flow matching
Slug: kl-div-and-matching
Summary: The relationship between KL-divergence, score matching, and flow matching

# Overview
KL-divergence minimization, score matching and flow matching are all different ways to train generative models.  KL-divergence minimization is typically used to train normalizing flows, score matching for diffusion models and flow matching for continuous normalizing flows.  In this post, we'll go over how these three methods are related and when to use each one.

# KL-divergence
Let $p$ and $q$ be two probability density functions defined on a Riemannian manifold $(\mathcal{M}, g)$ and let $dV_g$ be the volume form on $\mathcal{M}$.  The KL-divergence between $p$ and $q$ is defined as
$$
\begin{align}
\text{KL}[p\|q] &= \int_{\mathcal{M}}p \log \frac{p}{q} dV_g
\end{align}
$$
It has the nice property that $KL[p\|q] \geq 0$ and equals $0$ if and only if $p=q$.  Because of this, the KL divergence can be used to minimize the difference between two distributions.

In the context of generative models, we can use the KL divergence to minimize the difference between the distribution of the data and the distribution of our model.  Let $p$ be the distribution of the data and $q(\theta)$ be the distribution of the model with parameters $\theta$.  Then
$$
\begin{align}
  \nabla_{\theta}\text{KL}[p\|q(\theta)] &= \nabla_{\theta}\int_{\mathcal{M}}p \log \frac{p}{q(\theta)} dV_g \\
  &= \underbrace{\nabla_{\theta}\int_{\mathcal{M}}p \log p dV_g}_{0} - \nabla_{\theta}\int_{\mathcal{M}}p \log q(\theta) dV_g \\
  &= -\int_{\mathcal{M}}p \nabla_{\theta}\log q(\theta) dV_g \\
  &= -\nabla_{\theta}\mathbb{E}_p\left[\log q(\theta)\right]
\end{align}
$$
Because the gradients of the KL divergence are equal to the gradients of the expectation of the log likelihood of the data under the model, we can train our model by maximizing the likelihood of our model under the data.  This is the standard way to train a normalizing flow where we can compute the log likelihood under the model exactly.

# Matching
A more modern approach to training generative models is to use either score matching or flow matching.  These methods are based on the idea that we can construct a **probability path** for the target probability distribution and our model.  A probability path is a time dependent probability distribution that is characterized by how its samples change over time using a time dependent function called a flow.

### Probability paths
Let $p_t$ is a time dependent probability density function defined on a Riemannian manifold $(\mathcal{M},g)$.  Let $x_0\sim p_{t=0}$ be a sample at time $t=0$.  A flow associated with the probability path is a time dependent diffeomorphism $f_t$ such that $f_t(x_0)$ is distributed according to $p_t$, meaning $f_t(x_0) \sim p_t$.  It is often more convenient to work with the time derivative of the flow, which is a vector field $V_t \in \mathfrak{X}(\mathcal{M})$ so that $\frac{df_t}{dt} = V_t$.  If we evaluate the flow at a point $x_0$ and write $x_t = f_t(x_0)$, then we can write the equation in a more suggestive way
$$
\begin{align}
  \frac{dx_t}{dt} &= V_t(x_t),\text{ where }x_t := f_t(x_0)
\end{align}
$$
The probability path and vector field are related via the continuity equation (see my [continuous normalizing flows post]({filename}continuous_normalizing_flows.md) to see where it comes from):
$$
\begin{align}
  \frac{\partial p_t}{\partial t} &= -\text{Div}(p_tV_t)
\end{align}
$$
where $\text{Div}$ is the divergence operator on $\mathcal{M}$.  A useful property that we'll use later is that for any function $f\in C^\infty(\mathcal{M})$,
$$
\begin{align}
  \text{Div}(fV) &= f\text{Div}(V) + \langle \nabla f, V \rangle_g
\end{align}
$$

But where do probability paths come from if we are trying to learn how to model some fixed probabiltiy distribution?  It turns out that as long as we can sample from our target distribution $p_\text{data}$, which is the case when we are trying to learn the unknown data generating probability distribution, then we can always construct a probability path from any starting distribution $p_{t=0}$ to the target at $t=1$.  See my [flow matching post]({filename}flow_matching.md) for more details.


## Score matching
Now that we know what probability paths are, lets introduce score matching.  The score of a probability density function, in the context of generative modeling, is the gradient of the log likelihood function $\nabla_x \log p_t(x)$.  Score matching aims to minimize the norm between the score of the target distribution and the score of the model distribution at all times:
$$
\begin{align}
  \mathcal{L}_{\text{SM}}(\theta) &= \int_{t_0}^{t_1} \int_{\mathcal{M}}p_t \left\|\nabla_x \log p_t - \nabla_x \log q_t(\theta)\right\|_g^2 dV_g dt
\end{align}
$$
where $q(x;\theta)$ is the model distribution with parameters $\theta$.  Score matching is typically used to train [diffusion models](https://arxiv.org/pdf/2011.13456.pdf), but can suffer when $p_t(x)$ approaches 0 because the gradient of the log likelihood will approach infinity.

## Flow matching
Flow matching is similar to score matching, but instead of matching the score of the target distribution, it matches the vector field that generates the flow for each distribution.  Let $V_t$ be the vector field that generates the flow for $p_t$ and $W_t$ be the vector field that generates the flow for $q_t(\theta)$.  Then flow matching aims to minimize the norm between the vector fields of the target and model distributions at all times:
$$
\begin{align}
  \mathcal{L}_{\text{FM}}(\theta) &= \int_{t_0}^{t_1} \int_{\mathcal{M}}p_t \left\|V_t - W_t\right\|_g^2 dV_g dt
\end{align}
$$
Flow matching is used to train [continuous normalizing flows](https://arxiv.org/pdf/2002.02428.pdf) and has been shown to be a more stable alternative to score matching.

# Entropy
We can see how a generating vector field and score function interact through the time derivative of the entropy of a probability distribution.  If $(p_t,V_t)$ is a probability path, then
$$
\begin{align}
  \frac{d}{dt}H(p_t) &= -\frac{d}{dt}\int_{\mathcal{M}}p_t \log p_t dV_g \\
  &= -\int_{\mathcal{M}}\frac{dp_t}{dt} \log p_t dV_g - \underbrace{\int_{\mathcal{M}}\frac{dp_t}{dt}dV_g}_{0} \\
  &= \int_{\mathcal{M}}\text{Div}(p_tV_t) \log p_t dV_g \\
  &= -\int_{\mathcal{M}}\langle p_tV_t, \nabla\log p_t \rangle_g dV_g \\
  &= -\int_{\mathcal{M}}p_t\langle V_t, \nabla\log p_t \rangle_g dV_g \\
\end{align}
$$
So the inner product between the score function and the vector field tells us how the entropy changes.  We can see that to maximize this quantity, we need $V_t$ to be in the same opposite direction as $\nabla \log p_t$.  This makes sense as this corresponds to flowing outwards from the peak of the distribution.

# KL-Divergence
Now that we've introduced KL-divergence, score matching, and flow matching, we can see how they are related.  Say that we have a probability path for our target distribution $p_t$ and a path for our model distribution $q_t$ and assume that $p_0 = q_0$ (we construct the probability paths like this in flow matching).  We can express the KL divergence between the final two distributions, $p_{t=1}$ and $q_{t=1}$, as
$$
\begin{align}
  \text{KL}\left[p_1\|q_1\right] &= \underbrace{\text{KL}\left[p_0\|q_0\right]}_{0} + \int_{t=0}^1 \frac{d}{dt}\text{KL}\left[p_t\|q_t\right] dt \\
  &= \int_{t=0}^1 \frac{d}{dt}\text{KL}\left[p_t\|q_t\right] dt
\end{align}
$$
Before expanding the time derivative of the KL-divergence, lets go over the identities that we need to know.  Recall that we are assuming that $\mathcal{M}$ is a Riemannian manifold with metric $g$ and no boundary.  The identities we're using are:
1. Continuity equation: $\frac{\partial p_t}{\partial t} = -\text{Div}(p_tV_t)$
2. Integration by parts for boundryless manifolds: $-\int_{\mathcal{M}}f\text{Div}(V)dV_g = \int_\mathcal{M}\langle \nabla f, V\rangle_g dV_g$
See my post on [continuous normalizing flows]({filename}continuous_normalizing_flows.md) for a derivation of the continuity equation and [problem 16-12 of Lee](https://math.berkeley.edu/~jchaidez/materials/reu/lee_smooth_manifolds.pdf) for integration by parts.

Next, lets expand the time derivative of KL-divergence:
$$
\begin{align}
  \frac{d}{dt}\text{KL}\left[p_t\|q_t\right] &= \frac{d}{dt}\int_{\mathcal{M}}p_t \log \frac{p_t}{q_t} dV_g \\
  &= \int_{\mathcal{M}}\frac{d p_t}{dt} \log \frac{p_t}{q_t} dV_g + \int_{\mathcal{M}}p_t \frac{d}{dt}\log \frac{p_t}{q_t} dV_g \\
  &= -\int_{\mathcal{M}}\text{Div}(p_tV_t) \log \frac{p_t}{q_t} dV_g + \underbrace{\int_{\mathcal{M}}p_t \frac{d}{dt}\log p_t dV_g}_{0} - \int_{\mathcal{M}}\frac{p_t}{q_t} \frac{dq_t}{dt} dV_g \\
  &= \int_{\mathcal{M}}\langle p_t V_t, \nabla \log \frac{p_t}{q_t} \rangle_g dV_g + \int_{\mathcal{M}}\frac{p_t}{q_t} \text{Div}(q_tW_t) dV_g \\
  &= \int_{\mathcal{M}}p_t\langle V_t, \nabla \log \frac{p_t}{q_t} \rangle_g dV_g - \int_{\mathcal{M}}\langle \nabla \frac{p_t}{q_t}, q_tW_t\rangle_g  dV_g \\
  &= \int_{\mathcal{M}}p_t\langle V_t, \nabla \log \frac{p_t}{q_t} \rangle_g dV_g - \int_{\mathcal{M}}p_t \langle \nabla \log \frac{p_t}{q_t}, W_t\rangle_g  dV_g \\
  &= \int_{\mathcal{M}}p_t\langle V_t - W_t, \nabla \log p_t - \nabla \log q_t \rangle_g dV_g
\end{align}
$$
Notice that we have an equation that combines both the scores and vector fields.  We can write the score matching and flow matching objectives more suggestively by writing the $L2$ norm as an inner product:

$$
\begin{align}
  \text{KL}\left[p_1\|q_1\right] &= \int \int_{\mathcal{M}}p_t\langle V_t - W_t, \nabla \log p_t - \nabla \log q_t \rangle_g dV_g dt \\
  \mathcal{L}_{\text{SM}} &= \int_{t_0}^{t_1} \int_{\mathcal{M}}p_t \langle \nabla_x \log p_t - \nabla_x \log q_t, \nabla_x \log p_t - \nabla_x \log q_t \rangle_g dV_g dt \\
  \mathcal{L}_{\text{FM}} &= \int_{t_0}^{t_1} \int_{\mathcal{M}}p_t \langle V_t - W_t, V_t - W_t \rangle_g dV_g dt
\end{align}
$$
KL divergence, score matching and flow matching all take an expectation with respect to $p_t$ but differ in what they take the inner product with.
