Title: Equations for SDEs
Date: 2023-07-15
Modified: 2024-04-10
Category: Blog
status: hidden
Tags: SDE
Slug: SDE-equations
Summary: Some equations for SDEs

# Infinitesmal generator (relationship between SDE and transition probabilities)
Let $x(t)$ be an Ito process that is the solution to the SDE:
$$
\begin{align}
  dx_t = u_tdt + \sigma_t dW_t
\end{align}
$$
where $u_t$ is the drift and $\sigma_t$ is the diffusion coefficient matrix and $W_t$ is a Wiener process.  Suppose we characterize this SDE via its transition density $p(x_{t+s}|x_t)$, which is the probability of the process being at $x_{t+s}$ given that it started at $x_t$.  The infinitesmal generator tells us how a function changes when the state space $x_t$ changes over an infinitesmal time interval - if for every $x_t$ we sample $x_{t+s}$ from $p(x_{t+s}|x_t)$, how does $\phi(x_{t+s})$ compare to $\phi(x_t)$?  In particular, we compare the expected value of $\phi(x_{t+s})$ to $\phi(x_t)$ as $s\to 0$ to get the infinitesmal generator.  The infinitesmal generator of the stochastic process $x_t$ defined above for a function $\phi$ is defined as
$$
\begin{align}
  \mathcal{A}\phi(x_t) = \lim_{s\to 0+}\frac{\mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right] - \phi(x_t)}{s}
\end{align}
$$
where $\mathbb{E}_{\rho_{t+s|t}}$ is the expectation with respect to the distribution for $x_{t+s}$ starting at $x_t$, i.e. $p(x_{t+s}|x_t)$ where $p(x_t'|x_t) = \delta(x_t' - x_t)$.  We can derive the expression of the generator in terms of the drift and diffusion coefficients by first computing the Ito differential of $\phi(x_\tau)$ for $\tau > t$:
$$
\begin{align}
  d\phi(x_\tau) &= \frac{\partial \phi}{\partial x_\tau^i}dx_\tau^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_\tau^i \partial x_\tau^j}dx_\tau^i dx_\tau^j
\end{align}
$$
where mixed differentials are combined according to
$$
\begin{align}
    dW_\tau dt &= 0 \\
    dt dW_\tau &= 0 \\
    dW_\tau dW_\tau^T &= Idt
\end{align}
$$

We can compute $dx_\tau^i dx_\tau^j$ as
$$
\begin{align}
  dx_\tau^i dx_\tau^j &= (u_\tau^i dt + \sigma_\tau^{ik}dW_\tau^k)(u_\tau^j dt + \sigma_\tau^{jl}dW_\tau^l) \\
  &= u_\tau^i u_\tau^j \underbrace{dt^2}_{0} + u_\tau^i \sigma_\tau^{jl}\underbrace{dt dW_\tau^l}_{0} + u_\tau^j \sigma_\tau^{ik}\underbrace{dW_\tau^k dt}_{0} + \sigma_\tau^{ik}dW_\tau^k \sigma_\tau^{jl}dW_\tau^l \\
  &= \sigma_\tau^{ik}\sigma_\tau^{jl}dW_\tau^k dW_\tau^l \\
  &= \sigma_\tau^{ik}\sigma_\tau^{jk}dt
\end{align}
$$
Plugging this into the Ito formula yields:
$$
\begin{align}
  d\phi(x_\tau) &= \frac{\partial \phi}{\partial x_\tau^i}(u_\tau^i dt + \sigma_\tau^{ij}dW_\tau^j) + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_\tau^i \partial x_\tau^j}\sigma_\tau^{ik}\sigma_\tau^{jk}dt
\end{align}
$$

This tells us that the Ito process for $\phi(x_{t+s})$ is given by
$$
\begin{align}
  \phi(x_{t+s}) = \phi(x_t) + \int_t^{t+s} \left(\frac{\partial \phi}{\partial x_\tau^i}u_\tau^i + \frac{1}{2} \frac{\partial^2 \phi}{\partial x_\tau^i \partial x_\tau^j}\sigma_\tau^{ik}\sigma_\tau^{jk}\right) d\tau + \int_t^{t+s} \frac{\partial \phi}{\partial x_\tau^i}\sigma_\tau^{ij}dW_\tau^j
