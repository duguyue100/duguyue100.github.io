---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 2
date: 2013-10-07
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

###1. Wave Propagation

####1.1. Plane waves and interference

Generalizing to 3 dimensions, the wave equation becomes

$$\nabla^{2}\phi-\frac{1}{c^{2}}\frac{\partial^{2}\phi}{\partial t^{2}}=0$$

where

$$\nabla^{2}\equiv \frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}$$

or equivalently, with unit vectors $$ {\hat{x}}$$, $$ {\hat{y}}$$ and $$ {\hat{z}}$$ in the corresponding directions

$$\nabla^{2}\equiv \nabla\cdot\nabla=\left(\hat{x}\frac{\partial}{\partial x}+\hat{y}\frac{\partial}{\partial y}+\hat{z}\frac{\partial}{\partial z}\right)\left(\hat{x}\frac{\partial}{\partial x}+\hat{y}\frac{\partial}{\partial y}+\hat{z}\frac{\partial}{\partial z}\right)$$

Here is an example of plane wave. We can check that a monochromatic (one frequency) "plane wave" of the form $$ {\exp[i(\vec{k}\cdot\vec{r}-\omega t)]}$$ where $$ {\vec{r}=x\hat{x}+y\hat{y}+z\hat{z}}$$ and $$ {\vec{k}=k_{x}\hat{x}+k_{y}\hat{y}+k_{z}\hat{z}}$$ is a solution when $$ {k=\omega/c}$$.

$$\nabla^{2}\exp[i(\vec{k}\cdot\vec{r}-\omega t)]=\nabla\cdot\nabla\exp[i(\vec{k}\cdot\vec{r}-\omega t)]=-(k_{x}^{2}+k_{y}^{2}+k_{z}^{2})\exp[i(\vec{k}\cdot\vec{r}-\omega t)]$$

and

$$\frac{\partial^{2}}{\partial t^{2}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)]=-\omega^{2}\exp[i(k\cdot r-\omega t)]$$

Then choosing $$ {k=\omega/c}$$, the left hand of wave equation is 0.

Because the wave equation is linear, the sum is also a solution showing interference.

####1.2. Diffraction

For a source or aperture of width $$ {d}$$, the diffraction angle

$$\theta\sim\frac{\lambda}{d}$$

where $$ {\lambda}$$ is the wavelength.

####1.3. Diffraction from Periodic Structures

The angle $$ {\theta}$$ of theses diffracted waves is given by simple geometry

$$\sin\theta=\frac{\lambda}{s}$$

where $$ {\lambda}$$ is the wave length.

###2. Schroedinger's Wave Equation

####2.1. From de Broglie to Schroedinger

Recall de Broglie is that the electron wavelength $$ {\lambda}$$ is given by

$$\lambda=\frac{h}{p}$$

where $$ {p}$$ is the electron momentum and $${h}$$ is Plank's constant: $$ {h=6.63\times10^{-34}J\cdot s}$$.

In three dimensions, we can rewrite Helmholtz wave equation as:

$$\nabla^{2}\psi=-k^{2}\psi$$

And with de Broglie hypothesis and the definition $$ {k=2\pi/\lambda}$$, therefore $$ {k=p/\hbar}$$. Hence,

$$\nabla^{2}\psi=-\frac{p^{2}}{\hbar^{2}}\psi$$

Suppose the mass of the particle is $$ {m}$$, then we can change the equation to

$$-\frac{\hbar{2}}{2m}\nabla^{2}\psi=\frac{p^{2}}{2m}\psi$$

Notice that $$ {\frac{p^{2}}{2m}}$$ is the kinetic energy of the particle. Let $$ {E}$$ as the total energy of the particle and $$ {V(\vec{r})}$$ as potential energy of the particle. Finally, we can generate time-independent Schroedinger equation

$$\left(-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r})\right)\psi=E\psi$$

Born's postulate is that the probability $$ {P(\vec{r})}$$ of finding an electron near any specific point $$ {\vec{r}}$$ in space is proportional to the modulus squared $$ {\vert \psi(\vec{r})\vert ^{2}}$$ of the wave amplitude $$ {\psi(\vec{r})}$$. $$ {\vert \psi(\vec{r}\vert ^{2}}$$ can therefore be viewed as a "probability density" with $$ {\psi(\vec{r})}$$ called a "probability amplitude" or a "quantum mechanical amplitude".

####2.2. Diffraction by two slits

Young's slits is an opaque mask has two slits cut in it, a distance $$ {s}$$ apart. Then we shine a plane wave on the mask from the left. The slits as point sources give an interference pattern.

The distance from the upper source to point $$ {x}$$ on the screen is

$$\sqrt{(x-s/2)^{2}+z_{o}^{2}}$$

where $$ {x}$$ is the distance between the point and middle point of the screen, $$ {s}$$ is the distance between two slits, and $$ {z_{o}}$$ is the distance between mask and screen. Take the approximation of the above equation

