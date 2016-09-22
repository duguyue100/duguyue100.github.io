---
layout: post
title: Paper Review - Universal Intelligence - A Definition of Machine Intelligence
date: 2012-03-10
summary: 
categories: OldTimes
---

Four days ago, a friend passed me a paper called *Universal Intelligence: A Definition of Machine Intelligence*. At first, I thought this paper just proposes a wired mathematical model based on some philosophical method, because the whole section 2 is describing and explaining the so-called **Natural Intelligence**. Basically, finally I skip section 2 and start my reading from section 3. And section 3 presents a very great mathematical model. Although this model is still built on common definition, however, this model still determines a possible way to compute and measure the level of intelligence of a certain agent.

You can download this paper from [here](http://arxiv.org/abs/0712.3329). The author are **Shane Legg** from Switzerland and **Marcus Hutter** from Australia.

This post is more focusing on the mathematical deduction. If you want to find more analysis on interpretation, please go download the original paper. Now, universal intelligence is a important topic on **AGI** which refers to Artificial General Intelligence. The reason why I am interested in this topic is that I finally find a mathematical model to measure the learning or intelligence model I design. This sentence may be blurring as a low quality picture. In the near future, I would summarize the work I currently doing and show the relationship between my research and AGI.

As we know, when a human interacts with a certain environment, the human's action would get sort of feedback from environment. Usually, this feedback is simply defined as percepts. In this case, the percepts is divided into two parts: observation and reward. Since we are not just simply observe the environment all the time, via interaction, we also gain something, which is called reward from environment. For example, in a Gambling game, human get money when they won. And the money in this case is a type of reward gained from the game. Even the guy lose the money, that means his action is failed. And the model still can give a value to measure this situation. Therefore, based on our discussion, the essential elements in a intelligence system are environment, agent, actions, reward and observation.

Let $$\mathcal{A}=\{a_{1},a_{2},\ldots,a_{n}\}$$ as a finite action space, $$\mathcal{O}=\{o_{1},o_{2},\ldots,o_{n}\}$$ as a finite observation space, $$\mathcal{R}=\{r_{1},r_{2},\ldots,r_{n}\}$$ as a finite reward space which is always a subset of the rational unit interval $$[0,1]\cap\mathbb{Q}$$. Furthermore, a finite set which is called perception space $$\mathcal{P}=\mathcal{O}\times\mathcal{R}$$ is defined. As we discuss previously, the agent received perception from environment and perform a certain action. The action would also affect the perception provided by environment. Thus, the history of this agent can be denoted by $$o_{1}r_{1}a_{1}o_{2}r_{2}a_{2}o_{3}r_{3}a_{3}o_{4}\ldots$$. Normally, we denote agent as a function $$\pi$$. In this case, even though we do not have a direct way to determine the next action which will perform by agent, we can using the history to express it, for example, for $$a_{3}$$, the action is determined by $$\pi(a_{3}|o_{1}r_{1}a_{1}o_{2}r_{2})$$. The expression represent the probability of action $$a_{3}$$ in the third cycle based on the current history. This expression do not require that the environment is deterministic or full-observable. Similarly, we can define a environment $$\mu$$ based on current history. In this case, the role of environment is reversed. $$\pi$$ take action as input, therefore, environment could take observation and reward ad input. Thus, for $$o_{3}r_{3}$$, the expression could be $$\mu=(o_{3}r_{3}|o_{1}r_{1}a_{1}o_{2}r_{2}a_{2})$$. Based on this discussion, we can denote agent $$\pi$$ and environment $$\mu$$ as:

$$\pi(a_{i}|o_{1}r_{1}a_{1}o_{2}r_{2}a_{2}\ldots o_{i-1}r_{i-1})$$

$$\mu(o_{k}r_{k}|o_{1}r_{1}a_{1}o_{2}r_{2}a_{2}\ldots o_{k-1}r_{k-1}a_{k-1})$$

where $$i,k\geq 1$$.

In order to control how short term greedy, or long farsighted, the agent would be, the author proposed a discounting parameter $$\gamma\in (0,1)$$ to perform this role. Till now, we have defined agent, environment and found out the measure of success. Thus, for the infinite future, we can use these three definition to work out a expected value for a given agent and environment. We denote this expected value function as:

$$V_{\mu}^{\pi}(\gamma)=\frac{1}{\Gamma}\mathbf{E}(\sum_{i=1}^{\infty}\gamma^{i}r_{i})$$

where $$\Gamma=\sum_{i=1}^{\infty}\gamma^{i}$$ is the normalizing constant. If we examine this value equation here, we would find that $$\gamma$$ plays two roles. Firstly, $$\gamma$$ is able to normalize received rewards so that the sum is always finite. Secondly, $$\gamma$$ weights the reward at different points in the future. However, if we remove $$\gamma$$ and require the total reward returned by environment can never exceed 1, we can simplify the value equation as:

$$V_{\mu}^{\pi}=\mathbf{E}(\sum_{i=1}^{\infty}r_{i})\leq 1$$

Here, it's like that we give an additional constraint for reward. In section 5.2, the author discussed why this constraint is reasonable.

As we are familiar with, for a certain question, we may have several different way to solve it. Thus, we propose Occam's razor here to help us determine the decision made by agent:

>Given multiple hypotheses that are consistent with the data, the simplest should be preferred.

Besides the Occam's razor, we also need to calculate the environment complexity because when a agent get the same reward in a high complexity environment rather than a low complexity one, the agent could be considered as more intelligent. Here, author employ Kolmogorov complexity to compute environment complexity.

Kolmogorov complexity of a binary string $$x$$ is defined as being the length of the shorest program that compute $$x$$:

$$K(x)=\min_{p}\{l(p):\mathcal{U}(p)=x\}$$

where $$p$$ is a binary string which we call a *program*, $$l(p)$$ is the length of this string in bits, and $$\mathcal{U}$$ is a prefix universal Turing machine $$\mathcal{U}$$ called the *reference machine*.

For a certain environment space $$E=\{\mu_{1},\mu_{2},\ldots\}$$. We can simply encode the index of $$\mu_{i}$$ as a binary string, written as $$\langle i\rangle$$. For a certain reference machine, we can represent $$K(\mu_{i})$$ as $$K(\langle i\rangle)$$.

If we had described the environment $$\mu$$ in binary string, each additional bit of program length to reduce the environment's probability by one half, because the fact that each bit has two possible states. Thus, we can use the algorithmic probability distribution over the environment space, defined $$2^{-K(\mu)}$$.

Now, it is the time we can build a function which can calculate the universal intelligence of a agent $$\pi$$. Let $$E$$ as environment space, a reference machine $$\mathcal{U}$$. Let $$K$$ as the Kolmogorov complexity function. The expected performance of agent $$\pi$$ with respect to the universal distribution $$2^{-K(\mu)}$$ over the space of all environments $$E$$ is given by:

$$\Upsilon(\pi)=\sum_{\mu\in E}2^{-K(\mu)}V_{\mu}^{\pi}$$

And the equation above is the **universal intelligence** of agent $$\pi$$.

Just for record, this post is just a short introduction which shows how to the universal intelligence finally. I would write more explanation about this topic.

If you have any question or you have strong interest on this topic, I hope you can leave your comment below.
