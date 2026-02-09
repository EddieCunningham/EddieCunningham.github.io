Title: Lie bracket
Date: 2025-09-07
Category: Blog
Slug: lie-bracket
hidden: true
Summary: Properties of Lie brackets

In this post we will look at the stationary properties of the Lie bracket.  The lie bracket for vector fields measures how two vector fields commute.  Two vector fields $X$ and $Y$ commute if their Lie bracket is zero. An important consequence of this is that when $[X, Y] = 0$, $X$ and $Y$ are coordinate vectors in some coordinate system.  This is useful for when we want to learn coordinates for a manifold, because we can introduce the Lie bracket as a constraint that we can add on to our optimization problem using Lagrange multipliers.

# Preliminaries

Let $X$ and $Y$ be vector fields on a manifold $\mathcal{M}$.  We can write $X$ and $Y$ in terms of a coordinate system $(x^1, \dots, x^n)$ as:
$$
\begin{align}
  X = X^i \partial_i \\
  Y = Y^i \partial_i
\end{align}
$$
where $\partial_i$ is the coordinate basis vector field.  Then the Lie bracket of $X$ and $Y$ is given by
$$
\begin{align}
  [X,Y] &= \left(X^i \partial_i(Y^j) - Y^i \partial_i(X^j)\right) \partial_j \\
  &= \left(\nabla Y X - \nabla X Y\right)^j \partial_j
\end{align}
$$
We can see that this this expression vanishes when $X$ and $Y$ are coordinate vectors because suppose $X = \frac{\partial}{\partial z^1} = \frac{\partial x^i}{\partial z^1} \frac{\partial}{\partial x^i}$ and $Y = \frac{\partial}{\partial z^2} = \frac{\partial x^i}{\partial z^2} \frac{\partial}{\partial x^i}$.  Then:
$$
\begin{align}
  [X,Y] &= \left(X^i \partial_i(Y^j) - Y^i \partial_i(X^j)\right) \partial_j \\
  &= \left(\frac{\partial x^i}{\partial z^1}\frac{\partial^2 x^j}{\partial x^i \partial z^2} - \frac{\partial x^i}{\partial z^2}\frac{\partial^2 x^j}{\partial x^i \partial z^1}\right) \frac{\partial}{\partial x^j} \\
  &= \left(\frac{\partial^2 x^j}{\partial z^1 \partial z^2} - \frac{\partial^2 x^j}{\partial z^2 \partial z^1}\right) \frac{\partial}{\partial x^j} \\
  &= 0
\end{align}
$$

In practice, we might be interested in solving an optimization problem with the constraint that $X$ and $Y$ are coordinate vectors in some coordinate system.  For example, suppose we want to a minimum length coordinate system.  The length of a coordinate curve is given as the integral of the norm of the velocity vector along the coordinate curve:
$$
\begin{align}
  L = \int_0^1 \| \dot{x} \|^2 dt, \quad \text{where } \dot{x} = X
\end{align}
$$
Without any extra assumptions, $L$ is clearly minimized when $X$ is zero.  However, if we add the constraint that $X$ and $Y$ are coordinate vectors in some coordinate system, then we can get a non-trivial solution.  We will discuss how to incorporate the Lie bracket constraint into the optimization problem in the next section.


## Lagrange multiplier formulation
Let $(E_1,\dots,E_n)$ be a frame on $\mathbb{R}^n$.  In order to assert that $(E_1,\dots,E_n)$ is a coordinate frame, we need to assert that the Lie bracket of any two vectors in the frame is zero:
$$
\begin{align}
  [E_i,E_j] = 0, \quad \text{for all } i,j
\end{align}
$$
To work out the details of this constraint, lets start by just considering the first two vectors in the frame and introducing a Lagrange multiplier $\lambda = \lambda^i E_i$ to enforce the constraint.  Additionally, let $\rho$ be a density function on the manifold.  The constraint is then:
$$
\begin{align}
  \int \rho\left\langle \lambda, [E_1,E_2] \right\rangle dV &= \int \rho \lambda^j \left(E_1^i \partial_i(E_2^j) - E_2^i \partial_i(E_1^j)\right) dV \\
  &= \int \rho \langle \nabla E_2 E_1 - \nabla E_1 E_2, \lambda \rangle dV
