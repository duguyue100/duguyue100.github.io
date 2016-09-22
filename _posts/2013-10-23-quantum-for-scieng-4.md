---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 4
date: 2013-10-23
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

###1. Time Evolution

####1.1. Superposition for particle in a box

Suppose we have an infinitely deep potential well with the particle in a linear superposition, for example, with equal parts of the first and second states of the well (This superposition is normalized)

$$\Psi(z,t)=\frac{1}{\sqrt{L_{z}}}\left[\exp\left(-i\frac{E_{1}}{\hbar}t\right)\sin\left(\frac{\pi z}{L_{z}}\right)+\exp\left(-i\frac{E_{2}}{\hbar}t\right)\sin\left(\frac{2\pi z}{L_{z}}\right)\right]$$

For this superposition, the probability density:

$$\vert \Psi(z,t)\vert ^{2}=\frac{1}{L_{z}}\left[\sin^{2}\left(\frac{\pi z}{L_{z}}\right)+\sin^{2}\left(\frac{2\pi z}{L_{z}}\right)+2\cos\left(\frac{E_{2}-E_{1}}{\hbar}t\right)\sin\left(\frac{\pi z}{L_{z}}\right)\sin\left(\frac{2\pi z}{L_{z}}\right)\right]$$

Note that this probability density has a part that is oscillating time at an angular frequency $$ {\omega_{21}=(E_{2}-E_{1})/\hbar=3E_{1}/\hbar}$$. Note also that the absolute energy origin does not matter here for this measurable quantity, only the energy difference $$ {E_{2}-E_{1}}$$ matters.

For the probability density $$ {\vert \psi_{1}(z)\vert ^{2}}$$ is same as the probability density $$ {\vert \Psi_{1}(z,t)\vert ^{2}}$$ where

$$\Psi_{1}(z,t)=\exp\left(-i\frac{E_{1}}{\hbar}t\right)\psi_{1}(z)$$

And it's the same fact for $$ {\vert \psi_{2}(z)\vert ^{2}}$$ and $$ {\vert \Psi_{2}(z,t)\vert ^{2}}$$.

However, when you add the amplitude up and take the probability of the sum, the equal superposition of the two oscillates at th angular frequency $$ {\omega_{21}=(E_{2}-E_{1})/\hbar=3E_{1}/\hbar}$$ (just like we worked out).

####1.2. Superposition for the harmonic oscillator

Quite generally, if we make a linear combination of two energy eigenstates with energies $$ {E_{a}}$$ and $$ {E_{b}}$$. The resulting probability distribution with oscillate at the (angular) frequency $$ {\omega_{ab}=\vert E_{a}-E_{b}\vert /\hbar}$$. So, if we have a superposition wave function

$$  \Psi_{ab}(\vec{r},t)=c_{a}\exp\left(-i\frac{E_{a}}{\hbar}t\right)\psi_{a}(\vec{r})+c_{b}\exp\left(-i\frac{E_{b}}{\hbar}t\right)\psi_{b}(\vec{r})$$

then the probability distribution will be

$$ \vert \Psi_{ab}(\vec{r},t)\vert ^{2}=\vert c_{a}\vert ^{2}\vert \psi_{a}(\vec{r})\vert ^{2}+\vert c_{b}\vert ^{2}\vert \psi_{b}(\vec{r})\vert ^{2}+2\vert c_{a}^{*}\psi_{a}^{*}(\vec{r})c_{b}\psi_{b}(\vec{r})\vert \cos\left[\frac{(E_{a}-E_{b})t}{\hbar}-\theta_{ab}\right]$$

where $$ {\theta_{ab}=\arg(c_{a}\psi_{a}(\vec{r})c_{b}^{*}\psi_{b}^{*}(\vec{r}))}$$.

In harmonic oscillator, we take the first and second state as example, the probability density is

$$\vert \Psi(z,t)\vert ^{2}=\vert \Psi_{0}(z,t)+\Psi_{1}(z,t)\vert ^{2}=\vert \Psi_{0}(z)\vert ^{2}+\vert \Psi_{1}(z)\vert ^{2}+2\cos(\omega t)\psi_{0}(z)\psi_{1}(z)$$

