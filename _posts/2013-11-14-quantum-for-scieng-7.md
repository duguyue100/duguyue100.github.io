---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 7
date: 2013-11-14
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---


## 1. Angular Momentum

### 1.1. Angular momentum operators

We will have operators corresponding to angular momentum about different orthogonal axes $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$, and $$ {\hat{L}_{z}}$$ though they will not commute with each other, in contrast to the linear momentum operator $$ {\hat{p}_{x}}$$, $$ {\hat{p}_{y}}$$ and $$ {\hat{p}_{z}}$$ which do commute. We will, however, find another useful angular momentum operator $$ {\hat{L}^{2}}$$ which does commute separately with each of $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$ and $$ {\hat{L}_{z}}$$. The eignfunctions for $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$, $$ {\hat{L}_{z}}$$ are simple. Those for $$ {\hat{L}^{2}}$$, the spherical harmonics, are more complicated, but can be understood relatively simply and form the angular shapes of the hydrogen atom orbitals.

The classical angular momentum of a small object of (vector) linear momentum $$\mathbf{p}$$ centered at a point given by the vector displacement $$\mathbf{r}$$ relative to some origin is $$\mathbf{L}=\mathbf{r}\times\mathbf{p}$$.

As usual

$$
\mathbf{C}=\mathbf{A}\times\mathbf{B}=\mathbf{c}Ab\sin\theta\equiv\begin{vmatrix}\mathbf{i} & \mathbf{j} & \mathbf{k} \\ A_{x} & A_{y} & A_{z} \\ B_{x} & B_{y} & B_{z}\end{vmatrix}
$$

where $$ {\mathbf{i}}$$, $$ {\mathbf{j}}$$, $$ {\mathbf{k}}$$ are unit vectors in $$ {x}$$, $$ {y}$$ and $$ {z}$$ directions. $$ {\mathbf{C}}$$ is perpendicular to the plane of $$ {\mathbf{A}}$$ and $$ {\mathbf{B}}$$. $$ {\theta}$$ is the angle between the vector $$ {\mathbf{A}}$$ and $$ {\mathbf{B}}$$. $$ {\mathbf{c}}$$ is unit vector in the direction of the vector $$ {\mathbf{C}}$$. Note that, in previous equation, the ordering of the multiplications in the second line is chosen to work also for operators instead of numbers for one or other vector, the sequence of multiplications in each term is always in the sequence of the rows from top to bottom.

With classical angular momentum, we can explicitly write out the various components

$$
L_{x}=yp_{z}-zp_{y}\quad L_{y}=zp_{x}-xp_{z}\quad L_{z}=xp_{y}-yp_{x}
$$


Now we can propose a quantum mechanical angular momentum operator $$ {\hat{\mathbf{L}}}$$ based on substituting the position and momentum operators

$$
\hat{\mathbf{L}}=\hat{\mathbf{r}}\times\hat{\mathbf{p}}=-i\hbar(\mathbf{r}\times\nabla)
$$

and similarly write out component operators

$$
\begin{array}{rcl}  \hat{L}_{x}&=&\hat{y}\hat{p}_{z}-\hat{z}\hat{p}_{y}=-i\hbar\left(y\frac{\partial}{\partial z}-z\frac{\partial}{\partial y}\right) \\ \hat{L}_{y}&=&\hat{z}\hat{p}_{x}-\hat{x}\hat{p}_{z}=-i\hbar\left(z\frac{\partial}{\partial x}-x\frac{\partial}{\partial z}\right) \\ \hat{L}_{z}&=&\hat{x}\hat{p}_{y}-\hat{y}\hat{p}_{x}=-i\hbar\left(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x}\right) \end{array}
$$

which are each Hermitian, and so, correspondingly, is the operator $$ {\hat{\mathbf{L}}}$$ itself.

The operators corresponding to individual coordinate directions obey commutation relations