\end{align}
$$
Now, suppose that $E_1$ and $E_2$ depend on the scalar parameter $\theta$.  Then we can take a derivative of the expression with respect to $\theta$ to get:
$$
\begin{align}
  \frac{\partial}{\partial\theta} \int \rho\left\langle \lambda, [E_1,E_2] \right\rangle dV &= \int \rho \langle \nabla \frac{\partial E_2}{\partial \theta} E_1 + \nabla E_2 \frac{\partial E_1}{\partial \theta} - \nabla \frac{\partial E_1}{\partial \theta} E_2 - \nabla E_1 \frac{\partial E_2}{\partial \theta}, \lambda \rangle dV \\
  &= \int \rho \langle \left( \nabla \frac{\partial E_2}{\partial \theta} E_1 - \nabla E_1 \frac{\partial E_2}{\partial \theta} \right) - \left(\nabla \frac{\partial E_1}{\partial \theta} E_2 - \nabla E_2 \frac{\partial E_1}{\partial \theta} \right), \lambda \rangle dV
\end{align}
$$
We can simplify this expression by using integration by parts so that we only have first order derivatives of the frame vectors.  To do this, we can use the following identity:
$$
\begin{align}
  \int\; \rho\langle \nabla \frac{\partial E_2}{\partial \theta} E_1, \lambda \rangle \;dV &= \int\; \langle \rho E_1, \nabla \frac{\partial E_2}{\partial \theta} ^T \lambda \rangle \;dV \\
  &= \int\; \langle \rho E_1, \nabla \langle \frac{\partial E_2}{\partial \theta}, \lambda \rangle - \nabla \lambda^T \frac{\partial E_2}{\partial \theta} \rangle \;dV \\
  &= \int\; -\text{Div}(\rho E_1)\langle \frac{\partial E_2}{\partial \theta}, \lambda \rangle - \langle \rho E_1, \nabla \lambda^T \frac{\partial E_2}{\partial \theta} \rangle \;dV \\
  &= \int\; -\left(\rho \text{Div}(E_1) + \rho \langle \nabla \log \rho, E_1 \rangle \right)\langle \frac{\partial E_2}{\partial \theta}, \lambda \rangle - \langle \rho \nabla \lambda E_1, \frac{\partial E_2}{\partial \theta} \rangle \;dV \\
  &= \int\; -\rho \left \langle \left(\text{Div}(E_1) + \langle \nabla \log \rho, E_1 \rangle\right)\lambda + \nabla \lambda E_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$

Plugging this back into the first part of our overall expression, we get:
$$
\begin{align}
  \int \rho \langle \left( \nabla \frac{\partial E_2}{\partial \theta} E_1 - \nabla E_1 \frac{\partial E_2}{\partial \theta} \right), \lambda \rangle dV &= \int\; -\rho \left \langle \left(\;\nabla E_1^T + (\text{Div}(E_1) + \langle \nabla \log \rho, E_1 \rangle)\;I\;\right)\lambda + \nabla \lambda E_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$

So overall, we get:
$$
\begin{align}
  \frac{\partial}{\partial \theta} \int \rho\left\langle \lambda, [E_1,E_2] \right\rangle dV &= \int\; \rho \left \langle \left(\;\nabla E_2^T + (\text{Div}(E_2) + \langle \nabla \log \rho, E_2 \rangle)\;I\;\right)\lambda + \nabla \lambda E_2 , \frac{\partial E_1}{\partial \theta} \right \rangle \\ &\qquad \qquad-\rho \left \langle \left(\;\nabla E_1^T + (\text{Div}(E_1) + \langle \nabla \log \rho, E_1 \rangle)\;I\;\right)\lambda + \nabla \lambda E_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$

## With orthogonal frames
Now, suppose that $(E_1,\dots,E_n)$ is an orthonormal frame, meaning that $E_k = U_k s_k$ for some orthonormal basis $(U_1,\dots,U_n)$ and scalar functions $s_k$.  Lets simplify the terms in the expression for the Lie bracket:
### Gradient of frame vectors
$$
\begin{align}
  \nabla E_k^T = \nabla U_k^T s_k + \nabla s_k U_k^T = s_k\left(\nabla U_k^T + \nabla \log s_k U_k^T \right)
\end{align}
$$

### Divergence of frame vectors
$$
\begin{align}
  \text{Div}(E_k) = \text{Div}(U_k s_k) = s_k\left(\text{Div}(U_k) + \langle \nabla \log s_k, U_k \rangle\right)
\end{align}
$$
We can use the divergence identity for orthogonal coordinate frames, which states that:
$$
\begin{align}
  \text{Div}(U_k) = \langle U_k, \sum_i\nabla \log s_i \rangle - \langle U_k, \nabla \log s_k \rangle
