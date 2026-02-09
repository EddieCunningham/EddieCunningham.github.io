Title: Expectation Maximization for SDE based SSMs
Date: 2025-10-16
Modified: 2025-10-16
Category: Blog
Tags: SDEs, SSMs, EM
Slug: sde_ssm_em
Summary: Expectation maximization for SDE based SSMs

# Overview
Suppose we have sequence data $(y_1,\dots,y_n) \sim \mu(y_1,\dots,y_n)$ that we want to model using a latent linear time invariant SDE with distinct Gaussian emissions.  This generative model for $(y_1,\dots,y_n)$ is given by
$$
\begin{align}
  x_1 &\sim N(x_1|\mu_1, P_1) \\
  dx_t &= Fx_t dt + L dW_t \\
  y_k &\sim N(y_k|H_k x_{t_k} + u_k, R_k) \text{ for } k=1,\dots,n
\end{align}
$$
Since LTI-SDEs have Gaussian transitions, we can construct an equivalent linear dynamical system.  Recall that the transition distribution of an LTI-SDE of the form $dx_t = Fx_t dt + L dW_t$, from time $t$ to time $t+s$ is given by
$$
\begin{align}
    p(x_{t+s}|x_t) &= N(x_{t+s}|A_sx_t,\Sigma_s),\quad \text{where }\begin{bmatrix}A_s & \Sigma_s A_s^{-T} \\ 0 & A_s^{-T} \end{bmatrix} := \exp\{\begin{bmatrix}F & LL^T \\ 0 & -F^T \end{bmatrix}s\}
\end{align}
$$

If we assume that all of the observations are given at uniformly spaced times so that $t_k = k\Delta t$ for $k=0,\dots,n$, then we can construct the following linear dynamical system:
$$
\begin{align}
  x_1 &\sim N(x_1|\mu_1, P_1) \\
  x_{k+1} &= N(x_{k+1}|A x_k, \Sigma) \\
  y_k &\sim N(y_k|H_k x_k + u_k, R_k)
\end{align}
$$
where $A$ and $\Sigma$ are given by the expression above.  Next, we'll derive the EM algorithm for this model.

# Expectation Maximization
Here we'll generally describe how EM works.  Suppose we have a target distribution $\mu(Y)$ and a model with parameters $\theta$ that generates a distribution $p(Y|\theta)$.  Our goal is to minimize the KL divergence between the target distribution and the model distribution.  The KL divergence is given by
$$
\begin{align}
  \mathrm{KL}[\mu(Y)\|p(Y|\theta)] &= \int_{\mathcal{Y}} \mu(Y) \log \frac{\mu(Y)}{p(Y|\theta)} dY \\
  &= \text{const. } - \mathbb{E}_{\mu(Y)} \left[ \log p(Y|\theta) \right]
\end{align}
$$
Minimizing the KL divergence is equivalent to maximizing the log likelihood of the data under the model, so we'll focus on this.  In order to derive the EM algorithm, suppose $\theta^{(t)}$ is the current estimate of the parameters.  We can first rewrite the log likelihood using $\theta^{(t)}$ as follows:
$$
\begin{align}
  \log p(Y|\theta) &= \log p(Y,X|\theta) - \log p(X|Y,\theta) \\
  &= \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) \right] - \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(X|Y,\theta) \right]
\end{align}
$$
Although we have not done anything yet, notice that the right most term almost resembles KL divergence.  If we could somehow add the term $\mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(X|Y,\theta^{(t)}) \right]$, then we would get a KL divergence term, which we know is non-negative.  Then hopefully we would be able to bound whatever expression we introduced to get the KL divergence term.  If we subtract $\log p(Y|\theta)$ by $\log p(Y|\theta^{(t)})$, then we get this KL divergence term and are able to say something about the difference between the two distributions.  We can now write the log likelihood as
$$
\begin{align}
  \log p(Y|\theta) -  \log p(Y|\theta^{(t)}) &= \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) - \log p(Y,X|\theta^{(t)}) \right] \underbrace{- \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(X|Y,\theta) - \log p(X|Y,\theta^{(t)}) \right]}_{\text{KL divergence}} \\
  &= \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) - \log p(Y,X|\theta^{(t)}) \right] + \mathrm{KL}[p(Y,X|\theta^{(t)})\|p(X|Y,\theta)] \\
  &\geq \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) - \log p(Y,X|\theta^{(t)}) \right]
