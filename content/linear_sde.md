Title: Linear SDEs
Date: 2024-05-11
Category: Blog
status: hidden
Slug: linear-sde
Summary: Notes on linear SDEs

# Linear SDEs and transition density
We will consider SDEs of the form
$$
\begin{align}
  dx_t = (\alpha_t x_t + \beta_t^{(i)} x^{(i)}) dt + \sigma dW_t
\end{align}
$$
where no variables depend on $x_t$.  First, lets take a look at what the transition density is in closed form.  We know that linear SDEs like this have Gaussian transitions of the form $x_{t|s} \sim \mathcal{N}(\mu_{t|s}, \gamma_{t|s}^2 I)$, so we will solve for $\mu_{t|s}$ and $\gamma_{t|s}^2$.

To do this we need to define the transition kernel:
$$
\begin{align}
  &\psi_{t|s} \in \mathbb{R},\quad t\geq s \\
  \text{where}\quad &\frac{d\psi_{t|s}}{dt} = \psi_{t|s}\alpha_{t},\quad \psi_{t|r} = \psi_{t|s}(\psi_{r|s})^{-1} \quad \text{and} \quad \psi_{t|t} = 1
\end{align}
$$
Then we have that
$$
\begin{align}
  \mu_{t|s} &= \psi_{t|s}x_s + \int_s^t {(\psi_{t|s}(\psi_{r|s})^{-1})}(\beta_r^{(i)}  x^{(i)})dr \\
  &= \psi_{t|s}x_s + \psi_{t|s}\underbrace{(\int_s^t {(\psi_{r|s})^{-1}}\beta_r^{(i)} dr)}_{d_{t|s}^{(i)} } x^{(i)} \\
  &= \psi_{t|s}(x_s + d_{t|s}^{(i)} x^{(i)})
\end{align}
$$
and
$$
\begin{align}
  \gamma_{t|s}^2 &= \sigma^2\psi_{t|s}^2\int_s^t (\psi_{r|s})^{-2} dr
\end{align}
$$
So to summarize how we obtain the transition densities:
1. $\psi_{t|s} = 1 - \int_s^t {(\psi_{t|s}(\psi_{r|s})^{-1})}\alpha_r dr$
2. $d_{t|s}^{(i)} = \int_s^t {(\psi_{r|s})^{-1}}\beta_r^{(i)} dr$
3. $\mu_{t|s} = \psi_{t|s}(x_s + d_{t|s}^{(i)} x^{(i)})$
4. $\gamma_{t|s}^2 = \sigma^2\psi_{t|s}^2\int_s^t (\psi_{r|s})^{-2} dr$

and then return $\mu_{t|s}$ and $\gamma_{t|s}^2$.

Also the score function that we will use with conditioning is $\nabla \log p_{t|s}$ is
$$
\begin{align}
  \nabla_s \log p_{t|s} &= -\nabla_t \log p_{t|s} \\
  &= \frac{1}{\gamma_{t|s}^2}(x_t - \mu_{t|s})
\end{align}
$$

# Doob h-transform
Next, let's see how we can condition linear SDEs on endpoints.  Recall that the SDE for conditioning $x_t$ on $x_T$ is
$$
\begin{align}
  dx_{t|T} &= (\alpha_t x_t + \beta_t^{(i)} x^{(i)} + \sigma_t^2 \nabla \log p_{T|t}) dt + \sigma_t dW_t \\
  &= (\alpha_t x_t + \beta_t^{(i)} x^{(i)} + \underbrace{(\frac{\sigma_t}{\gamma_{T|t}})^2}_{\eta_{T|t}}(x_T - \underbrace{\mu_{T|t}}_{\psi_{T|t} x_t + d_{T|t}^{(i)} x^{(i)}})) dt + \sigma_t dW_t \\
  &= ((\alpha_t - \eta_{T|t} \psi_{T|t}) x_t + ((\beta_t^{(i)} - \eta_{T|t} d_{T|t}^{(i)}) x^{(i)} + \eta_{T|t} x_T)) dt + \sigma_t dW_t
\end{align}
$$