$$
\begin{array}{rcl}  \hat{L}_{x}\hat{L}_{y}-\hat{L}_{y}\hat{L}_{x}&=&[\hat{L}_{x}, \hat{L}_{y}]=i\hbar\hat{L}_{z} \\ \hat{L}_{y}\hat{L}_{z}-\hat{L}_{z}\hat{L}_{y}&=&[\hat{L}_{y}, \hat{L}_{z}]=i\hbar\hat{L}_{x} \\ \hat{L}_{z}\hat{L}_{x}-\hat{L}_{x}\hat{L}_{z}&=&[\hat{L}_{z}, \hat{L}_{x}]=i\hbar\hat{L}_{y} \\ \end{array}
$$

These individual commutation relations can be written in a more compact form

$$
\hat{\mathbf{L}}\times \hat{\mathbf{L}}=i\hbar\hat{\mathbf{L}}
$$

Unlike operators for position and for linear momentum, the different components of this angular momentum operator do not commute with one another. Though a particle can have simultaneously a well-defined position in both $$ {x}$$ and $$ {y}$$ directions or have simultaneously a well-defined momentum in both the $$ {x}$$ and $$ {y}$$ directions. A particle cannot in general simultaneously have a well-defined angular momentum component in more than one direction.

###1.2. Angular momentum eigenfunctions

The relation between spherical polar and Cartesian coordinates is

$$
\begin{array}{rcl}  x&=& r\sin\theta\cos\phi \\ y&=& r\sin\theta\sin\phi \\ z&=& r\cos\theta \end{array}
$$

$${\theta}$$ is called polar angle and $${\phi}$$ is the azimuthal angle.

In inverse form

$$
\begin{array}{rcl}  r&=&\sqrt{x^{2}+y^{2}+z^{2}} \\ \theta&=&\sin^{-1}\left(\frac{\sqrt{x^{2}+y^{2}}}{\sqrt{x^{2}+y^{2}+z^{2}}}\right) \\ \phi&=&\tan^{-1}\left(\frac{y}{x}\right) \end{array}
$$


With these definitions of spherical polar coordinates and with standard partial derivative relations of the form

$$
\frac{\partial}{\partial x}=\frac{\partial r}{\partial x}\frac{\partial}{\partial r}+\frac{\partial\theta}{\partial x}\frac{\partial}{\partial\theta}+\frac{\partial\phi}{\partial x}\frac{\partial}{\partial\phi}
$$

for each of the Cartesian coordinate directions, we can rewrite the angular momentum operator components in spherical polar coordinates.

From previous obtained commutators, we obtain

$$
\begin{array}{rcl}  \hat{L}_{x}&=&i\hbar\left(\sin\phi\frac{\partial}{\partial\theta}+\cot\theta\cos\phi\frac{\partial}{\partial\phi}\right) \\ \hat{L}_{y}&=&i\hbar\left(-\cos\phi\frac{\partial}{\partial\theta}+\cot\theta\cos\phi\frac{\partial}{\partial\phi}\right) \\ \hat{L}_{z}&=&-i\hbar\frac{\partial}{\partial\phi} \end{array}
$$

Using $$ {\hat{L}_{z}=-i\hbar\frac{\partial}{\partial\phi}}$$, we solve for the eigenfunctions and eigenvalues of $$ {\hat{L}_{z}}$$. The eigen equation is

$$
\hat{L}_{z}\Phi(\phi)=m\hbar\Phi(\phi)
$$

where $$ {m\hbar}$$ is the eigenvalue to be determined. The solution of this equation is

$$
\Phi(\phi)=\exp(im\phi)
$$

The requirements that the wavefunction and its derivative are continuous when we return to where we started, mean that $$ {m}$$ must be an integer (positive, negative or zero). Hence we find that the angular momentum around the $$ {z}$$ axis is quantized with units of angular momentum of $$ {\hbar}$$.

##2. The L Squared Operator

###2.1. Separating the L squared operator

In quantum mechanics, we also consider another operator associated with angular momentum the operator $$ {\hat{L}^{2}}$$. This should be thought of as the "dot" product of $$ {\hat{\mathbf{L}}}$$ with itself and is defined as