\end{align}
$$
Next, we can take the expectation of both sides to remove the last term:
$$
\begin{align}
  \mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right] &= \mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_t) + \int_t^{t+s} \left(\frac{\partial \phi}{\partial x_\tau^i}u_\tau^i + \frac{1}{2} \frac{\partial^2 \phi}{\partial x_\tau^i \partial x_\tau^j}\sigma_\tau^{ik}\sigma_\tau^{jk}\right) d\tau\right] \\
  &= \phi(x_t) + \mathbb{E}_{\rho_{t+s|t}}\left[\int_t^{t+s} \left(\frac{\partial \phi}{\partial x_\tau^i}u_\tau^i + \frac{1}{2} \frac{\partial^2 \phi}{\partial x_\tau^i \partial x_\tau^j}\sigma_\tau^{ik}\sigma_\tau^{jk}\right) d\tau\right]
\end{align}
$$
The current form of this expression is called "Dynkin's formula" and we will highlight it later.  Next, we can make a linear approximation of the integral:
$$
\begin{align}
  \mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right] &= \phi(x_t) + s\mathbb{E}_{\rho_{t+s|t}}\left[\frac{\partial \phi}{\partial x_t^i}u_t^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\sigma_t^{ik}\sigma_t^{jk} + \mathcal{O}(s^2) \right] \\
  &= \phi(x_t) + s\mathbb{E}_{\rho_{t+s|t}}\left[\frac{\partial \phi}{\partial x_t^i}u_t^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\sigma_t^{ik}\sigma_t^{jk} \right] + \mathcal{O}(s^2)
\end{align}
$$
Finally, plugging this all back into the definition of the infinitesmal generator allows us to cancel terms to get:
$$
\begin{align}
  \mathcal{A}\phi(x_t) &= \lim_{s\to 0+}\frac{\mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right] - \phi(x_t)}{s} \\
  &= \lim_{s\to 0^+}\frac{\phi(x_t) + s\mathbb{E}_{\rho_{t+s|t}}\left[\frac{\partial \phi}{\partial x_t^i}u_t^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\sigma_t^{ik}\sigma_t^{jk} \right] + \mathcal{O}(s^2) - \phi(x_t)}{s} \\
  &= \lim_{s\to 0^+}\mathbb{E}_{\rho_{t+s|t}}\left[\frac{\partial \phi}{\partial x_t^i}u_t^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\sigma_t^{ik}\sigma_t^{jk} \right] + \mathcal{O}(s) \\
  &= \frac{\partial \phi}{\partial x_t^i}u_t^i + \frac{1}{2}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\sigma_t^{ik}\sigma_t^{jk}
\end{align}
$$
So we're left with our final result:
$$
\begin{align}
  \mathcal{A}\phi(x_t) = u_t(x_t)^i\frac{\partial\phi(x_t)}{\partial x_t^i} + \frac{1}{2}\sigma_t(x_t)^{ik}\sigma_t(x_t)^{jk}\frac{\partial^2\phi(x_t)}{\partial x_t^i \partial x_t^j}
\end{align}
$$

## Dynkin's formula (Expectation over transition density)
An immediate consequence of this derivation (before the linear approximation) is Dynkin's formula.  We can recognize the infinitesmal generator inside the expression for $\mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right]$:
$$
\begin{align}
  \mathbb{E}_{\rho_{t+s|t}}\left[\phi(x_{t+s})\right] &= \phi(x_t) + \mathbb{E}_{\rho_{t+s|t}}\left[\int_t^{t+s} \mathcal{A}\phi(x_\tau) d\tau\right] \\
  &= \phi(x_t) + \int_t^{t+s} \mathbb{E}_{\rho_{\tau|t}}\left[\mathcal{A}\phi(x_\tau)\right]d\tau
\end{align}
$$
In the next section we will use this formula to derive the Kolmogorov backward equation.

# Kolmogorov backward equation (Change in transition density wrt terminal time)
Let $u(s,x_t) = \mathbb{E}_{\rho_{t+s|t}}[\phi(x_{t+s})]$ denote the expected value of $\phi$ at time $s$ time units from the start of the process at time $t$ and position $x_t$.  Then the Kolmogorov backward equation is given by
$$
\begin{align}
  \frac{\partial u(s,x_t)}{\partial s} = \mathcal{A}u(s,x_t)
\end{align}
$$
Proof:
$$
\begin{align}
  \frac{\partial u(s,x_t)}{\partial s} &= \lim_{h\to 0^+}\frac{1}{h}(u(s+h,x_t) - u(s,x_t))
