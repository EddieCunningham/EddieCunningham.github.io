Title: Matrix inverse
Date: 2024-01-28
Category: Blog
Slug: matrix-inverse
hidden: true
Summary: Relationship between inverse matrix rows and matrix column pseudo-inverses

In this post we'll look at the relationship between the inverse of a matrix and the pseudo-inverse of its columns.  We'll derive relationships between the rows of $G=\begin{bmatrix} - & G_1^T  & - \\ - & G_2^T & - \end{bmatrix}$ and the pseudo-inverse of the columns of $J$, $J^+$.  We'll also look at the relationship between the rows of $G$ and the inverse of the matrix $J=\begin{bmatrix} | & | \\ J_1 & J_2 \\  | & | \end{bmatrix}$.  We'll do this by using identities for the inverse of a block matrix in order to write $G_1 = G_1(G_1^TJ_1 + G_2^TJ_2)$ because the derivation of $GG^T$ will be the easiest way to incorporate the pseudo inverses $J_1^+$ and $J_2^+$.

First, we can write $GG^T$ in block form as
$$
\begin{bmatrix}
G_1G_1^T & G_1G_2^T \\
G_2G_1^T & G_2G_2^T
\end{bmatrix} = (\begin{bmatrix}
  J_1^TJ_1 & J_1^TJ_2 \\
  J_2^TJ_1 & J_2^TJ_2
\end{bmatrix})^{-1}
$$
Then, we can use the following matrix inverse identity to simplify:
$$
\begin{bmatrix}
  A & B \\
  C & D
\end{bmatrix}^{-1} = \begin{bmatrix}
  (A-BD^{-1}C)^{-1} & -(A-BD^{-1}C)^{-1}BD^{-1} \\
  -(D-CA^{-1}B)^{-1}CA^{-1} & (D-CA^{-1}B)^{-1}
\end{bmatrix}
$$
### Top left
The top left block of $GG^T$ is:
$$
\begin{align}
(A-BD^{-1}C)^{-1} &= (J_1^TJ_1 - J_1^T\underbrace{J_2(J_2^TJ_2)^{-1}J_2^T}_{J_2^\parallel}J_1)^{-1} \\
&= (J_1^TJ_1 - J_1^T J_2^\parallel J_1)^{-1} \\
\end{align}
$$
Next, we can use the Woodbury identity, $(A+UV)^{-1} = A^{-1} - A^{-1}U(I + VA^{-1}U)^{-1}VA^{-1}$ with $A=J_1^TJ_1$, $U=-J_1^T$, and $V=J_2^\parallel J_1$ to get:
$$
\begin{align}
&= (J_1^TJ_1)^{-1} + (J_1^TJ_1)^{-1}J_1^T\left(I - J_2^\parallel J_1(J_1^T J_1)^{-1}J_1^T  \right)^{-1} J_2^\parallel J_1 (J_1^TJ_1)^{-1} \\
&= (J_1^TJ_1)^{-1} + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^{+^T}
\end{align}
$$
# Top right
The top right block of $GG^T$ is:
$$
\begin{align}
-(A-BD^{-1}C)^{-1}BD^{-1} &= \left((J_1^TJ_1)^{-1} + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^{+^T}\right)(J_1^TJ_2)(J_2^TJ_2)^{-1} \\
&= J_1^+J_2^{+^T} + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel J_2^{+^T} \\
&= J_1^+\left(I +\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel \right) J_2^{+^T} \\
\end{align}
$$
# Bottom left and bottom right
The bottom left and bottom right blocks of $GG^T$ can be obtained by switching the subscript 1 and 2 in the top left and top right blocks.  This gives us:
$$
\begin{align}
\begin{bmatrix}
G_1G_1^T & G_1G_2^T \\
G_2G_1^T & G_2G_2^T
\end{bmatrix} &= \begin{bmatrix}
(J_1^TJ_1)^{-1} + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^{+^T} & -J_1^+\left(I +\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel \right) J_2^{+^T} \\
-J_2^+\left(I +\left(I - J_1^\parallel J_2^\parallel  \right)^{-1} J_1^\parallel J_2^\parallel \right) J_1^{+^T} & (J_2^TJ_2)^{-1} + J_2^+\left(I - J_1^\parallel J_2^\parallel  \right)^{-1} J_1^\parallel J_2^{+^T}
\end{bmatrix}
\end{align}
$$

# Solving for $G$
Finally, we can solve for $G1$ and $G_2$ as $G_1 = G_1G_1^TJ_1 + G_1G_2^TJ_2$ and $G_2 = G_2(G_1^TJ_1 + G_2^TJ_2).