where the angular frequency $$ {\omega=(E_{1}-E_{0})/\hbar}$$.

####1.3. The coherent state

The coherent state for a harmonic oscillator of frequency $$ {\omega}$$ is

$$\Psi_{N}(\xi, t)=\sum_{n=0}^{\infty}c_{Nn}\exp\left[-i\left(n+\frac{1}{2}\right)\omega t\right]\psi_{n}(\xi)$$

where

$$c_{Nn}=\sqrt{\frac{N^{n}\exp(-N)}{n!}}$$

and the $$ {\psi_{n}(\xi)}$$ are the harmonic oscillator eigenstates.

Incidentally, note that for the expansion coefficients $$ {c_{Nn}}$$

$$\vert c_{Nn}\vert ^{2}=\frac{N^{n}\exp(-N)}{n!}$$

This is the Poisson distribution from statistics with mean $$ {N}$$ and standard deviation $$ {\sqrt{N}}$$.

###2. Wavepackets

####2.1. Group velocity

Consider two waves at different frequencies $$ {\omega_{1}}$$ and $$ {\omega_{2}}$$ and suppose that the wave velocity $$ {v}$$ is the same independent of frequency. Then the corresponding wavevector magnitude $$ {k=\omega/v}$$ is the same for both wave. If we take two such waves of equal amplitudes and add them together, then we get spatial beats --- a "spatial envelope". The envelope moves at the same speed as the wave.

Algebraically, for two waves at different frequencies, one at frequency $$ {\omega+\delta\omega}$$ and wavevector $$ {k+\delta k}$$ and one at frequency $$ {\omega-\delta\omega}$$ and wavevector $$ {k-\delta k}$$. By using complex exponential waves, we got a total wave

$$f(z,t)=\exp\left\{-i\left[(\omega+\delta\omega)t-(k+\delta k)z\right]\right\}+\exp\exp\left\{-i\left[(\omega-\delta\omega)t-(k-\delta k)z\right]\right\}$$

The equation can be rewritten as

$$f(z,t)=2\cos(\delta\omega t-\delta kz)\exp[-i(\omega t-kz)]$$

Note here, because $$ {k=\omega/v}$$ and $$ {v=\omega/k}$$ then $$ {\delta k=\delta w/v}$$ and $$ {v=\delta w/\delta k}$$.

But suppose the wave velocity is different for different frequencies (e.g. suppose the higher frequency wave has a slower velocity). Then the "envelope velocity" $$ {v_{g}=\delta w/\delta k}$$ which we will call the *group velocity* is not the same as the underlying wave velocity. More precisely, we define

$$v_{g}=\frac{d\omega}{dk}$$

as group velocity. And

$$v_{p}=\frac{\omega}{k}$$

as *phase velocity*.

####2.2. Group velocity for a free electron

The small dispersion in glass gives significant effects in long fibers. Large dispersions are found near absorption lines. In waveguides, different spatial forms (modes) propagate at different velocities dispersion from geometry or structure. Any structure whose physical properties such as refractive index change on a scale with a wavelength will also show string "structural" dispersion.

For a free electron where $$ {V(z)=0}$$, in one direction $$ {z}$$ the Schroedinger equation is

$$\frac{-\hbar^{2}}{2m}\frac{d^{2}\psi}{dz^{2}}=E\psi$$

with solution $$ {\psi(z)\propto\psi\exp(\pm ikz)}$$ and $$ {E=\frac{\hbar^{2}k^{2}}{2m}}$$. This means that

$$\omega=\frac{E}{\hbar}=\frac{\hbar k^{2}}{2m}$$

so $$\omega \propto k^{2}$$

*not* $$ {\omega\propto k}$$.

The group velocity of a free electron is given by

$$v_{g}=\frac{d\omega}{dk}=\frac{1}{\hbar}\frac{dE}{dk}=\frac{\hbar k}{m}=\sqrt{\frac{2E}{m}}$$

