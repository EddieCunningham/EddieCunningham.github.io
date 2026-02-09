- Suppose you are given a dataset.  What is the best representation of data?
  - We are thinking about this problem from an ICA perspective - we assume that there are some underlying independent components that generate the data.
  - We want these components to also be good representations of the data.  How should we define "good representation?"
  - Given our intuition for information, we might want a good representation to have high mutual information with the data while also being low dimensional.  For the moment, lets not be technical and use our intuition to describe what we want.
    - What does this mean?  High mutual information should mean that knowing the representation tells us a lot about the data.
    - Take data that comes from a noisy circle.  Intuitively, a good representation seems to be the angle of the point on the circle because you can identify points on the circle easily using just the angle if you assume that there is noise.
    - Take data whose distribution looks like a tube in $\mathbb{R}^3$ with an ellipse cross section.
      - There is still an obvious choice for a single dimension representation of the data, which is the distance along the tube.
      - However, we need to make a decision about how to decompose the noise dimensions.
      - For this ellipse, we can decompose the noise into the major axis and the minor axis.
      - Why? It seems useful because these are aligned with the principal components of the noise.
    - But what if we have some more complicated data so that the probability distribution might not have a simple decomposition?
      - Try to find some example here.
    - Foreshadowing: It sort of seems like we were able to say that the angle is a good representation because we were able to decompose the data into a product of the angle and the noise.
  - So how do we make this rigorous?  This gets tricky because information needs to be described using a probability measure on the data space, which is not compatible with low dimensional manifolds.
    - If a representation is low dimensional, then maybe its sections (level sets?) are low dimensional manifolds in the data space.
    - However, the information about data is described using a probability measure on $\mathcal{P}(\mathbb{R}^n)$.  This measure cannot say anything about the information contained in the representation because the sections have measure zero in $\mathcal{P}(\mathbb{R}^n)$.
    - Saying that there is a stochastic relationship between the representation doesn't work for our setting because the independent components are deterministically related to the data.
  - To start, we can look to at PCA because in PCA is a well known dimensionality reduction technique that offers a useful representation of the data that is deterministically related to the data.
    1) PCA can be interpreted as a linear normalizing flow trained for max likelihood on data, but with a Jacobian matrix whose columns are orthogonal to each other.
    2) This matrix structure is the result of asserting that the flow is the solution to a dimensionality reduction problem.
    3) Taking the coordinate with maximum variance intuitively seems like a good way to reduce the dimensionality of the data.
    4) Foreshadowing: The information contained in the linear flow can be decomposed exactly into the information of its coordinates.
  - From our examples and PCA, we can see that having coordinates that are orthogonal to each other is a good thing.  Specifically, in PCA we showed that this orthogonality is the result of the flow being the solution to a dimensionality reduction problem.
  - Is there a way to generalize this idea to beyond linear flows?
  - We need to come up with a dimensionality reduction problem for a flow whose solution has orthogonal coordinates.
    - A first attempt might be to use the standard Euclidean distance in the data space to penalize the reconstruction error of the flow.
    - However, this ends up being difficult to work with because when you try to work out the details.
  - Rather than penalizing the squared error between data and its orthogonal projection to a coordinate manifold, we can penalize the squared error between data and its "flow based projection" to a coordinate manifold.
  - This flow based projection transports a point in the data space along a curve in the data space that is obtained by varying off-manifold coordinates while holding the on-manifold coordinates fixed.
  - This flow based projection reduces to the orthogonal projection when the flow is linear.
  - To say anything about this, we need to introduce some machinery from differential geometry.
    - We define a coordinate curve as the image of a coordinate axis in the base space in the data space.
    - We can define a flow (not normalizing flow, this refers to the concept from differential geometry) on the coordinate curve as a one-parameter family of diffeomorphisms that transports a point along the coordinate curve to another point.
    - It is useful to know how this flow varies with respect to modifications to various parameters.
      - For instance, the flow depends on the choice of diffeomorphism and the speed at which points on the flow move along the coordinate curve.
    - The length of the coordinate curve is then defined as the integral of the norm of the velocity vector along the coordinate curve.
  - We are interested in finding the diffeomorphism that minimizes the length of the coordinate curve.
  - To start, we can consider an easier, but equivalent, problem to work with - energy minimization.
    - The energy of the flow is defined as the integral of the square of the norm of the velocity vector along the coordinate curve.
    - This is not invariant under reparameterization, so we can use the Euler-Lagrange equation to find the geodesic equation that the flow optimal must satisfy.
    - The geodesic equation removes the dependence on the choice of parametrization of the coordinate curve, but we still need to see how the energy depends on the choice of diffeomorphism.
    - Before we take the variation with respect to the choice of diffeomorphism, we need to add the geodesic equation as a constraint and also the fact that the diffeomorphism pushes the prior to the data distributions as a constraint by ensuring that the log likelihood of the data distribution and the normalizing flow are equal.
    - We can add the geodesic equation as a Lagrangian multiplier to the energy minimization problem, and then take a variation with respect to the choice of diffeomorphism.




- But do orthogonal coordinates always exist?
  - Is the pullback metric isometric to a diagonal metric?
  - The question is whether or not the pullback metric can be diagonalized.
  - The metric is only diagonalizable when the off-diagonal terms of the Riemann curvature tensor are zero.
  - To see the implications of this, we need to see what the Riemann curvature tensor is for a given pullback metric assocaited with a probability density function $\rho$.









- Now that we have representations of data that decompose information, can we use this to construct low dimensional coding algorithms?
  - Construct a huffman code for the data space using the orthogonal coordinates.
  - Could use this to relate depth of huffman code tree to information in the data.
  - Low dimensional huffman code could refer to a prefix tree of the huffman code tree.
  - Could we then use this to construct efficient decision trees?
  - Could we also learn a hyperbolic embedding of the huffman code for a given data point?

<!--
- My story:
  - Back when I was working at Garmin, I worked on the algorithms and then GPS team.  The very first project that I worked on was a sleep stage detection algorithm that was supposed to be based on

  a deep dive into Bayesian probabilitstic modeling in general.
  - I learned about state -->