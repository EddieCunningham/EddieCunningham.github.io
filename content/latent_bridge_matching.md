Title: Latent bridge Matching
Date: 2024-05-06
Category: Blog
Slug: latent-bridge-matching
hidden: true
Summary: Latent bridge matching


[An Observed Value Consistent Diffusion Model for Imputing
Missing Values in Multivariate Time Series](http://home.ustc.edu.cn/~pengkun/files/Publications/KDD2023_1.pdf)

# Position velocity model
Suppose we want a model for sequences $y_1,\dots,y_n \sim \mu(y_1,\dots,y_n)$.  If we assume that these sequences represent noisy observations, then we can construct a model that assumes that there are noise-free latent variables that are used to generate the observations.  For example, a simple velocity model assumes that the latent variables contain information about the true position and velocity of the point so that $z_t = \begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix}$.  Then if we choose a step size $\Delta t$ so that $x_{t+\Delta t} = x_t + \dot{x}_t\Delta t$, then we can write the model as:
$$
\begin{align}
  dz_t &= \underbrace{\begin{bmatrix}0 & I \\ 0 & 0\end{bmatrix}}_{F}z_tdt + \underbrace{\sigma \begin{bmatrix}0 & 0 \\ 0 & I\end{bmatrix}}_{L}dW_t \\
  y_k &\sim N(y_k|\begin{bmatrix}I & 0 \end{bmatrix}z_{t_k},R)
\end{align}
$$
To perform efficient inference in this model, we can use the Kalman filter to compute queries like $\pi(z_t | y_{t_{1:k}})$.  To do this, we first need to know the transition distribution $\pi(z_t | z_{t-1})$.

### Transition distribution
The transition distribution can be solved in closed form because the SDE is linear and time-invariant.  Using the solutions in equations 6.19 and 6.20 of [Särkkä 2019](https://users.aalto.fi/~asolin/sde-book/sde-book.pdf), we first have that the transition matrix is given as:
$$
\begin{align}
  \frac{\partial \Psi_{t|s}}{\partial t} &= F \Psi_{t|s} \\
  \implies \Psi_{t|s} &= \exp\{F(t-s)\} = \begin{bmatrix}I & (t-s)I \\ 0 & I\end{bmatrix} \\
\end{align}
$$
Then the transition distribution is given as the Gaussian $N(z_t | m_{t|s}(z_s), P_{t|s}(z_s))$ where:
$$
\begin{align}
  m_{t|s} &= \Psi_{t|s}z_s = \begin{bmatrix}x_s + (t-s)\dot{x}_s \\ \dot{x}_s\end{bmatrix} \\
  P_{t|s} &= \int_s^t \Psi_{t|s}L L^T \Psi_{t|s}^T dt = \sigma^2 \begin{bmatrix} \frac{1}{3}(t-s)^3I & \frac{1}{2}(t-s)^2I \\ \frac{1}{2}(t-s)^2I & (t-s)I \end{bmatrix}
\end{align}
$$
To summarize, if $\Delta t = (t-s)$, then
$$
\begin{align}
  \pi(\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix} | \begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix}) &= N(\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix} | \begin{bmatrix}I & \Delta t \\ 0 & I\end{bmatrix}\begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix}, \sigma^2 \begin{bmatrix} \frac{1}{3}\Delta t^3I & \frac{1}{2}\Delta t^2I \\ \frac{1}{2}\Delta t^2I & \Delta tI \end{bmatrix})
\end{align}
$$

## Conditioned SDE
Now suppose we want to condition this tracking model on an endpoint.  We can do this using Doob's h-transform:
$$
\begin{align}
  d\begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix} &= (F\begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix} + \sigma^2 \nabla_t \log \pi(\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix} | \begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix}))dt + \sigma dW_t
\end{align}
$$
To compute this, we first need to know what the gradient of the log likelihood of a regression Gaussian is:

### Score function
$$
\begin{align}
  \nabla_x \log N(y|Ax,\Sigma) &= \nabla_x (-\frac{1}{2}(y-Ax)^T\Sigma^{-1}(y-Ax)) \\
  &= \nabla_x (-\frac{1}{2}x^TA^T\Sigma^{-1}Ax + x^TA^T\Sigma^{-1}y) \\
  &= -A^T\Sigma^{-1}Ax + A^T\Sigma^{-1}y
\end{align}
$$
Now lets plug in values.  First, note that $\Sigma^{-1} = \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ -\frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix}$ and $A = \begin{bmatrix}I & \Delta t \\ 0 & I\end{bmatrix}$.  So we have that
$$
\begin{align}
  A^T \Sigma^{-1} &= \frac{1}{\sigma^2} \begin{bmatrix}I & 0 \\ \Delta t & I\end{bmatrix}\begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ -\frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix} \\
  &= \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ (\frac{12}{\Delta t^2} - \frac{6}{\Delta t^2})I & (-\frac{6}{\Delta t} + \frac{4}{\Delta t})I \end{bmatrix} \\
  &= \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & -\frac{2}{\Delta t}I \end{bmatrix}