\end{align}
$$
So we have that the log likelihood is bounded above by the expected value of the log likelihood of the complete data under the current model.  If we maximize the right hand side, then we must increase the left hand side.  This is the key idea behind the EM algorithm.  Suppose we define the next set of parameters as
$$
\begin{align}
  \theta^{(t+1)} &= \arg \max_{\theta} \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) - \log p(Y,X|\theta^{(t)}) \right] \\
  &= \arg \max_{\theta} \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) \right]
\end{align}
$$
Then we can see that the KL divergence between $\mu(Y)$ and $p(Y|\theta^{(t+1)})$ must be less than or equal to the KL divergence between $\mu(Y)$ and $p(Y|\theta^{(t)})$:
$$
\begin{align}
  \mathrm{KL}[\mu(Y)\|p(Y|\theta^{(t)})] - \mathrm{KL}[\mu(Y)\|p(Y|\theta^{(t+1)})] &= \mathbb{E}_{\mu(Y)} \left[ \log p(Y|\theta^{(t+1)}) - \log p(Y|\theta^{(t)}) \right] \\
  &\geq \mathbb{E}_{\mu(Y)}\mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta^{(t+1)}) - \log p(Y,X|\theta^{(t)}) \right] \\
  & \geq 0 \quad \text{because $\theta^{(t+1)}$ maximizes the right hand side.}
\end{align}
$$

# EM for Gaussian distributions
If we can iteratively update $\theta^{(t)}$ to $\theta^{(t+1)}$ by setting $\theta^{(t+1)} = \arg \max_{\theta} \mathbb{E}_{p(X|Y,\theta^{(t)})} \left[ \log p(Y,X|\theta) \right]$, then we can maximize the log likelihood of the data under the model.  So now we'll look at how to do this for Gaussian distributions.

# EM for SDE based SSMs
Now that we know how EM works, we can apply it to our SDE based SSM.  In order to use EM, we need to be able to do two things.  We need to be able to compute likelihoods with respect to the posterior distribution $p(X|Y,\theta^{(t)})$ (this is called the E-step) and then we need to be able to maximize the expected log likelihood with respect to the parameters (this is called the M-step).

# E-step
Since our model for $p(X,Y|\theta)$ is an exponential family, we can perform the E-step analytically.

# M-step
To perform the M-step, we need to write out the expected joint distribution and then take the gradient with respect to the parameters.  From our model, we have the following expression for the joint distribution:
$$
\begin{align}
  \log p(X,Y|\theta) &= \log p(x_1,y_1|\theta) + \sum_{k=1}^{N-1} \log p(x_{k+1}|x_k,\theta) + \sum_{k=1}^N \log p(y_k|x_k,\theta) \\
  &= \log N(x_1|\mu_1,P_1) + \sum_{k=1}^{N-1} \log N(x_{k+1}|A_k x_k,\Sigma_k) + \sum_{k=1}^N \log N(y_k|H_k x_k + u_k,R_k)
\end{align}
$$

We'll go over the optimal parameters for each term separately.

## Prior
The expression (that depends on the parameters) of the prior is given by
$$
\begin{align}
  \log N(x_1|\mu_1,P_1) &= -\frac{1}{2}(x_1-\mu_1)^T P_1^{-1} (x_1-\mu_1) - \frac{1}{2} \log|P_1|
