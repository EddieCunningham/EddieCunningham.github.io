Title: SDEs with Gaussian marginals
Date: 2024-04-24
Category: Blog
Slug: gaussian-marginal-sde
hidden: true
Summary: SDEs with Gaussian marginals



In conditional bridge matching, we build bridges between probability distributions by creating a mixture model of pinned bridges at samples from the targets.  A popular way to build these pinned bridges is by using Gaussian probability paths whose standard deviation is 0 at its endpoints.  In this document we will go over all of the equations that are needed in order to build these bridges.

# Pinned Gaussian bridges
Suppose we have $x_0\sim \mu_0$ and $x_1\sim \mu_1$ and we want to build a bridge between $x_0$ and $x_1$.  In other words, we want to find a distribution $p_t(x_t|x_0,x_1)$ such that $p_0 = \delta_{x_0}$ and $p_1(x_1) = \delta_{x_1}$.  A choice we can make is to use a Gaussian distribution
$$
\begin{align}
  p_t(x_t|x_0,x_1) &= N(x_t|\mu_t,\gamma_t^2), \quad\text{ s.t. } p_0 = \delta_{x_0}, \quad p_1 = \delta_{x_1}
\end{align}
$$
With this choice, we can write the marginal density at time $t$ as a mixture under the targets as
$$
\begin{align}
  p_t(x_t) &= \int \int \mu_{0,1}N(x_t|\mu_t,\gamma_t^2;x_0,x_1) dx_1dx_0
\end{align}
$$

In order to learn a generative model with this marginal, we can use flow/score/drift matching to learn the parameters of the SDE.  However in order to apply these learning algorithms, we need to know the flow/score/drift of the pinned Gaussian bridges.  In this document, we will derive these equations.

### Gaussian score
The score of a Gaussian is given:
$$
\begin{align}
  \nabla \log N(x_t|\mu_t,\gamma_t^2) &= \nabla (-\frac{1}{2\gamma_t^2}\|x_t-\mu_t\|^2) \\
  &= \frac{1}{\gamma_t^2}(\mu_t - x_t)
\end{align}
$$

### Gaussian flow
To get the flow, we need to look at the generating process for the Gaussian.
$$
\begin{align}
  x_t = \mu_t + \gamma_t \epsilon, \quad \epsilon \sim N(0,I)
\end{align}
$$
therefore
$$
\begin{align}
  \frac{dx_t}{dt} &= \frac{d\mu_t}{dt} + \frac{d\gamma_t}{dt}\epsilon \\
  &= \frac{d\mu_t}{dt} - \frac{d\gamma_t}{dt}\frac{\mu_t - x_t}{\gamma_t} \\
  &= \frac{d\mu_t}{dt} - \frac{d\log \gamma_t}{dt}(\mu_t - x_t) \\
  &= \frac{d\mu_t}{dt} - \gamma_t\frac{d\gamma_t}{dt}\nabla \log p_t \\
  &= \frac{d\mu_t}{dt} - \frac{1}{2}\frac{d\gamma_t^2}{dt} \nabla \log p_t
\end{align}
$$

### Gaussian drift
We can use the relationship between the flow and the score to get the drift of the Gaussian.  Suppose that we have an SDE with diffusion coefficient $\sigma_t$ and flow $u_t$:
$$
\begin{align}
  dx_t = u_t dt + \sigma_t dW_t
\end{align}
$$
then the drift is given by
$$
\begin{align}
  u_t &= \frac{dx_t}{dt} + \frac{\sigma_t^2}{2}\nabla \log p_t \\
  &= \frac{d\mu_t}{dt} + \frac{1}{2}(\sigma_t^2 - \frac{d\gamma_t^2}{dt}) \nabla \log p_t
