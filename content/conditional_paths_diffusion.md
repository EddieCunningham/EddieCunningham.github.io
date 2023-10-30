Title: Diffusion as Gaussian conditional probability paths
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
Tags: diffusion, sde, cnf, conditional probability paths
Slug: gaussian-conditional-probability-path
Summary: How Gaussian conditional probability paths are related to diffusion

In my [previous post](flow_matching.md) on flow matching, we went over how to construct a [continuous normalizing flow](continuous_normalizing_flows.md) that transforms samples from a user specified prior, $p_{t=0}$, to a target probability distribution, $p_{t=1}$, that we can sample from.  In order to do this, we assumed that we could construct some probability path $p_t$ that can be written as a marginal distribution over a latent variable:
$$
\begin{align}
p_t(x_t) = \int p_y(y)p_{t|y}(x_t|y) dy
\end{align}
$$
In this post we'll go over one easy way to choose $p_y$ and $p_{t|y}$ and go over how this relates to diffusion models.

# Gaussian conditional flows
If we choose $p_0 = N(0,I)$, then we can make the following choices for $p_y$ and $p_{t|y}$:
$$
\begin{align}
p_y(y) &= p_\text{data}(y) \\
p_{t|y}(x_t|y) &= \mathcal{N}(x_t; \mu_t(y), \Sigma_t(y))
\end{align}
$$
where $\mu_t$ and $\Sigma_t$ are differentiable functions of $y$ that satisfy the following conditions:
$$
\begin{align}
\mu_{t=0}(y) = 0,\quad \Sigma_{t=0}(y) = I \\
\mu_{t=1}(y) = y,\quad \Sigma_{t=1}(y) = 0 \\
\end{align}
$$

We can verify that that these choices of $p_y$ and $p_{t|y}$ give us the correct marginals at $t=0$ and $t=1$:
$$
\begin{align}
  p_0(x_0) &= \int p_y(y)p_{t=0|y}(x_0|y) dy \\
  &= \int p_\text{data}(y)\mathcal{N}(x_0; \mu_0(y), \Sigma_0(y)) dy \\
  &= \int p_\text{data}(y)\mathcal{N}(x_0; 0, I) dy \\
  &= \mathcal{N}(x_0; 0, I)
\end{align}
$$

$$
\begin{align}
  p_1(x_1) &= \int p_y(y)p_{t=1|y}(x_1|y) dy \\
  &= \int p_\text{data}(y)\mathcal{N}(x_1; \mu_1(y), \Sigma_1(y)) dy \\
  &= \int p_\text{data}(y)\delta(x_1 - y) dy \\
  &= p_\text{data}(x_1)
\end{align}
$$

## Vector field that generates the probability path
In order to use these choices of $p_y$ and $p_{t|y}$, we need to be able to compute the vector field that generates the probability path.  Because we are working with simple distributions like Gaussians, everything is available to us in closed form.

