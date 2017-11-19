---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 1
date: 2013-10-03
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

### 1. Background Mathematics Review

#### 1.1. Symbols, Greek letters, algebra notations, functions

Relational symbols 

+ $$ {\equiv}$$: "is equivalent to"
+ $$ {\simeq}$$ or $$ {\cong}$$: "is approximately equal to"
+ $$ {\propto}$$: "is proportional to"
+ $$ {\gg}$$: "is much greater than"
+  $$ {\ll}$$: "is much less than"

Greek letters (Every Greek letter has its own Roman letter equivalent, you can search for yourself): 

+ Alpha: Lower case: $$ {\alpha}$$
+ Beta: Lower case: $$ {\beta}$$
+ Gamma: Upper case: $$ {\Gamma}$$, Lower case: $$ {\gamma}$$
+ Delta: Upper case: $$ {\Delta}$$, Lower case: $$ {\delta}$$
+ Epsilon: Lower case: $$ {\epsilon}$$
+ Zeta: Lower case: $$ {\zeta}$$
+ Eta: Lower case: $$ {\eta}$$
+ Theta: Upper case: $$ {\Theta}$$, Lower case: $$ {\theta}$$
+ Iota: Lower case: $$ {\iota}$$
+ Kappa: Lower case: $$ {\kappa}$$
+ Lambda: Upper case: $$ {\Lambda}$$, Lower case: $$ {\lambda}$$
+ Mu: Lower case: $$ {\mu}$$.
+ Nu: Lower case: $$ {\nu}$$
+ Xi: Upper case: $$ {\Xi}$$, Lower case: $$ {\xi}$$
+ Omicron: too similar to Roman "o"
+ Pi: Upper case: $$ {\Pi}$$, Lower case: $$ {\pi}$$
+ Rho: Lower case: $$ {\rho}$$
+ Sigma: Upper case: $$ {\Sigma}$$, Lower case: $$ {\sigma}$$
+ Tau: Lower case: $$ {\tau}$$
+ Upsilon: Lower case: $$ {\upsilon}$$
+ Phi: Upper case: $$ {\Phi}$$, Lower case: $$ {\Phi}$$
+ Chi: Lower case: $$ {\chi}$$
+ Psi: Upper case: $$ {\Psi}$$, Lower case: $$ {\psi}$$
+ Omega: Upper case: $$ {\Omega}$$, Lower case: $$ {\omega}$$ 

Trigonometric functions: 

+ Sine: $$ {\sin\theta}$$: $$ {\sin(-\theta)=-\sin(\theta)}$$,
+ Cosine: $$ {\cos\theta}$$: $$ {\cos(-\theta)=\cos(\theta)}$$,
+ Tangent: $$ {\tan\theta=\frac{\sin\theta}{\cos\theta}}$$,
+ Cosecant: $$ {\csc\theta=\frac{1}{\sin\theta}}$$,
+ Secant: $$ {\sec\theta=\frac{1}{\cos\theta}}$$,
+ Cotangent: $$ {\cot\theta=\frac{\cos\theta}{\sin\theta}}$$. 

#### 1.2. Power logs, exponentials, complex numbers


**Definition 1 (Logarithms)** A chain of $$ {n}$$ numbers $$ {g}$$ multiplied together is $$ {g\times g\times\ldots\times g=g^{n}}$$ and $$ {n}$$ is the "log to the base $$ {g}$$" of $$ {g^{n}}$$: $$ {n=\log_{n}(g^{n})}$$

**Definition 2 (Imaginary Unit)** $$ {i=\sqrt{-1}}$$, so $$ {i^{2}=-1}$$ and $$ {(-i)^{2}=-1}$$.

**Definition 3 (Complex Numbers)** A number that can be written

$$g=ai+b$$

where $$a$$ and $$b$$ are both real numbers, is called complex number. $$a$$ is called the "real part" of $$g$$: $$a=\text{Re}(g)$$, and $$b$$ is called the "imaginary part" of $$g$$: $$b=\text{Im}(g)$$.

**Definition 4 (Complex conjugate and modulus)** The "complex conjugate" has the sign of the imaginary part reversed. And is indicated by a superscript "$$*$$"

$$g^{*}=-ai+b$$

Modulus squared of $$g$$: $$\vert g\vert^{2}=g^{*}g=gg^{*}$$. The positive square root of this is called the "modulus" of $$g$$

$$\vert g\vert=+\sqrt{\vert g\vert^{2}}$$