\end{align}
$$
Lets focus on the first term of the right hand side:
$$
\begin{align}
  u(s+h,x_t) &= \mathbb{E}_{t+s+h|t}[\phi(x_{s+h+t})] \\
  &= \int p(x_{s+h+t}|x_t)\phi(x_{s+h+t})dx_{s+h+t} \\
  &= \int p(x_{h+t}|x_t)\underbrace{\int p(x_{s+h+t}|x_{h+t})\phi(x_{s+h+t})dx_{s+h+t}}_{u(s,x_{h+t})}dx_{h+t} \\
  &= \mathbb{E}_{h+t|t}\left[u(s,x_{h+t})\right] \\
  &= u(s,x_t) + \int_t^{t+h} \mathbb{E}_{\tau|t}\left[\mathcal{A}u(s,x_\tau)\right]d\tau \quad \text{by Dynkin's formula} \\
  &= u(s,x_t) + h\mathbb{E}_{t|t}\left[\mathcal{A}u(s,x_{t})\right] + O(h^2) \\
  &= u(s,x_t) + h\mathcal{A}u(s,x_{t}) + O(h^2)
\end{align}
$$
Plugging this back into the definition of the time derivative gives us the desired result:
$$
\begin{align}
  \frac{\partial u(s,x_t)}{\partial s} &= \lim_{h\to 0^+}\frac{1}{h}(u(s+h,x_t) - u(s,x_t)) \\
  &= \lim_{h\to 0^+}\frac{1}{h}(u(s,x_t) + h\mathcal{A}u(s,x_{t}) + O(h^2) - u(s,x_t)) \\
  &= \mathcal{A}u(s,x_t)
\end{align}
$$

A particularly useful form of the Kolmogorov backward equation is when we let $\phi(x_{t+s}') = \delta(x_{t+s} - x_{t+s}')$.  Then we get that $u(s,x_t) = \mathbb{E}_{\rho_{t+s|t}}[\delta(x_{t+s} - x_{t+s}')] = p(x_{t+s}|x_t)$ is the transition density from $x_t$ to $x_{t+s}$.  So the Kolmogorov backward equation tells us how the transition density changes with respect to the ending time:
$$
\begin{align}
  \frac{\partial p(x_{t+s}|x_t)}{\partial s} = \mathcal{A}p(x_{t+s}|x_t)
\end{align}
$$

# Doob's h-transform (Conditioning a transition density on end point + corresponding SDE)
Doob's h-transform gives us a way to construct new SDEs from old ones by changing their transition densities.  Suppose we have an SDE of the form
$$
\begin{align}
  dx_t = u_tdt + \sigma_t dW_t
\end{align}
$$
with transition density $\rho_{t+s|t}$.  Doob's h-transform introduces a function $h_t$ with a special property that is used to construct a new transition density, $q_{t+s|t}$ that depends on $\rho_{t+s|t}$ and $h_t$.  Then we solve for the SDE with this new transition density.  Specifically, if $h_t(x_t) = \mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})]$, then the new transition density is given by
$$
\begin{align}
  q_{t+s|t}(x_{t+s}|x_t) = \rho_{t+s|t}(x_{t+s}|x_t)\frac{h_{t+s}(x_{t+s})}{h_t(x_t)}
\end{align}
$$
and the corresponding SDE is given by
$$
\begin{align}
  dx_t = \left(u_t + \sigma_t \sigma_t^T \nabla \log h_t\right)dt + \sigma_t dW_t
\end{align}
$$


Proof:

First, lets confirm that $q_{t+s|t}$ is a valid probability density.
$$
\begin{align}
  \int q_{t+s|t}(x_{t+s}|x_t)dx_{t+s} &= \int \rho_{t+s|t}(x_{t+s}|x_t)\frac{h_{t+s}(x_{t+s})}{h_t(x_t)}dx_{t+s} \\
  &= \frac{1}{h_t(x_t)}\int \rho_{t+s|t}(x_{t+s}|x_t)h_{t+s}(x_{t+s})dx_{t+s} \\
  &= \frac{1}{h_t(x_t)}\underbrace{\mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})]}_{h_t(x_t)} \\
  &= 1
\end{align}
$$

Next, note that $\mathcal{A}h_t = 0$ because
$$
\begin{align}
  \mathcal{A}h_t(x_t) &= \lim_{s\to 0^+}\frac{\mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})] - h_t(x_t)}{s} \\
  &= \lim_{s\to 0^+}\frac{\mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})] - \mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})]}{s} \\
  &= 0
\end{align}
$$

