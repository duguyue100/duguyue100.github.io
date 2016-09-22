---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 3
date: 2013-10-17
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

###1. Particles and Barriers

####1.1. Sets of functions

Suppose we are interested in the behavior of some function, such as a loudspeaker cone displacement from time 0 to $$ {t_{o}}$$, presuming it starts and ends at 0 displacement. An appropriate Fourier series would be

$$f(t)=\sum_{n=1}^{\infty}a_{n}\sin\left(\frac{n\pi t}{t_{o}}\right)$$

where $$ {a_{n}}$$ are the amplitudes of those frequency components.

Similarly, if we had any function $$ {f(z)}$$ over the distance $$ {L_{z}}$$ from $$ {z=0}$$ to $$ {z=L_{z}}$$ and that started and ended at 0 height. We could similarly write it as

$$f(z)=\sum_{n=1}^{\infty}a_{n}\sin\left(\frac{n\pi z}{L_{z}}\right)$$

for some set of numbers or "amplitudes" $$ {a_{n}}$$.

We remember our set of normalized eigenfunctions

$$\psi_{n}(z)=\sqrt{\frac{2}{L_{z}}}\sin\left(\frac{n\pi z}{L_{z}}\right)$$

With some minor change, we could use these instead of sines

$$f(z)=\sum_{n=1}^{\infty}a_{n}\sin\left(\frac{n\pi z}{L_{z}}\right)=\sum_{n=1}^{\infty}b_{n}\psi_{n}(z)$$

where $$ {b_{n}=\sqrt{L_{z}/2}a_{n}}$$.

Now we can restate the same mathematics in new words

$$f(z)=\sum_{n=1}^{\infty}b_{n}\psi_{n}(z)$$

is now the expansion of $$ {f(z)}$$ in the complete set of (normalized) eigenfunctions $$ {\psi_{n}(z)}$$.

Note that, though we have illustrated this by connecting to Fourier series, this will work for other sets of eigenfunctions also.

A set of function such as the $$ {\psi_{n}(z)}$$ that can be used in this way to represent a function such as $$ {f(z)}$$ is referred to as a "basis set of functions" or, more simply, a "basis". The set of "expansion coefficients" (amplitudes) $$ {b_{n}}$$ is then the "representation" of $$ {f(z)}$$ in the basis $$ {\psi_{n}(z)}$$.

####1.2. Orthogonality of functions

Two non-zero functions $$ {g(z)}$$ and $$ {h(z)}$$ defined from 0 to $$ {L_{z}}$$ are said to be orthogonal if

$$\int_{0}^{L_{z}}g^{*}(z)h(z)\,dz=0$$

Mutual orthogonality is another common property of the eigenfunctions we will find.

$$\int_{0}^{L_{z}}\psi_{n}^{*}(z)\psi_{m}(z)\,dz=0 \text{ for } n\neq m$$

We can introduce the "Kronecker delta" for our normalized eigenfunctions,