$$
\hat{L}^{2}=\hat{L}_{x}^{2}+\hat{L}_{y}^{2}+\hat{L}_{z}^{2}
$$

It is straightforward to show when that

$$
\hat{L}^{2}=-\hbar^{2}\nabla_{\theta,\phi}^{2}
$$

when the operator $$ {\nabla_{\theta,\phi}^{2}}$$ is given by

$$
\nabla_{\theta,\phi}^{2}=\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)+\frac{1}{\sin^{2}\theta}\frac{\partial^{2}}{\partial\phi^{2}}\right]
$$

which is actually $$ {\theta}$$ and $$ {\phi}$$ part of the Laplacian ($$ {\nabla^{2}}$$) operator in spherical polar coordinator hence the notation.

$$ {\hat{L}^{2}}$$ commutes with each of $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$, and $$ {\hat{L}_{z}}$$. Of course, the choice of the $$ {z}$$ direction is arbitrary. We could equally well have chosen the polar axis along the $$ {x}$$ or $$ {y}$$ directions. Then it would similarly be obvious that $$ {\hat{L}^{2}}$$ commutes with $$ {\hat{L}_{x}}$$ or $$ {\hat{L}_{y}}$$. And the reason why $$ {\hat{L}^{2}}$$ commute with each of $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$ and $$ {\hat{L}_{z}}$$ is that we can choose the eigenfunctions of $$ {\hat{L}^{2}}$$ to be the same as those of any one of $$ {\hat{L}_{x}}$$, $$ {\hat{L}_{y}}$$, and $$ {\hat{L}_{z}}$$.

We want eigenfunctions of $$ {\hat{L}^{2}}$$ or, equivalently, $$ {\nabla_{\theta, \phi}^{2}}$$ and so the equation we hope to solve is of the form

$$
\nabla_{\theta,\phi}^{2}Y_{lm}(\theta,\phi)=-l(l+1)Y_{lm}(\theta,\phi)
$$

We anticipate the answer by writing the eigenvalue in the form $$ {-l(l+1)}$$ but it is just any arbitrary number to be determined. The notation $$ {Y_{lm}(\theta,\phi)}$$ also anticipates the final answer but it is arbitrary function to be determined.

We presume that the final eigenfunctions can be separated in the form

$$
Y_{lm}(\theta,\phi)=\Theta(\theta)\Phi(\phi)
$$

where $$ {\Theta(\theta)}$$ only depends on $$ {\theta}$$ and $$ {\Phi(\phi)}$$ only depends on $$ {\phi}$$.

Substituting this form in the previous equation gives

$$
\frac{\Phi(\phi)}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)\Theta(\theta)+\frac{\Theta(\theta)}{\sin^{2}\theta}\frac{\partial^{2}\Phi(\phi)}{\partial\phi^{2}}=-l(l+1)\Theta(\theta)\Phi(\phi)
$$

Multiplying by $$ {\sin^{2}\theta/\Theta(\theta)\Phi(\phi)}$$ and rearranging, gives

$$
\frac{1}{\Phi(\phi)}\frac{\partial^{2}\Phi(i)}{\partial\phi^{2}}=-l(l+1)\sin^{2}\theta-\frac{\sin\theta}{\Theta(\theta)}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)\Theta(\theta)
$$

The left hand side depends on only $$ {\phi}$$ whereas the right hand side depends only on $$ {\theta}$$ so these must both equal a ("separation") constant. Anticipating the answer, we choose a separation constant of $$ {-m^{2}}$$ where $$ {m}$$ is still to be determined.

Now for $$ {\phi}$$ equation, we have in the following form:

$$
\frac{d^{2}\Phi(\phi)}{d\phi^{2}}=-m^{2}\Phi(\phi)
$$

The solutions to an equation like this are of the form $$ {\sin m\phi}$$, $$ {\cos m\phi}$$ or $$ {\exp im\phi}$$. We choose the exponential form $$ {\exp im\phi}$$, so $$ {\Phi}$$ is also a solution of the $$ {\hat{L}_{z}}$$ eigen equation