Now we can derive the new SDE.  We can write the infinitesmal generator of the new SDE as
$$
\begin{align}
  \mathcal{A}\phi(x_t) &= \lim_{s\to 0^+}\frac{1}{s}\left(\mathbb{E}_{q_{t+s|t}}[\phi(x_{t+s})] - \phi(x_t)\right) \\
  &= \frac{1}{h_t(x_t)}\lim_{s\to 0^+}\frac{1}{s}\left(\mathbb{E}_{\rho_{t+s|t}}[h_{t+s}(x_{t+s})\phi(x_{t+s})] - h_t(x_t)\phi(x_t)\right) \quad \because \text{multiply by $\frac{h_t(x_t)}{h_t(x_t)}$} \\
  &= \frac{1}{h_t(x_t)}\mathcal{A}(h_t \phi)(x_t) \\
  &= \frac{1}{h_t}\left[\frac{\partial h_t}{\partial t}\phi + u_t^i\underbrace{\frac{\partial \phi h_t}{\partial x_t^i}}_{\phi\frac{\partial h_t}{\partial x_t^i} + h_t\frac{\partial \phi}{\partial x_t^i}} + \frac{1}{2}\sigma_t^{ik}\sigma_t^{jk}\underbrace{\frac{\partial^2 \phi h_t}{\partial x_t^i \partial x_t^j}}_{\phi \frac{\partial^2 h_t}{\partial x_t^i \partial x_t^j} +2 \frac{\partial \phi}{\partial x_t^i}\frac{\partial h_t}{\partial x_t^j} + \frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j} h_t} \right] \\
  &= \frac{1}{h_t}\left[ \phi\underbrace{\left(\frac{\partial h_t}{\partial x_t^i} + u_t^i\frac{\partial h_t}{\partial x_t^i} + \frac{1}{2}\sigma_t^{ik}\sigma_t^{jk}\frac{\partial^2 h_t}{\partial x_t^i \partial x_t^j}\right)}_{\mathcal{A}h_t = 0} + h_t\left(\frac{\partial \phi}{\partial x_t^i}\left(u_t^i + \sigma_t^{ik}\sigma_t^{jk}\frac{\partial \log h_t}{\partial x_t^i}\right) + \frac{1}{2}\sigma_t^{ik}\sigma_t^{jk}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\right) \right] \\
  &= \frac{\partial \phi}{\partial x_t^i}\left(u_t^i + \sigma_t^{ik}\sigma_t^{jk}\frac{\partial \log h_t}{\partial x_t^i}\right) + \frac{1}{2}\sigma_t^{ik}\sigma_t^{jk}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}
\end{align}
$$
We can recognize this as the infinitesmal generator of the SDE with the form
$$
\begin{align}
  dx_t = \left(u_t + \sigma_t \sigma_t^T \nabla \log h_t\right)dt + \sigma_t dW_t
\end{align}
$$
which completes the proof.

### Conditioning an SDE on an end point
An important instance of this is where $h_t(x_t) = \rho_{T|t}(x_T|x_t)$ for some $T \gt t$.  This satisfies the condition on $h_t$ because
$$
\begin{align}
  \mathbb{E}_{\rho_{t+s|t}}[\rho_{T|t+s}(x_T|x_{t+s})] &= \int \rho_{T|t+s}(x_T|x_{t+s})\rho_{t+s|t}(x_{t+s}|x_t)dx_{t+s} \\
  &= \rho_{T|t}(x_T|x_t)
\end{align}
$$
and with this choice, the corresponding transition density is
$$
\begin{align}
  q_{t+s|t}(x_{t+s}|x_t) &= \rho_{t+s|t}(x_{t+s}|x_t)\frac{\rho_{T|t+s}(x_T|x_{t+s})}{\rho_{T|t}(x_T|x_t)} \\
  &= \rho_{t+s|t}(x_{t+s}|x_t)\frac{\rho_{T|t+s}(x_T|x_{t+s},x_t)}{\rho_{T|t}(x_T|x_t)} \quad \text{by the markov property of SDEs} \\
  &= \frac{\rho_{T,t+s|t}(x_T,x_{t+s}|x_t)}{\rho_{T|t}(x_T|x_t)} \\
  &= \rho_{t+s|t,T}(x_{t+s}|x_t,x_T)
\end{align}
$$
i.e. the transition density of the SDE conditioned on the end point $x_T$.  The equation for the SDE is
$$
\begin{align}
  dx_t = \left(u_t + \sigma_t \sigma_t^T \nabla \log \rho_{T|t}(x_T|x_t)\right)dt + \sigma_t dW_t
\end{align}
$$

# Bridge matching
Suppose $\mu_0$ and $\mu_1$ are two marginal distributions that we would like to build a bridge between.  Furthermore, we want to preserve the coupling information between $\mu_0$ and $\mu_1$, given by $\mu_{0,1}$.  A modern solution to this problem is via bridge matching.  The idea is to construct an arbitrary bridge between any individual $x_0 \sim \mu_0$ and $x_1 \sim \mu_1$ and learn an SDE whose transition density from the source distribution is given by $\rho_{t|0}(x_t|x_0) = \int \mu_{1|0}(x_1|x_0)\rho_{t|0,1}(x_t|x_0, x_1) dx_1$.  In this section we'll show how to construct this bridge, derive the corresponding SDE, and show how to learn the bridge using bridge matching.

