---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 5
date: 2013-10-27
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

###1. Uncertainty Principle and Particle Current 

####1.1. Momentum, position, and the uncertainty principle

For momentum, we write an operator $$ {\hat{p}}$$. We postulate this can be written as

$$\hat{p}\equiv-i\hbar\nabla$$

with

$$\nabla\equiv\vec{x}_{o}\frac{\partial}{\partial x}+\vec{y}_{o}\frac{\partial}{\partial y}+\vec{y}_{o}\frac{\partial}{\partial y}$$

where $$ {\vec{x}_{o}}$$, $$ {\vec{y}_{o}}$$ and $$ {\vec{z}_{o}}$$ are unit vectors in the $$ {x}$$, $$ {y}$$ and $$ {z}$$ directions. With this postulated form, we find that

$$\frac{\hat{p}^{2}}{2m}\equiv-\frac{\hbar^{2}}{2m}\nabla^{2}$$

and we have a correspondence between the classical notion of the energy $$ {E}$$.

$$E=\frac{\hat{p}^{2}}{2m}+V$$

and the corresponding Hamiltonian operator of the Schroedinger equation

$$\hat{H}=-\frac{\hbar^{2}}{2m}\nabla^{2}+V=\frac{\hat{p}^{2}}{2m}+V$$

Note that

$$\hat{p}\exp(i\vec{k}\cdot\vec{r})=i\hbar\nabla\exp(i\vec{k}\cdot\vec{r})=\hbar\vec{k}\exp(i\vec{k}\cdot\vec{r})$$

This means the plane waves $$ {\exp(i\vec{k}\cdot\vec{r})}$$ are the eigenfunctions of the operator $$ {\hat{p}}$$ with eigenvalues of the operator $$ {\hat{p}}$$ with eigenvalues $$ {\hbar\vec{k}}$$.

We can therefore say for these eigenstates that the momentum is $$ {\vec{p}=\hbar\vec{k}}$$. Note that $$ {\vec{p}}$$ is a vector, with three components with scalar values and it is not an operator here.

For the position operator, the postulated operator is almost trivial when we are working with functions of position. It is simply the position vector $$ {\vec{r}}$$ itself. At least when we are working in a representation that is in term of position, we therefore typically do not write $$ {\hat{\vec{r}}}$$ through rigorously we should. The operator for the $$ {z}$$-component of position would, for example, also simply be $$ {z}$$ itself.

Here we illustrate the position-momentum uncertainty principle by example. We have looked at a Gaussian wavepacket before, we could write this as the sum over waves of different $$ {k}$$-values, with Gaussian weights, or we could take the limit of that process by using an integration.

$$\Psi_{G}(z,t)\propto\int_{k}\exp\left[-\left(\frac{k-\bar{k}}{2\Delta k}\right)^{2}\right]\exp\{-i[\omega(k)t-kz]\}\,dk$$

We could rewrite the above equation at time $$ {t=0}$$ as

$$\Psi(z,0)=\int_{k}\Psi_{k}(k)\exp(ikz)\,dk$$

where

$$\Psi_{k}(k)\propto\exp\left[-\left(\frac{k-\bar{k}}{2\Delta k}\right)^{2}\right]$$

$$ {\Psi_{k}(k)}$$ is the representation of the wave function in $$ {k}$$ space. $$ {\vert \Psi_{k}(k)\vert ^{2}}$$ is the probability density $$ {P_{k}}$$ that if we measured the momentum of the particle (actually the $$ {z}$$ component of momentum), it would be found to have value $$ {\hbar k}$$.

The probability of finding a value $$ {\hbar k}$$ for the momentum would be

$$P_{k}=\vert \Psi_{k}(k)\vert ^{2}\propto\exp\left[-\frac{(k-\bar{k})^{2}}{2(\Delta k)^{2}}\right]$$