**Theorem 5 (Euler's formula)**

$$\exp(i\theta)=\cos\theta+i\sin\theta$$

Note that

$$[\exp(i\theta)]^{*}=\exp(-i\theta)$$

Also

$$\exp(i\theta)\exp(-i\theta)=exp(i\theta-i\theta)=1$$



For any complex number $$ {g=a+ib}$$, we can write

$$g=\vert g\vert\frac{a+ib}{\vert g\vert}=\vert g\vert(\cos\theta+i\sin\theta)=\vert g\vert exp(i\theta)$$

*$${n}$$th roots of unity*: Note that the number $$ {\exp(2\pi i/n)}$$ when raised to the power is 1 (unity)

$$\left[\exp\left(\frac{2\pi i}{n}\right)^{n}\right]=\exp\left(\frac{2\pi i}{n}\times n\right)=\exp(2\pi i)=1$$

#### 1.3. Coordinates and vectors

*Right-handed axes*: using your right hand, *Thumb*: $$ {x}$$, *Index ("first") finger*: $$ {y}$$, *middle finger*: $$ {z}$$. No matter how you now rotate your whole hand, the axes remain right-handed.

Dot product among vectors gives a scalar result, cross product gives vector result.

**Definition 6 (Dot product)**

$$\vec{a}\cdot\vec{b}=\vert \vec{a}\vert\vert \vec{b}\vert\cos\theta$$

**Definition 7 (Cross product)** For two vectors:

$$\vec{a}=a_{x}\vec{i}+a_{y}\vec{j}+a_{z}\vec{k}$$

$$\vec{b}=b_{x}\vec{i}+b_{y}\vec{j}+b_{z}\vec{k}$$

the vector cross product is

$$\vec{a}\times\vec{b}=\vec{n}\vert \vec{a}\vert\vert \vec{b}\vert\sin\theta$$

$$ {\vec{n}}$$ is a unit vector with a direction given by the right hand screw rule.

Note that

$$\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}$$

A equivalent algebraic formula for the vector cross product is

$$\vec{a}\times\vec{b}=\begin{vmatrix}\vec{i} & \vec{j} & \vec{k} \\ a_{x} & a_{y} & a_{z} \\ b_{x} & b_{y} & b_{z}\end{vmatrix}$$

#### 1.4. Differential calculus

The derivative at some specific point $$ {x_{1}}$$ can be written

$$y^{'}(x_{1})\equiv\left.\frac{dy}{dx}\right\vert_{x_{1}}$$

The second derivative is the derivative of the first derivative

$$y^{''}(x)\equiv\frac{d^{2}y}{dx^{2}}\equiv\frac{d}{dx}\frac{dy}{dx}$$

The second derivative can be thought as the "curvature" of a function.

For two function $$ {u(x)}$$ and $$ {v(x)}$$, the derivative of the sum is the sum of the derivatives.

$$\frac{d}{dx}[u(x)+v(x)]=\frac{du}{dx}+\frac{dv}{dx}$$

For a function $$ {u(x)}$$, the derivative of a constant $$ {a}$$ times a function is $$ {a}$$ times the derivative.

$$\frac{d}{dx}[au]=a\frac{du}{dx}$$

An operation or function $$ {f(x)}$$ is linear if

$$f(x+z)=f(y)+f(z)$$

and

$$f(ax)=af(x)$$

For two functions $$ {u(x)}$$ and $$ {v(x)}$$, the derivative of the product is

$$\frac{d}{dx}(uv)=u\frac{dv}{dx}+v\frac{du}{dx}$$

For two functions $$ {u(x)}$$ and $$ {v(x)}$$, the derivative of the ratio or quotient is

$$\frac{d}{dx}\left(\frac{u}{v}\right)=\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^{2}}$$

*Chain rule*: for two functions $$ {f(x)}$$ and $$ {g(x)}$$, the derivative of the "function of a function" can be split into a product

$$\frac{d}{dx}f(g(x))=\left(\frac{df}{dg}\right)\times\left(\frac{dg}{dx}\right)$$

#### 1.5. Partial differentiation

Suppose we have a function $$ {f(x,y)}$$ of two variables. Then we have the gradient of $$ {f}$$ as a function of $$ {x}$$ with $$ {y}$$ held constant, which we write

$$\left.\frac{\partial f}{\partial x}\right\vert_{y}, \text{ or }\frac{\partial f}{\partial x}$$

Second partial derivatives is a measure of the curvature of the function in the $$ {y}$$ direction.

Cross derivative

$$\frac{\partial^{2}f}{\partial x\partial y}\equiv\left.\frac{\partial}{\partial x}\right\vert_{y}\left.\frac{\partial f }{\partial y}\right\vert_{x}$$

is a measure of how "warped" a surface is.

Differential or Exact Differential

$$df=\left.\frac{\partial f}{\partial x}\right\vert_{y}dx+\left.\frac{\partial f}{\partial y}\right\vert_{x}dy$$

Total derivative

$$\frac{df}{dt}=\left.\frac{\partial f}{\partial x}\right\vert_{y}\left(\frac{dx}{dt}\right)+\left.\frac{\partial f}{\partial y}\right\vert_{x}\left(\frac{dy}{dt}\right)$$