Let $dx_t = u_tdt + \sigma_t dW_t$ be an arbitrary SDE with a fixed initial point of $x_0$, transition density $\rho_{t+s|t}$ (known in closed form) and suppose $\sigma_t$ does not depend on $x_t$.  Using Doob's h-transform, we can condition this SDE on an endpoint $x_1$ so that the SDE $dx_t = (u_t + \sigma_t\sigma_t^T \nabla \log \rho_{1|0,t}) + \sigma_tdW_t$.  This SDE has a transition density given by $\rho_{t|0,1}$ with the condition that $\rho_{1|0,1} = \delta(x_0 - x_1)$ because it must start at $x_0$ and end at $x_1$.  If we let $\rho_{t|0}(x_t|x_0) = \int \mu_{1|0}(x_1|x_0)\rho_{t|0,1}(x_t|x_0, x_1) dx_1$ be a mixture of $\rho_{t|0,1}$ over $x_1$, then clearly $\rho_{1|0}(x_1|x_0) = \mu_{1|0}(x_1|x_0)$.   So what we need to do if find an SDE that has the transition density $\rho_{t|0}(x_t|x_0)$.

It turns out that this SDE has the form
$$
\begin{align}
  dx_t = \left(u_t + \sigma_t\sigma_t^T \mathbb{E}_{\rho_{1|0,t}}\left[\nabla \log \rho_{1|0,t}\right]\right)dt + \sigma_t dW_t
\end{align}
$$
where $\rho_{1|0,t} = \frac{\mu_{1|0}\rho_{t|0,1}}{\rho_{t|0}}$ is the posterior distribution of $x_1$ given $x_0$ and $x_t$.

Proof:

First, lets guess that the target SDE has the same drift as the one for $\rho_{t|0,1}$.  The proof strategy is to apply the Fokker-planck equation to $\rho_{t|0}$ and recognize what the drift of the SDE must be.
$$
\begin{align}
   \frac{\partial \rho_{t|0}}{\partial t} &= \mathbb{E}_{1|0}\left[\frac{\partial \rho_{t|0,1}}{\partial t} \right] \\
   &= \mathbb{E}_{1|0}\left[\mathcal{A}^*\rho_{t|0,1} \right] \\
   &= \mathbb{E}_{1|0}\left[-\text{Div}(\rho_{t|0,1}(u_t + \sigma_t\sigma_t^T \nabla \log \rho_{1|0,t})) + \sigma_t\sigma_t^T \text{Div}(\nabla \rho_{t|0,1}) \right] \\
   &= -\text{Div}(\mathbb{E}_{1|0}\left[\rho_{t|0,1} \right]u_t + \sigma_t\sigma_t^T \mathbb{E}_{1|0}\left[\rho_{t|0,1}\nabla \log \rho_{1|0,t}\right]) + \sigma_t\sigma_t^T \text{Div}(\nabla \mathbb{E}_{1|0}\left[\rho_{t|0,1} \right]) \\
   &= -\text{Div}(\rho_{t|0}u_t + \sigma_t\sigma_t^T \rho_{t|0}\mathbb{E}_{1|0,t}\left[\nabla \log \rho_{1|0,t}\right]) + \sigma_t\sigma_t^T \text{Div}(\nabla \rho_{t|0}) \\
   &= -\text{Div}(\rho_{t|0}\underbrace{\left(u_t + \sigma_t\sigma_t^T \mathbb{E}_{1|0,t}\left[\nabla \log \rho_{1|0,t}\right]\right)}_{\text{drift term}}) + \sigma_t\sigma_t^T \text{Div}(\nabla \rho_{t|0})
\end{align}
$$
The second to last line is true because
$$
\begin{align}
  \mathbb{E}_{1|0}\left[\rho_{t|0,1}\nabla \log \rho_{1|0,t}\right] &= \int p(x_1|x_0)p(x_t|x_0,x_1)\nabla \log p(x_1|x_t)dx_1 \\
  &= \int p(x_t,x_1|x_0)\nabla \log p(x_1|x_t)dx_1 \\
  &= \int p(x_1|x_t,x_0)p(x_t|x_0)\nabla \log p(x_1|x_t)dx_1 \\
  &= p(x_t|x_0)\int p(x_1|x_t,x_0)\nabla \log p(x_1|x_t)dx_1 \\
  &= \rho_{t|0}\mathbb{E}_{1|0,t}\left[\nabla \log \rho_{1|0,t}\right]