\end{align}
$$
Similarly, if we consider the reversed SDE, this has the form
$$
\begin{align}
  d\bar{x}_s &= \left(-u_{1-s} + \sigma_{1-s}^2\nabla \log \rho_{1-s}\right)ds + \sigma_{1-s} dW_s \\
  &= \left(-\frac{dx_{1-s}}{dt} - \frac{\sigma_{1-s}^2}{2}\nabla \log p_{1-s} + \sigma_{1-s}^2\nabla \log \rho_{1-s}\right)ds + \sigma_{1-s} dW_s \\
  &= \left(-\frac{dx_{1-s}}{dt} + \frac{\sigma_{1-s}^2}{2}\nabla \log p_{1-s}\right)ds + \sigma_{1-s} dW_s \\
  &= \bar{u}_{1-s} ds + \sigma_{1-s} dW_s
\end{align}
$$


# Brownian bridge
Now lets make these choices concrete.  Consider the brownian bridge between $x_0$ and $x_1$:
$$
\begin{align}
  p_{t|0,1}(x_t|x_0,x_1) = N(x_t|\mu_t(x_0,x_1),\gamma_t^2I), \quad \mu_t = (1-t)x_0 + tx_1, \quad \gamma_t^2 = t(1-t)\sigma_t^2
\end{align}
$$
We can compute the flow, score, and drift of this bridge.
### Flow
$$
\begin{align}
  \frac{dx_{t|0,1}}{dt} &= \frac{d\mu_t}{dt} - \frac{d\log \gamma_t}{dt}(\mu_t - x_t) \\
  &= \frac{d\mu_t}{dt} - \frac{1}{2}\frac{d\log \gamma_t^2}{dt}(\mu_t - x_t) \\
  &= x_1 - x_0 - \frac{1}{2}\frac{1-2t}{t(1-t)}((1-t)x_0 + tx_1 - x_t) \\
  &= x_1 - x_0 - \frac{1}{2}\frac{1-2t}{t}x_0 + \frac{1}{2}\frac{1-2t}{1-t}x_1 - \frac{1}{2}\frac{1-2t}{t(1-t)}x_t \\
  &= \frac{1}{2}\left(\frac{1}{1-t}x_1 - \frac{1}{t}x_0 + \frac{1-2t}{t(1-t)}x_t\right)
\end{align}
$$

### Score
$$
\begin{align}
  \nabla \log N(x_t|\mu_t,\gamma_t^2) &= \frac{1}{\gamma_t^2}(\mu_t - x_t) \\
  &= \frac{1}{t(1-t)\sigma_t^2}((1-t)x_0 + tx_1 - x_t) \\
  &= \frac{1}{\sigma_t^2}\left(\frac{1}{t}x_0 + \frac{1}{1-t}x_1 - \frac{1}{t(1-t)}x_t\right)
\end{align}
$$

### Forward drift
$$
\begin{align}
  u_{t|0,1} &= \frac{dx_{t|0,1}}{dt} + \frac{\sigma_t^2}{2}\nabla \log p_{t|0,1} \\
  &= \frac{1}{2}\left(\frac{1}{1-t}x_1 - \frac{1}{t}x_0 + \frac{1-2t}{t(1-t)}x_t\right) + \frac{1}{2}\left(\frac{1}{t}x_0 + \frac{1}{1-t}x_1 - \frac{1}{t(1-t)}x_t\right) \\
  &= \frac{x_1 - x_t}{1-t}
\end{align}
$$

### Backward drift
$$
\begin{align}
  \bar{u}_{t|0,1} &= -\frac{dx_{t|0,1}}{dt} + \frac{\sigma_t^2}{2}\nabla \log p_{t|0,1} \\
  &= -\frac{1}{2}\left(\frac{1}{1-t}x_1 - \frac{1}{t}x_0 + \frac{1-2t}{t(1-t)}x_t\right) + \frac{1}{2}\left(\frac{1}{t}x_0 + \frac{1}{1-t}x_1 - \frac{1}{t(1-t)}x_t\right) \\
  &= \frac{x_0 - x_t}{t}
\end{align}
$$

# Mixture of bridges
Now that we have a pinned Gaussian bridge, we can build a mixture of bridges by sampling from the targets and building a bridge between the samples.  The marginal density of the mixture of bridges is given by
$$
\begin{align}
  p_t &= \int \int \mu_{0,1}p_{t|0,1} dx_1dx_0
