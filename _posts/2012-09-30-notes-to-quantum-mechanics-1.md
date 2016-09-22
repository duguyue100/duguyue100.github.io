---
layout: post
title: Learning Notes to Quantum Mechanics 1
date: 2012-09-30
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

Quantum Mechanics might be the most difficult and simplest theory in the world. The assumption and foundation of Quantum Mechanics is extremely simple, but the analysis and interpretation is extremely complex. I'm learning Quantum Mechanics because of research purposes, some methods in my research topics have to take ideas from Quantum Mechanics.

The book I'm using is a popular book from David J. Griffiths which is a great scholar from Reed College. The book is named *[Introduction to Quantum Mechanics](http://www.amazon.com/Introduction-Quantum-Mechanics-2nd-Edition/dp/0131118927): Second Edition*. I encourage you to buy a hard copy of book because the book is written in a fascinating way. This book is also a practical book which carries many questions. You can find the solution manual everywhere from internet. (I forget where I get it.)

In addition, this note is only for self revision, nothing to do with teaching or lecturing. OK, let's start our first question, "*how does Quantum Mechanics measure particle?*"

###Schrödinger Equation

To measure a particle, Quantum Mechanics approaches the problem by solving *Schrödinger Equation*.

$$\large i\hbar\frac{\partial\Psi}{\partial t}=-\frac{\hbar^{2}}{2m}\frac{\partial^{2}\Psi}{\partial x^{2}}+V\Psi.$$

where $$i$$ is the square root of –1, and $$\hbar$$ is Planck's constant which is his original constant $$(h)$$ divided by $$2\pi$$:

$$\large\hbar=\frac{h}{2\pi}\]$$

###The Statistical Interpretation

Schrödinger Equation plays a role like Newton's Second Law. But how can such an object represent the state of a particle? The answer is provide by Born's statistical interpretation of the wave function.

$$\large\int_{a}^{b}|\Psi(x,t)|^{2}dx=\left\{\begin{array}{l}\text{probability of finding the particle} \\ \text{between } a \text{ and }b\text{, at time }t\end{array}\right\}$$

Probability is the area under the graph of $$|\Psi|^{2}$$. This equation means that $$|\Psi|^{2}$$ gives the probability of finding the particle at point $$x$$, at time $$t$$ between $$a$$ and $$b$$.


###Probability with Continuous Variable

The probability that an individual (chosen at random) lies between $$x$$ and $$x+dx$$ is given as $$\rho(x)dx$$ (probability density). Therefore, the probability that $$x$$ lies between $$a$$ and $$b$$ (a finite interval) is given by the integral of $$\rho(x)$$.

$$\large P_{ab}=\int_{a}^{b}\rho(x)dx$$

And some probability rules are:

$$\large 1=\int_{-\infty}^{+\infty}\rho(x)dx,$$

$$\large\langle x\rangle=\int_{-\infty}^{+\infty}x\rho(x)dx,$$

$$\large\langle f(x)\rangle=\int_{-\infty}^{+\infty}f(x)\rho(x)dx$$

$$\large\sigma^{2}\equiv\langle(\Delta x)^{2}\rangle=\langle x^{2}\rangle-\langle x\rangle^{2}$$

###Normalization

According to probability of continuous variable,

$$\large\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=1.$$

Here, we need to prove a important idea which is: if $$\Psi$$ s normalized at $$t=0$$, it stays normalized for all future time. To begin with

$$\large\frac{d}{dt}\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=\int_{-\infty}^{+\infty}\frac{\partial}{\partial t}|\Psi(x,t)|^{2}dx$$

By the produce rule:

$$\large\frac{\partial}{\partial t}|\Psi|^{2}=\frac{\partial}{\partial t}(\Psi^{*}\Psi)=\Psi^{*}\frac{\partial\Psi}{\partial t}+\frac{\partial\Psi^{*}}{\partial t}\Psi$$

Notice that (according to  Schrödinger Equation):

$$\large\frac{\partial\Psi^{*}}{\partial t}=-\frac{i\hbar}{2m}\frac{\partial^{2}\Psi^{*}}{\partial x^{2}}+\frac{i}{\hbar}V\Psi^{*}$$

so

$$\large\frac{\partial}{\partial t}|\Psi|^{2}=\frac{i\habar}{2m}(\Psi^{*}\frac{\partial^{2}\Psi}{\partial x^{2}}-\frac{\partial^{2}\Psi^{*}}{\partial x^{2}})$$

Now, we can get

$$\large\frac{d}{dt}\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=\frac{i\hbar}{2m}(\Psi^{*}\frac{\partial\Psi}{\partial x}-\frac{\partial\Psi^{*}}{\partial x}\Psi)\Big\vert_{-\infty}^{+\infty}$$

$$\Psi$$ must go to zero as $$x$$ goes to infinity---otherwise the wave function would not be normalizable. It follows that

$$\large\frac{d}{dt}\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=0$$

and hence that the integral is constant (independent of time); if $$\Psi$$ is normalized at t=0, it stays normalized for all future time.

###Momentum

First, I need to introduce a law from product rule

$$\large\int_{a}^{b}f\frac{dg}{dx}dx=-\int_{a}^{b}\frac{df}{dg}gdx+fg\vert_{a}^{b}.$$

We can get expectation value of velocity, where the final equation is:

$$\large\langle v\rangle=\frac{d\langle x\rangle}{dt}=-\frac{i\hbar}{m}\int\Psi^{*}\frac{\partial\Psi}{\partial x}dx$$

And thus the momentum is represented as

$$\large\langle p\rangle=m\langle v\rangle=-i\hbar\int(\Psi^{*}\frac{\partial\Psi}{\partial x})dx.$$

Let's write the expressions in more suggestive way. (They are so symmetric!)

$$\large\langle x\rangle=\int\Psi^{*}(x)\Psi dx$$

$$\large\langle p\rangle=\int\Psi^{*}(\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx$$

Actually, the reason why momentum expression is powerful is because you can represent any quantity , $$Q(x,p)$$ by simply replacing every $$p$$ by $$(\hbar/i)(\partial/\partial x)$$, inserting the resulting operator between $$\Psi^{*}$$ and $$\Psi$$, and integrating:

$$\large\langle Q(x,p)\rangle=\int\Psi^{*}Q(x,\frac{\hbar}{i}\frac{\partial}{\partial x})\Psi dx$$

The equation is a recipe for computing the expectation value of any dynamical quantity, for a particle in state $$\Psi$$.

###The Uncertainty Principle

To any wave phenomenon, and hence in particular to the quantum mechanical wave function. Now the Wavelength of $$\Psi$$ is related to the momentum of the particle by the *de Broglie formula*.

$$\large p=\frac{h}{\lambda}=\frac{2\pi\hbar}{\lambda}$$

And Heisenberg's famous *uncertainty principle*

$$\large\sigma_{x}\sigma_{p}\geq\frac{\hbar}{2}$$
