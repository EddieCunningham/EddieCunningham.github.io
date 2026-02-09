
% \begin{proposition}[No continuous deformation from OCT-ICs]
%     Suppose $\fb_0 \in \mathcal{F}_{\text{OCT}}$ and let $\fb_t$ be a smooth deformation of $\fb_0$.  Then $\fb_t$ has the same principal manifolds as $\fb_0$.
% \end{proposition}
% \begin{proof}
%     We will show that the Jacobian matrices of $\fb_0$ and $\fb_t$ both have the same left singular vectors.  To do this, first lets look at how the Jacobian matrix of $\fb_t$ changes at $t=0$.  Suppose there is a flow $\Phi_t$ that is defined by flowing on the time dependent vector field, $\mathbf{X}_t$.  Then $\fb_t = \Phi_t \circ \fb_0$ is defined as
%     \begin{align}
%         \fb_t = \fb_0 + \int_0^t \mathbf{X}_t dt
%     \end{align}
%     Let $\mathbf{J}_t = \frac{d\fb_t}{d\zb}$ be the Jacobian matrix of $\fb_t$.  \cref{cor:time derivative of gradient function in gradient field} tells us that the time derivative of $\mathbf{J}_t$ is
%     \begin{align}
%         \frac{d\mathbf{J}_t}{dt} = \nabla \mathbf{X}_t \mathbf{J}_t
%     \end{align}
%     Since we assume that $\fb_t \in \mathcal{F}_{\text{OCT}}$, the singular value decomposition of $\mathbf{J}_t$ is the product of an orthogonal matrix $\mathbf{U}$ and diagonal matrix $\mathbf{S}_t$, so $\mathbf{J}_t = \mathbf{U}_t\mathbf{S}_t$.  We can solve $\mathbf{U}_t$ directly and write it in terms of $\mathbf{U}_t$ and $\mathbf{S}_t$:
%     \begin{align}
%         \nabla \mathbf{X}_t &= \frac{d\mathbf{J}_t}{dt}\mathbf{J}_t^{-1} \\
%         &= \frac{d \mathbf{U}_t\mathbf{S}_t}{dt}\mathbf{S}_t^{-1}\mathbf{U}_t^T \\
%         &= \frac{d \mathbf{U}_t}{dt}\mathbf{U}_t + \mathbf{U}_t \frac{d\log \mathbf{S}_t}{dt}\mathbf{U}_t^T
%     \end{align}
%     A requirement that must be satisfied for $\fb_t \in \mathcal{F}_{\text{OCT}}$ is that $\frac{d\log \mathbf{S}_t}{dt}$ must be diagonal.  However, as we will see next, this condition implies that $\frac{d\mathbf{U}_t}{dt} = 0$.

%     Lets solve for $\frac{d\log \mathbf{S}_t}{dt}$ directly:
%     \begin{align}
%         \frac{d\log \mathbf{S}_t}{dt} = \mathbf{U}_t^T \nabla \mathbf{X}_t \mathbf{U}_t + \mathbf{U}_t^T \frac{d\mathbf{U}_t}{dt}
%     \end{align}
% \end{proof}