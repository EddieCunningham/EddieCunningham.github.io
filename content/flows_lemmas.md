Title: Flows Lemmas
Date: 2025-03-20
Category: Blog
Slug: flows_lemmas
hidden: true
Summary: Flows Lemmas


Here are some facts abouts flows that are useful for manipulating expressions involving time dependent diffeomorphisms and probability densities.

To start, lets define some notation.  We will use $\frac{\partial}{\partial t}$ to denote the partial derivative with respect to the parameter $t$.

## Time Dependent Flows (Lee Ch.9)
Let $F_t: \mathcal{M} \to \mathcal{M}$ be a time dependent diffeomorphism on an $n$-dimensional Riemannian manifold $(\mathcal{M}, g)$.  In this document, we will interpret $F_t$ as the central object that determines how things change with respect to time.  Although this means that the objects that we introduce will be defined in a much weaker way than they would be defined in general (by abstracting out $F_t$), the flows interpretation is concrete and easy to reason about.  Furthermore, many of the problems that we will use this machinery for are constructed using flows.

We start by defining the infinitesimal generator of a flow.  The infinitesimal generator of $F_t$ is the vector field that describes the instantaneous change of $x_t = F_t(x_0)$ as $t$ changes.  This vector field, which we denote by $X_t \in \mathfrak{X}(\mathcal{M})$ is defined as the vector field that satisfies:
$$
\begin{align}
  \frac{d}{dt}(F_t(x_0)) = \frac{dF_t}{dt}(x_0) = X_t\circ F_t(x_0)
\end{align}
$$
The infinitesimal generator tells us how $F_t$ itself changes with respect to time, which allows us to say how any $x_t \in \mathcal{M}$ changes as we advance $t$ because we have defined $x_t = F_t(x_0)$ for some $x_0$.
$$
\begin{align}
  x_1 - x_0 = \int_0^1 \frac{dx_t}{dt}dt = \int_0^1 X_t dt, \quad \text{where }x_t = F_t(x_0)
\end{align}
$$

Furthermore, it does so in a way where we do not need to refer to $F_t$.  This lets us define a linear operator that tells us how the value of a time dependent function on the space at a certain time changes as we advance time, called the material derivative.

## Material Derivative
Suppose $f_t: \mathcal{M} \to \mathbb{R}$ is a smooth, time dependent function defined on the image of the the time dependent flow $F_t: \mathcal{M} \to \mathcal{M}$.  Since $F_t$ defines how points on $\mathcal{M}$ move as time advances, it is natural to ask how the value of $f_t(x_t)$ changes as we advance time forward.  In order to answer this question, we need to know both how the function, $f_t$ and the space, $x_t$ change as $t$ changes.  For example computing the value of $f$ changes from an initial time of $0$ to a terminal time of $1$ can be written using the fundamental theorem of calculus:
$$
\begin{align}
  f_1(x_1) - f_0(x_0) = \int_0^1 \frac{d f_t(x_t)}{dt} dt, \quad \text{where } x_t = F_t(x_0)
\end{align}
$$
The material derivative is the integrand of this expression.  To derive its expression, it is convenient to finds its value as a function of the starting point of the flow.  Suppose $x_t = F_t(x_0)$.  Then we can derive:
$$
\begin{align}
  \frac{df_t(x_t)}{dt}|_{x_0} &= \frac{\partial f_t \circ F_t}{\partial t}(x_0) \\
  &= \frac{\partial f_t}{\partial t}\circ F_t(x_0) + (df_t)_{x_t}\frac{dF_t}{dt}(x_0) \\
  &= \frac{\partial f_t}{\partial t}\circ F_t(x_0) + \underbrace{(df_t)_{x_t}X_t}_{X_t(f_t)}\circ F_t (x_0) \\
  &= \left(\frac{\partial f_t}{\partial t} + X_t(f_t)\right)\circ F_t(x_0)
\end{align}
$$
and so we find that the expression for the material derivative at time $t$ is
$$
\begin{align}
  \frac{d f_t}{dt} &= \frac{\partial f_t}{\partial t} + X_t(f_t) = \frac{\partial f_t}{\partial t} + \langle \nabla f_t, X_t \rangle_g
\end{align}
$$
where we have just inserted the definition of the inner product (Lee Ch. 13).

