Title: VI with CNFs
Date: 2023-11-17
Modified: 2023-11-17
Category: Blog
status: hidden
Slug: vi-cnf
Summary: How to do variational inference with continuous normalizing flows

# Motivation
Suppose we want to be able to sample from some probability density function, $p$, that we can evaluate.  We can do this by using a continuous normalizing flow (CNF) to transform a simple distribution, $q_0$, into $p$.  CNFs do this by flowing samples from $q_0$ along a vector field $V_t$ that is parameterized by a neural network to time $t=1$.  The probability density function of the samples at time $t$ is denoted by $q_t$ and if the model is trained correctly then $q_1 = p$.

The current way of training CNFs is to minimize $KL[q_1||p]$ by maximizing the ELBO.  However, this can be expensive and lead to vector fields that are difficult to integrate numerically.  We will try to remedy this issue by first constructing a target probability path that starts at $q_0$ and ends at $p$ as:
$$
\begin{align}
  p_\beta &= \frac{1}{Z_\beta}q_0(x)^{1-\beta}p(x)^\beta
\end{align}
$$
Then we will try to learn a CNF by minimizing the objective
$$
\begin{align}
  \mathcal{L} = \int_{0}^1 \lambda(\beta)\text{KL}\left[q_{\beta}||p_{\beta}\right] d\beta
\end{align}
$$
where $\lambda(\beta)$ is a weighting function that we will choose later.  By doing so, the CNF will learn to transport samples from a fixed target distribution to the target distribution.  This should help the flow learn multimodal distributions better because the modes of the distribution are slowly formed as $\beta$ increases.

# Objective derivation
Let's start by deriving the KL term.  We'll take an approach that lets us completely bypass the normalization constant.

$$
\begin{align}
  \text{KL}\left[q_{\beta}||p_{\beta}\right] &= \text{KL}\left[q_0||p_{\beta}\right] + \int_{0}^\beta \frac{d}{dt}\text{KL}\left[q_t||p_\beta \right]dt \\
\end{align}
$$
Next,
$$
\begin{align}
  \frac{d}{dt}\text{KL}\left[q_t||p_\beta\right] &= \int \frac{d}{dt}q_t\log \frac{q_t}{p_\beta}dV \\
  &= \int \left((\frac{d q_t}{dt})\log \frac{q_t}{p_\beta} + q_t\frac{d \log q_t}{dt}\right)dV \\
  &= \int \left(-\text{Div}(q_t V_t) \log \frac{q_t}{p_\beta} + \underbrace{\frac{d q}{dt}}_{\text{$0$ in expectation}}\right)dV \\
  &= \int \langle \nabla \log \frac{q_t}{p_\beta} , q_t V_t\rangle dz \\
  &= \int q_t\left( \langle \nabla \log q_t , V_t\rangle  - \langle \nabla \log p_\beta, V_t\rangle  \right)dV \\
  &= \int \langle \nabla q_t , V_t\rangle  dV - \int q_t\langle \nabla \log p_\beta, V_t\rangle  dV \\
  &= -\int q_t \text{Div}(V_t) dV - \int q_t\langle \nabla \log p_\beta, V_t\rangle  dV \\
  &= -\mathbb{E}_{q_t}\left[\langle \nabla \log p_\beta, V_t \rangle  + \text{Div}(V_t)\right]
\end{align}
$$

This means that we can get an unbiased estimate of the KL term without having to compute the normalization constant.  Instead, we only need access to the score function:
$$
\begin{align}
  \nabla \log p_\beta &= (1-\beta)\nabla \log q_0 + \beta\nabla \log p
\end{align}
$$

Putting everything together yields the objective:
$$
\begin{align}
  \mathcal{L} &= \int_{0}^1 \text{KL}\left[q_{\beta}||p_{\beta}\right] d\beta \\
  &= \underbrace{\int_{0}^1 \text{KL}\left[q_0||p_{\beta}\right] d\beta}_{\text{C}} + \int_{0}^1 \int_{0}^\beta \frac{d}{dt}\text{KL}\left[q_t||p_\beta \right]dt d\beta \\
  &= \text{C} - \int_{0}^1 \int_{0}^\beta \mathbb{E}_{q_t}\left[\langle \nabla \log p_\beta, V_t \rangle  + \text{Div}(V_t)\right]dt d\beta \\
  &= \text{C} - \mathbb{E}_{q_0}\left[\int_{0}^1 \int_{0}^\beta \langle \nabla \log p_\beta, V_t \rangle  + \text{Div}(V_t)dt d\beta\right] \\
  &= \text{C} - \mathbb{E}_{q_0}[\int_{0}^1 \int_{0}^\beta (1-\beta)\langle \nabla \log q_0, V_t \rangle + \beta \langle \nabla \log p , V_t \rangle + \text{Div}(V_t)dt d\beta]
\end{align}
$$

## Integrating out $\beta$
Next, we'll integrate out $\beta$ by using the identity:
$$
\begin{align}
  \int_0^1 \int_0^\beta h(\beta)f(t)dt d\beta &= \int_0^1 \left[H(1) - H(t)\right]f(t) dt
\end{align}
$$
where $\frac{dH(\beta)}{d\beta} = h(\beta)$.