\end{align}
$$

So we can see that the drift term is the same as the one in the statement.

# Bridge matching
Although we know the exact form of the SDE want to learn is
$$
\begin{align}
  dx_t = \left(u_t + \sigma_t\sigma_t^T \mathbb{E}_{\rho_{1|0,t}}\left[\nabla \log \rho_{1|0,t}\right]\right)dt + \sigma_t dW_t
\end{align}
$$
we cannot simulate it because we do not have the closed form solution for $\mathbb{E}_{\rho_{1|0,t}}\left[\nabla \log \rho_{1|0,t}\right]$.  So instead, we can learn a parametric approximation $v_\theta(x_t;x_0)$ that we can plug into the SDE instead.  The objective that we would like to minimize is the bridge matching objective:
$$
\begin{align}
  \mathcal{L}(\theta) = \int_0^1 \int \mu_{0}\int \rho_{t|0}\|\mathbb{E}_{\rho_{1|0,t}}\left[\nabla \log \rho_{1|0,t}\right] - v_\theta(x_t;x_0)\|^2 dx_t dx_1 dx_0 dt
\end{align}
$$
Using the same tricks from flow matching, we get an equivalent objective that is easier to optimize:
$$
\begin{align}
  \mathcal{L}(\theta) = \int_0^1 \int \mu_{0}\int\mu_{1|0}\int \rho_{t|0,1}\|\nabla \log \rho_{1|0,t} - v_\theta(x_t;x_0)\|^2 dx_t dx_1 dx_0 dt
\end{align}
$$

# Kolmogorov forward equation (Change in transition density wrt initial time)
Let $\rho_{t+s|t}$ be the transition density of the SDE at time $t+s$ given the process started at $x_t$.  We are interested in the quantity $\frac{\partial \rho_{t+s|t}}{\partial s}$, which is how the transition density changes as time moves forward.  Our final result will end up being
$$
\begin{align}
  \frac{\partial \rho_{t+s|t}}{\partial s} = \mathcal{A}^*\rho_{t+s|t}
\end{align}
$$
Before giving the proof for the KFE, we first need to derive the "adjoint" of the infinitesmal generator.
### Adjoint infinitesmal generator
Let $\langle \phi, \rho \rangle := \int \phi(x) \rho(x) dx$ for some functions $\phi$ and $\rho$.  The adjoint of $\mathcal{A}$, denoted by $\mathcal{A}^*$, is defined as the operator such that $\langle \mathcal{A}\phi, \rho \rangle = \langle \phi, \mathcal{A}^*\rho \rangle$.  Lets derive $\mathcal{A}^*$:
$$
\begin{align}
  \langle \mathcal{A}\phi, \rho \rangle &= \int \mathcal{A}\phi(x) \rho(x) dx \\
  &= \int \left(u_t^i\frac{\partial \phi}{\partial x_t^i} + \frac{1}{2}\sigma_t^{ik}\sigma_t^{jk}\frac{\partial^2 \phi}{\partial x_t^i \partial x_t^j}\right)\rho dx \\
  &= \int \frac{\partial \phi}{\partial x_t^i}(u_t^i\rho) dx + \frac{1}{2}\int \frac{\partial}{\partial x_t^i}\frac{\partial \phi}{\partial x_t^j}\sigma_t^{ik}\sigma_t^{jk}\rho dx \\
  &= -\int \phi \frac{\partial}{\partial x_t^i}(u_t^i\rho) dx - \frac{1}{2}\int \frac{\partial \phi}{\partial x_t^j}\frac{\partial}{\partial x_t^i}(\sigma_t^{ik}\sigma_t^{jk}\rho) dx \quad \text{ (integration by parts)}\\
  &= -\langle \phi, \frac{\partial u_t^i\rho}{\partial x_t^i} \rangle + \frac{1}{2}\int \phi \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho) dx \\
  &= -\langle \phi, \frac{\partial u_t^i\rho}{\partial x_t^i} \rangle + \langle \phi,\frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho) \rangle \\
  &= \langle \phi, -\frac{\partial u_t^i\rho}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho) \rangle \\
  &:= \langle \phi, \mathcal{A}^*\rho \rangle
\end{align}
$$
So we are left with the exression for the adjoint infinitesmal generator:
$$
\begin{align}
  \mathcal{A}^*\rho &= -\frac{\partial u_t^i\rho}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho)
