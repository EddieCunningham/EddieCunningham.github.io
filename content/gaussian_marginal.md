Title: Multivariate Gaussian product marginal
Date: 2024-02-19
Category: Blog
Slug: gaussian-product
hidden: true
Summary: Multivariate Gaussian product marginal

Suppose we want to evaluate the integral
$$
\begin{align}
\int N(x|\mu,\Sigma)N(y|Ax + b,\Lambda)dx
\end{align}
$$
The solution is
$$
\begin{align}
    p(y) &= N^{-1}(y|J_y,h_y) \\
    &= N(y|\mu_y,\Sigma_y) \\
    &\text{where} \\
    \mu_y &= A\mu + b \\
    \Sigma_y &= \Lambda + A\Sigma A^T \\
    &\text{or} \\
    J_y &= (\Lambda + A\Sigma A^T)^{-1} \\
    h_y &= J_y(A\mu + b)
\end{align}
$$
## Information form of a Gaussian
The easiest way to manipulate equations with Gaussian pdfs is to use the information form of the Gaussian.  The information form is given by
$$
\begin{align}
  N^{-1}(x|J,h) := N(x|\mu,\Sigma)
\end{align}
$$
where $J=\Sigma^{-1}$, $\Sigma=J^{-1}$,  $h=\Sigma^{-1}\mu$ and $\mu=J^{-1}h$.  Written out, we get that
$$
\begin{equation}
    N^{-1}(x|J,h)=\exp\{-\frac{1}{2}x^TJx + x^Th - \log Z\}
\end{equation}
$$
where $\log Z$ is the log partition function
$$
\begin{align}
    \log Z=\frac{1}{2}\mu^T\Sigma^{-1}\mu + \frac{1}{2}\log|\Sigma| + \frac{\dim(x)}{2}\log(2\pi) \\
    = \frac{1}{2}h^TJ^{-1}h - \frac{1}{2}\log|J| + \frac{\dim(x)}{2}\log(2\pi)
\end{align}
$$


This form is particularly nice because the product of Gaussians can be evaluated easily:

$$
\begin{align}
    N^{-1}(x|J_1,h_1)N^{-1}(x|J_2,h_2)\nonumber=N^{-1}(x|J_1+J_2,h_1+h_2)
\end{align}
$$
Furthermore, we get the identity:
$$
\begin{align}
    \int \exp\{-\tfrac{1}{2}x^TJx + x^Th\}dx = \exp\{\log Z\}
\end{align}
$$

## Marginal distribution
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
    \log Z_x = \log Z - \frac{1}{2}h_1^T J_{11}^{-1}h_1 + \frac{1}{2}\log|J_{11}| - \frac{\text{dim}(x)}{2}\log(2\pi)
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
    \log Z_y = \log Z - \frac{1}{2}h_2^T J_{22}^{-1}h_2 + \frac{1}{2}\log|J_{22}| + \frac{\text{dim}(x)}{2}\log(2\pi)
\end{align}
$$

## Conditional distribution
If we want to find the conditional distribution of $x$ given $y$, we can start by first expanding out all of the terms in the joint distribution:
$$
\begin{align}
    &N^{-1}(\begin{bmatrix}y\\x\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_1\\h_2\end{bmatrix},\log Z) \\
    &= \exp\{-\frac{1}{2}(y^TJ_{11} y + y^TJ_{12}x + x^TJ_{12}^Ty + x^TJ_{22}x) + y^Th_1 + x^Th_2 - \log Z\} \\
    &= \exp\{-\frac{1}{2}y^T\underbrace{J_{11}}_{J_y}y + y^T\underbrace{(h_1 - J_{12}x)}_{h_y} - \underbrace{\left(\log Z + \frac{1}{2}x^TJ_{22}x - x^T h_2\right)}_{\log Z_y}\} \\
    &= \exp\{-\frac{1}{2}x^T\underbrace{J_{22}}_{J_x}x + x^T\underbrace{(h_2 - J_{21}y)}_{h_x} - \underbrace{\left(\log Z + \frac{1}{2}y^TJ_{11}y - y^T h_1\right)}_{\log Z_x}\}
\end{align}
$$
So we have that the conditional distributions are:
$$
\begin{align}
    p(x|y) &= N^{-1}(x|J_x,h_x,\log Z_x) \\
    p(y|x) &= N^{-1}(y|J_y,h_y,\log Z_y)
\end{align}
$$

## Marginalize product of Gaussians
Now back to the original problem.  Suppose that we want to evaluate
$$
\begin{align}
\int N(y|Ax + b,\Lambda)N(x|\mu,\Sigma)dx
\end{align}
$$
Step one is to write the information form of the Gaussians:
$$
\begin{align}
    N(x|\mu,\Sigma) &= N^{-1}(x|J=\Sigma^{-1},h=\Sigma^{-1}\mu) \\
    &\propto \exp\{-\frac{1}{2}x^T\Sigma^{-1}x + x^T\Sigma^{-1}\mu\} \\
    N(y|Ax + b,\Lambda) &= N^{-1}(y|J=\Lambda^{-1},h=\Lambda^{-1}(Ax+b)) \\
    &\propto \exp\{-\frac{1}{2}y^T\Lambda^{-1}y + y^T\Lambda^{-1}(Ax+b)\} \\
    &= \exp\{-\frac{1}{2}y^T\Lambda^{-1}y + y^T\Lambda^{-1}Ax + y^T\Lambda^{-1}b\}
\end{align}
$$
Next, we can write the joint density of $x$ and $y$ in information form:
$$
\begin{align}
  p(\begin{bmatrix}y \\ x\end{bmatrix}) &= N^{-1}(\begin{bmatrix}y\\x\end{bmatrix}|\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}, \begin{bmatrix}h_1\\h_2\end{bmatrix}) \\
  &\propto \exp\{-\frac{1}{2}\begin{bmatrix}y\\x\end{bmatrix}^T\begin{bmatrix}J_{11} & J_{12} \\ J_{12}^T & J_{22}\end{bmatrix}\begin{bmatrix}y\\x\end{bmatrix} + \begin{bmatrix}y\\x\end{bmatrix}^T\begin{bmatrix}h_1\\h_2\end{bmatrix}\} \\
  &=\exp\{-\frac{1}{2}\begin{bmatrix}y\\x\end{bmatrix}^T\begin{bmatrix}\Lambda^{-1} & -\Lambda^{-1}A \\ -A^T\Lambda^{-1} & \Sigma^{-1} + A^T\Lambda^{-1}A\end{bmatrix}\begin{bmatrix}y\\x\end{bmatrix} + \begin{bmatrix}y\\x\end{bmatrix}^T\begin{bmatrix}\Lambda^{-1}b \\ \Sigma^{-1}\mu - A^T\Lambda^{-1}b \end{bmatrix}\} \\
\end{align}
$$
Next we can integrate out $x$ using the expression from before:
$$
\begin{align}
    p(y) &= N^{-1}(y|J_y,h_y) \\
    &\text{where} \\
    J_y &= J_{11}-J_{12}J_{22}^{-1}J_{12}^T \\
    &= (\Lambda + A\Sigma A^T)^{-1} \\
    h_y &= h_1 - J_{12}J_{22}^{-1}h_2 \\
    &= J_y(A\mu + b)
\end{align}
$$
Converting back into the standard form of the Gaussian, we get
$$
\begin{align}
    p(y) &= N(y|\mu_y,\Sigma_y) \\
    &\text{where} \\
    \Sigma_y &= \Lambda + A\Sigma A^T \\
    \mu_y &= A\mu + b
\end{align}
$$