$$
\hat{L}_{z}\Phi(\phi)=m\hbar\Phi(\phi)
$$

We expect that $$ {\Phi}$$ and its derivative are continuous, so this wavefunction must repeat every $$ {2\pi}$$ of angle $$ {\phi}$$, hence, $$ {m}$$ must be an integer.

For $$ {\theta}$$ equation, we have in the following form (already rearranged)

$$
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d}{d\theta}\right)\Theta(\theta)-\frac{m^{2}}{\sin^{2}\theta}\Theta(\theta)+l(l+1)\Theta(\theta)=0
$$

This is the associated Legendre equation whose solution are the associated Legendre function

$$
\Theta(\theta)=P_{l}^{m}(\cos\theta)
$$

The solutions required that $$ {l=0,1,2,3,\ldots,}$$ and $$ {-l\leq m\leq l}$$ ($$ {m}$$ is integer).

The associated Legendre functions can conveniently be defined as using Rodrigue's formula

$$
P_{l}^{m}(x)=\frac{1}{2^{l}l!}(1-x^{2})^{m/2}\frac{d^{l+m}}{dx^{l+m}}(x^{2}-1)^{l}
$$

We see that these functions $$ {P_{l}^{m}(x)}$$ have following properties: 

+ The highest power of the argument $$ {x}$$ is always $$ {x^{l}}$$.
+ The functions for a given $${l}$$ for $$ {+m}$$ and $$ {-m}$$ are identical other than for numerical perfactors.
+ Less obviously, between -1 and +1 and not including the values at those end points the function have $$ {l-\vert m\vert}$$ zeros. 

Putting this all together, the eigen equation is

$$
\hat{L}^{2}Y_{lm}(\theta,\phi)=\hbar^{2}l(l+1)Y_{lm}(\theta,\phi)
$$

with *spherical harmonics* $$ {Y_{lm}(\theta,\phi)}$$ as the eigenfunctions which, after normalization, can be written

$$
Y_{lm}(\theta,\phi)=(-1)^{m}\sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}P_{l}^{m}(\cos\theta)\exp(im\phi)
$$

where $$ {l=0,1,2,3,\ldots}$$, where $$ {m}$$ is an integer, $$ {-l\leq m\leq l}$$ and the eigenvalues are $$ {\hbar^{2}l(l+1)}$$

As is easily verify these spherical harmonics are also eigenfunctions of the $$ {\hat{L}_{z}}$$ operator. Explicitly, we have the eigen equation

$$
\hat{L}_{z}Y_{lm}(\theta,\phi)=m\hbar Y_{lm}(\theta,\theta)
$$

with eigenvalues of $$ {\hat{L}_{z}}$$ being $$ {m\hbar}$$.

It makes no difference to the $$ {\hat{L}_{z}}$$ eigenfunctions if we multiply them by a function of $$ {\theta}$$.

###2.2. Visualizing spherical harmonics

The lowest solution $$ {l=0}$$, $$ {m=0}$$ is called "breathing" mode. The spherical shell expands and contracts periodically. For all other solutions there are one or more nodal circles on the sphere. A nodal circle is one that is unchanged in that particular oscillating mode.

Note the following rules for the spherical shell modes 

+ the surfaces on opposite sides of a nodal circle oscillate in opposite directions.
+ the total number of nodal circles is equal to $$ {l}$$.
+ the number of total nodal circles passing through the poles in $$ {m}$$, and they divide the sphere equally in the azimuthal angle $$ {\phi}$$.
+ the remaining nodal circles are either equatorial or parallel to the equator symmetrically distributed between top and bottom halves of the sphere.

###2.3. Notations for spherical harmonics

We often use Dirac notation in writing equations associated with angular momentum. It is common to write

$$
\hat{L}^{2}\vert l,m\rangle=\hbar^{2}l(l+1)\vert l,m\rangle
$$

and

$$
\hat{L}_{z}\vert l,m\rangle=m\hbar\vert l,m\rangle
$$