\end{align}
$$

### Kolmogorov forward equation proof
Now lets prove the Kolmorogov forward equation.
Proof:
$$
\begin{align}
  \langle \phi, \frac{\partial \rho_{t+s|t}}{\partial s} \rangle &= \frac{\partial}{\partial s}\langle \phi, \rho_{t+s|t} \rangle \\
  &= \frac{\partial}{\partial s}\mathbb{E}_{\rho_{t+s|t}}[\phi(x_{t+s})] \\
  &= \frac{\partial}{\partial s}\left(\phi(x_t) + \int_t^{t+s} \mathbb{E}_{\tau|t}\left[\mathcal{A}\phi(x_\tau)\right] d\tau\right) \quad \text{by Dynkin's formula} \\
  &= \mathbb{E}_{{t+s}|t}\left[\mathcal{A}\phi(x_{t+s})\right] \quad \text{by fundamental theorem of calculus} \\
  &= \langle \mathcal{A}\phi, \rho_{t+s|t} \rangle \\
  &= \langle \phi, \mathcal{A}^*\rho_{t+s|t}\rangle \quad \text{by adjoint definition}
\end{align}
$$

Because $\phi$ is arbitrary, we have our result:
$$
\begin{align}
  \frac{\partial \rho_{t+s|t}}{\partial s} &= \mathcal{A}^*\rho_{t+s|t} \\
  &= -\frac{\partial u_t^i\rho_{t+s|t}}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho_{t+s|t})
\end{align}
$$

## Fokker-Planck equation (Change in marginal density wrt time)
The same result applies using the marginal distribution of particles, $\rho_t$.  The resulting equation is called the Fokker-Planck equation:
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} = -\frac{\partial u_t^i\rho_t}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\sigma_t^{ik}\sigma_t^{jk}\rho_t)
\end{align}
$$

# Probability flow ODE (Evolution of marginal density)
Next, we'll derive the equivalent ODE that is associated with the SDE $dx_t = u_tdt + \sigma_t dW_t$.  All we need to do is manipulate the Fokker-Plack equation to look like the continuity equation.  Also we can introduce a skew symmetric matrix $R_t^{ij}$ that to help expand the space of probability flow ODEs associated with the SDE.  Let $R_t^{ij}$ be a skew symmetric matrix $(R=-R^T)$. Note that $\frac{\partial^2 (f R_t^{ij})}{\partial x_t^i \partial x_t^j} = 0$ for any function $f$.  Next, let $\Sigma_t^{ij} = \sigma_t^{ik}\sigma_t^{jk}$.  Then we can write the Fokker-Planck equation as

$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} &= -\frac{\partial u_t^i\rho_t}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(\Sigma_t^{ij}\rho_t) + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}(R_t^{ij}\rho_t) \\
  &= -\frac{\partial u_t^i\rho_t}{\partial x_t^i} + \frac{1}{2} \frac{\partial^2}{\partial x_t^i \partial x_t^j}((\Sigma_t^{ij} + R_t^{ij})\rho_t) \\
  &= -\frac{\partial}{\partial x_t^i}\left[u_t^i\rho_t - \frac{1}{2} \frac{\partial}{\partial x_t^j}((\Sigma_t^{ij} + R_t^{ij})\rho_t) \right] \\
  &= -\frac{\partial}{\partial x_t^i}\rho_t\left[u_t^i - \frac{1}{2} \frac{1}{\rho_t} \frac{\partial}{\partial x_t^j}((\Sigma_t^{ij} + R_t^{ij})\rho_t) \right] \\
  &= -\frac{\partial}{\partial x_t^i}\left(\rho_t\left[u_t^i - \frac{1}{2}\left((\underbrace{\Sigma_t^{ij} + R_t^{ij}}_{A_t^{ij}})\frac{\partial\log \rho_t}{\partial x_t^j} + \frac{\partial\Sigma_t^{ij} + R_t^{ij}}{\partial x_t^j}\right) \right]\right) \\
  &= -\frac{\partial}{\partial x_t^i}\left(\rho_t\left[u_t^i - \frac{1}{2}\left(A_t^{ij}\frac{\partial\log \rho_t}{\partial x_t^j} + \frac{\partial A_t^{ij}}{\partial x_t^j}\right) \right]\right) \\
\end{align}
$$
Recall that the continuity equation has the form
$$
\begin{align}
  \frac{\partial \rho_t}{\partial t} = -\frac{\partial}{\partial x_t^i}(\rho_t V_t^i)