#### 1.6. Ordinary and partial differential equations

A differential equation involves derivatives of some function. It is easy to verify solutions, but it can be harder to find them.

"First order" differential equation has no derivatives higher than first order. The solution with undetermined constant is called "general solution". The constants are determined by boundary condition.

Boundary conditions that specify the value of a function at some position or "boundary" are called "Dirichlet" boundary conditions. Boundary conditions that specify the derivatives or slope of a function at some position or "boundary" are called "Neumann" boundary condition.

Imaginary first derivative

$$\frac{dy}{dx}=iby$$

with $$ {b}$$ real has the general solution

$$y=A\exp(ibx)\equiv A(\cos(bx)+i\sin(bx))$$

Note that neither $$ {\cos(bx)}$$ or $$ {\sin(bx)}$$ is a solution of this equation.

A second-order differential equations contains no derivatives higher than second order. Since derivatives with respect to time arises in many situations, there is a shorthand notation using dots above the variable being differentiated with respect to time with the number of dots indicating the order of differentiating, e.g.,

$$\dot{a}\equiv\frac{da}{dt}, \text{ and } \ddot{a}\equiv\frac{d^{2}a}{dt^{2}}$$

Classical one-dimensional scalar wave equation:

$$\frac{\partial^{2}\phi(z,t)}{\partial z^{2}}-\frac{1}{c^{2}}\frac{\partial^{2}\phi(z,t)}{\partial t^{2}}=0 $$

relates how strongly curved a function $$ {\phi}$$ is (from the second spatial derivative) to the second time (or temporal) derivate. For this function, any function of the form $$ {f(z-ct)}$$ or $$ {g(z+ct)}$$ are solutions.

Monochromatic waves are oscillating at one specific (angular) frequency $$ {\omega}$$, e.g,

$$T(t)=\exp(i\omega t), \exp(-i\omega t), \cos(\omega t), \sin(\omega t)$$

or any combination of these, then writing $$ {\phi(z,t)\equiv Z(z)T(t)}$$, we have

$$\frac{\partial^{2}\phi}{\partial t^{2}}=-\omega^{2}\phi$$

Leaving a wave equation for the spatial part, then

$$\frac{d^{2} Z(z)}{dz^{2}}+k^{2}Z(z)=0, \text{ where } k^{2}=\frac{\omega^{2}}{c^{2}}$$

The Laplacian operator can be defined for ordinary Cartesian coordinates

$$\nabla^{2}\equiv\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}$$

A convenient way to say it is "del squared". Sometimes it is written $$ {\Delta}$$ instead of $$ {\nabla^{2}}$$.

The gradient of a function $$ {f(x,y,z)}$$ is

$$\nabla f\equiv\text{grad }f=\vec{i}\frac{\partial f}{\partial x}+\vec{j}\frac{\partial f}{\partial y}+\vec{k}\frac{\partial f}{\partial z}$$

#### 1.7. Matrices

The leading diagonal of a matrix is the diagonal from top left to bottom right.

An important manipulation from matrices and vector is the transpose denoted by a superscript "$$ {T}$$", a reflection about a diagonal line from top to bottom right for a matrix.

Another common manipulation is the "*Hermitian adjoint*", "*Hermitian transpose*", or "conjugate transpose", denoted by a superscript "$$ {\dagger}$$", a reflection about a diagonal line from top left to bottom right for a matrix and taking the complex conjugate of all the elements.

$$(\hat{D}^{\dagger})_{mn}=\hat{D}^{*}_{nm}$$

A matrix is said to be *Hermitian* if it is equal to its own Hermitian adjoint:

$$\hat{B}^{\dagger}=\hat{B}$$

In "inner" product of a row and a column vector collapses two vectors to a number, analogous to geometrical vector dot product. An "outer product" of a column and a row vector generates a square matrix.

Hermitian adjoint of a product is the reversed product of the Hermitian adjoints

$$(\hat{A}\hat{B})^{\dagger}=\hat{B}^{\dagger}\hat{A}^{\dagger}$$

For a matrix, if it has an inverse $$ {\hat{A}^{-1}}$$, it has the property $$ {\hat{A}^{-1}\hat{A}=\hat{I}}$$

#### 1.8. Linear algebra, matrices and eigen equations

The determinant of a matrix $$ {\hat{A}}$$ is written in two notations

$$\det(\hat{A})=\begin{vmatrix} A_{11} & A_{12} & \cdots & A_{1N} \\ A_{21} & A_{22} & \cdots & A_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ A_{N1} & A_{N2} & \cdots & A_{NN}\end{vmatrix}$$

A equation of the from

$$\hat{A}d=\lambda d$$