\end{align}
$$
Plugging this back into the expression for the divergence of $E_k$, we get:
$$
\begin{align}
  \text{Div}(E_k) &= s_k \langle U_k, \sum_i\nabla \log s_i \rangle \\
  &= -s_k \langle U_k, \nabla \log \det G \rangle, \quad \text{where } \det G = \prod_i \frac{1}{s_i}
\end{align}
$$

### Putting it all together
$$
\begin{align}
  \nabla E_k^T + (\text{Div}(E_k) + \langle \nabla \log \rho, E_k \rangle)\;I &= s_k\left[\;\;\nabla U_k^T + \nabla \log s_k U_k^T + \langle U_k, \nabla \log \rho - \nabla \log \det G \rangle I\;\;\right]
\end{align}
$$
So overall, we get:
$$
\begin{align}
  \frac{\partial}{\partial \theta} \int \rho\left\langle \lambda, [U_1s_1,U_2s_2] \right\rangle dV &= \int\; \rho s_2\left \langle \left[\;\;\nabla U_2^T + \nabla \log s_2 U_2^T + \langle U_2, \nabla \log \rho - \nabla \log \det G \rangle I\;\;\right]\lambda + \nabla \lambda U_2 , \frac{\partial E_1}{\partial \theta} \right \rangle \\ & \;\;\quad-\rho s_1 \left \langle \left[\;\;\nabla U_1^T + \nabla \log s_1 U_1^T + \langle U_1, \nabla \log \rho - \nabla \log \det G \rangle I\;\;\right]\lambda + \nabla \lambda U_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$

### Further simplification
If we let $\rho = \frac{1}{s_1 s_2}$, then $\nabla \log \rho - \nabla \log \det G = 0$.  So we get:
$$
\begin{align}
  \frac{\partial}{\partial \theta} \int \frac{1}{s_1 s_2}\left\langle \lambda, [U_1s_1,U_2s_2] \right\rangle dV &= \int\; \frac{1}{s_1}\left \langle \left[\;\;\nabla U_2^T + \nabla \log s_2 U_2^T\;\;\right]\lambda + \nabla \lambda U_2 , \frac{\partial E_1}{\partial \theta} \right \rangle \\ & \;\;\quad-\frac{1}{s_2} \left \langle \left[\;\;\nabla U_1^T + \nabla \log s_1 U_1^T\;\;\right]\lambda + \nabla \lambda U_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$
<!--
## Distributional regularization
Under the assumption that $(E_1,\dots,E_n)$ is a coordinate frame, there exists a coordinate system $(z_1,\dots,z_n)$ such that $E_i = \frac{\partial}{\partial z_i}$.  As is the case in normalizing flows, we can introduce a prior distribution over each coordinate and use the change of variables formula to get the following distributional regularization term:
$$
\begin{align}
  \log q(x) = \log \nu\circ F^{-1}(x) + \frac{1}{2}\log\det G, \quad \text{where } G = dF^{-1},\quad \text{and } \frac{dF(z)}{dz_k} = E_k
\end{align}
$$

## Shortest coordinate curves
Suppose we have a probability density function $\rho$ on $\mathbb{R}^2$ and we want to find the coordinate system with the shortest first coordinate curve.  The average length of the first coordinate curve is given by:
$$
\begin{align}
  L = \int \rho \frac{1}{2}\| E_1\|^2 dV
\end{align}
$$
where $E_1$ is the first coordinate vector.  In order to ensure that $E_1$ is a coordinate vector, we need to add the constraint that $[E_1,E_2] = 0$.  This can be done by introducing a Lagrange multiplier $\lambda = \lambda^i E_i$ to enforce the constraint.  The Lagrangian is then:
$$
\begin{align}
  \mathcal{L}(\theta) = \int \rho \left( \frac{1}{2}\| E_1\|^2 + \left\langle \lambda, [E_1,E_2] \right\rangle \right) dV
\end{align}
$$
The derivative of the first term with respect to $\theta$ is given by:
$$
\begin{align}
  \frac{\partial}{\partial \theta} \int \rho \frac{1}{2}\| E_1\|^2 dV = \int \rho \left \langle E_1, \frac{\partial E_1}{\partial \theta} \right \rangle dV