\end{align}
$$
Next we'll take the gradient with respect to the parameters (we'll take the gradient with respect to the inverse covariance matrix beacuse the math is easier):
$$
\begin{align}
  \nabla_{\mu_1} \mathbb{E}_{X,Y}[\log N(x_1|\mu_1,P_1)] &= P_1^{-1} (\mathbb{E}_{X}[x_1]-\mu_1) \\
  \nabla_{P_1^{-1}} \mathbb{E}_{X,Y}[\log N(x_1|\mu_1,P_1)] &= -\frac{1}{2} \mathbb{E}_{X}[(x_1-\mu_1)(x_1-\mu_1)^T] + \frac{1}{2} P_1 \\
  &= \frac{1}{2}\left[P_1 - \left(\mathbb{E}_{X}[x_1x_1^T] - \mathbb{E}_{X}[x_1]\mu_1^T - \mu_1\mathbb{E}_{X}[x_1^T] + \mu_1\mu_1^T\right)\right]
\end{align}
$$
With these gradients, we can wrap the terms in an expectation and then see when the gradient is zero to get the optimal parameters.
$$
\begin{align}
  \mu_1^{(t+1)} &= \mathbb{E}_{X}[x_1] \\
  P_1^{(t+1)} &= \mathbb{E}_{X}[x_1x_1^T] - \mathbb{E}_{X}[x_1]{\mu_1^{(t+1)}}^T - {\mu_1^{(t+1)}}\mathbb{E}_{X|\theta^{(t)}}[x_1^T] + {\mu_1^{(t+1)}}{\mu_1^{(t+1)}}^T \\
  &= \mathbb{E}_{X}[x_1x_1^T] - \mathbb{E}_{X}[x_1]\mathbb{E}_{X}[x_1]^T
\end{align}
$$

## Emissions
Next we'll look at the emission parameters.  The log likelihood of the emissions is given by
$$
\begin{align}
  \sum_{k=1}^N \log N(y_k|H_k x_k + u_k,R_k) &= \sum_{k=1}^N \left[-\frac{1}{2}(y_k-H_k x_k - u_k)^T R_k^{-1} (y_k-H_k x_k - u_k) - \frac{1}{2} \log|R_k|\right]
\end{align}
$$
To make this expression easier to work with, we will augment the latent variables with an extra dimension so that we can group the input term together with the transition matrix.  Let $W$ be the matrix that contains the input term and the transition matrix:
$$
\begin{align}
  W_k = \begin{bmatrix}&|\\H_k & u_k \\&|\end{bmatrix}, \quad \hat{x}_k = \begin{bmatrix}x_k \\ 1\end{bmatrix}
\end{align}
$$
Then we can rewrite the expression as
$$
\begin{align}
  \sum_{k=1}^N \log N(y_k|H_k x_k + u_k,R_k) &= \sum_{k=1}^N \left[-\frac{1}{2}(y_k-W_k \hat{x}_k)^T R_k^{-1} (y_k-W_k \hat{x}_k) - \frac{1}{2} \log|R_k|\right]
\end{align}
$$

Now we can take the gradient with respect to the parameters.  First, the gradient with respect to $W_k$:
$$
\begin{align}
  \nabla_{W_k} \mathbb{E}_{X,Y}[\log N(y_k \mid W_k \hat{x}_k, R_k)] &= \mathbb{E}_{X,Y}[R_k^{-1} (y_k - W_k \hat{x}_k) \hat{x}_k^T]
\end{align}
$$
Solving for $W_k$ gives
$$
\begin{align}
  \implies W_k &= \left( \mathbb{E}_{X,Y}[y_k \hat{x}_k^T]\right) \left( \mathbb{E}_{X}[\hat{x}_k \hat{x}_k^T] \right)^{-1}
\end{align}
$$
The optimal $H_k$ and $u_k$ are then found by looking in the columns of $W_k$.



Next $R_k$:
$$
\begin{align}
  &\nabla_{R_k^{-1}} \mathbb{E}_{X,Y}[\log N(y_k|W_k \hat{x}_k,R_k)] =  -\frac{1}{2}\mathbb{E}_{X,Y}[(y_k-W_k \hat{x}_k)(y_k-W_k \hat{x}_k)^T] + \frac{1}{2} R_k
\end{align}
$$

Expanding terms and solving for $R_k$ gives