The group velocity $$ {v_{g}=\sqrt{\frac{2E}{m}}}$$ does gives us $$ {E=\frac{1}{2}mv_{g}^{2}}$$ which corresponds with out classical ideas of velocity and kinetic energy. This suggests it is meaningful to think of the electron as moving at the group velocity.

Note that phase velocity does not give us this kind of relation with $$ {E\equiv\hbar\omega=\hbar^{2}k^{2}/2m}$$, we have $$ {\frac{\omega}{k}\equiv v_{p}=\frac{\hbar k}{2m}}$$, then we can deduce

$$E=2mv_{p}^{2}$$

####2.3. Electron wavepackets

We can construct a "wavepacket" by putting together a liner superposition of energy eigensolutions. For a free electron or a similar particle of mass $$ {m}$$, the individual eignsolutions are plane waves. For propagating in the $$ {z}$$ direction, these are of the form

$$\Psi_{k}(z,t)\propto\exp\left\{-i\left[\frac{E(k)}{\hbar}t-kz\right]\right\}=\exp\{-i[\omega(k)t-kz\}$$

for some chosen value of $$ {k}$$, and hence of

$$\text{energy: } E(k)=\frac{\hbar^{2}k^{2}}{2m} \text{ frequency: }\omega(k)=\frac{E(k)}{\hbar}$$

One convenient and useful set of $$ {k}$$ values and amplitudes $$ {a_{k}}$$ to choose is a set of equally spaced $$ {k}$$ values with Gaussian amplitudes or "weights" for $$ {a_{k}}$$

$$\Psi_{G}(z,t)\propto\sum_{k}\exp\left[-\left(\frac{k-\bar{k}}{2\Delta k}\right)^{2}\right]\exp\{-i[\omega(k)t-kz\}$$

Here $$ {\bar{k}}$$ is the center of the distribution of $$ {k}$$ values, $$ {\Delta k}$$ is width parameter for the Gaussian function. Note that this gives a "pulse" that is also Gaussian in space.

As we let time evolve, by simply adding up the terms in our wavepackets sum at each time. We can see the wavepacket propagate moving to the right and getting wider. A wavepackets that increases in width as it propagates is said to be "dispersing". It gets wider because the change in $$ {\omega}$$ with $$ {k}$$ is not even linear. The effect is known as group velocity dispersion.

###3. Measurement, Operators and Expectation Values

####3.1. Quantum-mechanical measurement

Suppose we take some (normalized) quantum mechanical wave function $$ {\Psi(\vec{r},t)}$$ and expand it in some complete orthonormal set of spatial functions $$ {\psi_{n}(\vec{r})}$$. At least if we allow the expansion coefficients $$ {c_{n}}$$ to vary in time. We know we can always do this:

$$\Psi(\vec{r},t)=\sum_{n}c_{n}(t)\psi_{n}(\vec{r})$$

Then the fact that $$ {\Psi(\vec{r},t)}$$ is normalized means that we know the answer for the normalization integral

$$ \int_{-\infty}^{\infty}\vert \Psi(\vec{r},t)\vert ^{2}\,d^{3}\vec{r}=\int_{-\infty}^{\infty}\left[\sum_{n}c_{n}^{*}(t)\psi_{n}^{*}(\vec{r})\right]\times\left[\sum_{m}c_{m}(t)\psi_{m}(\vec{r})\right]\,d^{3}\vec{r}=1$$

Because of the orthogonality of the basis functions, only the terms with $$ {n=m}$$ survive the integration. Because of the orthonormality of the basis functions, the result from any such term will simply be $$ {\vert c_{n}(t)\vert ^{2}}$$, hence we have

$$\sum_{n}\vert c_{n}\vert ^{2}=1$$

On measurement of a state, the system collapses into the $$ {n}$$-th eigenstate of the quantity being measured with probability:

$$P_{n}=\vert c_{n}\vert ^{2}$$

In the expansion of the state in the eigenfunctions of the quantity being measured $$ {c_{n}}$$ is the expansion coefficient of the $$ {n}$$-th eigenfunction.

Suppose we do an experiment to measure the energy $$ {E}$$ of some quantum mechanical system. We could repeat the experiment many times and get statistical distribution of results. Given the probabilities $$ {P_{n}}$$ of getting a specific energy eigenstate, with energy $$ {E_{n}}$$. We would get an average answer:

$$\langle E\rangle=\sum_{n} E_{n}P_{n}=\sum_{n}E_{n}\vert c_{n}\vert ^{2}$$

where we call this average $$ {\langle E\rangle}$$ the "*expectation value*".

In the following context, we are describing Stern-Gerlach experiment with electrons which has shocking different result than classical view of the experiment. The apparatus has a non-uniform magnetic filed where locally the magnetic filed is more concentrated near the north pole magnet face. Imagine firing some small magnets. Initially along the dashed line (you need to see the video to get this). Because the magnetic field is non-uniform, a vertical magnet will be deflected up or down. A horizontally-oriented magnet will not be deflected and magnets of other orientations should be deflected by intermediate amounts. After "firing" many randomly oriented magnets, we should end up with a line on the screen.

Electrons have a quantum mechanical property called spin. It gives them a "magnetic moment" just like a small magnet. And when we fire electrons with no particular "orientation" of the spin into the Stern-Gerlach apparatus, we got only two dots! The explanation of this would be that we are measuring the vertical component of the spin. There are two eigenstates of this component: "up" and "down", so we have collapsed to the eigenstates.

####3.2. Expectation values and operators

In classical mechanics, the Hamiltonian is a function of position and momentum representing the total energy of the system. In quantum mechanical systems that can be analyzed by Schroedinger equation, we can define the entity

$$\hat{H}=-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r},t)$$

