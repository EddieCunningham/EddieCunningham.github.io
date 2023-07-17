Title: Diffusion as Gaussian conditional probability paths
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
Tags: diffusion, sde, cnf, conditional probability paths
Slug: gaussian-conditional-probability-path
Summary: How Gaussian conditional probability paths are related to diffusion


# Relationship between diffusion and flow matching
Here we'll go over the relationship between diffusion and flow matching.

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
\frac{\partial p_t}{\partial t} = -\text{Div}(\underbrace{(f_t - \frac{g_t^2}{2}\nabla \log p_t)}_{w_t}p_t )
\end{align}
$$
where $w_t$ is the vector field that generates the flow of $p_t$.  So the vector field that generates the flow of $p_t$ is given by $w_t = f_t - \frac{g_t^2}{2}\nabla \log p_t$.

## SDE from a CNF
Next, we'll go in the reverse direction and show how CNFs that are constructed using conditional probability paths can be expressed as stochastic differential equations.

Let $p_t(x_t)$ be the probability path of our CNF and assume that it has the following form:
$$
p_t(x_t) = \int q(x_1)N(x_t|\mu_t(x_1),\Sigma_t)dx_1
$$
Gaussian distributions have the special property that the vector field that generates their flow can be written in terms of the score function.

### Score function and vector field of a Gaussian
Recall that we can sample by first sampling $x_0 \sim N(0,I)$ and then computing $x_t = \mu_t + \Sigma_t^\frac{1}{2}x_0$ and that the score function of a Gaussian is given by $\nabla \log N(x_t|\mu_t,\Sigma_t) = \Sigma_t^{-1}(x_t - \mu_t)$.  We can write the score function in terms of $x_0$ as follows:
$$
\begin{align}
\nabla \log N(x_t|\mu_t,\Sigma_t) &= \Sigma_t^{-1}(x_t - \mu_t) \\
&= \Sigma_t^{-1}(\mu_t + \Sigma_t^\frac{1}{2}x_0 - \mu_t) \\
&= \Sigma_t^{-1}\Sigma_t^\frac{1}{2}x_0 \\
&= \Sigma_t^{-\frac{1}{2}}x_0
\end{align}
$$
Next, we can compute the vector field that generates the flow of $N(x_t|\mu_t,\Sigma_t)$ by taking the time derivative of a sample from $N(x_t|\mu_t,\Sigma_t)$:
$$
\begin{align}
u_t &= \frac{dx_t}{dt} \\
 &= \frac{d}{dt}(\mu_t + \Sigma_t^\frac{1}{2}x_0) \\
&= \frac{d \mu_t}{dt} + \frac{d\Sigma_t^\frac{1}{2}}{dt}x_0
\end{align}
$$
So by replacing $x_0$ in terms of the score function, we have our final relationship:
$$
\begin{align}
u_t &= \frac{d \mu_t}{dt} + \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log N(x_t|\mu_t,\Sigma_t)
\end{align}
$$

## Relationship of marginals
Now that we have a relationship between the conditional probability path and the vector field that generates its flow, we can use this to relate the marginal vector field and score function.  The key property that we will exploit is that the score function, like the vector field, can be written as an expectation of the conditional versions over the posterior distribution:
$$
\begin{align}
\nabla \log p_t(x_t) &= \int p_t(x_1|x_t)\nabla \log p_t(x_t|x_1)dx_1 \\
u_t(x_t) &= \int p_t(x_1|x_t)u_t(x_t|x_1)dx_1
\end{align}
$$
So we can plug in our expression for the conditional vector field:
$$
\begin{align}
u_t(x_t) &= \int p_t(x_1|x_t)u_t(x_t|x_1)dx_1 \\
&= \int p_t(x_1|x_t)(\frac{d \mu_t(x_1)}{dt} + \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log N(x_t|\mu_t(x_1),\Sigma_t))dx_1 \\
&= \underbrace{\int p_t(x_1|x_t)\frac{d \mu_t(x_1)}{dt}dx_1}_{f_t(x_t)} + \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\int p_t(x_1|x_t)\nabla \log N(x_t|\mu_t(x_1),\Sigma_t)dx_1 \\
&= f_t(x_t) + \frac{d\Sigma_t^\frac{1}{2}}{dt}\Sigma_t^{\frac{1}{2}}\nabla \log p_t(x_t)
\end{align}
$$
Notice that this almost matches the form of the vector field for a diffusion model.

## Optimal transport conditional paths
We can look at the special case where we use the optimal transport conditional path where $\mu_t(x_1) = tx_1$ and $\Sigma_t = (1-t)^2I$.  In this case, we can simplify $f_t(x_t)$ as follows:
$$
\begin{align}
f_t(x_t) &= \int p_t(x_1|x_t)\frac{d \mu_t(x_1)}{dt}dx_1 \\
&= \int p_t(x_1|x_t)t \mu_t(x_1)dx_1 \\
&= t \int p_t(x_1|x_t)  \\
\end{align}
$$