\end{align}
$$
where $V_t := \frac{dx_t}{dt}$ is a vector field that governs how samples move.  We can see that the vector field associated with the SDE is given by
$$
\begin{align}
  V_t^i &= u_t^i - \frac{1}{2}\left(A_t^{ij}\frac{\partial\log \rho_t}{\partial x_t^j} + \frac{\partial A_t^{ij}}{\partial x_t^j}\right)
\end{align}
$$
In partiular, when $A_t$ does not depend on $x$ and $\sigma_t$ is a scalar, then we can write the probability flow ODE in a more familiar form:
$$
\begin{align}
  V_t = u_t - \frac{\sigma_t^2}{2}\nabla \log \rho_t
\end{align}
$$

# Time reversal SDE (Equivalent SDE for time reversed process)
Suppose we start at time $T$ and increment time backwards using the scalar parameter $s$.  Assuming that we keep the diffusion coefficient the same, we want to find an SDE of the form
$$
\begin{align}
  d\bar{x}_s = \bar{u}_s ds + \sigma_{T-s} dW_s
\end{align}
$$
so that the marginal distribution of $\bar{x}_s$ is the same as the marginal distribution of $x_{T-s}$.  Suppose the marginal of $\bar{x}_s$ is $\bar{\rho}_s = \rho_{T - s}$.

From the previous section, we know that the probability flow ODE is given by
$$
\begin{align}
  \frac{\partial \bar{\rho}_s}{\partial s} &= -\frac{\partial}{\partial \bar{x}_s^i}\left(\bar{\rho}_s\left[\bar{u}_s^i - \frac{1}{2}\left(A_{T-s}^{ij}\frac{\partial\log \bar{\rho}_s}{\partial \bar{x}_s^j} + \frac{\partial A_{T-s}^{ij}}{\partial \bar{x}_s^j}\right) \right]\right)
\end{align}
$$
But also, we can write the probability flow ODE using the forward SDE as

$$
\begin{align}
  \frac{\partial \bar{\rho}_s}{\partial s} &= -\frac{\partial \rho_{T-s}}{\partial t} \\
  &= -\frac{\partial}{\partial x_{T-s}^i}(\rho_{T-s} (-V_{T-s}^i)) \\
  &= -\frac{\partial}{\partial x_{T-s}^i}(\rho_{T-s} (-u_{T-s}^i + \frac{1}{2}\left(A_{T-s}^{ij}\frac{\partial\log \rho_{T-s}}{\partial x_{T-s}^j} + \frac{\partial A_{T-s}^{ij}}{\partial x_{T-s}^j}\right) ))
\end{align}
$$
Using the assumption that $\bar{x}_s = \bar{x}_{T-s}$ and $\rho_{T-s} = \bar{\rho}_s$, we can simplify the above equation to
$$
\begin{align}
  &= -\frac{\partial}{\partial \bar{x}_s^i}\left(\bar{\rho}_s\left[-u_{T-s}^i + \frac{1}{2}\left(A_{T-s}^{ij}\frac{\partial\log \bar{\rho}_s}{\partial \bar{x}_s^j} + \frac{\partial A_{T-s}^{ij}}{\partial \bar{x}_s^j}\right) \right]\right) \\
  &= -\frac{\partial}{\partial \bar{x}_s^i}\left(\bar{\rho}_s\left[\underbrace{-u_{T-s}^i + \left(A_{T-s}^{ij}\frac{\partial\log \bar{\rho}_s}{\partial \bar{x}_s^j} + \frac{\partial A_{T-s}^{ij}}{\partial \bar{x}_s^j}\right)}_{\bar{u}_s} - \frac{1}{2}\left(A_{T-s}^{ij}\frac{\partial\log \bar{\rho}_s}{\partial \bar{x}_s^j} + \frac{\partial A_{T-s}^{ij}}{\partial \bar{x}_s^j}\right) \right]\right) \\
\end{align}
$$
We can recognize the drift of the time reversal SDE and so we are left with:
$$
\begin{align}
  d\bar{x}_s = \left(-u_{T-s}^i + \left(A_{T-s}^{ij}\frac{\partial\log \rho_{T-s}}{\partial \bar{x}_s^j} + \frac{\partial A_{T-s}^{ij}}{\partial \bar{x}_s^j}\right)\right)ds + \sigma_{T-s} dW_s
\end{align}
$$
In particular when $A_t$ does not depend on $x$ and $\sigma_t$ is a scalar, then we can write the backward SDE in a more familiar form:
$$
\begin{align}
  d\bar{x}_s = \left(-u_{T-s} + \sigma_{T-s}^2\nabla \log \rho_{T-s}\right)ds + \sigma_{T-s} dW_s
\end{align}
$$
