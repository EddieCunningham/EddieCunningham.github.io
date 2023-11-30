Title: Score matching with CNFs
Date: 2023-11-25
Category: Blog
status: hidden
Slug: score-matching-cnf
Summary: Training CNFs with score matching

# Score function dynamics
First lets see how the gradient of any time-dependent function changes w.r.t. time.  Let $f_t$ be a time-dependent function.  Then
$$
\begin{align}
  \frac{d}{dt}\frac{\partial f_t}{\partial x_t^i} &= \frac{d}{dt}\frac{\partial x_0^j}{\partial x_t^i}\frac{\partial f_t}{\partial x_0^j} \\
  &= \left(\frac{d}{dt}\frac{\partial x_0^j}{\partial x_t^i}\right)\frac{\partial f_t}{\partial x_0^j} + \frac{\partial x_0^j}{\partial x_t^i}\left(\frac{d}{dt}\frac{\partial f_t}{\partial x_0^j}\right) \\
  &= \left( -\frac{\partial x_0^j}{\partial x_t^k} \frac{\partial u_t^k}{\partial x_t^i} \right)\frac{\partial f_t}{\partial x_0^j} + \frac{\partial x_0^j}{\partial x_t^i}\left(\frac{\partial}{\partial x_0^j}\frac{d f_t}{dt}\right) \\
  &= -\frac{\partial u_t^k}{\partial x_t^i}\frac{\partial f_t}{\partial x_t^k} + \frac{\partial}{\partial x_t^i}\frac{d f_t}{dt}
\end{align}
$$
In operator form, we can write:
$$
\frac{d}{dt}\frac{\partial}{\partial x_t^i} = -\frac{\partial u_t^k}{\partial x_t^i}\frac{\partial}{\partial x_t^k} + \frac{\partial}{\partial x_t^i}\frac{d}{dt}
$$

So plugging in $\log p_t$ for $f_t$, we have that
$$
\begin{align}
  \frac{d}{dt}\frac{\partial \log p_t}{\partial x_t^i} &= -\frac{\partial u_t^k}{\partial x_t^i}\frac{\partial \log p_t}{\partial x_t^k} + \frac{\partial}{\partial x_t^i}\frac{d \log p_t}{dt} \\
  &= -\frac{\partial u_t^k}{\partial x_t^i}\frac{\partial \log p_t}{\partial x_t^k} - \frac{\partial}{\partial x_t^i}\frac{\partial u_t^k}{\partial x_t^k}
\end{align}
$$
which in matrix notation is:
$$
\frac{d}{dt}\nabla \log p_t = -\nabla u_t^T\nabla \log p_t - \nabla \text{Tr}(\nabla u_t)
$$