## Lie derivative (material derivative) of vectors
The material derivative told us how the value of a time dependent function changes as we move along a flow.  A natural next question is how other things, like vector fields, change as we move along a flow.  This is something answered by the Lie derivative.  Let $V_t \in \mathfrak{X}(\mathcal{M})$ be a vector field on $\mathcal{M}$.  We can assign a time derivative for $V_t$ by first pushing the vector back to the starting time, taking the derivative there, and then pushing forward to the current time:
$$
\begin{align}
  \frac{d}{dt}V_t &= (F_t)_* \frac{d}{dt}\left((F_t^{-1})_* V_t \right) \\
  &= (F_t)_* (F_t^{-1})_* \left(\mathcal{L}_{X_t}V_t + \frac{\partial}{\partial t}V_t\right), \quad \text{(Exact same approach as Lee, Prop. 22.15)} \\
  &= [X_t,V_t] + \frac{\partial}{\partial t}V_t
\end{align}
$$
$[X_t,V_t]$ is the Lie bracket (Lee Ch.8) between the infinitesmal generator of the flow and the vector field $V_t$ and $\frac{\partial}{\partial t}V_t$ is vector whose components are the partial derivatives of the components of $V_t$ with respect to time.  We can see that this is a reasonable choice for a derivative because it is linear and satisfies the product rule.  Let $a, b \in \mathbb{R}$ and let $f$ be a smooth function on $\mathcal{M}$.  Then the Lie derivative for vectors is linear and satisfies a product rule:
$$
\begin{align}
  \frac{d}{dt}(aV + bW) = [X_t,aV + bW] = a[X_t,V] + b[X_t,W] = a\frac{d}{dt}V + b\frac{d}{dt}W \\
  \frac{d}{dt}(fV) = [X_t,fV] = f[X_t,V] + X_t(f)W = f\frac{d}{dt}V + \frac{df}{dt}V
\end{align}
$$

However, the Lie derivative is NOT a connection like the covariant derivative because it is not linear in over $C^\infty(\mathcal{M})$ in X (Lee Riemannian manifolds Ch. 4).  A connection $\nabla$ must satisfy $\nabla_{fX_1 + gX_2}Y = f\nabla_{X_1}Y + g\nabla_{X_2}Y$ for all $f,g \in C^\infty(\mathcal{M})$ and $X_1, X_2, Y \in \mathfrak{X}(\mathcal{M})$, however we can see that the Lie derivative does not satisfy this property:
$$
\begin{align}
  \mathcal{L}_{fX_1 + gX_2}Y &= [fX_1 + gX_2,Y] \\
  &= [fX_1,Y] + [gX_2,Y] \\
  &= f[X_1,Y] + g[X_2,Y] - Y(f)X_1 - Y(g)X_2 \\
  &= f\mathcal{L}_{X_1}Y + g\mathcal{L}_{X_2}Y - Y(f)X_1 - Y(g)X_2
\end{align}
$$

This is particularly relevant when we take the Lie derivative in the direction of a vector field that we can write in a coordinate basis.  Let $(E_1,\dots,E_n)$ be a basis for $\mathfrak{X}(\mathcal{M})$.  Then we can write any vector field $V$ as $X = \sum_{i=1}^n X^i E_i$.  Then we can compute:
$$
\begin{align}
  \mathcal{L}_X Y &= \mathcal{L}_{X^i E_i} Y \\
  &= X^i \mathcal{L}_{E_i} Y - Y(X^i)E_i
\end{align}
$$