we can write the Schroedinger equation as

$$\hat{H}\psi(\vec{r})=E\psi(\vec{r}) \text{ and } \hat{H}\Psi(\vec{r},t)=i\hbar\frac{\partial\Psi(\vec{r},t)}{\partial t}$$

The entity $$ {\hat{H}}$$ is an "operator". The most general definition of an operator is an entity that turns one function into another. The particular operator $$ {\hat{H}}$$ is called the Hamiltonian operator. Just like the classical Hamiltonian function, it is related to the total energy of the system. This Hamiltonian idea extends beyond the specific Schroedinger-equation definition we have so far which is for single, non-magnetic particles. In general, in non-relativistic quantum mechanics, the Hamiltonian is the operator related to the total energy of the system.

In order to understand the relation between the Hamiltonian operator, the wave function and the expectation value of the energy. We start by looking at the integral

$$I=\int\Psi^{*}(\vec{r},t)\hat{H}\Psi(\vec{r},t)\,d^{3}\vec{r}$$

where $$ {\Psi(\vec{r},t)}$$ is the wave function of some system of interest. Let expend the wave function $$ {\Psi(\vec{r},t)}$$ in the (normalized) energy eigenstates $$ {\psi_{n}(\vec{r})}$$

$$\Psi(\vec{r},t)=\sum_{n}c_{n}(t)\psi_{n}(\vec{r})$$

So

$$\hat{H}\Psi(\vec{r},t)=\left[-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r},t)\right]\Psi(\vec{r},t)=\sum_{n}c_{n}E_{n}\psi_{n}(\vec{r})$$

Hence the integral becomes

$$ \int\Psi^{*}(\vec{r},t)\hat{H}\Psi(\vec{r},t)\,d^{3}\vec{r}=\int_{-\infty}^{\infty}\left[\sum_{m}c_{m}^{*}(t)\psi_{m}^{*}(\vec{r})\right]\times\left[\sum_{n}c_{n}(t)E_{n}\psi_{n}(\vec{r})\right]\,d^{3}\vec{r}$$

Because of the orthonormality of the basis functions $$ {\psi_{n}(\vec{r})}$$, the only terms in the double sum that survive are the ones for which $$ {n=m}$$. So