The spherical harmonics arises in the solution of the hydrogen atom problem. Different value of $$ {l}$$ give rise to different sets of spectral lines from hydrogen identified empirically in the 19th century. Spectroscopists identified groups of lines called 

+ "spectral" (s)
+ "principal" (p)
+ "diffuse" (d) and
+ "fundamental" (f)

Each of these is now identified with the specific values of $$ {l}$$. Now we also alphabetically extend to higher $$ {l}$$ values: s: $$ {l=0}$$, p: $$ {l=1}$$, d: $$ {l=2}$$, f: $$ {l=3}$$, g: $$ {l=4}$$, h: $$ {l=5}$$ and so on. It is convenient that the "s" wavefunctions are all spherically symmetric even though the "s" of the notation originally had nothing to do with the spherical symmetry.

##3. The Hydrogen Atom

###3.1. Multiple particle wavefunctions

We start by generalizing the Schroedinger equation, writing generally for time-dependent problems

$$
\hat{H}\psi=E\psi
$$

where now we mean that the Hamiltonian $$ {\hat{H}}$$ is the operator representing the energy of the entire system. And $$ {\psi}$$ is the wavefunction representing the state of the entire system.

For a hydrogen atom, there are two particles: the electron and the proton. Each of these has a set of coordinates associated with it: $$ {x_{e}}$$, $$ {y_{e}}$$ and $$ {z_{e}}$$ for the electron and $$ {x_{p}}$$, $$ {y_{p}}$$ and $$ {z_{p}}$$ for the proton. The wavefunction will therefore in general be a function of all six of these coordinates.

###3.2. Solving the hydrogen atom problem

The electron and proton each have a mass $$ {m_{e}}$$ and $$ {m_{p}}$$ respectively. We expected kinetic energy operators associated with each of theses masses and potential energy from the electrostatic attraction of electron and proton.

Hence, the Hamiltonian becomes

$$
\hat{H}=-\frac{\hbar^{2}}{2m_{e}}\nabla_{e}^{2}-\frac{\hbar^{2}}{2m_{p}}\nabla_{p}^{2}+V(\vert \mathbf{r}_{e}-\mathbf{r}_{p}\vert)
$$

where we mean $$ {\nabla_{e}^{2}\equiv\frac{\partial^{2}}{\partial x_{e}^{2}}+\frac{\partial^{2}}{\partial y_{e}^{2}}+\frac{\partial^{2}}{\partial z_{e}^{2}}}$$ and similarly for $$ {\nabla_{p}^{2}}$$ and $$ {\mathbf{r}_{e}=x_{e}\mathbf{i}+y_{e}\mathbf{j}+z_{e}\mathbf{k}}$$ is the position vector of the electron coordinates and similarly for $$ {\mathbf{r}_{p}}$$.

The Coulomb potential energy

$$
V(\vert\mathbf{r}_{e}-\mathbf{r}_{p}\vert)=-\frac{e^{2}}{4\pi\varepsilon_{0}\vert\mathbf{r}_{e}-\mathbf{r}_{p}\vert}
$$

depends on the distance between the electron and proton coordinates which is important in simplifying the solution.

The potential here is only a function of $$ {\vert \mathbf{r}_{e}-\mathbf{r}_{p}\vert}$$. We could choose a new set of six coordinates in which three are the relative positions $$ {x=x_{e}-x_{p}}$$, $$ {y=y_{e}-y_{p}}$$, $$ {z=z_{e}-z_{p}}$$ from which we obtain

$$
r=\sqrt{x^{2}+y^{2}+z^{2}}=\vert \mathbf{r}_{e}-\mathbf{r}_{p}\vert
$$

The position $$ {\mathbf{R}}$$ of the center of mass of two masses is the same as the balance point of a light-weight beam with the two masses at possible ends and so is the weighted average of the positions of the two individual masses

$$
\mathbf{R}=\frac{m_{e}\mathbf{r}_{e}+m_{p}\mathbf{r}_{p}}{M}
$$

where $$ {M}$$ is the total mass $$ {M=m_{e}+m_{p}}$$.