\end{align}
$$

Furthermore, the flow, score and drift are given by expectations under the posterior of the mixture model:

### Flow
$$
\begin{align}
  \frac{dx_t}{dt} = \frac{1}{2}\left(\frac{1}{1-t}\mathbb{E}_{x_0,x_1|t}[x_1] - \frac{1}{t}\mathbb{E}_{x_0,x_1|t}[x_0] + \frac{1-2t}{t(1-t)}x_t\right)
\end{align}
$$

### Score
$$
\begin{align}
  \nabla \log p_t = \frac{1}{\sigma_t^2}\left(\frac{1}{t}\mathbb{E}_{x_0,x_1|t}[x_0] + \frac{1}{1-t}\mathbb{E}_{x_0,x_1|t}[x_1] - \frac{1}{t(1-t)}x_t\right)
\end{align}
$$

### Forward drift
$$
\begin{align}
  u_t = \frac{\mathbb{E}_{x_0,x_1|t}[x_1] - x_t}{1-t}
\end{align}
$$

### Backward drift
$$
\begin{align}
  \bar{u}_t = \frac{\mathbb{E}_{x_0,x_1|t}[x_0] - x_t}{t}
\end{align}
$$

As we can see, if we could compute $\mathbb{E}_{x_0,x_1|t}[x_0]$ and $\mathbb{E}_{x_0,x_1|t}[x_1]$, then we would be able to compute the flow, score, and drift of the mixture of bridges, therefore we can match the endpoints in order to learn a bridge.

## Conditional distributions
We can also construct conditional distributions with the correct endpoint distributions.  For example, let
$$
\begin{align}
  p_{t|0} = \int \mu_{1|0}p_{t|0,1} dx_1
\end{align}
$$
Then we get that the networks that we need to learn are $\mathbb{E}_{x_1|x_0,t}[x_0]$ and $\mathbb{E}_{x_0,x_1|t}[x_1]$.

# Gaussian process SDE
Now lets take a look at what happens if we construct the Gaussian path using a Gaussian process.  This will allow us to condition on the entire path and not just the endpoints.

### Joint distribution
A Gaussian process can be thought of as a distribution over points that are jointly Gaussian.  For example, suppose we have (for the moment 1-dimensional) points $x_{t_1},\dots,x_{t_n}$ that are jointly Gaussian and a test point $x_t$.  We assert that the collection of points are distributed as:
$$
\begin{align}
  \begin{bmatrix}x_t \\ x_{t_1} \\ \vdots \\ x_{t_k} \end{bmatrix} \sim N(\begin{bmatrix}0 \\ 0 \\ \vdots \\ 0\end{bmatrix},\begin{bmatrix}k(t,t) & k(t,t_1) & \cdots & k(t,t_k) \\ k(t_1,t) & k(t_1,t_1) & \cdots & k(t_1,t_k) \\ \vdots & \vdots & \ddots & \vdots \\ k(t_k,t) & k(t_k,t_1) & \cdots & k(t_k,t_k) \end{bmatrix})
