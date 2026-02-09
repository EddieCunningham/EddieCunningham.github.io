Title: Linear gaussian state space models
Date: 2024-05-20
Category: Blog
Slug: lgssm
hidden: true
Summary: Linear Gaussian state space models

# Background
Assume we have a chain structured graph where observations $y_{1:T}$ are known and latent variables $x_{1:T}$ are unknown.  We can factor the joint distribution as:

$$
\begin{align}
    p(x_{1:T}, y_{1:T})=p(x_1)\prod_{t=1}^{T-1}p(x_{t+1}|x_t)\prod_{t=1}^{T}p(y_{t}|x_t)
\end{align}
$$

We will use Gaussians with inputs $u_{1:T}$ to model each of the conditional probability distributions:

$$
\begin{align}
    p(x_1)=N(x_1|\mu_0, \Sigma_0) \\
    p(x_{t+1}|x_t)=N(x_{t+1}|Ax_{t} + u_t, \Sigma) \\
    p(y_t|x_t)=N(y_t|Cx_t, R)
\end{align}
$$

## Information Form

We will be using the information form of Gaussians.  This is represented by:
$$
\begin{align}
    N(x|\mu,\Sigma)=N^{-1}(x|J,h)
\end{align}
$$
where $J=\Sigma^{-1}$, $\Sigma=J^{-1}$,  $h=\Sigma^{-1}\mu$ and $\mu=J^{-1}h$.  Written out, we get that
$$
\begin{align}
    N^{-1}(x|J,h)=\exp\{-\frac{1}{2}x^TJx + x^Th - \log Z\}
\end{align}
$$
where $\log Z$ is the log partition function.  The algorithm will compute Gaussian factors that will not necessarily normalize to 1, so we will make the dependence on $\log Z$ explicit using
$$
\begin{align}
    N^{-1}(x|J,h,\log Z)
\end{align}
$$
It is also true that
$$
\begin{align}
    \log Z=\frac{1}{2}\mu^T\Sigma^{-1}\mu + \frac{1}{2}\log|\Sigma| + \frac{\dim(x)}{2}\log(2\pi) \\
    = \frac{1}{2}h^TJ^{-1}h - \frac{1}{2}\log|J| + \frac{\dim(x)}{2}\log(2\pi)
\end{align}
$$

This form is particularly nice because the product of Gaussians can be evaluated easily:

$$
\begin{align}
    N^{-1}(x|J_1,h_1,\log Z_1)N^{-1}(x|J_2,h_2,\log Z_2)\nonumber\\=N^{-1}(x|J_1+J_2,h_1+h_2,\log Z_1+\log Z_2)
\end{align}
$$
Furthermore, we get the identity:
$$
\begin{align}
    \int \exp\{x^TJx + x^Th\}dx = \exp\{\log Z\}
\end{align}
$$

When we have a joint distribution over variables $x$ and $y$, we can marginalize over either variable using the equations:
$$
\begin{align}
    p(x) = \int N^{-1}(\begin{bmatrix}y\\x\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_1\\h_2\end{bmatrix},\log Z)dy \\
    = N^{-1}(x|J_x,h_x,\log Z_x)
\end{align}
$$
where
$$
\begin{align}
    J_x=J_{22}-J_{12}^TJ_{11}^{-1}J_{12}\\
    h_x=h_2 - J_{12}^TJ_{11}^{-1}h_1\\
    \log Z_x = \log Z - \frac{1}{2}h_1^T J_{11}^{-1}h_1 + \frac{1}{2}|J_{11}| - \frac{\text{dim}(x)}{2}\log(2\pi)
\end{align}
$$

Similarly, if we integrate over $x$, we get

$$
\begin{align}
    p(y)=N^{-1}(y|J_y,h_y,\log Z_y)
\end{align}
$$

$$
\begin{align}
    J_y=J_{11}-J_{12}J_{22}^{-1}J_{12}^T\\
    h_y=h_1 - J_{12}J_{22}^{-1}h_2\\
    \log Z_y = \log Z - \frac{1}{2}h_2^T J_{22}^{-1}h_2 + \frac{1}{2}|J_{22}| + \frac{\text{dim}(x)}{2}\log(2\pi)
\end{align}
$$

(See info form paper for details)

## Information Form of Joint Distribution
The information form of $p(x_1), p(x_{t+1}|x_t)\text{ and }p(y_t|x_t)$ can be written as follows:

### $p(x_1)$
$$
\begin{align}
    p(x_1)=N^{-1}(x_1|J_0,h_0,\log Z_0)
\end{align}
$$
where
$$
\begin{align}
    J_0=\Sigma_0^{-1}\\
    h_0=\Sigma_0^{-1}\mu_0 \\
    \log Z_0=\frac{1}{2}\mu_0^T\Sigma_0^{-1}\mu_0 + \frac{1}{2}|\Sigma_0| + \frac{1}{2}\log(2\pi)
\end{align}
$$

## $p(x_{t+1}|x_t)$
$$
\begin{align}
    p(x_{t+1}|x_t) = N^{-1}(\begin{bmatrix}x_{t+1}\\x_t\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_{1_{u_t}}\\h_{2_{u_t}}\end{bmatrix},\log Z_{u_t})
\end{align}
$$
where
$$
\begin{align}
    J_{11}=\Sigma^{-1}\\
    J_{12}=-\Sigma^{-1}A\\
    J_{22}=A^T\Sigma^{-1}A\\
    h_{1_{u_t}}=\Sigma^{-1}u_{t}\\
    h_{2_{u_t}}=-A^T\Sigma^{-1}u_{t}\\
    \log Z_{u_t} = \frac{1}{2}u_t^T\Sigma^{-1}u_t+\frac{1}{2}\log|\Sigma|+\frac{1}{2}\log(2\pi)
\end{align}
$$

### $p(y_t|x_t)$
$$
\begin{align}
    p(y_t|x_t) = N^{-1}(x_t|J_{y_t},h_{y_t},\log Z_{y_t})
\end{align}
$$
where
$$
\begin{align}
    J_{y_t}=C^TR^{-1}C\\
    h_{y_t}=C^TR^{-1}y_t \\
    \log Z_{y_t}= \frac{1}{2}y_tR^{-1}y_t + \frac{1}{2}|R| + \frac{1}{2}\log(2\pi)
\end{align}
$$


# Problem
The goal will be to calculate $p(y_{1:T})$.  This can be done with log partition function of the smoothed probabilities

$$
\begin{align}
    p(x_t,y_{1:T})=p(x_t,y_{1:t})p(y_{t+1:T}|x_t)
\end{align}
$$

$p(x_t,y_{1:t})$ and $p(y_{t+1:T}|x_t)$ can each be calculated using the message passing algorithms described below.

# Forward Messages $p(x_t,y_{1:t})$

The forward messages, $p(x_t,y_{1:t})$, are going to take the form:
$$
\begin{align}
    p(x_t,y_{1:t}) = N^{-1}(x_t|J_{t|t}^f,h_{t|t}^f,\log Z_{t|t}^f)
\end{align}
$$

### Base Case $p(x_1,y_1)$
The base case is
$$
\begin{align}
    p(x_1,y_1)=N^{-1}(x_1|J_{1|1}^f,h_{1|1}^f,\log Z_{1|1}^f)
\end{align}
$$
where
$$
\begin{align}
    J_{1|1}^f=J_0+J_{y_1}\\
    h_{1|1}^f=h_0+h_{y_1}\\
    \log Z_{1|1}^f=\log Z_0+\log Z_{y_1}
\end{align}
$$

### General Case $p(x_t,y_{1:t})$
The recursions can be calculated using the relationship:

$$
\begin{align}
    p(x_{t+1},y_{1:t+1})=N^{-1}(x_{t+1}|J_{t+1|t+1}^f,h_{t+1|t+1}^f,\log Z_{t+1|t+1}^f) \\
    =p(y_{t+1}|x_{t+1})\int p(x_{t+1}|x_t)p(x_t,y_{1:t})dx_t \\
    =N^{-1}(x_{t+1}|J_{y_{t+1}},h_{y_{t+1}},\log Z_{y_{t+1}}) \nonumber \\\int N^{-1}(\begin{bmatrix}x_{t+1}\\x_t\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_{1_{u_t}}\\h_{2_{u_t}}\end{bmatrix},\log Z_{u_t})N^{-1}(x_{t}|J_{t|t}^f,h_{t|t}^f,\log Z_{t|t}^f)dx_t
\end{align}
$$