This Gaussian corresponds to the statistical Gaussian probability distribution with standard deviation $$ {\Delta k}$$.

Note also that $$ {\Psi(z,0)=\int_{k}\Psi_{k}(k)\exp(ikz)\,dk}$$ is the Fourier transform $$ {\Psi_{k}(k)}$$ and, as it well known, the Fourier transform of a Gaussian is a Gaussian, specifically here

$$\Psi(z,0)\propto\exp[-(\Delta k)^{2}z^{2}]$$

and

$$\vert \Psi(z,0)\vert ^{2}\propto\exp[-2(\Delta k)^{2}z^{2}]$$

is the standard form

$$\vert \Psi(z,0)\vert ^{2}\propto\exp\left[-\frac{z^{2}}{2(\Delta z)^{2}}\right]$$

where the parameter $$ {\Delta z}$$ would now be the standard deviation in the probability distribution for $$ {z}$$. Then $$ {\Delta k\Delta z=1/2}$$.

From $$ {\Delta k\Delta z=1/2}$$, if we now multiply by $$ {\hbar}$$ to get the standard deviation we would measure in momentum, we have

$$\Delta p\Delta z=\frac{\hbar}{2}$$

which is the relation between the standard deviations we would see in measurements of position and measurements of momentum.

This relation is as good as we can get for a Gaussian. It also turns out that the Gaussian shape is the one with the minimum possible product of $$ {\Delta p}$$ and $$ {\Delta z}$$, so quite generally

$$\Delta p\Delta z\geq\frac{\hbar}{2}$$

which is the *uncertainty principle* for position and momentum in one direction.

Uncertain principles are well known in Fourier analysis. One cannot simultaneously have both a well defined frequency and a well defined time. If a signal is a short pulse, it is necessary made up out of a range of frequencies

$$\Delta\omega\Delta t\geq\frac{1}{2}$$

The shorter the pulse is, the larger the range of frequencies.

####1.2. Particle current

In Cartesian coordinates, the divergence of a vector $$ {\vec{F}}$$ is

$$\text{div}\vec{F}=\nabla\cdot\vec{F}=\frac{\partial F_{x}}{\partial x}+\frac{\partial F_{y}}{\partial y}+\frac{\partial F_{z}}{\partial z}$$

When we are thinking of flow of particles, to conserve particles

$$\frac{\partial s}{\partial t}=-\nabla\vec{j}_{p}$$

where $$ {s}$$ is the particle density and $$ {\vec{j}_{p}}$$ is the particle current density.

The minus sign is because the divergence of the flow or current is the the net amount leaving the volume.

In quantum mechanical case, the particle density is $$ {\vert \Psi(vec{r},t)\vert ^{2}}$$, so we are looking for a relation of the form $$ {\partial s/\partial t=-\nabla\vec{j}_{p}}$$, but with $$ {\vert \Psi(\vec{r},t)\vert ^{2}}$$ instead of $$ {s}$$.

We know that

$$\frac{\partial\Psi(\vec{r},t)}{\partial t}=\frac{1}{i\hbar}\hat{H}\Psi(\vec{r},t)$$

We can also take the complex conjugate of both sides

$$\frac{\partial\Psi^{*}(\vec{r},t)}{\partial t}=-\frac{1}{i\hbar}\hat{H}^{*}\Psi^{*}(\vec{r},t)$$

Noting that

$$\frac{\partial}{\partial t}[\Psi^{*}\Psi]=\Psi^{*}\frac{\partial\Psi}{\partial t}+\Psi\frac{\partial\Psi^{*}}{\partial t}$$

Then we have

$$\frac{\partial}{\partial t}[\Psi^{*}\Psi]+\frac{i}{\hbar}(\Psi^{*}\hat{H}\Psi-\Psi\hat{H}^{*}\Psi^{*})=0$$

Presuming the potential $$ {V}$$ is real and does not depend in time and taking our Hamiltonian to be of the form