\end{align}
$$
and
$$
\begin{align}
  A^T \Sigma^{-1}A &= \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & -\frac{2}{\Delta t}I \end{bmatrix}\begin{bmatrix}I & \Delta t \\ 0 & I\end{bmatrix} \\
  &= \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & (\frac{12}{\Delta t^2} - \frac{6}{\Delta t^2})I \\ \frac{6}{\Delta t^2}I & (\frac{6}{\Delta t}-\frac{2}{\Delta t})I \end{bmatrix} \\
  &= \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & \frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix}
\end{align}
$$
So the score function is:
$$
\begin{align}
  \nabla \log N(y|Ax,\Sigma) &= -A^T\Sigma^{-1}Ax + A^T\Sigma^{-1}y \\
  &= -\frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & \frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix} + \frac{1}{\sigma^2} \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & -\frac{2}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix}
\end{align}
$$

and the correction term for the SDE is:
$$
\begin{align}
  \sigma^2 \begin{bmatrix}0 & 0 \\ 0 & I\end{bmatrix}\nabla \log N(y|Ax,\Sigma) &= \begin{bmatrix}0 & 0 \\ 0 & I\end{bmatrix}\left(-\begin{bmatrix} \frac{12}{\Delta t^3}I & \frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix} + \begin{bmatrix} \frac{12}{\Delta t^3}I & -\frac{6}{\Delta t^2}I \\ \frac{6}{\Delta t^2}I & -\frac{2}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix}\right) \\
  &= -\begin{bmatrix} 0 & 0 \\ \frac{6}{\Delta t^2}I & \frac{4}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_t \\ \dot{x}_t\end{bmatrix} + \begin{bmatrix} 0 & 0 \\ \frac{6}{\Delta t^2}I & -\frac{2}{\Delta t}I \end{bmatrix}\begin{bmatrix}x_{t+\Delta t} \\ \dot{x}_{t+\Delta t}\end{bmatrix}
\end{align}
$$

### Plugging it back in
Now we can plug in the values to get the conditioned SDE:
$$
\begin{align}
  d\begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix} &= \left(\left(\begin{bmatrix}0 & I \\ 0 & 0\end{bmatrix} - \begin{bmatrix} 0 & \frac{6}{(T - t)^2}I \\ \frac{6}{(T - t)^2}I & \frac{4}{(T - t)}I \end{bmatrix}\right)\begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix} + \begin{bmatrix} 0 & -\frac{6}{(T - t)^2}I \\ \frac{6}{(T - t)^2}I & -\frac{2}{(T - t)}I \end{bmatrix}\begin{bmatrix}x_{T} \\ \dot{x}_{T}\end{bmatrix}\right)dt + \sigma \begin{bmatrix}0 & 0 \\ 0 & I\end{bmatrix}dW_t \\
  &= \left(\begin{bmatrix} 0 & I \\ -\frac{6}{(T - t)^2}I & -\frac{4}{(T - t)}I \end{bmatrix}\begin{bmatrix}x_t \\ \dot{x}_t \end{bmatrix} + \begin{bmatrix} 0 &0 \\ \frac{6}{(T - t)^2}I & -\frac{2}{(T - t)}I \end{bmatrix}\begin{bmatrix}x_{T} \\ \dot{x}_{T}\end{bmatrix}\right)dt + \sigma \begin{bmatrix}0 & 0 \\ 0 & I\end{bmatrix}dW_t
\end{align}
$$

# Schrodinger bridge matching
There are 2 shortcomings of the above model.  The first is that the model might be misspecified - the true dynamics might not be linear, so the distribution of the observations under the model might not be correct.  The second is that we might not have full sequences of data available to us.  Instead, we might have access to marginals of the data, i.e. only have access to $y_i \sim \mu(y_i)$.  We can use Schrodinger bridge matching to solve both of these problems.

Schrodinger bridge matching consists of iteratively solving the following 2 steps:
1. Learn an SDE that matches the marginals of the data
2. Improve the coupling between the marginals to match the joint distribution of the data

The first step is solved using bridge matching and the second step is solved by optimizing a value function.

## Bridge matching
Bridge matching is a method for learning an SDE that matches the marginals of the data.  Let $\hat{\mu}(y_{1:N})$ be some coupling of the data marginals.  For example, if we only have access to the marginals of $\mu$, we could construct $\hat{\mu}$ as the product of marginals, $\hat{\mu}(y_{1:N}) = \prod_{i=1}^N \mu(y_i)$.  Then we construct a distribution over the latent variables as:
$$
\begin{align}
  p_t(z_t) = \int \hat{\mu}(y_{1:N}) \pi(z_t | y_{1:N}) dy_{1:N}