Proof:
We can change the region of integration by letting $s=1-t$ and $\gamma = 1-\beta$ and then we have:
$$
\begin{align}
  \int_{\beta=0}^1 \int_{t=0}^\beta h(\beta)f(t)dt d\beta &= \int_{s=0}^1 \int_{\gamma=s}^0 h(1-\gamma)f(1-s)d\gamma ds \\
  &= \int_{s=0}^1 f(1-s) \int_{\gamma=s}^0 h(1-\gamma)d\gamma ds \\
  &= \int_{s=0}^1 f(1-s) \left[H(1-s) - H(1)\right] ds \\
  &= \int_{t=0}^1 f(t) \left[H(1) - H(t)\right] ds
\end{align}
$$

### Choosing $\lambda(\beta)$
$\lambda(\beta)$ will be absorbed into $h(\beta)$ above.  In particular, $h(\beta)$ will take the form of either:
$$
\begin{align}
  h_1(\beta) &= \lambda(\beta) \\
  h_2(\beta) &= \beta \lambda(\beta)
\end{align}
$$
Therefore, we will need to be able to evaluate the anti-derivative of $\lambda(\beta)$ and $\beta \lambda(\beta)$.  The anti-derivative of $x\lambda(\beta)$ can be evaluated using integration by parts:
$$
\begin{align}
  \int_a^b \beta\lambda(\beta) d\beta &= (\beta \Lambda(\beta))\big|_a^b - \int_a^b \Lambda(\beta) d\beta
\end{align}
$$
where $\Lambda(\beta)$ is the anti-derivative of $\lambda(\beta)$.  Therefore, we need to be able to evaluate 2 anti-derivatives of $\lambda(\beta)$ in order to have a closed form expression for the objective.

The trivial choice of letting $\lambda(\beta) = 1$ gives us the expreessions:
$$
\begin{align}
  \int_{0}^1 \int_{0}^\beta C(t) dt d\beta &= \int_0^1 (1-t)C(t)dt \\
  \int_{0}^1 \int_{0}^\beta \beta B(t) dt d\beta &= \int_0^1 \frac{1}{2}(1-t^2)B(t)dt \\
  \int_{0}^1 \int_{0}^\beta (1-\beta)A(t) dt d\beta &= \int_0^1 \frac{1}{2}(1-t)^2A(t)dt
\end{align}
$$
With the choice of $\lambda(\beta) = 1$, the objective becomes:
$$
\begin{align}
  \mathcal{L} &= \text{C} - \mathbb{E}_{q_0}[\int_{0}^1 \frac{1}{2}(1-t)^2\langle \nabla \log q_0, V_t \rangle + \frac{1}{2}(1-t^2) \langle \nabla \log p , V_t \rangle + (1-t)\text{Div}(V_t)dt]
\end{align}
$$

### Polynomial $\lambda(\beta)$
We can also choose $\lambda(\beta)$ to be a polynomial of degree $n$:
$$
\begin{align}
  \lambda(\beta) &= \sum_{i=0}^n a_i \beta^i
\end{align}
$$
The anti-derivatives are then:
$$
\begin{align}
  H_1(\beta) = \int \lambda(\beta) d\beta &= \sum_{i=0}^n \frac{a_i}{i+1}\beta^{i+1} \\
  H_2(\beta) = \int \beta \lambda(\beta) d\beta &= \sum_{i=0}^n \frac{a_i}{i+2}\beta^{i+2} \\
  H_3(\beta) = \int (1 - \beta) \lambda(\beta) d\beta &= \sum_{i=0}^n a_i\beta^{i+1}(\frac{1}{i+1} - \frac{1}{i+2}\beta)
\end{align}
$$
And plugging this into $H(1) - H(t)$ gives us:
$$
\begin{align}
  H_1(1) - H_1(t) &= \sum_{i=0}^n \frac{a_i}{i+1}(1 - t^{i+1}) \\
  H_2(1) - H_2(t) &= \sum_{i=0}^n \frac{a_i}{i+2}(1-t^{i+2}) \\
  H_3(1) - H_3(t) &= \sum_{i=0}^n \frac{a_i}{i+1}(1 - t^{i+1})(1 - \frac{i+1}{i+2}t)
\end{align}
$$


# Comparison to ELBO maximization
Lets see how this compares to maximizing the ELBO
$$
\begin{align}
  -\log p(x) &= \int q_1(z_1)\log \frac{q_1(z_1)}{p(x,z_1)}dz_1 - \text{KL}\left[q_1(z_1)||p(z_1|x)\right] \\
  &\leq \int q_1(z_1)\log \frac{q_1(z_1)}{p(x,z_1)}dz_1 \\
  &= \int q_0(z_0)\log q_1(F_1(z_0))dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
  &= \int q_0(z_0)\left[\log q_0(z_0) + \int_0^1 \frac{d\log q_t(z_t)}{dt}dt\right]dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
  &= \int q_0(z_0)\left[\log q_0(z_0) - \int_0^1 \text{Div}(V_t(z_t))\right]dz_0 - \int q_1(z_1)\log p(x,z_1)dz_1 \\
\end{align}
$$