Now we construct the differential operators we need in terms of these coordinates with

$$
\mathbf{R}=X\mathbf{i}+Y\mathbf{j}+Z\mathbf{k}
$$

then for the new coordinates in the $$ {x}$$ direction, we have

$$
X=\frac{m_{e}x_{e}+m_{p}x_{p}}{M}
$$

and similarly for the $$ {y}$$ and $$ {z}$$ directions.

Using the standard method of changing partial derivatives to new coordinates and fully notating the variables held constant. The first derivatives in the $$ {x}$$ direction become

$$
\left.\frac{\partial}{\partial x_{e}}\right\vert_{x_{p}}=\left.\frac{\partial X}{\partial x_{e}}\right\vert_{x_{p}}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial x}{\partial x_{e}}\right\vert_{x_{p}}\left.\frac{\partial}{\partial x}\right\vert_{X}=\frac{m_{e}}{M}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial}{\partial x}\right\vert_{X}
$$

and similarly

$$
\left.\frac{\partial}{\partial x_{p}}\right\vert_{x_{e}}=\left.\frac{\partial X}{\partial x_{p}}\right\vert_{x_{e}}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial x}{\partial x_{p}}\right\vert_{x_{e}}\left.\frac{\partial}{\partial x}\right\vert_{X}=\frac{m_{p}}{M}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial}{\partial x}\right\vert_{X}
$$

The second derivatives become

$$
\left.\frac{\partial^{2}}{\partial x_{e}^{2}}\right\vert_{x_{p}}=\left(\frac{m_{e}}{M}\right)^{2}\left.\frac{\partial^{2}}{\partial X^{2}}\right\vert_{x}+\left.\frac{\partial^{2}}{\partial x^{2}}\right\vert_{X}+\frac{m_{e}}{M}\left(\left.\frac{\partial}{\partial x}\right\vert_{X}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial}{\partial X}\right\vert_{x}\left.\frac{\partial}{\partial x}\right\vert_{X}\right)
$$

and similarly

$$
\left.\frac{\partial^{2}}{\partial x_{p}^{2}}\right\vert_{x_{e}}=\left(\frac{m_{p}}{M}\right)^{2}\left.\frac{\partial^{2}}{\partial X^{2}}\right\vert_{x}+\left.\frac{\partial^{2}}{\partial x^{2}}\right\vert_{X}-\frac{m_{p}}{M}\left(\left.\frac{\partial}{\partial x}\right\vert_{X}\left.\frac{\partial}{\partial X}\right\vert_{x}+\left.\frac{\partial}{\partial X}\right\vert_{x}\left.\frac{\partial}{\partial x}\right\vert_{X}\right)
$$

So dropping the explicit statement of variables held constant

$$
\frac{1}{m_{e}}\frac{\partial^{2}}{\partial x_{e}^{2}}+\frac{1}{m_{p}}\frac{\partial^{2}}{\partial x_{p}^{2}}=\frac{1}{M}\frac{\partial^{2}}{\partial X^{2}}+\frac{1}{\mu}\frac{\partial^{2}}{\partial x^{2}}
$$

where $$ {\mu}$$ is the so-called reduced mass $$ {\mu=\frac{m_{e}m_{p}}{m_{e}+m_{p}}}$$.

The same kind of relations can be written for each of the other Cartesian directions, so if we define

$$
\nabla_{\mathbf{R}}^{2}\equiv\frac{\partial^{2}}{\partial X^{2}}+\frac{\partial^{2}}{\partial Y^{2}}+\frac{\partial^{2}}{\partial Z^{2}}\quad \nabla_{\mathbf{r}}^{2}\equiv\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}
$$

We can write the Hamiltonian in a new form with center of mass coordinates

$$
\hat{H}=-\frac{\hbar}{2M}\nabla_{\mathbf{R}}^{2}-\frac{\hbar^{2}}{2\mu}\nabla_{\mathbf{r}}^{2}+V(\mathbf{r})
$$

which now allows us to separate the problem.

Presume the wavefunction can be written

