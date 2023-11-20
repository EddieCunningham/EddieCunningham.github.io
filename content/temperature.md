Title: The dynamics of temperature sampling
Date: 2023-11-15
Category: Blog
status: hidden
Slug: temperature-sampling
Summary: The dynamics of temperature sampling

Given a probability distribution $p(x)$, temperature sampling is about finding a way to sample from $\frac{1}{Z_t} p(x)^t$ where $Z_t$ is a normalization constant.  This is an interesting problem because it allows us to sample from a distribution that is more peakedthan $p(x)$ (when $t > 1$) or less peakedthan $p(x)$ (when $t < 1$).  This is trivial when we use a sampling procedure that depends on the score function because the tempered score function is simply $t \nabla \log p(x)$.  However, for flow based generative models it is not as straight forward.  The goal of this post is to derive the dynamics of temperature sampling for continuous normalizing flows.


Let $p_t(x) := \frac{1}{Z_t}p(x)^t$.  The first thing that we can notice is that we can write $\log p(x)$ in terms of $p_t$ and $Z_t$:
$$
\begin{align}
  \log p_t(x) &= -\log Z_t + t \log p(x) \\
  \nabla \log p_t(x) &= t \nabla \log p(x) \\
\end{align}
$$

# Likelihood dynamics
Lets look at how the log normalization constant changes with respect to $t$:
$$
\begin{align}
  \frac{\partial\log Z_t}{\partial t} &= \frac{1}{Z_t}\frac{\partial}{\partial t} \int p(x)^t dx \\
  &= \frac{1}{Z_t}\int \frac{\partial}{\partial t}\exp\{\log p(x) t\} dx \\
  &= \frac{1}{Z_t}\int \exp\{\log p(x) t\}\frac{\partial}{\partial t}(\log p(x) t) dx \\
  &= \frac{1}{Z_t}\int p(x)^t\log p(x) dx \\
  &= \int p_t(x)\log p(x) dx \\
  &= \mathbb{E}_{p_t}\left[\log p\right]
\end{align}
$$
This means that
$$
\begin{align}
  \frac{\partial\log p_t(x)}{\partial t} &= \frac{\partial}{\partial t}t \log p(x) - \frac{\partial}{\partial t}\log Z_t \\
  &= \log p(x) - \mathbb{E}_{p_t}\left[\log p\right]
\end{align}
$$

Next, lets look at the total derivative.
$$
\begin{align}
\frac{d \log p_t(x_t)}{dt} &= \frac{\partial \log p_t(x_t)}{\partial t} + \nabla \log p_t(x_t)^Tu_t(x_t) \\
-\text{Div}(u_t(x_t)) &= \log p(x_t) - \mathbb{E}_{p_t}\left[\log p\right] + \nabla \log p_t(x_t)^Tu_t(x_t) \\
&= \log p(x_t) - \mathbb{E}_{p_t}\left[\log p\right] + t\nabla \log p(x_t)^Tu_t(x_t) \\
\end{align}
$$

# Gradient dynamics
Next, lets look at the gradient dynamics.  We already have seen that
$$
\begin{align}
\nabla \log p_t(x) = t \nabla \log p(x)
\end{align}
$$
So the partial derivative w.r.t. $t$ is
$$
\begin{align}
\frac{\partial \nabla \log p_t(x)}{\partial t} = \nabla \log p(x)
\end{align}
$$
Next, lets look at the total derivative.  We can expand the total derivative in 3 different ways:

#### 1.
$$
\begin{align}
  \frac{d\nabla \log p_t(x_t)}{dt} &= -\nabla u_t(x_t)^T\nabla \log p_t(x_t) + \nabla \frac{d \log p_t(x_t)}{dt} \\
  &= -\nabla u_t(x_t)^T\nabla \log p_t(x_t) + \nabla (\log p(x_t) - \mathbb{E}_{p_t}\left[\log p\right] + \nabla \log p_t(x_t)^Tu_t(x_t)) \\
  &= \nabla \log p(x_t) + \nabla^2 \log p_t(x_t)^Tu_t(x_t) \\
  &= \nabla \log p(x_t) + t \nabla^2 \log p(x_t)^Tu_t(x_t) \\
\end{align}
$$

#### 2.
$$
\begin{align}
  \frac{d\nabla \log p_t(x_t)}{dt} &= -\nabla u_t(x_t)^T\nabla \log p_t(x_t) + \nabla \frac{d \log p_t(x_t)}{dt} \\
   &= -\nabla u_t(x_t)^T\nabla \log p_t(x_t) - \nabla \text{Div}(u_t)
\end{align}
$$

#### 3.
$$
\begin{align}
  \frac{d\nabla \log p_t(x_t)}{dt} &= \frac{dt \nabla \log p(x_t)}{dt} \\
  &= \nabla \log p(x_t) + t\frac{d\nabla \log p(x_t)}{dt} \\
\end{align}
$$


Setting 1 and 2 equal to each other and noting that $\nabla^2 \log p$ is symmetric yields
$$
\begin{align}
  \nabla^2 \log p(x_t)u_t(x_t) &= \frac{d\nabla \log p(x_t)}{dt}
\end{align}
$$
Then plugging in 2 for the rhs yields
$$
\begin{align}
  \nabla^2 \log p(x_t)u_t(x_t) &= -\nabla u_t(x_t)^T\nabla \log p_t(x_t) - \nabla \text{Div}(u_t)
\end{align}
$$
Rerranging terms gives the final expression for $u_t$:
$$
\begin{align}
  \nabla^2 \log p(x_t)u_t(x_t) + \nabla u_t(x_t)^T\nabla \log p_t(x_t) + \nabla \text{Div}(u_t) = 0
\end{align}
$$