$$
\begin{align}
\implies R_k &= \mathbb{E}_{X,Y}[y_k y_k^T] - \mathbb{E}_{X,Y}[y_k \hat{x}_k^T] W_k^T - W_k \mathbb{E}_{X,Y}[\hat{x}_k y_k^T] + W_k \mathbb{E}_{X,Y}[\hat{x}_k \hat{x}_k^T] W_k^T
\end{align}
$$


## Transitions
Finally, we'll derive the optimal transition parameters.  This is basically the same derivation as the one for the emissions, except that we need to keep in mind that the parameters of the transition distributions are shared across time.

The log likelihood of the transitions is given by
$$
\begin{align}
  \sum_{k=1}^{N-1} \log N(x_k|A x_{k-1},\Sigma) &= \sum_{k=1}^{N-1} \left[-\frac{1}{2}(x_k-A x_{k-1})^T \Sigma^{-1} (x_k-A x_{k-1}) - \frac{1}{2} \log|\Sigma|\right] \\
  &= \sum_{k=1}^{N-1} \left[-\frac{1}{2}(x_k-A x_{k-1})^T \Sigma^{-1} (x_k-A x_{k-1})\right] - \frac{N-1}{2} \log|\Sigma|
\end{align}
$$
It is important to note that the constant term $N$ here is due to $0$ indexing!  If we did not use $0$ indexing into the sequence, then we would have $N-1$ terms in the sum!

First we'll take the gradient with respect to $\Sigma^{-1}$.
$$
\begin{align}
  \nabla_{\Sigma^{-1}} \mathbb{E}_{X,Y}[\log N(x_k|A x_{k-1},\Sigma)] &= -\frac{1}{2}\mathbb{E}_{X,Y}[\sum_{k=1}^{N-1} (x_k-A x_{k-1})(x_k-A x_{k-1})^T] + \frac{N-1}{2}\Sigma \\
\end{align}
$$
Setting this equal to zero and solving for $\Sigma$ gives
$$
\begin{align}
  \Sigma &= \frac{1}{N-1} \mathbb{E}_{X,Y}[\sum_{k=1}^{N-1} (x_k-A x_{k-1})(x_k-A x_{k-1})^T] \\
  &= \frac{1}{N-1} \sum_{k=1}^{N-1} \left( \mathbb{E}_{X}[x_k x_k^T] - \mathbb{E}_{X}[x_k x_{k-1}^T]\,A^T - A\,\mathbb{E}_{X}[x_{k-1} x_k^T] + A\,\mathbb{E}_{X}[x_{k-1} x_{k-1}^T]\,A^T \right)
\end{align}
$$

The last term we need to solve for is $A$:
$$
\begin{align}
  \nabla_{A} \mathbb{E}_{X,Y}[\log N(x_k|A x_{k-1},\Sigma)] &= \mathbb{E}_{X,Y}[\sum_{k=1}^{N-1} \Sigma^{-1} (x_k-A x_{k-1}) x_{k-1}^T]
\end{align}
$$
Solving for $A$ gives
$$
\begin{align}
  \implies A &= \left( \sum_{k=1}^{N-1} \mathbb{E}_{X}[x_k x_{k-1}^T] \right) \left( \sum_{k=1}^{N-1} \mathbb{E}_{X}[x_{k-1} x_{k-1}^T] \right)^{-1}
\end{align}
$$

## Optimal SDE parameters
Now that we have the M-step updates for the parameters of the linear dynamical system, we can use the optimal parameters to compute the optimal SDE parameters.  Recall that the SDE parameters are related to the transition parameters by
$$
\begin{align}
  \begin{bmatrix}A & \Sigma A^{-T} \\ 0 & A^{-T} \end{bmatrix} = \exp\{\begin{bmatrix}F & LL^T \\ 0 & -F^T \end{bmatrix}s\}
\end{align}
$$
We can solve for $F$ and $L$ by taking the matrix logarithm of the LHS and dividing by $s$.  This gives
$$
\begin{align}
  \begin{bmatrix}F & LL^T \\ 0 & -F^T \end{bmatrix} = \frac{1}{s}\log \begin{bmatrix}A & \Sigma A^{-T} \\ 0 & A^{-T} \end{bmatrix}
\end{align}
$$