\end{align}
$$
In order to apply bridge matching, we need to find an SDE whose marginal distribution is the same as $p_t$.  This can be done by finding the times adjacent to $t$.  Suppose $t_k \lt t \lt t_{k+1}$, then we can write the marginal distribution as:
$$
\begin{align}
  p_t(z_t) &= \int \hat{\mu}(y_{1:N}) \pi(z_t | y_{1:N}) dy_{1:N} \\
  &= \int \hat{\mu}(y_{1:N}) \int\int \pi(z_t,z_{t_k},z_{t_{k+1}} | y_{1:N}) dz_{t_k} dz_{t_{k+1}} dy_{1:N} \\
  &= \int \hat{\mu}(y_{1:N}) \int\int \pi(z_t | z_{t_k},z_{t_{k+1}},y_{1:N}) \pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N}) dz_{t_k} dz_{t_{k+1}} dy_{1:N} \\
  &= \int \hat{\mu}(y_{1:N}) \int\int \pi(z_t | z_{t_k},z_{t_{k+1}}) \pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N}) dz_{t_k} dz_{t_{k+1}} dy_{1:N} \\
  &= \int\int\int \hat{\mu}(y_{1:N})\pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N}) \pi(z_t | z_{t_k},z_{t_{k+1}})  dz_{t_k} dz_{t_{k+1}} dy_{1:N}
\end{align}
$$
Note that $\pi(z_t | z_{t_k},z_{t_{k+1}})$ is the marginal distribution of $\pi$ conditioned to start at $z_{t_k}$ and end at $z_{t_{k+1}}$.  We can write this as:
$$
\begin{align}
  dz_t &= (Fz_t + \sigma^2 \nabla \log \pi(z_{t_{k+1}}|z_t))dt + \sigma LdW_t, \quad z_{t=t_k} = z_{t_k}
\end{align}
$$
Furthermore, we can sample from $\pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N})$ efficiently using Kalman smoothing:
$$
\begin{align}
  \pi(z_{t_k}, z_{t_{k+1}} | y_{1:N}) &\propto  \pi(z_{t_k}, z_{t_{k+1}}, y_{1:N}) \\
  &= \pi(y_{k+1:N} | z_{t_{k+1}}) \pi(z_{t_{k+1}} | z_{t_k}) \pi(z_{t_k}, y_{1:k})
\end{align}
$$

We can then solve for the SDE that has the marginal $p_t$ by taking a time derivative and using the Fokker-Planck equation:
$$
\begin{align}
  \frac{\partial p_t(z_t)}{\partial t} &= \int\int\int \hat{\mu}(y_{1:N})\pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N}) \pi(z_t | z_{t_k},z_{t_{k+1}})  dz_{t_k} dz_{t_{k+1}} dy_{1:N} \\
  &= \int\int\int \hat{\mu}(y_{1:N})\pi_{t_k}(z_{t_k}, z_{t_{k+1}} | y_{1:N}) \frac{\partial \pi(z_t | z_{t_k},z_{t_{k+1}})}{\partial t}  dz_{t_k} dz_{t_{k+1}} dy_{1:N} \\
  &= \mathbb{E}_{z_{t_k},z_{t_{k+1}}}\left[\frac{\partial \pi(z_t | z_{t_k},z_{t_{k+1}})}{\partial t}\right] \\
  &= \mathbb{E}_{z_{t_k},z_{t_{k+1}}}\left[-\text{Div}(\pi(z_t | z_{t_k},z_{t_{k+1}})(Fz_t + \sigma^2 \nabla \log \pi(z_{t_{k+1}}|z_t))) + \frac{\sigma^2}{2}\text{Div}(\nabla \pi(z_t | z_{t_k},z_{t_{k+1}}))\right] \\
  &= -\text{Div}(\mathbb{E}_{z_{t_k},z_{t_{k+1}}}\left[\pi(z_t | z_{t_k},z_{t_{k+1}})(Fz_t + \sigma^2 \nabla \log \pi(z_{t_{k+1}}|z_t))\right]) + \frac{\sigma^2}{2}\text{Div}(\nabla \mathbb{E}_{z_{t_k},z_{t_{k+1}}}\left[\pi(z_t | z_{t_k},z_{t_{k+1}})\right]) \\
  &= -\text{Div}(p_t(z_t)(\underbrace{Fz_t + \sigma^2 \mathbb{E}_{z_{t_k},z_{t_{k+1}}|z_t}\left[\nabla \log \pi(z_{t_{k+1}}|z_t)\right]}_{\text{new drift}})) + \frac{\sigma^2}{2}\text{Div}(\nabla p_t(z_t))
\end{align}
$$
So we can recognize the SDE of $p_t(z_t)$ as:
$$
\begin{align}
  dz_t &= (Fz_t + \sigma^2 \mathbb{E}_{z_{t_k},z_{t_{k+1}}|z_t}\left[\nabla \log \pi(z_{t_{k+1}}|z_t)\right])dt + \sigma dW_t
\end{align}
$$