## Lie derivative of one-forms
The same approach can be used to define the Lie derivative of one-forms.  Let $\omega_t \in \Omega^1(\mathcal{M})$ be a one-form on $\mathcal{M}$.  We can pull back the one-form to the starting time, take the derivative there, and then push forward to the current time:
$$
\begin{align}
  \frac{d}{dt}\omega_t &= (F_t^{-1})^* \frac{d}{dt}\left((F_t)^* \omega_t \right) \\
  &= (F_t^{-1})^* \left(\mathcal{L}_{X_t} \omega_t + \frac{\partial}{\partial t} \omega_t\right) \\
  &= \mathcal{L}_{X_t} \omega_t + \frac{\partial}{\partial t} \omega_t \\
  &= X_t \lrcorner d\omega_t + d(X_t \lrcorner \omega_t) + \frac{\partial}{\partial t} \omega_t \quad \text{(Cartan's magic formula)}
\end{align}
$$

Furthermore, if $\omega_t$ is an exact form, i.e. $\omega_t = df_t$, then we can use the product rule to see that:
$$
\begin{align}
  \frac{d}{dt}df_t &=  X_t \lrcorner \underbrace{ddf_t}_{0} + d(X_t \lrcorner df_t) + \frac{\partial}{\partial t} df_t \\
  &= d(X_t(f_t)) + \frac{\partial}{\partial t} df_t
\end{align}
$$

## Volume forms (Lee Ch.15)
In differential geometry, we can measure the volumes of subsets of $\mathcal{M}$ using the volume form $dV_g \in \Omega^n(\mathcal{M})$.   The volume form is a differential form on $\mathcal{M}$ that has the unique, identifying property that for any orthonormal basis $\{E_i\}_{i=1}^n$ of $T_x\mathcal{M}$ with respect to the metric $g$, we have:
$$
\begin{align}
  dV_g(E_1, \ldots, E_n) = 1
\end{align}
$$
The volume form can be used to measure the volume of subsets of $\mathcal{M}$ using integration.  For example, the volume of a subset $D \subset \mathcal{M}$ is given by:
$$
\begin{align}
  \mathrm{Vol}_g(D) = \int_D dV_g
\end{align}
$$
Note that the volume inherently depends on the metric $g$ and that in Euclidean space, this is just the Lebesgue measure.  A useful property of volume is that it is invariant under diffeomorphisms.  That is, if $F: \mathcal{M} \to \mathcal{M}$ is a diffeomorphism, then $\mathrm{Vol}_g(F(D)) = \mathrm{Vol}_{F^*g}(D)$.  Intuitively, this is because the diffeomorphism cannot change the amount of space in a region (Lee 16.6.d):
$$
\begin{align}
  \mathrm{Vol}_g(F(D)) = \int_{F(D)} dV_g = \int_{D} F^* dV_g = \int_{D} dV_{F^*g} = \mathrm{Vol}_{F^*g}(D)
\end{align}
$$
Since in Riemannian geometry we usually want the metric to stay fixed, we can rewrite the pullback of the volume form in terms of the original volume form.  This is possible because volume forms are all equal to each other up to a scalar function (Lee 15.29).
$$
\begin{align}
  dV_{F^*g} = \det(DF) dV_g
\end{align}
$$
where $DF$ is the Jacobian matrix of $F$ and $\det(DF)$ is the determinant of $DF$.  More generally, for any function $f: \mathcal{M} \to \mathbb{R}$, we have (Lee 14.20):
$$
\begin{align}
  F^* (f dV_g) = (f\circ F) \det(DF) dV_g
\end{align}
$$


## Probability measures
We can use the volume form to define probability measures on $\mathcal{M}$.  Let $\rho: \mathcal{M} \to \mathbb{R}$ be a smooth, positive function on $\mathcal{M}$ that integrates to one over $\mathcal{M}$, i.e.
$$
\begin{align}
  \int_{\mathcal{M}} \rho dV_g = 1
\end{align}
$$
$\rho$ is called a probability density function on $\mathcal{M}$.  We can define a probability measure by integrating $\rho$ over a subset $D \subset \mathcal{M}$:
$$
\begin{align}
  \mathbb{P}(x \in D) = \int_D \rho dV_g
\end{align}
$$

## Pullback of probability measures (change of variables)
Suppose $F: \mathcal{Z} \to \mathcal{X}$ is a diffeomorphism.  If we have a probability measure, $\rho_z$, defined on $\mathcal{Z}$, we can construct an equivalent probability measure on $\mathcal{X}$ using the pullback of the measure.  Let $D \subset \mathcal{X}$.  Then the probability mass contained in $F^{-1}(D)$ is the same as the probability mass contained in $D$:
$$
\begin{align}
  \mathbb{P}(z \in F^{-1}(D)) &= \int_{F^{-1}(D)} \rho_z dV_g \\
  &= \int_{D} (F^{-1})^* (\rho_z dV_g) \\
  &= \int_{D} \underbrace{(\rho_z \circ F^{-1}) \det(DF^{-1})}_{\rho_x} dV_g \\
  &= \int_{D} \rho_x dV_g \\
  &= \mathbb{P}(x \in D)
\end{align}
$$
We used the probability density function $\rho_z$ and the determinant of the diffeomorphism to define a new probability density function $\rho_x$ on $\mathcal{X}$.  This is equivalent to the change of variables formula for probability densities.  A more common way to write the relationship between $\rho_z$ and $\rho_x$ is using the pushforward operator on probability densities:
$$
\begin{align}
  \rho_x = F_\# \rho_z := (\rho_z \circ F^{-1}) \det(DF^{-1})
\end{align}
$$


## Lie derivative of the volume form
The lie derivative is the more general notion of the material derivative for tensor fields that tells us how different the value of a tensor field is as we move along a flow.  For the purposes of this post, we will only look at the Lie derivative of differential forms.

Let $\omega \in \Omega^k(\mathcal{M})$ be a $k$-form on $\mathcal{M}$.  The lie derivative of $\omega$ along a vector field $X$ is given by Cartan's magic formula (Lee 14.33):
$$
\begin{align}
  \mathcal{L}_{X} \omega = d(X \lrcorner \omega) + (X \lrcorner d \omega)
\end{align}
$$
where $X \lrcorner \omega$ is the interior product of $X$ and $\omega$.

In our context, the most useful application of the Lie derivative is when $\omega$ is the volume form $dV_g$.  The volume form is closed, so $d(dV_g) = 0$ (this might be why we use the suggestive notation $dV_g$ for the volume form even though it might not actually be an exact form).  In this case, we can use the definition of divergence (Lee 16.30) to rewrite the lie derivative as:
$$
\begin{align}
  \mathcal{L}_{X} dV_g = \mathrm{Div}(X) dV_g
\end{align}
$$
Furthermore, if $f: \mathcal{M} \to \mathbb{R}$ is a smooth function, then
$$
\begin{align}
  \mathcal{L}_{X} (fdV_g) = \mathrm{Div}(fX) dV_g
\end{align}
$$

## Continuity equation (instantaneous change of variables formula)
Next we can see how probability mass changes as samples flow along a vector field.  Let $\rho_0$ be a probability density function on $\mathcal{X}_0$ and let $F_t: \mathcal{X}_0 \to \mathcal{X}_t$ be a time-dependent diffeomorphism whose infinitesimal generator is $X_t$.  Let $D_0 \subset \mathcal{X}_0$ be a subset of $\mathcal{X}_0$ and let $D_t = F_t(D_0) \subset \mathcal{X}_t$.  The probability mass in $D_0$ is given by:
$$
\begin{align}
  \mathbb{P}(x_0 \in D_0) = \int_{D_0} \rho_0 dV_{g}
\end{align}
$$
and as we saw ealier, we can pull this probability measure back through $F_t^{-1}$ to define a probability measure on $\mathcal{X}_t$:
$$
\begin{align}
  \mathbb{P}(x_t \in D_t) = \int_{D_t} \rho_t dV_{g}
\end{align}
$$
where $\rho_t = (F_t)_\# \rho_0$ is the pushforward of $\rho_0$ by $F_t$.  Since this is the same probability measure, i.e. $\mathbb{P}(x_t \in D_t) = \mathbb{P}(x_0 \in D_0)$ for any $t$, we know that the probability mass contained in $D_t$ must not change as $t$ varies.  This conservation of probability mass leads us to the continuity equation:
$$
\begin{align}
  0 &= \frac{\partial}{\partial t}\mathbb{P}(x_t \in D_t) \\
  &= \frac{\partial}{\partial t}\int_{F_t(D_0)} \rho_t dV_{g} \\
  &= \int_{D_0} \frac{\partial}{\partial t}F_t^* (\rho_t dV_{g}),\quad \text{use Lee 22.15} \\
  &= \int_{D_0} F_t^* \left(\frac{\partial}{\partial t} \rho_t dV_{g} + \mathcal{L}_{X_t} (\rho_t dV_{g})\right) \\
  &= \int_{D_t} \frac{\partial \rho_t}{\partial t} dV_{g} + \mathrm{Div}(\rho_t X_t) dV_{g} \\
  &= \int_{D_t} \left(\frac{\partial \rho_t}{\partial t} + \mathrm{Div}(\rho_t X_t)\right) dV_{g}
\end{align}
$$
The integrand must be equal to zero, so we are left with the continuity equation:
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} + \mathrm{Div}(\rho_t X_t) = 0
\end{align}
$$
The continuity equation is one of the most important equations that we will use because it lets us look at how probability distributions, and their samples, change with respect to a flow without needing to know exactly how the diffeomorphism $F_t$ is defined.  This lets us take a "transport" view of probability distributions where we can move individual samples along the flow of a vector field and see how the distribution of the samples changes by solving the continuity equation.

### Instantaneous change of variables formula
A more commonly used form of the continuity equation in the context of [continuous normalizing flows](https://arxiv.org/pdf/1806.07366.pdf) is the instantaneous change of variables formula.  It is easy to derive using the following property of the divergence operator (Lee problem 16-12):
$$
\begin{align}
  \text{Div}(\rho X) = \rho \text{Div}(X) + \langle \nabla \rho , X \rangle
\end{align}
$$
And so it is easy to see that
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} + \mathrm{Div}(\rho_t X_t) = \frac{\partial \rho_t}{\partial t} + \rho_t \text{Div}(X_t) + \langle \nabla \rho_t , X_t \rangle = \frac{d\rho_t}{dt} + \rho_t \text{Div}(X_t) = 0
\end{align}
$$
Pulling out the $\rho_t$ term, we get the instantaneous change of variables formula:
$$
\begin{align}
  \frac{d\log \rho_t}{dt} = -\text{Div}(X_t)
\end{align}
$$


## Information content and information flow
We can define the information content of a region $D \subset \mathcal{M}$ using the probability mass function in $D$:
$$
\begin{align}
  I(\rho,D) = -\log \mathbb{P}(x \in D), \quad \text{where } \mathbb{P}(x \in D) = \int_D \rho dV_g
\end{align}
$$
Suppose we flow the probability mass along a vector field $X_t$, then the information content of the time dependent region is constant:
$$
\begin{align}
  \frac{dI(\rho_t,D_t)}{dt} &= -\frac{1}{\mathbb{P}_t}\frac{d\mathbb{P}_t}{dt} \\
  &= -\frac{1}{\mathbb{P}_t}\underbrace{\frac{d}{dt}\int_{D_t} \rho_t dV_g}_{=0}\quad \because \text{conservation of probability} \\
  &= 0
\end{align}
$$
This matches the intution that information cannot be created or destroyed simply by moving around points on $\mathcal{M}$.

## Probability flow through a fixed region
A direct consequence of the continuity equation is to look at how probability flows through a region by applying the divergence theorem (Lee 16.32).  Let $D \subset \mathcal{M}$ be a **fixed** subset of $\mathcal{M}$ and let $\rho_t$ be a time dependent probability density function on $\mathcal{M}$.  The amount of probability mass in $D$ at time $t$ is given by:
$$
\begin{align}
  \mathbb{P}(x_t \in D) = \int_D \rho_t dV_g
\end{align}
$$
Notice here that $D$ is fixed and not time dependent like before.  So when we take the time derivative of the probability mass, we can use the divergence theorem to get:
$$
\begin{align}
  \frac{\partial}{\partial t} \mathbb{P}(x_t \in D) &= \int_D \frac{\partial \rho_t}{\partial t} dV_g \\
  &= \int_D -\mathrm{Div}(\rho_t X_t) dV_g \\
  &= -\int_{\partial D} \langle J_t, N \rangle_g dV_{\tilde{g}}
\end{align}
$$
where $\partial D$ is the boundary of $D$ and $N$ is the outward normal vector to the boundary of $D$, and $dV_{\tilde{g}}$ is the induced volume form on the boundary of $D$ (Lee 15.32).  The probability current vector is denoted by $J_t$ and is defined as:
$$
\begin{align}
  J_t = \rho_t X_t
\end{align}
$$

## Probability current
The probability current is a vector field that tells us the rate of change of probability mass per unit area, and is useful for working with probability at a macroscopic level.  We saw earlier that the definition of the probability current is given by:
$$
\begin{align}
  J_t = \rho_t X_t
\end{align}
$$
where $X_t$ is the vector field that flows the probability mass along $\mathcal{M}$, and that it describes the flow of probability mass through a *fixed* region in space.

## Information flow through a fixed region
If we consider a fixed region $D \subset \mathcal{M}$ and let $X_t$ be the vector field that flows the probability mass along $D$, then the information content of $D$ has the following time derivative:
$$
\begin{align}
  \frac{dI(\rho_t,D)}{dt} &= -\frac{1}{\mathbb{P}_t}\frac{d}{dt}\int_{D} \rho_t dV_g \\
  &= \frac{1}{\mathbb{P}_t}\int_{\partial D} \langle J_t, N \rangle_g dV_{\tilde{g}}
\end{align}
$$
where $J_t = \rho_t X_t$ is the probability current vector.



## Instantaneous change of expectation
Next, we can start looking at how more interesting expressions involving probability distributions change as we move along a flow.  Let $\rho_t$ be a time dependent probability density function on $\mathcal{M}$ and let $f_t: \mathcal{M} \to \mathbb{R}$ be a time dependent function on $\mathcal{M}$.  The expected value of $f_t$ is given by:
$$
\begin{align}
  \mathbb{E}[f_t] = \int_{\mathcal{M}} \rho_t f_t dV_g
\end{align}
$$
Also assume that $\mathcal{M}$ either has no boundary or that the probability density function is $0$ on the boundary, and recall that the integration by parts formula on manifolds is given by (Lee problem 16-12.b):
$$
\begin{align}
  \int_{\mathcal{M}} \langle \nabla f, X \rangle_g dV_g = \int_{\partial \mathcal{M}} f \langle X, N \rangle_g dV_{\tilde{g}} - \int_{\mathcal{M}} f \text{Div}(X) dV_g
\end{align}
$$

Then we can compute the time derivative of the expected value of $f_t$ by taking the time derivative of the integral:
$$
\begin{align}
  \frac{\partial}{\partial t} \mathbb{E}[f_t] &= \int_{\mathcal{M}} \frac{\partial \rho_t}{\partial t} f_t dV_g + \int_{\mathcal{M}} \rho_t \frac{\partial f_t}{\partial t} dV_g \\
  &= -\int_{\mathcal{M}}\mathrm{Div}(\rho_t X_t) f_t dV_g + \int_{\mathcal{M}} \rho_t \frac{\partial f_t}{\partial t} dV_g \\
  &= \int_{\mathcal{M}}\rho_t \langle \nabla f_t, X_t \rangle_g dV_g + \int_{\mathcal{M}} \rho_t \frac{\partial f_t}{\partial t} dV_g \\
  &= \int_{\mathcal{M}} \rho_t \frac{d f_t}{dt} dV_g
\end{align}
$$
Our result says that the rate of change of the expected value of $f_t$ is equal to the expected material derivative of $f_t$:
$$
\begin{align}
  \frac{\partial }{\partial t}\mathbb{E}[f_t] = \mathbb{E}\left[\frac{d f_t}{dt}\right]
\end{align}
$$

## Instantaneous change of expectation with respect to a moving region
This result also holds if we consider an expectation over a moving region.  Let $D \subset \mathcal{M}$ be a subset and let $F_t: \mathcal{M} \to \mathcal{M}$ be a diffeomorphism whose infinitesimal generator is $X_t$.  Then the expected value of $f_t$ over $F_t(D)$ is given by:
$$
\begin{align}
  \int_{F_t(D)} \rho_t f_t dV_g
\end{align}
$$
Taking the time derivative of this expression, we get:
$$
\begin{align}
  \frac{\partial}{\partial t} \int_{F_t(D)} \rho_t f_t dV_g &= \int_{D} \frac{\partial}{\partial t}F_t^* \left(\rho_t f_t dV_g \right) \\
  &= \int_{D} F_t^* \left[\underbrace{\mathcal{L}_{X_t} \left(\rho_t f_t dV_g \right)}_{=d(X_t \lrcorner \rho_t f_t dV_g) + \cancel{X_t \lrcorner d(\rho_t f_t dV_g)}} + \frac{\partial}{\partial t} \left(\rho_t f_t\right) dV_g  \right] \\
  &= \int_{F_t(D)} \left[\text{Div}(\rho_t f_tX_t) + \frac{\partial}{\partial t} \left(\rho_t f_t\right)\right] dV_g  \\
  &= \int_{F_t(D)} \left[f_t \text{Div}(\rho_tX_t) + \langle \nabla f_t, \rho_tX_t \rangle + \frac{\partial \rho_t}{\partial t} f_t + \rho_t \frac{\partial f_t}{\partial t}\right] dV_g \\
  &= \int_{F_t(D)} \left[f_t\underbrace{\left(\text{Div}(\rho_tX_t)+ \frac{\partial \rho_t}{\partial t}\right)}_{=0\text{ by continuity equation}} + \rho_t\underbrace{\left(\langle \nabla f_t, X_t \rangle  + \frac{\partial f_t}{\partial t}\right)}_{=\frac{df_t}{dt}}\right] dV_g \\
  &= \int_{F_t(D)} \rho_t \frac{df_t}{dt} dV_g
\end{align}
$$