$$\int\Psi^{*}(\vec{r},t)\hat{H}\Psi(\vec{r},t)\,d^{3}\vec{r}=\sum_{n}E_{n}\vert c_{n}\vert^{2}$$

Equally,

$$\langle E\rangle=\int\Psi^{*}(\vec{r},t)\hat{H}\Psi(\vec{r},t)\,d^{3}\vec{r}$$

####3.3. Time evolution and the Hamiltonian

Taking Schroedinger's time dependent equation and rewriting as

$$\frac{\partial\Psi(\vec{r},t)}{\partial t}=-\frac{i\hat{H}}{\hbar}\Psi(\vec{r},t)$$

And now, we are targeting to seek the relationship between two different states in different times.

First we note that, because $$ {\hat{H}}$$ is a linear operator, for any number $$ {a}$$

$$\hat{H}[a\Psi(\vec{r},t)]=a[\hat{H}\Psi(\vec{r},t)]$$

Since this works for any function $$ {\Psi(\vec{r},t)}$$, we can write as a shorthand

$$\hat{H}a\equiv a\hat{H}$$

We define

$$\hat{H}^{2}=\hat{H}[\hat{H}\Psi(\vec{r},t)]$$

Specifically, for example, for the energy eigenfunction $$ {\psi_{n}(\vec{r})}$$

$$\hat{H}^{2}\psi_{n}(\vec{r})=\hat{H}[\hat{H}\psi_{n}(\vec{r})]=\hat{H}[E_{n}\psi_{n}(\vec{r})]=E_{n}^{2}\psi_{n}(\vec{r})$$

We can proceed inductively to define all higher powers: $$ {\hat{H}^{m+1}=\hat{H}[\hat{H}^{m}]}$$ which will give, for an energy eigenfunction

$$\hat{H}^{m}\psi_{n}(\vec{r})=E_{n}^{m}\psi_{n}(\vec{r})$$

Suppose the wave function at time $$ {t_{0}}$$ is $$ {\psi(\vec{r})}$$ which we expand in the energy eigenfunction $$ {\psi_{n}(\vec{r})}$$ as $$ {\psi(\vec{r})=\sum_{n}a_{n}\psi_{n}(\vec{r})}$$, and we know that

$$\Psi(\vec{r},t_{1})=\sum_{n}a_{n}\exp\left[-\frac{iE_{n}(t_{1}-t_{0})}{\hbar}\right]\psi_{n}(\vec{r})$$

We can write exponentials as power series,

$$ \Psi(\vec{r},t_{1})=\sum_{n}a_{n}\left[1+\left(-\frac{iE_{n}(t_{1}-t_{0})}{\hbar}\right)+\frac{1}{2!}\left(-\frac{iE_{n}(t_{1}-t_{0})}{\hbar}\right)^{2}+\ldots\right]\psi_{n}(\vec{r})$$

Because we showed that $$ {\hat{H}^{m}\psi_{n}(\vec{r})=E_{n}^{m}\psi_{n}(\vec{r})}$$,

$$ \Psi(\vec{r},t_{1})=\sum_{n}a_{n}\left[1+\left(-\frac{i\hat{H}(t_{1}-t_{0})}{\hbar}\right)+\frac{1}{2!}\left(-\frac{i\hat{H}(t_{1}-t_{0})}{\hbar}\right)^{2}+\ldots\right]\psi_{n}(\vec{r})$$

Because the operator $$ {\hat{H}}$$ and all its power commute with scalar quantities (numbers) we can rewrite

$$ \Psi(\vec{r},t_{1})=\left[1+\left(-\frac{i\hat{H}(t_{1}-t_{0})}{\hbar}\right)+\frac{1}{2!}\left(-\frac{i\hat{H}(t_{1}-t_{0})}{\hbar}\right)^{2}+\ldots\right]\sum_{n}a_{n}\psi_{n}(\vec{r})$$

And this equation can be reverse to exponential

$$\Psi(\vec{r},t_{1})=\exp\left(-\frac{i\hat{H}(t_{1}-t_{0})}{\hbar}\right)\Psi(\vec{r},t_{0})$$
