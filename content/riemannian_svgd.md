Title: Riemannian stein variational gradient descent
Date: 2023-07-15
Modified: 2023-07-15
Category: Blog
Tags: stein discrepancy, kernels, stein variational gradient descent, rkhs
Slug: stein-vi
Summary: A tutorial on Stein variational gradient descent

The Stein discrepancy measure is a way of measuring the distance between two probability distributions.  It is used in Stein variational gradient descent (SVGD) to construct a flow that minimizes the reverse KL divergence to a target distribution.  In this post, we'll go over the kernel Stein discrepancy as introduced by [Liu et al.](https://arxiv.org/pdf/1602.03253.pdf) and the extensions in [Liu and Zhu](https://arxiv.org/pdf/1711.11216.pdf).

# Motivation
Consider the task of minimizing the reverse KL divergence between a target distribution $p$ and a model distribution $q$ over a Riemannian manifold $(\mathcal{M},g)$.  If we have a probability path as the solution where $q_t$ where $q_0$ is arbitrary and $q_1 = p$, then we could be interested in seeing how the reverse KL divergence between $q_t$ and $p$ changes as $t$ changes.

Let $(q_t, V_t)$ be a probability path between $q_0$ and $q_1$ where $V_t\in \mathfrak{X}(\mathcal{M})$ is the vector field that generates the flow of $q_t$ and let $\omega_g$ be the volume form on $\mathcal{M}$.  Then the time derivative of the reverse KL divergence is:
$$
\begin{align}
  \frac{d}{dt}\text{KL}\left[q_t||p\right] &= \int \frac{d}{dt}q_t\log \frac{q_t}{p}\omega_g \\
  &= \int \left((\frac{d q_t}{dt})\log \frac{q_t}{p} + q_t\frac{d \log q}{dt}\right)\omega_g \\
  &= \int \left(-\text{Div}(q_t V_t) \log \frac{q_t}{p} + \underbrace{\frac{d q}{dt}}_{\text{$0$ in expectation}}\right)\omega_g \\
  &= \int \langle \text{grad } \log \frac{q_t}{p} , q_t V_t\rangle_g\omega_g \\
  &= \int q_t\left( \langle \text{grad } \log q_t , V_t\rangle_g - \langle \text{grad } \log p, V_t\rangle_g \right)\omega_g \\
  &= \int \langle \text{grad } q_t , V_t\rangle_g \omega_g - \int q_t\langle \text{grad } \log p, V_t\rangle_g \omega_g \\
  &= -\int q_t \text{Div}(V_t) \omega_g - \int q_t\langle \text{grad } \log p, V_t\rangle_g \omega_g \\
  &= -\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, V_t \rangle_g + \text{Div}(V_t)\right]
\end{align}
$$

Notice that if $V_t$ is nonvanishing except when $\text{KL}\left[q_t||p\right] = 0$, then $\text{KL}\left[q_t||p\right] = 0$ if and only if $\frac{d}{dt}\text{KL}\left[q_t||p\right] = 0$ which only happens at $t=1$, which implies that
$$
\begin{align}
\mathbb{E}_{p}\left[\langle \text{grad } \log p, V_t \rangle_g + \text{Div}(V_t)\right] = 0
\end{align}
$$
This is called the result in theorem 2 of [Liu et al.](https://arxiv.org/pdf/1711.11216.pdf).  The integrand is called the generalized Stein operator:
$$
\begin{align}
\mathcal{A}_p V_t = \langle \text{grad } \log p, V_t \rangle_g + \text{Div}(V_t)
\end{align}
$$

## Finding the direction of steepest descent
Next we'll show how to construct the $V_t$ that maximizes the time derivative of the reverse KL divergence.  Specifically, we want to choose a space called $\mathfrak{X}$ that is equipped with some metric so to find
$$
\begin{align}
  \text{Loss}\left(V_t\right) &= \min_{V_t\in \mathfrak{X}} \frac{d}{dt}\text{KL}\left[q_t||p\right] \\
  &= \min_{V_t\in \mathfrak{X}}-\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, V_t \rangle_g + \text{Div}(V_t)\right] \\
  &= \max_{V_t\in \mathfrak{X}}\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, V_t \rangle_g + \text{Div}(V_t)\right]
\end{align}
$$

[Liu et al.](https://arxiv.org/pdf/1711.11216.pdf) proposes looking at the space of vector fields that are the gradient of some function $f$:
$$
\begin{align}
  \mathfrak{X} = \left\{V_t = \text{grad } f \mid f \in \mathcal{H}_K \right\}
\end{align}
$$
where $\mathcal{H}_k$ is a reproducing kernel Hilbert space (RKHS) with kernel $K$.  Check out my [post on RKHS](reproducing_kernel_hilbert_space.md) for a quick introduction to RKHS and derivations of the properties that we'll use here.  Say that $V_t = \text{grad } f_t$.  Also recall that $\text{grad } f_t = \langle f_t, \text{grad }  K_x \rangle_{\mathcal{H}_K}$ and $\text{Div}(\text{grad } f_t) = \langle f_t, \text{Div}(\text{grad }  K_x) \rangle_{\mathcal{H}_K}$.

Then we can simplify the objective further by rewriting $V_t$ in terms of $f_t$:
$$
\begin{align}
  \text{Loss}\left(f_t\right) &= \max_{f_t \in \mathcal{H}_K}\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, \text{grad } f_t \rangle_g + \text{Div}(\text{grad } f_t)\right] \\
  &= \max_{f_t \in \mathcal{H}_K}\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, \langle f_t, \text{grad }  K_x \rangle_{\mathcal{H}_K} \rangle_g + \langle f_t, \text{Div}(\text{grad }  K_x) \rangle_{\mathcal{H}_K}\right] \\
  &= \max_{f_t \in \mathcal{H}_K}\langle f_t, \mathbb{E}_{q_t}\left[\langle \text{grad } \log p, \text{grad }  K_x \rangle_g \right]\rangle_{\mathcal{H}_K} + \langle f_t, \mathbb{E}_{q_t}\left[\text{Div}(\text{grad }  K_x) \right] \rangle_{\mathcal{H}_K} \\
  &= \max_{f_t \in \mathcal{H}_K} \langle f_t, \underbrace{\mathbb{E}_{q_t}\left[\langle \text{grad } \log p, \text{grad }  K_x \rangle_g + \text{Div}(\text{grad }  K_x)\right]}_{\hat{f}_t}\rangle_{\mathcal{H}_K} \\
  &= \max_{f_t \in \mathcal{H}_K} \langle f_t, \hat{f}_t\rangle_{\mathcal{H}_K}
\end{align}
$$

Clearly we obtain best loss when we choose $f_t = \hat{f}_t$ (up to a scaling constant), so the vector field that minimizes the rate of change of the reverse KL divergence is
$$
\begin{align}
  V_t^* &= \text{grad } \hat{f}_t \\
  &= \text{grad } \mathbb{E}_{q_t}\left[\langle \text{grad } \log p, \text{grad }  K_x \rangle_g + \text{Div}(\text{grad }  K_x)\right]
\end{align}
$$