To find the vector field, we first need to the equation for the path that a sample can evolve on.  Notice that we can sample $x_t \sim p_{t|y}(x_t|y)$ using the model:
$$
\begin{align}
x_0 &\sim N(0,I) \\
x_t &= \mu_t(y) + \Sigma_t(y)^{1/2}x_0
\end{align}
$$
So we can differentiate $x_t$ to get the conditional vector field:
$$
\begin{align}
\tilde{V}_t(x_t|y) &= \frac{dx_t}{dt} \\
&= \frac{d}{dt}\left[\mu_t(y) + \Sigma_t(y)^{1/2}x_0\right] \\
&= \frac{d \mu_t(y)}{dt} + \frac{d \Sigma_t(y)^{1/2}}{dt}\underbrace{x_0}_{\Sigma_t^{\frac{-1}{2}}(x_t - \mu_t(y))} \\
&= \frac{d \mu_t(y)}{dt} + \frac{d \Sigma_t(y)^{1/2}}{dt}\Sigma_t^{\frac{-1}{2}}(x_t - \mu_t(y))
\end{align}
$$
The simplest choice of $\mu_t$ and $\Sigma_t$ that satisfies our boundary conditions is:
$$
\begin{align}
\mu_t(y) &= ty \\
\Sigma_t(y) &= (1-t)^2I
\end{align}
$$
This leads us to the optimal transport conditional VFs from the [flow matching paper](https://arxiv.org/pdf/2210.02747.pdf) and straight path example from my [post on flow matching](flow_matching.md) which has
$$
\begin{align}
  x_t(x_0;y) &= x_0 + t(y - x_0) \\
  \tilde{V}_t(x_t|y) &= y - x_0
\end{align}
$$

Even though we are free to parametrize $\Sigma$ in terms of $y$ as well as $t$, we will only consider the case where $\Sigma$ only depends on $t$ going forward so that things simplify.  This is also the case that appears in practice.


# Relationship between diffusion and flow matching
Now that we have the equations that describe the probability path, we can relate this to diffusion models by relating the vector fields that generate the probability path to the score function.

## CNF from an SDE
The appendix of the flow matching paper has a section that shows how to go from a stochastic differential equation to vector field that generates its flow.  This is expressed by the Fokker-Planck equation:
If we have a stochastic differential equation of the form $dx = f_tdt + g_t dw$, the its probability path has the form
$$
\begin{align}
\frac{\partial p_t}{\partial t} = -\text{Div}(f_tp_t) + \frac{g_t^2}{2}\Delta p_t
\end{align}
$$
where $\Delta$ is the Laplace operator.  If we rearrange terms to match the form of the continuity equation, we have that
$$
\begin{align}
\frac{\partial p_t}{\partial t} = -\text{Div}(\underbrace{(f_t - \frac{g_t^2}{2}\nabla \log p_t)}_{V_t}p_t )
\end{align}
$$
where $w_t$ is the vector field that generates the flow of $p_t$.  So the vector field that generates the flow of $p_t$ is given by $V_t = f_t - \frac{g_t^2}{2}\nabla \log p_t$.

## SDE from a CNF
Next, we'll go in the reverse direction and show how CNFs that are constructed using conditional Gaussian probability paths can be expressed as stochastic differential equations.

Recall that our probability path has the form:
$$
\begin{align}
p_t(x_t) = \int p_\text{data}(y)\mathcal{N}(x_t; \mu_t(y), \Sigma_t) dy
\end{align}
$$
To get the score function of the probability path, we'll first show how the score function of the conditional Gaussian relates to its vector field that generates its flow.

### Score function and vector field of a Gaussian
Recall that the score function of a Gaussian is given by
$$
\begin{align}
  \nabla \log N(x_t|\mu_t,\Sigma_t) = -\Sigma_t^{-1}(x_t - \mu_t)
\end{align}
$$
and the vector field that generates the flow is
$$
\begin{align}
  \tilde{V}_t &= \frac{d \mu_t}{dt} + \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{-\frac{1}{2}}(x_t - \mu_t)
\end{align}
$$
We can multiply the score function by $\Sigma_t^\frac{1}{2}$ and then plug it into the vector field equation to relate the two:
$$
\begin{align}
  \tilde{V}_t &= \frac{d \mu_t}{dt} - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log N(x_t|\mu_t,\Sigma_t)
\end{align}
$$

Now that we have a relationship between the score and vector field for the conditional distribution, we can take a look at how this relates to the score function and vector field of the marginal distribution.

## Relationship of marginals
The key property that we will exploit is the posterior expectation property that both the score function and marginal vector field satisfy:
$$
\begin{align}
\nabla \log p_t(x_t) &= \int p_t(y|x_t)\nabla \log p_t(x_t|y)dy \\
V_t(x_t) &= \int p_t(y|x_t)\tilde{V}_t(x_t|y)dy
\end{align}
$$
This is easily seen for the score function because
$$
\begin{align}
\nabla \log p_t(x_t) &= \frac{1}{p_t(x_t)}\nabla\int p_y(y)p_{t|y}(x_t|y)dy \\
&= \frac{1}{p_t(x_t)}\int p_y(y)\nabla p_{t|y}(x_t|y)dy \\
&= \int \frac{p_y(y)p_{t|y}(x_t|y)}{p_t(x_t)} \nabla \log p_{t|y}(x_t|y)dy \\
&= \int p_t(y|x_t)\nabla \log p_{t|y}(x_t|y)dy
\end{align}
$$
and the marginal vector field because of the continuity equation (see my [flow matching](flow_matching.md) post).

So now we can plug and chug our equations for the conditional distribution into these marginal equations:
$$
\begin{align}
  V_t(x_t) &= \int p_t(y|x_t)\tilde{V}_t(x_t|y)dy \\
  &= \int p_t(y|x_t)\left(\frac{d \mu_t(y)}{dt} - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\underbrace{\nabla \log N(x_t|\mu_t(y),\Sigma_t)}_{\nabla \log p_{t|y}(x_t|y)}\right)dy \\
  &= \int p_t(y|x_t)\frac{d \mu_t(y)}{dt}dy - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\int p_t(y|x_t)\nabla \log p_{t|y}(x_t|y)dy \\
  &= \int p_t(y|x_t)\frac{d \mu_t(y)}{dt}dy - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log p_t(x_t)
\end{align}
$$
Notice the similarity between this equation and the equation that we get from the Fokker-planck equation.  Next, we'll show that in the conditional optimal transport case, the first term can be simplified fully.

## Optimal transport conditional paths
We can look at the special case where we use the optimal transport conditional path where $\mu_t(y) = ty$ and $\Sigma_t = (1-t)^2I$.  In this case, we can fully simplify the expression of the marginal distribution's vector field by exploiting the fact that $\frac{d\mu_t(y)}{dt} = \frac{1}{t}\mu_t(y)$.  Again, because we want to relate everything to the score function, lets write $\mu_t(y)$ in terms of $\nabla \log p_{t|y}$:
$$
\begin{align}
  \nabla \log N(x_t|\mu_t,\Sigma_t) = -\Sigma_t^{-1}(x_t - \mu_t) \\
  \implies \mu_t = \Sigma_t\nabla \log N(x_t|\mu_t,\Sigma_t) + x_t
\end{align}
$$

Now lets simplify the posterior expectation:
$$
\begin{align}
  \int p_t(y|x_t)\frac{d \mu_t(y)}{dt}dy &= \int p_t(y|x_t)\frac{1}{t}\mu_t(y)dy \\
  &= \frac{1}{t}\int p_t(y|x_t)\left(\Sigma_t\nabla \log N(x_t|\mu_t(y),\Sigma_t) + x_t\right)dy \\
  &= \frac{1}{t}\left(\Sigma_t\int p_t(y|x_t)\log N(x_t|\mu_t(y),\Sigma_t)dy + x_t\right) \\
  &= \frac{1}{t}\left(\Sigma_t \nabla \log p_t(x_t) + x_t\right)
\end{align}
$$
Now we're almost done!  Next, we'll substitute $\Sigma_t = (1-t)^2I$ into the full expression:
$$
\begin{align}
  V_t(x_t) &= \int p_t(y|x_t)\frac{d \mu_t(y)}{dt}dy - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log p_t(x_t) \\
  &= \frac{1}{t}\left(\Sigma_t \nabla \log p_t(x_t) + x_t\right) - \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log p_t(x_t) \\
  &= \frac{1}{t}\left((1-t)^2\nabla \log p_t(x_t) + x_t \right) - \frac{d (1-t)}{dt}(1-t)\nabla \log p_t(x_t) \\
  &= \frac{1}{t}x_t + \left[\frac{(1-t)^2}{t} + (1-t)\right]\nabla \log p_t(x_t) \\
  &= \frac{1}{t}x_t + \frac{1-t}{t}\nabla \log p_t(x_t) \\
  &= \frac{1}{t}(x_t + (1-t)\nabla \log p_t(x_t))
\end{align}
$$
Our final expression that relates the vector field that generates the probability path and the score function of a CNF that is constructed using conditional probability paths is:
$$
\begin{align}
  V_t(x_t) &= \frac{1}{t}(x_t + (1-t)\nabla \log p_t(x_t))
\end{align}
$$