$$\sqrt{\left(x-\frac{s}{2}\right)^{2}+z_{o}^{2}}\simeq z_{o}+\frac{(x-s/2)^{2}}{2z_{o}}=z_{o}+\frac{x^{2}}{2z_{o}}+\frac{s^{2}}{8z_{o}}-\frac{sx}{2z_{o}}$$

Similarly, the distance from the lower source to point $$ {x}$$ on the screen is

$$\sqrt{(x+s/2)^{2}+z_{o}^{2}}$$

and the approximation is given by

$$\sqrt{\left(x+\frac{s}{2}\right)^{2}+z_{o}^{2}}\simeq z_{o}+\frac{(x+s/2)^{2}}{2z_{o}}=z_{o}+\frac{x^{2}}{2z_{o}}+\frac{s^{2}}{8z_{o}}+\frac{sx}{2z_{o}}$$

For large $$ {z_{o}}$$ the waves are approximately uniformly "bright"

$$\psi_{s}(x)\propto \exp\left[ik\sqrt{\left(x-\frac{s}{2}\right)^{2}+z_{o}^{2}}\right]+\exp\left[ik\sqrt{\left(x+\frac{s}{2}\right)^{2}+z_{o}^{2}}\right]$$

Using the approximation for the distance gives

$$\psi_{s}(x)\propto \exp(i\alpha)\left\{\exp\left[ik\frac{sx}{2z_{o}}\right]+\exp\left[-ik\frac{sx}{2z_{o}}\right]\right\}$$

where $$ {\alpha=k(z_{o}+x^{2}/2z_{o}+s^{2}/8z_{o})}$$.

Now, noted that $$ {\exp(i\theta)+\exp(-i\theta)=2\cos(\theta)}$$ and in general, angular wavenumber $$ {k=2\pi/\lambda}$$

$$\psi_{s}(x)\propto \exp(i\alpha)\cos\left(k\frac{sx}{2z_{o}}\right)=\exp(i\alpha)\cos\left(\frac{\pi sx}{\lambda z_{o}}\right)$$

So the "intensity" of the beam

$$\vert \psi_{s}(x)\vert ^{2}\propto \cos^{2}\left(\frac{\pi sx}{\lambda z_{o}}\right)=\frac{1}{2}\left[1+\cos\left(\frac{2\pi sx}{\lambda z_{o}}\right)\right]$$

Therefore, the interference fringes are spaced by $$ {d_{s}=\lambda z_{o}/s}$$.

###3. Particle in Box

####3.1. Linearity and normalization

We see that Schroedinger's equation is linear. The wave function $$ {\psi}$$ appears only in first order, there are no second order or higher order terms. So if $$ {\psi}$$ is a solution to Schroedinger's equation, so also is $$ {a\psi}$$.

Born postulated the probability $$ {P(\vec{r})}$$ of finding a particle near a point $$ {\vec{r}}$$ is $$ {\propto\vert \psi(\vec{r})\vert ^{2}}$$. Specifically let us define $$ {P(\vec{r})}$$ as a "probability density". For some very small (infinitesimal) volume $$ {d^{3}\vec{r}}$$ around $$ {\vec{r}}$$. The probability of finding the particle in that volume is $$ {P(\vec{r})d^{3}r}$$. So, the sum of all such probabilities should be 1

$$\int P(\vec{r})d^{3}\vec{r}=1$$

However, unless we have been lucky, out solution to Schroedinger's equation did not give a $$ {\psi(\vec{r})}$$ so that $$ {\int\vert \psi(\vec{r})\vert ^{2}d^{3}\vec{r}=1}$$.

Generally, this integral would give some other real positive number which we could write as $$ {1/\vert a\vert ^{2}}$$ where $$ {a}$$ is some (possible complex) number. That is

$$\int\vert \psi(\vec{r})\vert ^{2}d^{3}\vec{r}=\frac{1}{\vert a\vert ^{2}}$$

But we know that if $$ {\psi(\vec{r})}$$ is a solution of Schroedinger equation, so also is $$ {a\psi(\vec{r})}$$. So if we use the solution $$ {\psi_{N}=a\psi}$$ instead of $$ {\psi}$$ then

$$\int\vert \psi_{N}(\vec{r})\vert ^{2}d^{3}\vec{r}=1$$

and we can use $$ {\vert \psi_{N}(\vec{r})\vert ^{2}}$$ as the probability density. $$ {\psi_{N}(\vec{r})}$$ would then be called a "normalization wave function".

Note that normalization only sets the magnitude of $$ {a}$$, not the phase. We are free to choose any phase for $$ {a}$$ or indeed for the original solution $$ {\psi}$$. If we think of space as infinite functions like $$ {\sin(kx)}$$, $$ {\cos(kx)}$$ and $$ {\exp(i\vec{k}\cdot\vec{r})}$$ cannot be normalized in this way. Technically, their squared modulus is not "Lebesgue integrable" (They are not "L2" functions). This difficulty is mathematical, not physical. It is caused by over-idealizing the mathematics to get functions that are simple to use. There are few "work-around" for this difficulty 