The first term is
$$
\begin{align}
G_1G_1^TJ_1 &= \left((J_1^TJ_1)^{-1} + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^{+^T}\right)J_1 \\
&= J_1^+ + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel
\end{align}
$$
next,
$$
\begin{align}
G_1G_2^TJ_2 &= -J_1^+\left(I +\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel \right) J_2^{+^T}J_2 \\
&= -\left(J_1^+ + J_1^+\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel J_1^\parallel \right)J_2^\parallel
\end{align}
$$
Putting these together, we get
$$
\begin{align}
G_1 &= J_1^+\left(I + \underbrace{\left(I - J_2^\parallel J_1^\parallel  \right)^{-1} J_2^\parallel}_{J_2^\parallel \left(I - J_1^\parallel J_2^\parallel  \right)^{-1}} J_1^\parallel\right)\underbrace{(I - J_2^\parallel)}_{J_2^\perp} \\
&= J_1^+\underbrace{\left(I + J_2^\parallel \left(I - J_1^\parallel J_2^\parallel  \right)^{-1} J_1^\parallel\right)}_{(I - J_2^\parallel J_1^\parallel)^{-1}}J_2^\perp \\
&= J_1^+\left(I - J_2^\parallel J_1^\parallel\right)^{-1}J_2^\perp
\end{align}
$$
and similarly,
$$
\begin{align}
G_2 &= J_2^+\left(I - J_1^\parallel J_2^\parallel\right)^{-1}J_1^\perp
\end{align}
$$


Interestingly, we also have that
$$
\begin{align}
I - \left(I - J_2^\parallel J_1^\parallel\right)^{-1}J_2^\perp  &= \left(I - J_1^\parallel J_2^\parallel\right)^{-1}J_1^\perp
\end{align}
$$

# Summary
We've shown that the rows of $G$ are related to the pseudo-inverses of the columns of $J$ as
$$
\begin{align}
G_1 &= J_1^+\Phi J_2^\perp  \\
G_2 &= J_2^+\Phi^T J_1^\perp  \\
\text{where }\Phi &= \left(I - J_2^\parallel J_1^\parallel\right)^{-1} \\
\text{ and }\Phi^T &= \left(I - J_1^\parallel J_2^\parallel\right)^{-1}
\end{align}
$$

Note that when $J_1^\parallel J_2^\parallel = 0$, then $\Phi = I$ and $G_1 = J_1^+$ and $G_2 = J_2^+$ because $J_2^\perp = J_1^\parallel$ and $J_1^\perp = J_2^\parallel$.

Also because $J_1G_1 + J_2G_2 = I$, we have the identity:
$$
\begin{align}
\Phi J_2^\perp + \Phi^T J_1^\perp &= I \\
\end{align}
$$
and also
$$
\begin{align}
\Phi J_2^\parallel &= J_2^\parallel\Phi^T \\
\Phi^T J_1^\parallel &= J_1^\parallel\Phi
\end{align}
$$
An identity with $\Phi$ is that
$$
\begin{align}
  \Phi J_2^\perp J_1 &= J_1 \\
  \Phi^T J_1^\perp J_2 &= J_2
\end{align}
$$

# Dual formulation
We can also do everything in terms of the inverse matrix:
$$
\begin{align}
  J_1 &= G_2^\perp \hat{\Phi}G_1^+ \\
  J_2 &= G_1^\perp \hat{\Phi}^TG_2^+ \\
  \text{where }\hat{\Phi}^T &= \left(I - G_2^\parallel G_1^\parallel\right)^{-1} \\
  \text{and }\hat{\Phi} &= \left(I - G_1^\parallel G_2^\parallel\right)^{-1}
\end{align}
$$

Furthermore
$$
\begin{align}
  G_2^\perp \hat{\Phi} + G_1^\perp \hat{\Phi}^T &= I \\
\end{align}
$$
and also
$$
\begin{align}
\hat{\Phi}^T G_2^\parallel &= G_2^\parallel\hat{\Phi} \\
\hat{\Phi} G_1^\parallel &= G_1^\parallel\hat{\Phi}^T
\end{align}
$$

# Relationship between matrices
There is the following relationship between $\Phi$ and $\hat{\Phi}$.  Suppose the singular value decomposition of $\Phi$ is
$$
\begin{align}
  \Phi &= U\text{diag}(s_1,s_2)V^T
\end{align}
$$
Then the singular value decomposition of $\hat{\Phi}$ is
$$
\begin{align}
  \hat{\Phi} &= U\text{diag}(s_2,s_1)V^T
\end{align}
$$

# Other relationships
$$
\begin{align}
  \log \det \Phi &= \log \det J_1^TJ_1 + \log \det G_1G_1^T \\
  &= \log \det J_2^TJ_2 + \log \det G_2G_2^T
\end{align}
$$