$$\hat{H}\equiv-\frac{\hbar^{2}}{2m}\nabla^{2}+V(r)$$

then

$$\Psi^{*}\hat{H}\Psi-\Psi\hat{H}^{*}\Psi^{*}=-\frac{\hbar^{2}}{2m}[\Psi^{*}\nabla^{2}\Psi-\Psi\nabla^{2}\Psi^{*}]$$

So our equation becomes

$$\frac{\partial}{\partial t}[\Psi^{*}\Psi]+\frac{i\hbar}{2m}(\Psi^{*}\nabla^{2}\Psi-\Psi\nabla^{2}\Psi^{*})=0$$

Now we use the following algebraic trick:

$$\Psi\nabla^{2}\Psi^{*}-\Psi^{*}\nabla^{2}\Psi=\nabla\cdot(\Psi\nabla\Psi^{*}-\Psi^{*}\nabla\Psi)$$

Hence, we have

$$\frac{\partial(\Psi^{*}\Psi)}{\partial t}=-\frac{i\hbar}{2m}\nabla\cdot(\Psi\nabla\Psi^{*}-\Psi^{*}\nabla\Psi)$$

which is an equation in the same form as $$ {\frac{\partial s}{\partial t}=-\nabla\vec{j}_{p}}$$. And

$$\vec{j}_{p}=\frac{i\hbar}{2m}(\Psi\nabla\Psi^{*}-\Psi^{*}\nabla\Psi)$$

So we can calculate particle currents from the wave function when the potential does not depend on time.

This expression applies also for an energy eigenstate. Suppose we are in the $$ {n}$$th energy eigenstate

$$\Psi_{n}(\vec{r},t)=\exp\left(-i\frac{E_{n}}{\hbar}t\right)\psi_{n}(\vec{r})$$

Then

$$ \vec{j}_{pn}(\vec{r},t)=\frac{i\hbar}{2m}(\Psi_{n}(\vec{r},t)\nabla\Psi_{n}^{*}(\vec{r},t)-\Psi_{n}^{*}(\vec{r},t)\nabla\Psi_{n}(\vec{r},t))$$

In the equation above, the gradient has no effect on the time factor, so the time term can be factored to the front of the expression and multiply to unity

$$\vec{j}_{pn}(\vec{r},t)=\frac{i\hbar}{2m}(\psi_{n}(\vec{r})\nabla\psi_{n}^{*}(\vec{r})-\psi_{n}^{*}(\vec{r})\nabla\psi_{n}(\vec{r}))$$

Therefore, the particle current $$ {\vec{j}_{pn}}$$ does not depend on time. That is, for any energy eigenstate $$ {n}$$,

$$\vec{j}_{pn}(\vec{r},t)=\vec{j}_{pn}(\vec{r})$$

Therefore, particle current is constant in any energy eigenstate. And for real spatial eigenfunctions, particle current is actually zero.

###2. Functions and Dirac Notation

####2.1. Functions as vectors

One kind of list of arguments would be the list of all real numbers which we could list in order as $$ {x_{1}}$$, $$ {x_{2}}$$, $$ {x_{3}}$$ and so on. This is an infinitely long list and the adjacent values in the list are infinitesimally close together but we will regard these infinite as details.

If we presume that we know this list of possible arguments of the function, we can write out the function as the corresponding list of values, and we choose to write this list as a column vector

