Title: Locally invertible maps and pushforwards
Date: 2024-02-12
Category: Blog
Slug: locally-invertible
hidden: true
Summary: A derivation of how to sample from a Boltzmann distribution using a locally invertible map.

## Problem statement and introduction
Let $(\mathcal{M}, g)$ be a Riemannian manifold and let $\phi: \mathcal{M} \to \mathbb{R}$ be a smooth function.  The Boltzmann distribution on $\mathcal{M}$ is given by:
$$
\begin{align}
  \rho(x) = \frac{1}{Z}\exp\{-\phi(x)\}
\end{align}
$$
where $Z$ is an unknown normalization constant.  Our goal will be to produce samples from this distribution using transport along a carefully chosen time-dependent vector field $V_t$ on $\mathcal{M}$ from time $t=0$ to $t=1$.  To do this, we will first construct a time-dependent probability distribution that interpolates between some initial distribution, which we will denote by $\rho_0$, and the Boltzmann distribution, which going forward we will denote by $\rho_1$.  We will assume that $\rho_0$ is a tractable distribution that we can sample from and can evaluate the log likelihood.  To be explicit, we will write $\rho_0$ and $\rho_1$ as:
$$
\begin{align}
  \rho_0(x) = \frac{1}{Z_0}\exp\{-\phi_0(x)\} \\
  \rho_1(x) = \frac{1}{Z_1}\exp\{-\phi_1(x)\}
\end{align}
$$
Note that when $\rho_0$ is Gaussian, $\phi_0(x) = \frac{1}{2}x^T\Sigma^{-1}x - x^T\Sigma^{-1}\mu$.  Next, we will construct a time-dependent distribution $\rho_t$ that linearly interpolates between $\rho_0$ and $\rho_1$:
$$
\begin{align}
  \rho_t(x_t) &= \frac{1}{Z_t}\rho_0(x_t)^{(1-t)} \rho_1(x_t)^t \\
  &= \frac{1}{Z_t}\exp\{\underbrace{-(1-t)\phi_0(x_t) - t\phi_1(x_t)}_{=: \;-\phi_t(x_t)}\} \\
  &= \frac{1}{Z_t}\exp\{-\phi_t(x_t)\}
\end{align}
$$
Notice that $\rho_t$ still depends on an unknown normalization constant $Z_t$, which will stop us from being able to sample from or evaluate $\rho_t$.  However, the gradient of its log likelihood, called the score function, is tractable because the normalization constant does not depend on $x$.  The score function is given by:
$$
\begin{align}
  \nabla \log \rho_t(x_t) &= -\phi_t(x_t)
\end{align}
$$
We will use this tractability to design our sampling algorithm for $\rho_1$.  This algorithm will first sample an initial point $x_0$ from $\rho_0$ and then transport it using a time dependent vector field, $V_t$, so that $\frac{dx_t}{dt} := V_t$.  We will design $V_t$ so that at $t=1$, the point $x_1 = x_0 + \int_0^1 \frac{dx_t}{dt} dt$ is distributed according to $\rho_1$.  Our main insight will be to use the tractability of $\nabla \log \rho_t(x_t)$ to build an objective function for $V_t$ that whose solution ensures that the distribution of $x_t$ is equal to $\rho_t$ for all $t \in [0,1]$.  Next we will derive this objective function.

## Objective function derivation
To begin, we assume that $V_t$ is the infinitesimal generator of a time dependent flow $F_t: \mathcal{M} \to \mathcal{M}$ (Lee Thm 9.48) that begins at time $t=0$.  From a theoretical perspective, this will help us ensure that $V_t$ has nice properties to transport samples in a probability mass preserving way and from a practical perspective, will allow us to efficiently evaluate the divergence of $V_t$ if $F_t$ is constructed as a normalizing flow (see the section below on divergence of pushforward vector fields).  The explicit relationship between $F_t$ and $V_t$ is given by:
$$
\begin{align}
  \frac{d}{dt}F_t(x_0) = V_t(x_t), \quad \text{where } x_t = F_t(x_0)