\end{align}
$$
Combining this with the result from the previous section, we get the derivative of the Lagrangian with respect to $\theta$:
$$
\begin{align}
  \frac{\partial}{\partial \theta} \mathcal{L}(\theta) &= \int\; \rho \left \langle E_1 + \left(\;\nabla E_2^T + (\text{Div}(E_2) + \langle \nabla \log \rho, E_2 \rangle)\;I\;\right)\lambda + \nabla \lambda E_2 , \frac{\partial E_1}{\partial \theta} \right \rangle \\ &\qquad \qquad-\rho \left \langle \left(\;\nabla E_1^T + (\text{Div}(E_1) + \langle \nabla \log \rho, E_1 \rangle)\;I\;\right)\lambda + \nabla \lambda E_1 , \frac{\partial E_2}{\partial \theta} \right \rangle \; dV
\end{align}
$$ -->

## Orthogonality via a determinant-constrained energy

Let $E = [E_1,\dots,E_n]$ be the frame and $g = E^\top E$. Consider
$$
\min_E \int \rho \,\frac{1}{2}\,\mathrm{tr}(g)\, dV
\quad\text{s.t.}\quad
\det E = J(x),\;\; [E_i,E_j]=0.
$$
Pointwise, enforce $\det E = J$ with a multiplier $\mu(x)$ and use the local Lagrangian
$\mathcal{L}(E,\mu) = \frac{1}{2}\mathrm{tr}(E^\top E) + \mu \log\det E$.
The first variation yields $E + \mu E^{-\top} = 0$, hence $E^\top E = \alpha^2 I$ for some $\alpha>0$.
Imposing $\det E = \alpha^n = J$ gives $\alpha = J^{1/n}$ and thus $E(x) = J(x)^{1/n} R(x)$ with $R(x)\in O(n)$.

Therefore, among frames with fixed determinant, the sum of squared column norms is minimized when the columns are orthogonal and have equal length (conformal differential). The bracket constraints restrict realizability of $R$ globally but do not change the orthogonality conclusion.

### Gradient w.r.t. E (columns 1..k only)
$$
\begin{align}
&\text{Let } E\in\mathbb{R}^{n\times m},\; E_k = E_{:,1:k}\ \text{(full column rank)},\; C_k = \begin{bmatrix}I_k\\ 0\end{bmatrix} \in \mathbb{R}^{m\times k}.\\
&\nabla_E \,\tfrac{1}{2}\log\det(E_k^\top E_k)
= \big[\, E_k(E_k^\top E_k)^{-1}\;\;,\;\; 0_{\,n\times(m-k)} \,\big] \\
&\quad=\; E\,C_k\,\big(C_k^\top E^\top E\,C_k\big)^{-1} C_k^\top \\
&\quad=\; P_k\,E\,C_k\,(E_k^\top E_k)^{-1} C_k^\top,\quad
P_k := E_k(E_k^\top E_k)^{-1}E_k^\top,\; P_k^\perp := I - P_k.\\
&\text{Consequently }\; P_k^\perp \Big(\nabla_E \,\tfrac{1}{2}\log\det(E_k^\top E_k)\Big) = 0,\quad
\Big(\nabla_E \,\tfrac{1}{2}\log\det(E_k^\top E_k)\Big)\,(I - C_k C_k^\top) = 0.
\end{align}
$$

### Gradient w.r.t. G (row k only)
$$
\begin{align}
&\text{Given } G = E^{-1}:\\[2pt]
&\nabla_E \,\log\det G \;=\; -\,E^{-\top}.\\[8pt]
&\text{For the $k$th row } G^k \text{ and } s_k := G^k (G^k)^\top = e_k^\top G G^\top e_k,\\[2pt]
&\nabla_E \,\log\!\big(G^k (G^k)^\top\big)
\;=\; -\,\frac{2}{s_k}\, G G^\top e_k e_k^\top G
\;=\; -\,2\, G\,P_k^{\text{row}},\\[4pt]
&\text{where } P_k^{\text{row}} \;:=\; \frac{(G^k)^\top G^k}{G^k (G^k)^\top}
\;=\; \frac{G^\top e_k e_k^\top G}{e_k^\top G G^\top e_k}
\quad\text{(rank-1 projector onto } (G^k)^\top\text{).}
\end{align}
$$