$$
\psi(\mathbf{R},\mathbf{r})=S(\mathbf{R})U(\mathbf{r})
$$

Substituting this form in the Schroedinger equation with the Hamiltonian above. We obtain

$$
-\frac{1}{S(\mathbf{R})}\frac{\hbar^{2}}{2M}\nabla_{\mathbf{R}}^{2}S(\mathbf{R})=E-\frac{1}{U(\mathbf{r})}\left[-\frac{\hbar^{2}}{2\mu}\nabla_{\mathbf{r}}^{2}+V(\mathbf{r})\right]U(\mathbf{r})=E_{CoM}
$$

The left hand side depends only on $$ {\mathbf{R}}$$ and the right hand side depends only on $$ {\mathbf{r}}$$, so both must equal a "separation" constant which we call $$ {E_{CoM}}$$.

Hence, we have two separated equations

$$
-\frac{\hbar^{2}}{2M}\nabla_{\mathbf{R}}^{2}S(\mathbf{R})=E_{CoM}S(\mathbf{R})\quad\text{Center of mass motion}
$$

$$
\left[-\frac{\hbar^{2}}{2\mu}\nabla_{\mathbf{r}}^{2}+V(\mathbf{r})\right]U(\mathbf{r})=E_{H}U(\mathbf{r})\quad\text{Relative motion}
$$

where $$ {E_{H}=E-E_{CoM}}$$

The *center of mass motion* is the Schroedinger equation for free particle of mass $${M}$$ with wavefunction solutions

$$
S(\mathbf{R})=\exp(i\mathbf{K}\cdot\mathbf{R})
$$

and eigenenergies

$$
E_{CoM}=\frac{\hbar^{2}K^{2}}{2M}
$$

This is the motion of the entire hydrogen atom as a particle of mass $$ {M}$$.

The *relative motion* equation corresponds to the "internal" relative motion of the electron and proton and will give us the internal states of the hydrogen atom.

###3.3. Informal solution for the relative motion

We presume that the hydrogen atom will have some characteristic size which is called the Bohr radius $$ {a_{0}}$$. We expect that the "average" potential energy strictly, its expectation value will therefore be

$$
\langle E_{potential}\rangle\approx-\frac{e^{2}}{4\pi\varepsilon_{0}a_{0}}
$$

For a reasonable smooth wavefunction $$ {\psi(\mathbf{r})}$$ of size $$ {\sim a_{0}}$$, the second spatial derivative will be

$$
\sim-\psi(0)/a_{0}^{2}
$$

Remembering that for a mass $$ {\mu}$$, the kinetic energy operator is $$ {-(\hbar^{2}/2\mu)\nabla^{2}}$$. The "average" kinetic energy will therefore be

$$
\langle E_{kinetic}\rangle\approx\frac{\hbar^{2}}{2\mu a_{0}^{2}}
$$

Now, in the spirit of a "variational" calculation. We adjust the parameter $$ {a_{0}}$$ to get the lowest value of the total energy. Some variational approaches can be justified rigorously as approximation for the lowest energy.

With our very simple model, the total energy is

$$
\langle E_{total}\rangle\approx\frac{\hbar^{2}}{2\mu a_{0}^{2}}-\frac{e^{2}}{4\pi\varepsilon_{0}a_{0}}
$$

The total energy is balance between the potential energy and the kinetic energy. For this simple model, differentiation shows that the chose of $$ {a_{0}}$$ that minimizes the energy overall is

$$
a_{0}=\frac{4\pi\varepsilon_{0}\hbar^{2}}{e^{2}\mu}\approx 0.529 A=5.29\times 10^{-11} m
$$

which is the standard definition of the Bohr radius. With this choice of $$ {a_{0}}$$, the corresponding total energy of the state is

$$
E_{total}=-\frac{\mu}{2}\left(\frac{e^{2}}{4\pi\varepsilon_{0}\hbar}\right)^{2}
$$

We can usually define a "Rydberg" energy unit.

$$
Ry=-\langle E_{total}\rangle\approx 13.6eV
$$