+ only work with finite volumes in actual problems (this is the most common solution)
+ use "normalization to delta function" (introduces another infinity to compensate for the first one) 

####3.2. Solving for the particle in a box

We consider a particle of mass $$ {m}$$ with a spatially-varying potential $$ {V(z)}$$ in the $$ {z}$$ direction, so the Schroedinger equation

$$-\frac{\hbar^{2}}{2m}\frac{d^{2}\psi(z)}{dz^{2}}+V(z)\psi(z)=E\psi(z)$$

when $$ {E}$$ is the energy of the particle and $$ {\psi(z)}$$ is the wave function.

Suppose the potential energy is a simple "rectangular" potential well thickness $$ {L_{z}}$$. Potential energy is constant inside, and we choose $$ {V=0}$$ there. Rising to infinity at the walls. We will sometimes call this an infinite or infinitely deep (potential) well. Because these potentials at $$ {z=0}$$ and $$ {z=L_{z}}$$ are infinitely high, but the particle's energy $$ {E}$$ is presumably finite. We presume there is no possibility of finding the particle outside. So the wave function $$ {\psi}$$ is 0 there so $$ {\psi}$$ should be 0 at the walls. With these choices, the Schroedinger's equation becomes

$$-\frac{\hbar^{2}}{2m}\frac{d^{2}\psi(z)}{dz^{2}}=E\psi(z)$$

with the boundary conditions $$ {\psi(0)=0}$$ and $$ {\psi(L_{z})=0}$$.

The general solution to previous equation is

$$\psi(z)=A\sin(kz)+B\cos(kz)$$

where $$ {A}$$ and $$ {B}$$ are constants and $$ {k\sqrt{2mE/\hbar^{2}}}$$. The boundary condition $$ {\psi(0)=0}$$, means $$ {B=0}$$. Then the solution reduced to

$$\psi(z)=A\sin(kz)$$

and because of boundary $$ {\psi(L_{z})=0}$$, $$ {kz}$$ must be multiple of $$ {\pi}$$, therefore $$ {k=\sqrt{2mE/\hbar^{2}}=n\pi/L_{z}}$$ where $$ {n}$$ is an integer. Since $$ {E=(\hbar^{2}k^{2})/2m}$$, the solutions are

$$\psi_{n}(z)=A\sin\left(\frac{n\pi z}{L_{z}}\right) \text{ with } E_{n}=\frac{\hbar^{2}}{2m}\left(\frac{n\pi}{L_{z}}\right)^{2}$$


We restrict $$ {n}$$ to positive integers for following reasons: since $$ {\sin(-a)=-sin(a)}$$ for any real number $$ {a}$$, the wave functions with negative $$ {n}$$ are same as those with positive $$ {n}$$ with an arbitrary factor, here -1. The wave function for $$ {n=0}$$ is trivial, the wave function is 0 everywhere.

We can normalize the wave function

$$\int_{0}^{L_{z}}\vert A_{n}\vert ^{2}\sin^{2}\left(\frac{n\pi z}{L_{z}}\right)\,dz=\vert A_{n}\vert ^{2}\frac{L_{z}}{2}$$

to have this integral equal 1 by choosing $$ {\vert A_{n}\vert=\sqrt{2/L_{z}}}$$. Note that $$ {A_{n}}$$ can be complex.

####3.3. Nature of the particle-in-a-box solutions

Solutions with a specific set of allowed values of a parameter (here energy) are eigenvalues and with a particular function associated with each such value are eigenfunctions or eigensolutions. Here, since the parameter is an energy, we can call the eigenvalues as eigenenergies and we can refer to the eigenfunctions as the energy eigenfunctions.

Note in some problem, it can be possible to have more then one eigenfunction with a given eigenvalue, this phenomenon is known as "degeneracy". The number of such states with a same eigenvalue is called "the degeneracy" of that state.

Note that these eigenfunctions have definite symmetry the $$ {n=2k-1}$$ functions are the mirror image on the left of what they are on the right, such a function has "even parity" or is said to be an "even function". The $$ {n=2k}$$ eigenfunctions are an inverted image. The value at any point on the right of the center is exactly minus the value of the "mirror image" point on the left of the center. Such a function has "odd parity" or is said to be an "odd function".

This particle-in-a-box behavior is very different from the classical case 

+ there is only a discrete set of possible value for the energy
+ there is a minimum possible energy for the particle, corresponding to $$ {n=1}$$, sometimes called a "zero-point energy"
+ the particle is not uniformly distributed over the box, and its distribution is different for different energies. The probability obeys a standing wave pattern. 

In quantum mechanical calculations, we can always use Joules as unit of energy but these are rather large. A very convenient energy unit which also has a simple physical significance is electron-volt (eV)

$$1\text{eV}\simeq1.602\times10^{-19}J $$

1 eV is the energy change of an electron in moving through an electrostatic potential change of 1 V.