$$\left[\begin{array}{c}f(x_{1} \\ f(x_{2}) \\ f(x_{3}) \\ \vdots\end{array}\right]$$

For example, we could specify the function at points spaced by small amount $$ {\delta x}$$, with $$ {x_{2}=x_{1}+\delta x}$$, $$ {x_{3}=x_{2}+\delta x}$$ and so on. We would do this for sufficiently many values of $$ {x}$$ and over a sufficient range of $$ {x}$$ to get a sufficiently useful representation for some calculation such as integral. The integral of $$ {\vert f(x)\vert ^{2}}$$ could be written as

$$\int\vert f(x)\vert ^{2}\,dx\approx[f^{*}(x), f^{*}(x_{2}), f^{*}(x_{3}), \cdots]\left[\begin{array}{c}f(x_{1}) \\ f(x_{2}) \\ f(x_{3}) \\ \vdots\end{array}\right]\delta x$$

where $$ {\delta x}$$ is sufficiently small and the corresponding vectors therefore sufficiently long, we can get an arbitrarily good approximation to be integral.

####2.2. Dirac notation

The first part of the Dirac "bra-ket" notation $$ {\vert f(x)\rangle}$$ is called a "ket", which refers to our column vector. For the case of our function $$ {f(x)}$$, one way to define the "ket" is

$$\vert f(x)\rangle\equiv\left[\begin{array}{c}f(x_{1})\sqrt{\delta x} \\ f(x_{2})\sqrt{\delta x} \\ f(x_{3})\sqrt{\delta x} \\ \vdots\end{array}\right]$$

or the limit of this as $$ {\delta x\rightarrow 0}$$. We put $$ {\sqrt{\delta x}}$$ into the vector for normalization. The function is still a vector list of numbers.

We can similarly define the "bra" $$ {\langle f(x)\vert }$$ to refer a row vector

$$\langle f(x)\vert \equiv[f^{*}(x_{1})\sqrt{\delta x}\quad f^{*}(x_{2})\sqrt{\delta x}\quad f^{*}(x_{3})\sqrt{\delta x}\quad\cdots]$$

where we mean the limit of this as $$ {\delta s\rightarrow 0}$$.

Note that, in our row vector, we take the complex conjugate of all the values. Note that this "bra" refers to exactly the same function as the "ket". These are different ways to writing the same function.

The vector

$$[a_{1}^{*}\quad a_{2}^{*}\quad a_{3}^{*}\quad\cdots]$$

is called, variously the *Hermitian adjoint*, the *Hermitian transpose*, the *Hermitian conjugate* or the *adjoint* of the vector

$$\left[\begin{array}{c}a_{1} \\ a_{2}\\ a_{3}\\ \vdots\end{array}\right]$$

A common notation used to indicate the Hermitian adjoint is to use the character "$$ {\dag}$$" as a superscript

$$\left[\begin{array}{c}a_{1} \\ a_{2}\\ a_{3}\\ \vdots\end{array}\right]^{\dag}=[a_{1}^{*}\quad a_{2}^{*}\quad a_{3}^{*}\quad\cdots]$$

Forming the Hermitian adjoint is like reflecting about a $$ {-45^{\circ}}$$ line, then taking the complex conjugate of all the elements.

The "bra" is the Hermitian adjoint of the "ket" and vice versa

$$(\vert f(x)\rangle)^{\dag}=\langle f(x)\vert \qquad (\langle f(x)\vert )^{\dag}=\vert f(x)\rangle$$

The Hermitian adjoint of the Hermitian adjoint brings us back to where we started.

Considering $$ {f(x)}$$ as a vector and following our previous result and adding bra-ket notation

$$\begin{array}{rcl}  \int\vert f(x)\vert ^{2}\,dx&\equiv&[f^{*}(x_{1})\sqrt{\delta x}\quad f^{*}(x_{2})\sqrt{\delta x}\quad f^{*}(x_{3})\sqrt{\delta x}\quad \cdots]\left[\begin{array}{c}f^{*}(x_{1})\sqrt{\delta x} \\ f^{*}(x_{2})\sqrt{\delta x} \\ f^{*}(x_{3})\sqrt{\delta x} \\ \cdots\end{array}\right] \\ &\equiv&\sum_{n}f^{*}(x_{n})\sqrt{\delta x}f(x_{n})\sqrt{\delta x} \\ &\equiv&\langle f(x)\vert f(x)\rangle \end{array}$$

where again the strict equality applies in the limit when $$ {\delta x\rightarrow 0}$$.

Note that the use of the bra-ket notation here eliminates the need to write an integral or a sum. The sum is implicit in the vector multiplication. Note that shorthand for the vector product of the "bra" and "ket"

$$\langle g\vert \times\vert f\rangle=\langle g\vert f\rangle$$

The middle vertical line is usually omitted though it would not matter if it was still there. This notation is also useful for integrals of two different functions.

In general this kind of "product" $$ {\langle g\vert \times\vert f\rangle\equiv\langle g\vert f\rangle}$$ is called an inner product in linear algebra. The geometric vector dot product is an inner product. The bra-ket "product" $$ {\langle g\vert f\rangle}$$ is an inner product. The "overlap" integral" $$ {\int g^{*}(x)f(x)\,dx}$$ is an inner product. It is "inner" because it takes two vectors and turns them into a number a "small" entity. In the Dirac notation $$ {\langle g\vert f\rangle}$$, the bra-ket gives an inner "feel" to this product. The special parentheses gives a "closed" look.

####2.3. Using Dirac notation

Suppose the function is not represented directly as a set of values for each point in space but is expanded in a complete orthonormal basis $$ {\psi_{n}(x)}$$.

$$f(x)\sum_{n}c_{n}\psi_{n}(x)$$

We could also write the function as the "ket"

$$\vert f(x)\rangle\equiv\left[\begin{array}{c}c_{1} \\ c_{2} \\ c_{3} \\ \vdots\end{array}\right]$$

(with possibly an infinite number of elements)

In this case, the "bra" version becomes

$$\langle f(x)\vert \equiv [c_{1}^{*}\quad c_{2}^{*}\quad c_{3}^{*}\quad \cdots]$$

When we write the function in this different form as a vector containing these expansion coefficients, we say we have changed its "representation". The function $$ {f(x)}$$ is still the same function. The vector $$ {\vert f(x)\rangle}$$ is the same vector in our space. We have just changed the axes we used to represent the function, so the coordinates of the vector have changed.

The result of a bra-ket expression like $$ {\langle f(x)\vert f(x)\rangle}$$ or $$ {\langle g(x)\vert f(x)\rangle}$$ is simply a number (in general, complex) which is easy to see if we think of this as a vector multiplication. Note that this number is not changed as we change the representation. Just as the dot product of two vectors is independent of the coordinate system.

Evaluating $$ {c_{n}}$$ in $$ {f(x)=\sum_{n}c_{n}\psi_{n}(x)}$$ or the $$ {d_{n}}$$ in $$ {g(x)=\sum_{n}d_{n}\psi_{n}(x)}$$ is simple because the functions $$ {\psi_{n}(x)}$$ are orthonormal. Since $$ {\psi_{n(x)}}$$ is just a function, we write it as a ket $$ {\vert \psi_{n}\rangle}$$. To evaluate the coefficient $$ {c_{m}}$$, we premultiply by the bra $$ {\langle\psi_{m}\vert }$$ to get

$$\langle\psi_{m}(x)\vert f(x)\rangle=\sum_{n}c_{n}\langle\psi_{m}(x)\vert \psi_{n}(x)\rangle=\sum_{n}c_{n}\delta_{mn}=c_{m}$$

Using bra-ket notation, we can write $$ {f(x)=\sum_{n}c_{n}\psi_{n}(x)}$$ as

$$\vert f(x)\rangle=\sum_{n}c_{n}\vert \Psi_{n}(x)\rangle=\sum_{n}\vert \psi_{n}(x)\rangle c_{n}=\sum_{n}\vert \psi_{n}(x)\rangle\langle\psi_{n}(x)\vert f(x)\rangle$$

Because $$ {c_{n}}$$ is just a number, it can be moved about in the product. Multiplication of vectors and numbers is commutative.

In quantum mechanics, where the function $$ {f}$$ represents the state of quantum mechanical system, such as the wave function. The set of numbers represented by the bra $$ {\langle f\vert }$$ or ket $$ {\vert f\rangle}$$ vector represent the state of the system. Hence, we refer to $$ {\vert f\rangle}$$ as the "state vector" of the system and $$ {\langle f\vert }$$ as the (Hermitian) adjoint of the state vector.

In quantum mechanics, the bra or ket always represents either the quantum mechanical state of the system such as the spatial wave function $$ {\psi(x)}$$ or some state the system could be in such as one of the basis states $$ {\psi_{n}(x)}$$.

The convention for what is inside the bra or ket is loose, usually one deduces from the context what is meant. For example, it is obvious what basis we were working with. We might use $$ {\vert n\rangle}$$ to represent the $$ {n}$$th basis function (or basis "state") rather than the notation $$ {\vert \psi_{n}(x)\rangle}$$ or $$ {\vert \psi_{n}\rangle}$$. The symbols inside the bra or ket should be enough to make it clear what state we are discussing. Other wise there are essentially no rules for the notation.

###3. Vector Spaces, Operators and Matrices

####3.1. Vector space

For a function expressed as its value at a set of points, we may have infinite number of orthogonal axes labeled with their associated basis function. Just as we label axes in conventional space with unit vectors, one notation is $$ {\hat{x}}$$, $$ {\hat{y}}$$ and $$ {\hat{z}}$$ for the unit vectors, so also here we label the axes with the kets $$ {\vert \psi_{n}\rangle}$$.

Our vector space has an inner product that defines both the orthogonality of the basis functions

$$\langle\psi_{m}\vert \psi_{n}\rangle=\delta_{nm}$$

as well as the components $$ {c_{m}=\langle\psi_{m}\vert f\rangle}$$.

With respect to addition of vectors, our vector space is commutative and associative

$$\vert f\rangle+\vert g\rangle=\vert g\rangle+\vert f\rangle\qquad \vert f\rangle+(\vert g\rangle+\vert h\rangle)=(\vert f\rangle+\vert g\rangle)+\vert h\rangle$$

Our vector space is linear in multiplying by constants

$$c(\vert f\rangle+g\rangle)=c\vert f\rangle+c\vert g\rangle$$

And the inner product is linear, both in multiplying by constants and in superposition of vectors

$$\langle f\vert cg\rangle=c\langle f\vert g\rangle$$

$$\langle f\vert (\vert g\rangle+\vert h\rangle)=\langle f\vert g\rangle+\langle f\vert h\rangle$$

There is a well-defined "length" to a vector formally a "norm"

$$\vert \vert f\vert \vert =\sqrt{\langle f\vert f\rangle}$$

Any vector in the space can be represented to an arbitrary degree of accuracy as a linear combination of the basis vectors. This is the completeness requirement on the basis set. In vector spaces, this property of the vector space itself is sometimes described as "compactness".

With complex coefficients rather than real lengths, we choose a non-commutative inner product form

$$\langle f\vert g\rangle=(\langle g\vert f\rangle)^{*}$$

####3.2. Operators

An operator turns one function into another. In the vector space representation of a function. An operator turns one vector into another.

Suppose that we are constructing the new function $$ {g(y)}$$ from the function $$ {f(x)}$$ by acting on $$ {f(x)}$$ with the operator $$ {\hat{A}}$$. The variables $$ {x}$$ and $$ {y}$$ might be same kind of variable or quite different. A standard notation for writing such any such operation on a function is

$$g(y)=\hat{A}f(x)$$

This should be read as $$ {\hat{A}}$$ operating on $$ {f(x)}$$.

For $$ {\hat{A}}$$ to be the most general operation possible, it should be possible for the value of $$ {g(y)}$$, for example, at some particular value of $$ {y=y_{1}}$$ to depend on the values of $$ {f(x)}$$ for all values of the argument $$ {x}$$.

We are interested here solely in linear operators. They are only ones we will use in quantum mechanics because of the fundamental linearity of quantum mechanics. A linear operator has the following characteristics

$$\hat{A}[f(x)+g(x)]=\hat{A}f(x)+\hat{A}h(x)$$

$$\hat{A}[cf(x)]=c\hat{A}f(x)$$

for any complex number $$ {c}$$.

Let us consider the most general way we could have the function $$ {g(y)}$$ at some specific value $$ {y_{1}}$$ of its argument, that is, $$ {g(y_{1})}$$ be related to have values of $$ {f(x)}$$ for possibly all values of $$ {x}$$ and still retain the linearity properties for this relation.

Think of the function $$ {f(x)}$$ as being represented by a list of values $$ {f(x_{1})}$$, $$ {f(x_{2})}$$, $$ {f(x_{3})}$$, ... . We can take the values of $$ {x}$$ to be as closely spaced as we want. We believe that this representation can give us as accurate a representation of $$ {f(x)}$$ for any calculation we need to perform.

Then we propose that for a linear operation, the value of $$ {g(y_{1})}$$ might be related to the values of $$ {f(x)}$$ by a relation of the form

$$g(y_{1})=a_{11}f(x_{1})+a_{12}f(x_{2})+a_{13}f(x_{3})+\ldots$$

where the $$ {a_{ij}}$$ are complex constants. This form shows the linearity behavior we want. And we can conclude that this form is the most general form possible for the relation between $$ {g(y_{1})}$$ and $$ {f(x)}$$ if this relation is to a linear operator.

To construct the entire function $$ {g(y)}$$, if we write $$ {f(x)}$$ and $$ {g(y)}$$ as vectors, then we can write all these series at once

$$\left[\begin{array}{c}g(y_{1})\\g(y_{2})\\g(y_{3})\\\vdots\end{array}\right]=\left[\begin{array}{cccc} a_{11} & a_{12} & a_{13} & \cdots \\ a_{21} & a_{22} & a_{23} & \cdots \\ a_{31} & a_{32} & a_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots\end{array}\right]\left[\begin{array}{c}f(x_{1})\\f(x_{2})\\f(x_{3})\\\vdots\end{array}\right]$$

The above relation can be written as $$ {g(y)=\hat{A}f(x)}$$ where the operator $$ {\hat{A}}$$ can be written as a matrix

$$\left[\begin{array}{cccc} a_{11} & a_{12} & a_{13} & \cdots \\ a_{21} & a_{22} & a_{23} & \cdots \\ a_{31} & a_{32} & a_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots\end{array}\right]$$

Presuming functions can be represented as vectors, then linear operators can be represented by matrices. In bra-ket notation, we can write $$ {g(y)=\hat{A}f(x)}$$ as

$$\vert g\rangle=\hat{A}\vert f\rangle$$

If we regard the ket as a vector, we now regard the (linear) operator $$ {\hat{A}}$$ as a matrix.

####3.3. Linear operators and their algebra

Operators do not in general commute and it is very important in quantum mechanics. We expanded $$ {f(x)=\sum_{n}\psi_{n}(x)}$$ and $$ {g(x)=\sum_{n}d_{n}\psi_{n}(x)}$$. We could have followed a similar argument requiring each expansion coefficient $$ {d_{i}}$$ depends linearly on all the expansion coefficients $$ {c_{n}}$$.

By similar arguments, we would deduce the most general linear relation between the vectors of expansion coefficients could be represented as a matrix, the bra-ket statement of the relation between $$ {f}$$, $$ {g}$$ and $$ {\hat{A}}$$ remains unchanged as $$ {\vert g\rangle=\hat{A}\vert f\rangle}$$.

$$\left[\begin{array}{c}d_{1}\\d_{2}\\d_{3}\\\vdots\end{array}\right]=\left[\begin{array}{cccc} A_{11} & A_{12} & A_{13} & \cdots \\ A_{21} & A_{22} & A_{23} & \cdots \\ A_{31} & A_{32} & A_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots\end{array}\right]\left[\begin{array}{c}c_{1}\\c_{2}\\c_{3}\\\vdots\end{array}\right]$$

Now we will find out how we can write some operator as a matrix, that is, we will deduce how to calculate all the elements of the matrix if we know the operator. Suppose we choose our function $$ {f(x)}$$ to be the $$ {j}$$th basis function $$ {\psi_{j}(x)}$$ so $$ {f(x)=\psi_{j}(x)}$$ or equivalently $$ {\vert f\rangle=\vert \psi_{j}\rangle}$$. Then, in the expansion $$ {f(x)=\sum_{n}c_{n}\psi_{n}(x)}$$, we are choosing $$ {c_{j}=1}$$ with all operate on this $$ {\vert f\rangle}$$ with $$ {\hat{A}}$$ in $$ {\vert g\rangle=\hat{A}\vert f\rangle}$$ to get $$ {\vert g\rangle}$$. Suppose specifically we want to know the resulting coefficient $$ {d_{i}}$$ in the expansion $$ {g(x)=\sum_{n}d_{n}\psi_{n}(x)}$$. With our choice $$ {c_{j}=1}$$, and all other $$ {c}$$'s 0 then we would have $$ {d_{i}=A_{ij}}$$.

But, from the expansion for $$ {\vert f\rangle}$$ and $$ {\vert g\rangle}$$, for the specific case of $$ {\vert f\rangle=\vert \psi_{j}\rangle}$$

$$\vert g\rangle=\sum_{n}d_{n}\vert \psi_{n}\rangle=\hat{A}\vert f\rangle=\hat{A}\vert \psi_{j}\rangle$$

To extract $$ {d_{i}}$$ from this expression, we multiply by $$ {\langle\psi_{i}\vert }$$ on both sides to obtain

$$d_{i}=\langle\psi_{i}\vert \hat{A}\vert \psi_{j}\rangle$$

But we already concluded for this case that $$ {d_{i}=A_{ij}}$$, so

$$A_{ij}=\langle\psi_{i}\vert \hat{A}\vert \psi_{j}\rangle$$

Operator $$ {\hat{A}}$$ acting on the unit vector $$ {\vert \psi_{j}\rangle}$$ generates the vector $$ {\hat{A}\vert \psi_{j}\rangle}$$ with generally a new length and direction. The matrix element $$ {\langle\psi_{i}\vert \hat{A}\vert \psi_{j}\rangle}$$ is the projection of $$ {\hat{A}\vert \psi_{j}\rangle}$$ onto the $$ {\vert \psi_{i}\rangle}$$ axis.

We can write the matrix for the operator $$ {\hat{A}}$$

$$\hat{A}\equiv\left[\begin{array}{cccc} \langle\psi_{1}\vert \hat{A}\vert \psi_{1}\rangle & \langle\psi_{1}\vert \hat{A}\vert \psi_{2}\rangle & \langle\psi_{1}\vert \hat{A}\vert \psi_{3}\rangle & \cdots \\ \langle\psi_{2}\vert \hat{A}\vert \psi_{1}\rangle & \langle\psi_{2}\vert \hat{A}\vert \psi_{2}\rangle & \langle\psi_{2}\vert \hat{A}\vert \psi_{3}\rangle & \cdots \\ \langle\psi_{3}\vert \hat{A}\vert \psi_{1}\rangle & \langle\psi_{3}\vert \hat{A}\vert \psi_{2}\rangle & \langle\psi_{3}\vert \hat{A}\vert \psi_{3}\rangle & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{array}\right]$$

We have now deduce how to set up a function as a vector and a linear operator as a matrix which can operate on the vectors.