where $$ {d}$$ is a vector, $$ {\lambda}$$ is a number, and $$ {\hat{A}}$$ is a square matrix is called an eigenequation with eigenvalue $$ {\lambda}$$ and eigenvector $$ {d}$$. If there are solutions, they may only exist for specific values of $$ {\lambda}$$.

If $$ {\hat{B}=\hat{A}-\lambda\hat{I}}$$ have a inverse, then there is no non-zero solution $$ {d}$$. Otherwise, there is non-zero solution.

### 2. Introduction to Quantum Mechanics

#### 2.1. Plank's Proposal (December 14th, 1900)

Light is emitted in quanta of energy

$$E=h\nu$$

where $$ {\nu}$$ (Greek letter "nu") is the light's frequency in Hz (Hertz) and $$ {h}$$ is Plank's constant

$$h=6.62606957\times 10^{-34}J\cdot s$$

#### 2.2. Einstein's Proposal (1905)

Light is actually made up out of particles: photons, of energy $$ {E=h\nu}$$. The kinetic energy of the emitted electrons is the energy left over after the electron has been "lifted" over the work function barrier.

#### 2.3. Bohr model of the hydrogen atom

A small negatively charged electron orbits small positively charged core (the proton) but with electrostatic attraction. Key assumption (Neils Bohr, 1913) is angular momentum is "quantized" in units of Plank's constant, $$ {h}$$ over $$ {2\pi}$$

$$\hbar\equiv\frac{h}{2\pi}$$

#### 2.4. de Broglie hypothesis

A particle with mass also behaves as a wave with wavelength

$$\lambda=\frac{h}{p}$$

where $$ {p}$$ is the particle's momentum.

#### 2.5. Quantum mechanics formation

Werner Heisenberg (1925) proposed matrix formulation of quantum mechanics.

Erwin Schrodinger (1926) proposed wave equation.

More key contributions by Max Born, Pascual Jordan, Paul Dirac, John von Neumann ...

### 3. Classical Mechanics, Oscillations and Waves

#### 3.1. Elementary classical mechanics

For a particle of mass $$ {m}$$ which is a vector because it has direction is

$$\vec{p}=m\vec{v}$$

where $$ {\vec{v}}$$ is the (vector) velocity.

The kinetic energy is the energy associated with motion is

$$K.E.=\frac{p^{2}}{2m}$$

where $$ {p^2=\vec{p}\cdot\vec{p}}$$.

Potential energy is defined as energy due to position. It is usually denoted by $$ {V}$$ in quantum mechanics. It can be written as $$ {V(\vec{r})}$$. We can talk about potential energy if the energy only depends on where we are, not how we got there. Classical "fields" with this property are called "conservative" or "irrotational" fields.

The total energy can be the sum of potential energy and kinetic energies. When this total energy is written as a function of position and momentum, it can be called the (classical) "Hamiltonian". For a classical particle of mass $$ {m}$$ in a conservative potential $$ {V(\vec{r})}$$

$$H=\frac{p^{2}}{2m}+V(\vec{r})$$

Newton's second law relates force and acceleration

$$\vec{F}=m\vec{a}$$

Equivalently,

$$\vec{F}=\frac{d\vec{p}}{dt}$$

The relation between force and potential is

$$F_{x}=-\frac{dV}{dx}$$

We can generalize the relation between force and potential to three dimensions with force as a vector by using the gradient operator

$$\vec{F}=-\nabla V=-\left[\frac{\partial V}{\partial x}\vec{i}+\frac{\partial V}{\partial y}\vec{j}+\frac{\partial V}{\partial z}\vec{k}\right]$$

#### 3.2. Oscillations

A simple spring will have a restoring force $$ {F}$$ acting on the mass $$ {M}$$ proportional to the amount $$ {y}$$ by which it is stretched. For some "spring constant" $$ {K}$$

$$F=-Ky$$

The minus sign is because this is restoring. This gives a "simple harmonic oscillator".

From Newton's second law

$$F=Ma=M\frac{d^{2}y}{dt^{2}}=-Ky$$

i.e.,

$$\frac{d^{2}y}{dt^{2}}=-\frac{K}{M}y=-\omega^{2}$$

where we define $$ {\omega=K/M}$$. We have oscillatory solutions of angular frequency $$ {\omega=\sqrt{K/M}}$$. e.g. $$ {y\propto\sin\omega t}$$.

A physical system described by an equation like

$$\frac{d^{2}y}{dt^{2}}=-\omega^{2}y$$

is called a *simple harmonic oscillator*.

#### 3.3. The classical wave equation

$$\displaystyle  \frac{\partial^{2} y}{\partial z^{2}}-\frac{1}{v^{2}}\frac{\partial^{2} y}{\partial t^{2}}=0$$

where velocity $${v=\sqrt{T/\rho}}$$