Using the properties of the information form of Gaussians, we get
$$
\begin{align}
    J_{t+1|t+1}^f = J_{t+1|t}^f + J_{y_{t+1}} \\
    h_{t+1|t+1}^f = h_{t+1|t}^f + h_{y_{t+1}} \\
    \log Z_{t+1|t+1}^f = \log Z_{t+1|t}^f + \log Z_{y_{t+1}} \\
\end{align}
$$
$$
\begin{align}
    \hat{J}_{22} = J_{22} + J_{t|t}^f \\
    \hat{h}_2 = h_{2_{u_t}} + h_{t|t}^f \\
    J_{t+1|t}^f=J_{11}-J_{12}\hat{J}_{22}^{-1}J_{12}^T\\
    h_{t+1|t}^f=h_{1_{u_t}} - J_{12}\hat{J}_{22}^{-1}\hat{h}_2\\
    \log Z_{t+1|t}^f = \log Z - \frac{1}{2}\hat{h}_2^T \hat{J}_{22}^{-1}\hat{h}_2 + \frac{1}{2}|\hat{J}_{22}| + \frac{\text{dim}(x)}{2}\log(2\pi)
\end{align}
$$

# Backward Messages $p(y_{t+1:T}|x_t)$

The backward messages, $p(y_{t+1:T}|x_t)$, are going to take the form:
$$
\begin{align}
    p(y_{t+1:T}|x_t) = N^{-1}(x_t|J_{t|t}^b,h_{t|t}^b,\log Z_{t|t}^b)
\end{align}
$$

### Base Case
The base case just sets the distribution to 0 ($y_{T+1}$ does not exist).

### General Case $p(y_{t+1:T}|x_t)$
The recursions can be calculated using the relationship:

$$
\begin{align}
    p(y_{t+1:T}|x_t) = \int p(y_{t+1}|x_{t+1})p(x_{t+1}|x_{t})p(y_{t+2:T}|x_{t+1})dx_{t+1} \\
    \int N^{-1}(x_{t+1}|J_{y_{t+1}},h_{y_{t+1}},\log Z_{y_{t+1}}) \nonumber \\ N^{-1}(\begin{bmatrix}x_{t+1}\\x_t\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_{1_{u_t}}\\h_{2_{u_t}}\end{bmatrix},\log Z_{u_t})N^{-1}(x_{t+1}|J_{t+1|t+1}^b,h_{t+1|t+1}^b,\log Z_{t+1|t+1}^b)dx_{t+1}
\end{align}
$$

Using the properties of the information form of Gaussians, we get
$$
\begin{align}
    \hat{J}_{11} = J_{y_{t+1}} + J_{11} + J_{t+1|t+1}^b \\
    \hat{h}_1 = h_{y_{t+1}} + h_{1_{u_t}} + h_{t+1|t+1}^b \\
    J_{t|t}^b=J_{22}-J_{12}^T\hat{J}_{11}^{-1}J_{12}\\
    h_{t|t}^b=h_2 - J_{12}^TJ_{11}^{-1}\hat{h}_1\\
    \log Z_{t|t}^b = \log Z - \frac{1}{2}\hat{h}_1^T \hat{J}_{11}^{-1}\hat{h}_1 + \frac{1}{2}|\hat{J}_{11}| - \frac{\text{dim}(x)}{2}\log(2\pi)
\end{align}
$$

# Smoothed Messages $p(x_t|y_{1:T})$
Once we have the forward and backward messages, we can easily compute the smoothed messages as follows:

$$
\begin{align}
    p(x_t,y_{1:T})=p(x_t,y_{1:t})p(y_{t+1:T}|x_t) \\
    = N^{-1}(x_t|J_{t|t}^f + J_{t|t}^b, h_{t|t}^f + h_{t|t}^b, \log Z_{t|t}^f + \log Z_{t|t}^b) \\
    = N^{-1}(x_t|J_{t|t}^s, h_{t|t}^s, \log Z_{t|t}^s)
\end{align}
$$

To calculate $p(y_{1:T})$, we can take any smoothed message and integrate out $x_t$:

$$
\begin{align}
    \log p(y_{1:T}) = \log Z(J_{t|t}^s, h_{t|t}^s) - \log Z_{t|t}^s \\
    = \frac{1}{2}{h_{t|t}^s}^T{J_{t|t}^s}^{-1}h_{t|t}^s - \frac{1}{2}\log|J_{t|t}^s| + \frac{\dim(x)}{2}\log(2\pi) - \log Z_{t|t}^s
\end{align}
$$