\end{align}
$$
We will also use $q_t$ to denote the pushforward of the prior distribution, $\rho_0$, through $F_t$.  This probability density function is given by the change of variables formula:
$$
\begin{align}
  q_t(x_t) &:= (F_t)_{\#}\rho_0(x_0), \quad \text{where } x_t = F_t(x_0) \\
  &= \rho_0(x_0) \det(DF_t(x_0))^{-1}
\end{align}
$$
where $DF_t(x_0)$ is the Jacobian matrix of $\frac{dF_t(x_0)}{dx_0}$.

Recall that our goal is to ensure that the distribution of $x_t$ is equal to $\rho_t$ for all $t \in [0,1]$.  This means that we want to ensure that $q_t = \rho_t$ for all $t \in [0,1]$.  An equivalent condition is to ensure that the score function of $q_t$ is equal to the score function of $\rho_t$ for all $t \in [0,1]$.  The score function of $q_t(x_t)$ can be written using the fundamental theorem of calculus:
$$
\begin{align}
  \nabla \log q_t(x_t) &= \nabla \log \rho_0(x_0) + \int_0^t \frac{d}{ds}\nabla \log q_s(x_s) ds
\end{align}
$$
On the other hand, the score function of $\rho_t(x_t)$ is given by:
$$
\begin{align}
  \nabla \log \rho_t(x_t) &= \nabla \log \rho_0(x_0) + \int_0^t \frac{d}{ds}\nabla \log \rho_s(x_s) ds
\end{align}
$$
We can see that if we could enforce that $\frac{d}{dt}\nabla \log q_t(x_t) = \frac{d}{dt}\nabla \log \rho_t(x_t)$ for all $t \in [0,1]$, then we would have that $q_t = \rho_t$ for all $t \in [0,1]$.  This motivates the following definition for a vector field $V_t^*$ that transports $\rho_0$ to $\rho_t$:
$$
\begin{align}
  V_t^*(x_t) = \text{argmin}_{V_t} \left\| \frac{d}{dt}\nabla \log q_t(x_t) - \frac{d}{dt}\nabla \log \rho_t(x_t) \right\|^2
\end{align}
$$
where $\frac{d}{dt}$ denotes the material derivative along the flow of $V_t^*$.In order for there to exist a time-dependent flow associated with $V_t^*$, we need to check that $V_t^*$ is smooth on $J\times \mathcal{M}$, where $J \subset (0,1)$ is an open interval.




## Material derivative of the score function
The material derivative of the score function of $\rho_t$ is something that we can evaluate in closed form.  Recall that the material derivative of a function $f_t$ along the flow of the vector field $V_t$ is given by:
$$
\begin{align}
  \frac{d}{dt}f(x_t) = \frac{\partial f_t(x_t)}{\partial t} + \langle \nabla f_t(x_t), V_t(x_t) \rangle
\end{align}
$$
and that the material derivative of the gradient is given by:
$$
\begin{align}
  \frac{d}{dt}\nabla f_t(x_t) = -\nabla V_t^T\nabla f_t + \nabla\frac{d}{dt} f_t
\end{align}
$$
Plugging in the expression for the score function of $\rho_t$ (and dropping the application to $x_t$ for brevity), we get that:
$$
\begin{align}
  \frac{d}{dt}\nabla \log \rho_t &= -\nabla V_t^T\nabla \log \rho_t + \nabla\frac{d}{dt} \log \rho_t
\end{align}
$$
We already know that $\nabla \log \rho_t = -\phi_t(x_t)$ is computable, so we just need to check that $\nabla\frac{d}{dt} \log \rho_t$ is also computable.  We can expand this term as follows:
$$
\begin{align}
  \nabla\frac{d}{dt} \log \rho_t &= \nabla\left(\frac{\partial \log \rho_t}{\partial t} + \langle \nabla \log \rho_t, V_t \rangle \right) \\
  &= \nabla\left(-\frac{\partial \phi_t}{\partial t} - \underbrace{\frac{\partial Z_t}{\partial t}}_{\text{const. w.r.t. x}} - \langle \nabla \phi_t, V_t \rangle \right) \\
  &= \nabla\left(-\frac{\partial \phi_t}{\partial t} - \langle \nabla \phi_t, V_t \rangle \right)
\end{align}
$$
And so we see that we can compute $\frac{d}{dt}\nabla \log \rho_t$.  Next, we can look at the material derivative of the score function of $q_t$:
$$
\begin{align}
  \frac{d}{dt}\nabla \log q_t &= -\nabla V_t^T\nabla \log q_t + \nabla\frac{d}{dt} \log q_t \\
  &= -\nabla V_t^T\nabla \log q_t - \nabla\text{Div}(V_t)
\end{align}
$$
where we used the instantaneous change of variables formula, $\frac{d}{dt}\log q_t = -\text{Div}(V_t)$.

And so we get that:
$$
\begin{align}
  V_t^*(x_t) &= \text{argmin}_{V_t} \left\| \frac{d}{dt}\nabla \log q_t(x_t) - \frac{d}{dt}\nabla \log \rho_t(x_t) \right\|^2 \\
  &= \text{argmin}_{V_t} \left\| -\nabla V_t^T(\nabla \log \rho_t - \nabla \log q_t) + \nabla\left(-\frac{\partial \phi_t}{\partial t} - \langle \nabla \phi_t, V_t \rangle + \text{Div}(V_t) \right) \right\|^2
\end{align}
$$

## Inductive construction of $V_t^*$
Although we have a preliminary definition of $V_t^*$, we need to ensure that it exists.  We can do this inductively.  At $t=0$, we have that $\nabla \log \rho_0 = \nabla \log q_0$, and so the first part of the expression cancels out.  This leaves us with:
$$
\begin{align}
  V_0^*(x_0) = \text{argmin}_{V_0} \left\| \nabla\left(-\frac{\partial \phi_0}{\partial t} - \langle \nabla \phi_0, V_0 \rangle + \text{Div}(V_0) \right) \right\|^2
\end{align}
$$
We can then use the implicit function theorem to ensure that $V_0^*$ exists.  Let $\mathcal{C}(t, x_0, \phi, V) = \|\nabla\left(-\frac{\partial \phi}{\partial t} - \langle \nabla \phi, V \rangle + \text{Div}(V) \right)\|^2$.  The implicit function theorem says that if there is a combination of $t, x_0, \phi, V$ such that $\mathcal{C}(0, x_0, \phi_0, V_0) = 0$, and furthermore $\frac{\partial \mathcal{C}}{\partial V} \neq 0$ at $(0, x_0, \phi_0, V_0)$, then there exists a unique $V_0^*(0, x_0, \phi_0)$ such that $\mathcal{C}(0, x_0, \phi_0, V_0^*(0, x_0, \phi_0)) = 0$.  First, there are an infinite number of solutions to $\mathcal{C}(0, x_0, \phi_0, V_0) = 0$ because we can choose any vector field that satisfies the continuity equation with $\rho_0$.  Next, we can compute the partial derivative of $\mathcal{C}$ with respect to a component of $V$, $V^i$, as follows:
$$
\begin{align}
  \frac{\partial \mathcal{C}}{\partial V^i} = 2\left\langle \nabla\left(-\frac{\partial \phi_0}{\partial t} - \langle \nabla \phi_0, V_0 \rangle + \text{Div}(V_0) \right), \frac{\partial}{\partial V^i}\nabla\left(-\frac{\partial \phi_0}{\partial t} - \langle \nabla \phi_0, V_0 \rangle + \text{Div}(V_0) \right) \right\rangle
\end{align}
$$

We can focus on the second term in the expression above:
$$
\begin{align}
  \frac{\partial}{\partial V^i}\nabla\left(-\frac{\partial \phi_0}{\partial t} - \langle \nabla \phi_0, V_0 \rangle + \text{Div}(V_0) \right) &= \frac{\partial}{\partial V^i}\frac{\partial}{\partial x^k}\left(-\frac{\partial \phi_0}{\partial x^j}V^j + \frac{\partial V^j}{\partial x^j}\right) \\
  &= \frac{\partial}{\partial V^i}\left(-\frac{\partial^2 \phi_0}{\partial x^k \partial x^j}V^j - \frac{\partial \phi_0}{\partial x^j}\frac{\partial V^j}{\partial x^k} + \frac{\partial^2 V^j}{\partial x^i \partial x^j}\right) \\
  &= -\frac{\partial^2 \phi_0}{\partial x^k \partial x^i} - \frac{\partial \phi_0}{\partial x^j}\frac{\partial}{\partial V^i}\frac{\partial V^j}{\partial x^k} + \frac{\partial}{\partial V^i}\frac{\partial^2 V^j}{\partial x^i \partial x^j}
\end{align}
$$



## Divergence of pushforward vector fields
Suppose $F: \mathcal{Z} \to \mathcal{X}$ is a diffeomorphism and let $Z \in \mathfrak{X}(\mathcal{Z})$ be a vector field.  The vector field $X = F_*Z$ is the pushforward of $Z$ through $F$ and has the following divergence:

$$
\begin{align}
  \text{Div}_g(\rho_x X) dV_{g} &= d(X \lrcorner \rho_x dV_{g}) \\
  &= d(F_*Z \lrcorner \rho_x dV_{g}) \\
  &= d((F^{-1})^*(Z \lrcorner F^* \rho_x dV_{g})) \\
  &= (F^{-1})^*d(Z \lrcorner \rho_z dV_{g_z}) \\
  &= (F^{-1})^*\text{Div}(\rho_z Z) dV_{g_z} \\
  &= (F^{-1})^*(\rho_z \text{Div}(Z) + \langle Z, \nabla_z \rho_z \rangle ) dV_{g_z} \\
  &= (F^{-1})^*(\text{Div}(Z) + \langle Z, \nabla_z \log \rho_z
  \rangle ) \rho_z dV_{g_z} \\
  &= \left( (\text{Div}(Z) + \langle Z, \nabla_z \log \rho_z
  \rangle )\circ F^{-1}\right) (F^{-1})^*(\rho_z dV_{g_z}) \\
  &= \left( (\text{Div}(Z) + \langle Z, \nabla_z \log \rho_z
  \rangle )\circ F^{-1}\right) dV_{g_x}
\end{align}
$$
