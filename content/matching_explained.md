Title: Flow/score matching explained
Date: 2023-11-06
Modified: 2023-11-06
Category: Blog
Tags: flow matching, score matching, conditional probability paths
Slug: matching-explained
status: hidden
Summary: An overview of flow matching and score matching

The field of generative modelling has undergone extraordinary advancements over the past few years due to the ability to parametrize generative models with unrestricted neural network architectures and train them extremely efficiently.  At the forefront of these methods are diffusion models, which learn to undo a process that progressively turns data to random Gaussian noise.  However, diffusion models are not the only class of successful generative models.  Recently continuous normalizing flows have been shown to be competitive with diffusion models in terms of sample quality and due to breakthroughs in how to train them in a simulation free way.  At the heart of these success is a new way to learn generative models based on learning a **probability path** between a prior and target probability distribution.  In this post we'll go over how to construct probability paths and how to use them to train generative models.

# Problem setting
Let $p_\text{data}(x)$ be an unknown probability distribution whose samples represent elements of a dataset.  For example, we posit that a dataset $\mathcal{D}$ consists of a finite number of samples from $p_\text{data}(x)$.  Our goal is to learn a parametric approximation of $p_\text{data}(x)$, denoted by $p_\theta(x)$, that we can sample from.  In order to do this, we will want to devise a procedure to turn samples from a known prior called $p_0(x_0)$ into samples from $p_\text{data}$.

Traditionally this was done using likelihood based methods where we would maximize the likelihood of the data under the model $p_\theta$.  However, the methods that are used to train modern generative models are fundamentally different.  Instead, we will first **construct** a time-dependent probability distribution $p_t(x_t)$ so that $p_{t=0} = p_0$ and $p_{t=1} = p_1$ and then learn a time-dependent neural network that we can use to sample from $p_t(x_t)$ at any time $t$.

# Probability paths


Lets construct a probability path between any prior distribution $p_0$ and target $p_\text{data}$.  In other words, lets write down the expression for a $p_t(x_t)$ that satisfies $p_{t=0} = p_0$ and $p_{t=1} = p_1$.  The trick is to assume that $p_t(x_t)$ is a marginal distribution:
$$
\begin{align}
  p_t(x_t) = \int p_1(x_1)p_t(x_t|x_1)dx_1
\end{align}
$$
where $p_1 := p_\text{data}$.  The choice of setting $p_1 = p_\text{data}$ is deliberate because it means that we can pull samples from $p_t(x_t)$ by first sampling $x_1 \sim p_1$ and then $x_t \sim p_t(x_t|x_1)$.  Next we need to choose $p_t(x_t|x_1)$ so that $p_{t=0} = p_0$ and $p_{t=1} = p_1$.  A simple choice (that is used in practice) is to use a Gaussian: $p_t(x_t|x_1) = N(x_t|\mu_t(x_1), \Sigma_t(x_1))$ with appropriately chosen