$$\left\{\begin{array}{l} \delta_{nm}=0 \text{ for } n\neq m \\ \delta_{nn}=1 \end{array}\right.$$

We can therefore write the orthogonality and the normalization as one condition.

$$\int_{0}^{L_{z}}\psi_{n}^{*}(z)\psi_{m(z)}\,dz=\delta_{nm}$$

A set of functions that is both normalized and mutually orthogonal is "orthonormal".

Suppose we want to write the function $$ {f(x)}$$ in terms of a complete set of orthonormal functions $$ {\psi_{n}(x)}$$

$$f(x)=\sum_{n}c_{n}\psi_{n}(x)$$

To find the "expansion coefficients" $$ {c_{n}}$$ premultiply $$ {\psi_{m}^{*}(x)}$$ and integrate

$$\begin{array}{rcl}  \int\psi_{m}^{*}(x)f(x)\,dx&=&\int\psi_{m}^{*}(x)\left[\sum_{n}c_{n}\psi_{n}(x)\right]\,dx \\ &=&\sum_{n}c_{n}\int\psi_{m}^{*}(x)\psi_{n}(x)\,dx=\sum_{n}c_{n}\delta_{mn} \\ &=&c_{m} \end{array}$$

If we have an orthonormal complete set, we can now expand any function in it. Generally, an integral like $$ {\int\psi_{m}^{*}(x)f(x)\,dx}$$ is also called an "overlap integral".

####1.3. Barriers and boundary conditions

For our Schroedinger equation

$$-\frac{\hbar^{2}}{2m}\frac{d^{2}\psi(z)}{dz^{2}}+V(z)\psi(z)=E\psi(z)$$

If we presume that $$ {E}$$, $$ {V}$$ and $$ {\psi}$$ are finite, then $$ {d^{2}\psi/dz^{2}}$$ must be finite, so $$ {d\psi/dz}$$ *must be continuous* (if there is a jump in $$ {d\psi/dz}$$ then $$ {d^{2}\psi/dz^{2}}$$ would be infinite at that point). Also, $$ {d\psi/dz}$$ must be finite otherwise $$ {d^{2}\psi/dz^{2}}$$ could be infinite. For $$ {d\psi/dz}$$ to be finite, $$ {\psi}$$ *must be continuous*

Suppose we have a barrier of height $$ {V_{o}}$$ with potential 0 to the left of the barrier. A quantum mechanical wave is incident from the left. The energy $$ {E}$$ of this wave is positive. We allow for reflection from the barrier into the general region on the left. Using the general solution on the left with complex exponential waves.

$$\psi_{\text{left}}(z)=C\exp(ikz)+D\exp(-ikz)$$

where, as before $$ {k=\sqrt{2mE/\hbar^{2}}}$$. $$ {C\exp(ikz)}$$ is the incident wave, going right. And $$ {D\exp(-ikz)}$$ is the reflected wave, going left.

We change the Schroedinger equation to represent the wave equation inside the barrier:

$$\frac{d^{2}\psi(z)}{dz^{2}}=\frac{2m}{\hbar^{2}}(V_{o}-E)\psi(z)$$

where $$ {V_{o}>E}$$. The general solution for the wave on the right is

$$\psi_{\text{right}}=F\exp(\kappa z)+G\exp(-\kappa z)$$

where $$ {\kappa=\sqrt{2m(V_{o}-E)/\hbar^{2}}}$$, we presume $$ {F=0}$$, otherwise the wave increases exponentially to the right forever. The solution proposes that the wave inside the barrier is not zero. Instead, it falls off exponentially.

Using the boundary conditions, according to continuity of the wave function, at $$ {z=0}$$ gives

$$C+D=G$$

and according to continuity of the wave function derivative, at $$ {z=0}$$ gives

$$ikC-ikD=-\kappa G.$$

The solution to these two equations is

$$2C=\left(1+\frac{i\kappa}{k}\right)$$

Equivalently,

$$G=\frac{2k}{k+i\kappa}C=\frac{2k(k-i\kappa)}{k^{2}+\kappa^{2}}C$$

And $$D=\frac{k-i\kappa}{k+i\kappa}C$$

So, we have found the amplitude $$ {G}$$ of the wave in the barrier and the amplitude $$ {D}$$ of the reflected wave in terms of the amplitude $$ {C}$$ of the incident wave.

Note that

$$\left\vert \frac{D}{C}\right\vert ^{2}=\frac{k-i\kappa}{k+i\kappa}\frac{k+i\kappa}{k-i\kappa}=1$$

So the barrier is 100%; reflecting though there is a phase shift on reflection.

Probability density $$ {\propto\vert \psi_{\text{right}}(z)\vert ^{2}}$$ with $$ {\psi_{\text{right}}\propto\exp(-\kappa z)}$$ then $$ {\vert \psi_{\text{right}}\vert ^{2}\propto\exp(-2\kappa z)}$$

###2. Finite Well and Harmonic Oscillator

####2.1. The finite potential well

We will choose the height of the potential barriers at $$ {V_{o}}$$ with 0 potential energy at the bottom of the well. The thickness of the well is $$ {L_{z}}$$. Now we will choose the positive origin in the center of the well.

If there is an energy $$ {E}$$ for which there is a solution, then we already know what form the solution has to take. Sinusoidal in the middle exponentially decaying on either side.

For some eigenenergy $$E$$, with $$k=\sqrt{2mE/\hbar^{2}}$$ and $$\kappa=\sqrt{2m(V_{o}-E)/\hbar^{2}}$$:

for $$z<-L_{z}/2$$

$$\psi(z)=G\exp(\kappa z)$$

for $$-L_{z}/2<z<L_{z}/2$$

$$\psi(z)=A\sin(kz)+B\cos(kz)$$

for $$z>L_{z}/2$$

$$\psi(z)=F\exp(-\kappa z)$$

with constant $$ {A}$$, $$ {B}$$, $$ {G}$$ and $$ {F}$$.

From continuity of the wavefunction at $$z=L_{z}/2$$

$$FX_{L}=AS_{L}+BC_{L}$$

where $$ {X_{L}=exp(-\kappa L_{z}/2)}$$, $$ {S_{L}=\sin(kL_{z}/2)}$$, $$ {C_{L}=\cos(kL_{z}/2)}$$. Similarly at $$ {z=-L_{z}/2}$$

$$GX_{L}=-AS_{L}+BC_{L}$$

Continuity of the derivate gives at $$ {z=-L_{z}/2}$$

$$\frac{\kappa}{k}GX_{L}=AC_{L}+BS_{L}$$

at $$ {z=L_{z}/2}$$

$$-\frac{\kappa}{k}FX_{L}=AC_{L}-BS_{L}$$

Solve the above equations, the following can be obtained as long as $$ {F\neq -G}$$:

$$\tan\left(\frac{kL_{z}}{2}\right)=\frac{\kappa}{k}$$

This relation is effectively a condition for eigenvalues. And as long as $$ {F\neq G}$$:

$$-\cot\left(\frac{kL_{z}}{2}\right)=\frac{\kappa}{k}$$

This relation is also effectively a condition for eigenvalues.

+ $$ {F=G}$$, and $$ {\tan(kL_{z}/2)=\kappa/k}$$. One can derive that $$ {A=0}$$, therefore, inside the well

   $$\psi(z)\propto\cos(kz)$$

   which is an even function.

+ $$ {F=-G}$$, and $$ {-\cot(kL_{z}/2)=\kappa/k}$$. One can derive that $$ {B=0}$$, therefore, inside the well

   $$\psi(z)\propto\sin(kz)$$

   which is an odd function 

In order to solve for the eigenenergies, we need to change to "dimensionless" units. Let

$$E_{1}^{\infty}=\frac{\hbar^{2}}{2m}\left(\frac{\pi}{L_{z}}\right)^{2}$$

as the energy of the first level in the "infinite" potential well width $$ {L_{z}}$$, leading to dimensionless eigenenergy $$ {\varepsilon\equiv E/E_{1}^{\infty}}$$ and a dimensionless barrier height $$ {v_{o}\equiv V_{o}/E_{1}^{\infty}}$$, Also

$$k=\sqrt{2mE/\hbar^{2}}=(\pi/L_{z})\sqrt{\varepsilon}$$

$$\kappa=\sqrt{2m(V_{o}-E)/\hbar^{2}}=(\pi/L_{z})\sqrt{v_{o}-\varepsilon}$$

Consequently,

$$\frac{\kappa}{k}=\sqrt{\frac{v_{o}-\varepsilon}{\varepsilon}}$$

So,

$$\sqrt{\varepsilon}\tan[(\pi/2)\sqrt{\varepsilon}]=\sqrt{(v_{o}-\varepsilon)}$$

and

$$-\sqrt{\varepsilon}\cot[(\pi/2)\sqrt{\varepsilon}]=\sqrt{(v_{o}-\varepsilon)}$$

We can solve the eigenergies by using choosing specific $$ {v_{o}}$$ and use numeric approach to find intersection of above equations.

####2.2. The harmonic oscillator

The potential from the restoring force $$ {F}$$ is

$$V(z)=\int_{0}^{z}-F\,dz_{o}=\int_{0}^{z}Kz_{o}\,dz_{o}=\frac{1}{2}Kz^{2}=\frac{1}{2}m\omega^{2}z^{2}$$

Then we plug it into Schroedinger equation is

$$-\frac{\hbar^{2}}{2m}\frac{d^{2}\psi}{dz^{2}}+\frac{1}{2}m\omega^{2}z^{2}\psi=E\psi$$

For convenience, we define a dimensionless distance unit

$$\xi=\sqrt{\frac{m\omega}{\hbar}}z$$

so the Schroedinger equation becomes

$$\frac{1}{2}\frac{d^{2}\psi}{d\xi^{2}}-\frac{\xi^{2}}{2}\psi=-\frac{E}{\hbar\omega}\psi$$

One of the specific solution is

$$\psi\propto\exp(-\xi^{2}/2)$$

with a corresponding energy $$ {E=\hbar\omega/2}$$.

This suggests we look for solutions of the form

$$\psi_{n}(\xi)=A_{n}\exp(-\xi^{2}/2)H_{n}(\xi)$$

where $$ {H_{n}}$$ is some set of functions still to be determined.

Substituting the above equation into the Schroedinger equation gives

$$\frac{d^{2}H_{n}(\xi)}{d\xi^{2}}-2\xi\frac{dH_{n}(\xi)}{d\xi}+\left(\frac{2E}{\hbar\omega}-1\right)H_{n}(\xi)=0$$

This is the defining differential equation for the Hermite polynomials.

The solutions for above equation exist provided

$$\frac{2E}{\hbar\omega}-1=2n\quad n=0,1,2,\ldots$$

that is,

$$E_{n}=\left(n+\frac{1}{2}\right)\hbar\omega \text{ for } n=0,1,2,\ldots$$

are eigenengeries. The allowed energy levels are equally spaced separated by an amount $$ {\hbar\omega}$$ where $$ {\omega}$$ is the classical oscillation frequency.

The Hermite polynomials are satisfy a "recurrence relations"

$$H_{n}=2\xi H_{n-1}(\xi)-2(n-1)H_{n-2}(\xi)$$

and $$ {H_{1}=1}$$, $$ {H_{2}(\xi)=2\xi}$$.

By normalizing

$$\psi_{n}(\xi)=A_{n}\exp(-\xi^{2}/2)H_{n}(\xi)$$

gives

$$A_{n}=\sqrt{\frac{1}{\sqrt{\pi}2^{n}n!}}, \quad \xi=\sqrt{\frac{m\omega}{\hbar}}z$$

The above solution is dimensionless form, the original one is

$$  \psi_{n}(z)=\sqrt{\frac{1}{2^{n}n!}\sqrt{\frac{m\omega}{\pi\hbar}}}\exp\left(-\frac{m\omega}{2\hbar}z^{2}\right)H_{n}\left(\sqrt{\frac{m\omega}{\hbar}z}\right)$$

The intersection of the parabola and the dashed lines gives the "classical turning points" where a classical mass of that energy turns round and goes back downhill. (You need to watch the lecture for this interpretation).

###3. The Time-Dependent Schroedinger Equation

####3.1. Rationalizing the time-dependent Schroedinger equation

The relation between energy and frequency for quantum mechanics is

$$E=h\nu=\hbar\omega.$$

Schroedinger postulated the time-dependent equation

$$-\frac{\hbar^{2}}{2m}\nabla^{2}\Psi(\vec{r},t)+V(\vec{r},t)\Psi(\vec{r},t)=i\hbar\frac{\partial\Psi(\vec{r},t)}{\partial t}$$


Note that for a uniform potential. Schroedinger chose a sign for the right hand side, which that a wave with spatial part $$ {\propto\exp(ikz)}$$ is definitely going in the positive $$ {z}$$ direction. That is, including its time dependence would be of the form (for $$ {V=0}$$)

$$\exp[i(kz-Et/\hbar)]$$

To test compatibility with time-independent equation, time-independent equation solution $$ {\psi(\vec{r})}$$ can be written as

$$\Psi(\vec{r},t)=\psi(\vec{r})\exp(-iEt/\hbar)$$

We can tested that the above equation is indeed a solution to time-dependent equation. Therefore, every solution of time-independent Schroedinger equation is also a solution to time-dependent equation, with eigenenergy $$ {E}$$.

####3.2. Solutions of the time-dependent Schroedinger equation

Note that Schroedinger's use of a complex wave equation with the $$ {i}$$ on the right hand side, which means that generally the wave $$ {\Psi}$$ is required to be a complex entity. For example, for $$ {V=0}$$ though $$ {\exp[i(kz-Et/\hbar)]}$$ is a solution, $$ {\sin(kz-Et/\hbar)}$$ is not a solution.

In Schroedinger's equation, for a known potential $$ {V}$$. If we knew the wave function $$ {\Psi(\vec{r},t_{o})}$$ at every point in space at some time $$ {t_{o}}$$, we could evaluate the left hand side of the equation at that time for all $$ {\vec{r}}$$, so we would know $$ {\partial\Psi(\vec{r},t)/\partial t}$$ for all $$ {\vec{r}}$$, so we could integrate the equation to deduce $$ {\Psi(\vec{r},t)}$$ at all future times. Explicitly, knowing $$ {\partial\Psi(\vec{r},t)/\partial t}$$, we can calculate

$$\Psi(\vec{r},t_{o}+\delta t)\simeq\Psi(\vec{r},t_{o})+\left.\frac{\partial\Psi}{\partial t}\right\vert_{\vec{r},t_{o}}\delta t$$

That is, we can know the new wave function in space at the next instant in time and we can continue on the next instant and so on. We can then predict all future evolution of the wave function.

####3.3. Linear superposition

The time-dependent Schroedinger equation is linear in the wave function $$ {\Psi}$$. One reason is that no higher powers of $$ {\Psi}$$ appear anywhere in the equation. A second reason is that $$ {\Psi}$$ appears in every term there is no additive constant term anywhere.

Linearity requires two conditions obeyed by Schroedinger time-dependent equation. The two conditions can be summarized in

$$\Psi_{c}(\vec{r},t)=c_{a}\Psi_{a}(\vec{r},t)+c_{b}\Psi_{b}(\vec{r},t)$$

where $$ {\Psi_{a}}$$ and $$ {\Psi_{b}}$$ are solutions to time-dependent equation, $$ {c_{a}}$$ and $$ {c_{b}}$$ are (complex) constants. The above equation is also a solution.

We know that if the potential $$ {V}$$ is constant in time, each of the energy eigenstates $$ {\psi_{n}(\vec{r})}$$ with eigenenergy $$ {E_{n}}$$ is separately a solution of the time-dependent Schroedinger equation.

Now we also know that the set of eigenfunctions of problems we will consider is a complete set so the wave function at $$ {t=0}$$ can be expanded in them

$$\Psi(\vec{r},0)=\sum_{n}a_{n}\psi_{n}(\vec{r})$$

where the $$ {a_{n}}$$ are the expansion coefficients.

But we know that a function that starts out as $$ {\psi_{n}(\vec{r})}$$ will evolve in time as $$ {\Psi_{n}(\vec{r},t)=\exp(-iEt/\hbar)\psi_{n}(\vec{r})}$$. So, by linear superposition, the solution at time t is

$$\Psi(\vec{r},t)=\sum_{n}a_{n}\Psi_{n}(\vec{r},t)=\sum_{n}a_{n}\exp(-iEt/\hbar)\psi_{n}(\vec{r})$$