\end{align}
$$
where $k(t,t')$ is a kernel function over the times.  We can write this more compactly using block matrices as
$$
\begin{align}
  \begin{bmatrix}x_t \\ x_{\mathcal{T}} \end{bmatrix} \sim N(0,\begin{bmatrix}k_{t,t} & k_{t,\mathcal{T}} \\ k_{\mathcal{T},t} & k_{\mathcal{T},\mathcal{T}} \end{bmatrix})
\end{align}
$$
where $x_{\mathcal{T}} = \begin{bmatrix}x_{t_1} \\ \vdots \\ x_{t_k} \end{bmatrix}$ and $k_{t,t'} = k(t,t')$ and $k_{\mathcal{T},\mathcal{T}} = \begin{bmatrix}k(t_1,t_1) & \cdots & k(t_1,t_k) \\ \vdots & \ddots & \vdots \\ k(t_k,t_1) & \cdots & k(t_k,t_k) \end{bmatrix}$.

### Conditional distribution
With this joint distribution in mind, we are interested in the conditional distribution obtained by conditioning on the points $x_{\mathcal{T}}$:
$$
\begin{align}
  p_{t|\mathcal{T}}(x_t|x_{\mathcal{T}}) = N(x_t|k_{t,\mathcal{T}}k_{\mathcal{T},\mathcal{T}}^{-1}x_{\mathcal{T}},k_{t,t} - k_{t,\mathcal{T}}k_{\mathcal{T},\mathcal{T}}^{-1}k_{\mathcal{T},t})
\end{align}
$$
By construction, we are guaranteed that when $t\in \mathcal{T}$, the conditional distribution is a delta function at the observed point.  Our next task is to figure out what the flow, score, and drift of this conditional distribution are.

## Gaussian process flow
The first thing that we can do is see how to construct samples from the Gaussian process:
$$
\begin{align}
  x_t = k_{t,\mathcal{T}}k_{\mathcal{T},\mathcal{T}}^{-1}x_{\mathcal{T}} + \sqrt{k_{t,t} - k_{t,\mathcal{T}}k_{\mathcal{T},\mathcal{T}}^{-1}k_{\mathcal{T},t}}\epsilon, \quad \epsilon \sim N(0,1)
\end{align}
$$

# Variance
Now suppose that we have a score function that is written as a linear combination of expected values:
$$
\begin{align}
  \nabla \log p_{t|\mathcal{T}} &= \alpha x_t + \sum_{j=1}^n \beta_j x_{t_j} \\
  \nabla \log p_t &= \alpha x_t + \sum_{j=1}^n \beta_j \mathbb{E}_{\mathcal{T}|t}[x_{t_j}]
\end{align}
$$
where $\mathcal{T}=\{t_1,\dots,t_k\}$,  $p_t = \int p_{\mathcal{T}}p_{t|\mathcal{T}}dx_{\mathcal{T}}$.  Note that we have that
$$
\begin{align}
  \nabla \log p_{\mathcal{T}|t} &= \nabla \log p_{t|\mathcal{T}} - \nabla \log p_t \\
  &= \sum_{j=1}^n \beta_j (x_{t_j} - \mathbb{E}_{\mathcal{T}|t}[x_{t_j}])
\end{align}
$$

Now, lets compute the gradient of the expected value of a variable:
$$
\begin{align}
  \nabla \mathbb{E}_{\mathcal{T}|t}[x_{t_i}] &= \int p_{\mathcal{T}|t}\nabla \log p_{\mathcal{T}|t} x_{t_i}^T dx_{\mathcal{T}} \\
  &= \int p_{\mathcal{T}|t}\left[\sum_{j=1}^n \beta_j (x_{t_j} - \mathbb{E}_{\mathcal{T}|t}[x_{t_j}])\right] x_{t_i}^T dx_{\mathcal{T}} \\
  &= \left[\sum_{j\neq i}^n \beta_j \underbrace{(\mathbb{E}_{\mathcal{T}|t}[x_{t_j}] - \mathbb{E}_{\mathcal{T}|t}[x_{t_j}])}_{0}\right]\mathbb{E}_{\mathcal{T}|t}[x_{t_i}]^T +  \beta_i \int p_{\mathcal{T}|t}\left[(x_{t_i} - \mathbb{E}_{\mathcal{T}|t}[x_{t_i}])\right] x_{t_i}^T dx_{\mathcal{T}} \\
  &= \beta_i \left[\mathbb{E}_{\mathcal{T}|t}[x_{t_i}x_{t_i}^T] - \mathbb{E}_{\mathcal{T}|t}[x_{t_i}]\mathbb{E}_{\mathcal{T}|t}[x_{t_i}]^T\right] \\
  &= \beta_i \text{Var}[x_{t_i}|\mathcal{T}]
\end{align}
$$
So we're left with
$$
\begin{align}
  \text{Var}_{\mathcal{T}|t}[x_{t_i}] &= \frac{1}{\beta_i }\nabla \mathbb{E}_{\mathcal{T}|t}[x_{t_i}]
\end{align}
$$