### Gradient w.r.t. G (rows 1..k only)
$$
\begin{align}
&\text{Let } G = E^{-1}. \\[4pt]
&\nabla_E \,\log\det G \;=\; -\,E^{-\top}. \\[10pt]
&\text{Let } R_k = \begin{bmatrix} I_k & 0 \end{bmatrix} \in \mathbb{R}^{k\times n},\quad G^{k} := R_k G,\quad S_k := G^{k} (G^{k})^\top = R_k G G^\top R_k^\top. \\[4pt]
&\nabla_E \,\log\det\!\big(G^{k} (G^{k})^\top\big)
\;=\; -\,2\, G\,G^\top R_k^\top\, S_k^{-1}\, R_k\, G
\;=\; -\,2\,G\,P^{\text{row}}_k, \\[4pt]
&\text{where } P^{\text{row}}_k \;:=\; G^\top R_k^\top \big(R_k G G^\top R_k^\top\big)^{-1} R_k G
\;\text{ is the (symmetric, idempotent) projector onto } \operatorname{span}\{(G^{k})^\top\}.
\end{align}
$$

### Gradient w.r.t. E (columns 1..k only)
$$
\begin{align}
&\text{Let } E\in\mathbb{R}^{n\times m},\; E_k = E C_k\ \text{(first $k$ columns)},\; S_k := E_k^\top E_k,\; H := E^\top E.\\[2pt]
&\nabla_E \,\log\det(E_k^\top E_k) \;=\; 2\,E\,C_k\,S_k^{-1}C_k^\top.\\[6pt]
&\text{Projector (data-space) form with } P_k := E_k S_k^{-1} E_k^\top:\\
&\qquad \nabla_E \,\log\det(E_k^\top E_k) \;=\; 2\,P_k\,E\,C_k\,S_k^{-1}C_k^\top,
\quad\text{so } P_k^\perp(\nabla_E f)=0,\; (\nabla_E f)(I-C_kC_k^\top)=0.\\[6pt]
&\text{“Matrix times projector” form (parameter-space, $H$-orthogonal projector):}\\
&\qquad \Pi_k := C_k\,(C_k^\top H C_k)^{-1} C_k^\top H \;\;\Rightarrow\;\;
\nabla_E \,\log\det(E_k^\top E_k) \;=\; 2\,E\,\Pi_k\,H^{-1}.
\end{align}
$$

### Gradient w.r.t. G (columns 1..k only)
$$
\begin{align}
&\text{Let }E\in\mathbb{R}^{n\times n}\text{ be invertible},\; G=E^{-1},\; E_k = E C_k\text{ (first $k$ columns)},\; P_k:=C_kC_k^\top.\\[2pt]
&f(E)=\tfrac12\|E_k\|_F^2=\tfrac12\,\mathrm{tr}(E^\top E P_k).\\[6pt]
&\nabla_E f \;=\; E P_k,\qquad dE \;=\; -\,E\,dG\,E.\\[4pt]
&\Rightarrow\; df \;=\; \mathrm{tr}((\nabla_E f)^\top dE)\;=\; -\,\mathrm{tr}(E P_k E^\top E\, dG)\;=\;\mathrm{tr}\big((\nabla_G f)^\top dG\big).\\[6pt]
&\boxed{\,\nabla_G f \;=\; -\,E^\top E_k E_k^\top \;=\; -\,E^\top E P_k E^\top \;=\; -\,G^{-\top}G^{-1}P_k G^{-\top}\, }\\[4pt]
&\text{Equivalently: }\;\boxed{\,\nabla_G f \;=\; -\,G^{-\top}\,(E_k E_k^\top)\,G^{-\top}\, }.
\end{align}
$$

### Gradient w.r.t. E
$$
\begin{align}
&f(E)\;=\;\log\det E \;-\; \sum_{k=1}^n \tfrac{1}{2}\,\log\!\big(E_k^\top E_k\big),\quad E\in\mathbb{R}^{n\times n}\ \text{invertible}.\\[4pt]
&\nabla_E f \;=\; E^{-\top}\;-\;E\,\mathrm{diag}\!\Big(\tfrac{1}{E_1^\top E_1},\dots,\tfrac{1}{E_n^\top E_n}\Big).\\[4pt]
&\text{Equivalently, columnwise: } \big(\nabla_E f\big)_{:,k} \;=\; (E^{-\top})_{:,k}\;-\;\frac{E_k}{E_k^\top E_k}\,.
\end{align}
$$
when $\nabla_E f = 0$, we get:
$$
\begin{align}
  E^{-\top} &= E\,\mathrm{diag}\!\Big(\tfrac{1}{E_1^\top E_1},\dots,\tfrac{1}{E_n^\top E_n}\Big) \\
  \implies & \mathrm{diag}\!\Big(E_1^\top E_1,\dots,E_n^\top E_n\Big) = E^\top E
\end{align}
$$
