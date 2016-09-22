---
layout: post
title: Quantum Mechanics for Scientists and Engineers Notes 6
date: 2013-11-01
summary: Quantum Mechanics Learning Notes
categories: OldTimes
---

###1. Types of Linear Operators

####1.1. Bilinear expansion of operators

We know that we can expand functions in a basis set as in $$ {f(x)=\sum_{n}c_{n}\psi_{n}(x)}$$ or $$ {\vert f(x)\rangle=\sum_{n}c_{n}\vert \psi_{n}(x)\rangle}$$. What is the equivalent expansion for an operator? We can deduce this from our matrix representation.

Consider an arbitrary function $$ {f}$$, written as the ket $$ {\vert f\rangle}$$ from which we can calculate a function $$ {g}$$, written as the ket $$ {\vert g\rangle}$$ by acting with a specific operator $$ {\hat{A}}$$:

$$\vert g\rangle=\hat{A}\vert f\rangle$$

We expand $$ {g}$$ and $$ {f}$$ on the basis set $$ {\psi_{i}}$$: $$ {\vert g\rangle=\sum_{i}d_{i}\vert \psi_{i}\rangle}$$, $$ {\vert f\rangle=\sum_{j}c_{j}\vert \psi_{j}\rangle}$$. From our matrix representation of $$ {\vert g\rangle=\hat{A}\vert f\rangle}$$, we know that $$ {d_{i}=\sum_{j}A_{ij}c_{j}}$$, and, by the definition of the expansion coefficient, we know that $$ {c_{j}=\langle\psi_{j}\vert f\rangle}$$ so

$$d_{i}=\sum_{j}\langle\psi_{j}\vert f\rangle$$

Substituting the above equation to $$ {\vert g\rangle=\sum_{i}d_{i}\vert \psi_{i}\rangle}$$, gives

$$\vert g\rangle=\sum_{i,j}A_{ij}\langle\psi_{i}\vert f\rangle\vert \psi_{i}\rangle$$

Remember that $$ {\langle\psi_{j}\vert f\rangle\equiv c_{j}}$$ is simply a number, so we can move it within the multiplication expression. Hence we have

$$ \vert g\rangle=\sum_{i,j}A_{ij}\vert \psi_{i}\rangle\langle\psi_{j}\vert f\rangle=\left[\sum_{i,j}A_{ij}\vert \psi_{i}\rangle\langle\psi_{j}\vert \right]\vert f\rangle$$

But $$ {\vert g\rangle=\hat{A}\vert f\rangle}$$ and $$ {\vert g\rangle}$$ and $$ {\vert f\rangle}$$ are arbitrary, so

$$\hat{A}\equiv\sum_{i,j}A_{ij}\vert \psi_{i}\rangle\langle\psi_{j}\vert $$

This form is referred to as a "bilinear expansion" of the operator $$ {\hat{A}}$$ on the basis $$ {\vert \psi_{i}\rangle}$$ and is analogous to the linear expansion of a vector on a basis. Any linear operator that operates within the space can be written this way.

Though the Dirac notation is more general and elegant for functions of a simple variables where

$$g(x)=\int\hat{A}f(x_{1})\,dx_{1}$$

We can analogously write the bilinear expansion in the form

$$\hat{A}\equiv\sum_{i,j}A_{ij}\psi_{i}(x)\psi_{j}^{*}(x_{1})$$

The Dirac form of expansion contains an outer product of two vectors. An outer product expression of the form $$ {\vert g\rangle\langle f\vert }$$ generates matrix. The specific notation $$ {\hat{A}\equiv A_{ij}\vert \psi_{i}\rangle\langle\psi_{j}\vert }$$ is actually, then, a sum of matrices. In the matrix $$ {\vert \psi_{i}\rangle\langle\psi_{j}\vert }$$ the element in the $$ {j}$$th column and $$ {i}$$th row is 1, all other elements are zero.

####1.2. The identity operator

The identity operator $$ {\hat{I}}$$ is the operator that when it operates on a vector (function) leaves it unchanged. In matrix form, the identity operator is

$$\left[\begin{array}{cccc}1 & 0 & 0 & \cdots \\ 0 & 1 & 0 & \cdots \\ 0 & 0 & 1 & \cdots \\ \vdots & \vdots & \vdots & \ddots\end{array}\right]$$

In bra-ket form, the identity operator can be written as

$$\hat{I}=\sum_{i}\vert \psi_{i}\rangle\langle\psi_{i}\vert $$

where the $$ {\vert \psi_{i}\rangle}$$ form a complete basis for the space. This statement is trivial if $$ {\vert \psi_{i}\rangle}$$ is the basis used to represent the space.

Note, however that $$ {\hat{I}=\sum_{i}\vert \psi_{i}\rangle\langle\psi_{i}\vert }$$ even if the basis used is not the set $$ {\vert \psi_{i}\rangle}$$. Then some specific $$ {\vert \psi_{i}\rangle}$$ is not a vector with an $$ {i}$$th element of 1 and all other elements 0 and the matrix $$ {\vert \psi_{i}\rangle\langle\psi_{i}\vert }$$ in general has possibly and of its elements non-zero. Nonetheless, the sum of all matrices $$ {\vert \psi_{i}\rangle\langle\psi_{i}\vert }$$ still gives the identity matrix $$ {\hat{I}}$$.

The expression above has a simple vector meaning. In the expression $$ {\vert f\rangle=\sum_{i}\vert \psi_{i}\rangle\langle\psi_{i}\vert f\rangle}$$, $$ {\langle\psi_{i}\vert f\rangle}$$ is just the projection of $$ {\vert f\rangle}$$ onto the $$ {\vert \psi_{i}\rangle}$$ axis, so multiplying $$ {\vert \psi_{i}\rangle}$$ by $$ {\langle\psi_{i}\vert f\rangle}$$ that is $$ {\langle\psi_{i}\vert f\rangle\vert \psi_{i}\rangle=\vert \psi_{i}\rangle\langle\psi_{i}\vert f\rangle}$$ gives the vector component of $$ {\vert f\rangle}$$ on the $$ {\vert \psi_{i}\rangle}$$ axis.

Since the identity matrix is the identity matrix, so no matter what complete orthonormal basis we use to represent it, we can use the following tricks: First, we "insert" the identity matrix in some basis into a expression. Then, we rearrange the expression. Then, we find an identity matrix we can take out of the result.

Consider the sum $$ {S}$$ of the diagonal elements of an operator $$ {\hat{A}}$$ on some complete orthonormal basis $$ {\vert \psi_{i}\rangle}$$

$$S=\sum_{i}\langle\psi_{i}\vert \hat{A}\vert \psi_{i}\rangle$$

Now we suppose we have some other complete orthonormal basis $$ {\vert \phi_{m}\rangle}$$. We can therefore also write the identity operator as

$$\hat{I}=\sum_{m}\vert \phi_{m}\rangle\langle\phi_{m}\vert $$

In $$ {S}$$, we can insert an identity operator just before $$ {\hat{A}}$$ which makes no difference to the result since $$ {\hat{I}\hat{A}=\hat{A}}$$, so we have

$$S=\sum_{i}\langle\psi_{i}\vert \hat{I}\hat{A}\vert \psi_{i}\rangle=\sum_{i}\langle\psi_{i}\vert \left(\sum_{m}\vert \phi_{m}\rangle\langle\phi_{m}\vert \right)\hat{A}\vert \psi_{i}\rangle$$

Then we can rearranging the above equation in following sequence:

$$\begin{array}{rcl}  S&=&\sum_{m}\sum_{i}\langle\psi_{i}\vert \phi_{m}\rangle\langle\phi_{m}\vert \hat{A}\vert \psi_{i}\rangle \\ &=&\sum_{m}\sum_{i}\langle\phi_{m}\vert \hat{A}\vert \psi_{i}\rangle\langle\psi_{i}\vert \phi_{i}\rangle \\ &=&\sum_{m}\langle\phi_{m}\vert \hat{A}\left(\sum_{i}\vert \psi_{i}\rangle\langle\psi_{i}\vert \right)\vert \phi_{m}\rangle \\ &=&\sum_{m}\langle\phi_{m}\vert \hat{A}\vert \phi_{m}\rangle \end{array}$$

Hence the trace of an operator (the sum of the diagonal elements) is independent of the basis used to represent the operator.

####1.3. Inverse and unitary operators

For an operator $$ {\hat{A}}$$ on an arbitrary function $$ {\vert f\rangle}$$, then the inverse operator, if it exists is that operator $$ {\hat{A}^{-1}}$$ such that

$$\vert f\rangle=\hat{A}^{-1}\hat{A}\vert f\rangle$$

Since the function $$ {\vert f\rangle}$$ is arbitrary, we can therefore identify

$$\hat{A}^{-1}\hat{A}=\hat{I}$$

Since the operator can be represent by a matrix, finding the inverse of the operator reduces to finding the inverse of a matrix.

A unitary operator $$ {\hat{U}}$$, is one for which

$$\hat{U}^{-1}=\hat{U}^{\dag}$$

that is, its inverse is its Hermitian adjoint.

Note first that it can shown generally that for two matrices $$ {\hat{A}}$$ and $$ {\hat{B}}$$ that can be multiplied

$$(\hat{A}\hat{B})^{\dag}=\hat{B}^{\dag}\hat{A}^{\dag}$$

That is, the Hermitian adjoint of the product is the "flipped round" product of the Hermitian adjoint. Explicitly, for matrix-vector multiplication

$$(\hat{A}\vert h\rangle)^{\dag}=\langle h\vert \hat{A}^{\dag}$$

Consider the unitary operator $$ {\hat{U}}$$ and vectors $$ {\vert f_{old}\rangle}$$ and $$ {\vert g\rangle}$$. We form two new vector by operating with $$ {\hat{U}}$$

$$\vert f_{new}\rangle=\hat{U}\vert f_{old}\rangle\qquad \vert g_{new}\rangle=\hat{U}\vert g_{new}\rangle$$

Then $$ {\langle g_{new}\vert =\langle g_{old}\vert \hat{U}^{\dag}}$$.

So,

$$\langle g_{new}\vert f_{new}\rangle=\langle g_{old}\hat{U}^{\dag}\hat{U}\vert f_{old}\rangle=\langle g_{old}\vert f_{old}\rangle$$

Hence, the unitary operation does not change the inner product. So, in particular $$ {\langle f_{new}\vert f_{new}\rangle=\langle f_{old}\vert f_{old}\rangle}$$, the length of a vector is not changed by a unitary operator.

###2. Unitary and Hermitian Operators

####2.1. Using unitary operators

Suppose that we have a vector (function) $$ {\vert f_{old}\rangle}$$ that is represented when expressed as an expansion on the function $$ {\vert \psi_{n}\rangle}$$ as the mathematical column vector

$$\vert f_{old}\rangle=\left[\begin{array}{c}c_{1} \\ c_{2} \\ c_{3} \\ \vdots\end{array}\right]$$

These numbers $$ {c_{1}}$$, $$ {c_{2}}$$, $$ {c_{3}}$$, ... are projections of $$ {\vert f_{old}\rangle}$$ on the orthogonal coordinate axes in the vector space labeled with $$ {\vert \psi_{1}\rangle}$$, $$ {\psi_{2}\rangle}$$, $$ {\vert \psi_{3}\rangle}$$, ...

Suppose we want to represent this vector on a set of orthogonal axes which will label $$ {\vert \phi_{1}\rangle}$$, $$ {\vert \phi_{2}\rangle}$$, $$ {\vert \phi_{3}\rangle}$$, ... Changing the axes which is equivalent to changing the basis set of functions does not change the vector we are representing but it does change the column numbers used to represent the vector.

Write transformations for each basis vector $$ {\vert \psi_{n}\rangle}$$, we get the correct transformation if we define a matrix

$$\hat{U}=\left[\begin{array}{cccc}u_{11} & u_{12} & u_{13} & \cdots \\ u_{21} & u_{22} & u_{23} & \cdots \\ u_{31} & u_{32} & u_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots\end{array}\right]$$

where $$ {u_{ij}=\langle\phi_{i}\vert \psi_{j}\rangle}$$ and we define our new column of numbers $$ {\vert f_{new}\rangle}$$

$$\vert f_{new}\rangle=\hat{U}\vert f_{old}\rangle$$

Now we can prove $$ {\hat{U}}$$ is unitary. Writing the matrix multiplication in its sum form

$$\begin{array}{rcl}  (\hat{U}^{\dag}\hat{U})_{ij}&=&\sum_{m}u_{mi}^{*}u_{mj}=\sum_{m}\langle\phi_{m}\vert \psi_{i}\rangle^{*}\langle\phi_{m}\vert \psi_{j}\rangle \\ &=&\langle\psi_{i}\vert \left(\sum_{m}\vert \phi_{m}\rangle\langle\phi_{m}\vert \right)\vert \psi_{j}\rangle \\ &=&\langle\psi_{i}\vert \psi_{j}\rangle=\delta_{ij} \end{array}$$

So, $$ {\hat{U}^{\dag}\hat{U}=\hat{I}}$$, hence, $$ {\hat{U}}$$ is unitary.

Consider a number such as $$ {\langle g\vert \hat{A}\vert f\rangle}$$ where vector $$ {\vert g\rangle}$$, $$ {\vert f\rangle}$$ and operator $$ {\hat{A}}$$ are arbitrary. This result should not depend on the coordinate system. So the result in an "old" coordinate system should be the same in a "new" coordinate system, that is, we should have $$ {\langle g_{new}\vert \hat{A}_new\vert f_{new}\rangle=\langle g_{old}\vert \hat{A}\vert f_{old}\rangle}$$. Note the subscripts "new" and "old" refer to representations not the vectors (or operators) themselves which are not changed by change of representation. Only the numbers that represent them are changed. With unitary $$ {\hat{U}}$$ operator to go from "old" to "new" systems, we can write

$$\begin{array}{rcl}  \langle g_{new}\vert \hat{A}_{new}\vert f_{new}\rangle&=&(\vert g_{new}\rangle^{\dag})\hat{A}_{new}\vert f_{new}\rangle \\ &=&(\hat{U}\vert g_{old}\rangle)^{\dag}\hat{A}_{new}(\hat{U}\vert f_{old}\rangle) \\ &=&\langle g_{old}\vert U^{\dag}\hat{A}_{new}\hat{U}\vert f_{old}\rangle=\langle g_{old}\vert \hat{A}_{old}\vert f_{old}\rangle \end{array}$$

since $$ {\hat{A}_{old}=\hat{U}^{\dag}\hat{A}_{new}\hat{U}}$$ or $$ {\hat{U}\hat{A}_{old}\hat{U}^{\dag}=(\hat{U}\hat{U}^{\dag})\hat{A}_{new}(\hat{U}\hat{U}^{\dag})=\hat{A}_{new}}$$.

If the quantum state $$ {\vert \psi\rangle}$$ is expanded on the basis $$ {\vert \psi_{n}\rangle}$$ to give

$$\vert \psi\rangle=\sum_{n}a_{n}\vert \psi_{n}\rangle$$

then $$ {\sum_{n}\vert a_{n}\vert ^{2}=1}$$. And if the particle is to be conserved then this sum is retained as the quantum mechanical system evolves in time. Hence, a unitary operator, which conserves length describes changes that conserve the particle.

####2.2. Hermitian operators

A Hermitian operator is equal to its own Hermitian adjoint

$$\hat{M}^{\dag}=\hat{M}$$

Equivalently it is self-adjoint. In matrix terms, the Hermiticity implies $$ {\hat{M}_{ij}=\hat{M}_{ji}^{*}}$$ for all $$ {i}$$ and $$ {j}$$. So, also the diagonal elements of a Hermitian operator must be real.

To understand Hermiticity in the most general sense, consider $$ {\langle g\vert \hat{M}\vert f\rangle}$$ for arbitrary $$ {\vert f\rangle}$$ and $$ {\vert g\rangle}$$ and some operator $$ {\hat{M}}$$.

We examine

$$(\langle g\vert \hat{M}\vert f\rangle)^{\dag}$$

Since this is just a number, it is also true that

$$(\langle g\vert \hat{M}\vert f\rangle)^{\dag}=(\langle g\vert \hat{M}\vert f\rangle)^{*}$$

We can analyze $$ {(\langle g\vert \hat{M}\vert f\rangle)^{\dag}}$$ using the rule $$ {(\hat{A}\hat{B})^{\dag}=\hat{B}^{\dag}\hat{A}^{\dag}}$$ for Hermitian adjoints of products. So

$$(\hat{A}\hat{B})^{\dag}=\hat{B}^{\dag}\hat{A}^{*}=(\hat{A}\hat{B})^{\dag}=\hat{B}^{\dag}\hat{A}^{\dag}=(\hat{M}\vert f\rangle)^{\dag}(\langle g\vert )^{\dag}=\langle f\vert \hat{M}^{\dag}\vert g\rangle$$

Hence, if $$ {\hat{M}}$$ is Hermitian, with therefore $$ {\hat{M}^{\dag}=\hat{M}}$$, then

$$(\langle g\vert \hat{M}\vert f\rangle)^{*}=\langle f\vert \hat{M}^{\dag}\vert g\rangle$$

even if $$ {\vert f\rangle}$$ and $$ {\vert g\rangle}$$ are not orthogonal.

In integral form, for function $$ {f(x)}$$ and $$ {g(x)}$$, the statement above can be written

$$\int g^{*}(x)\hat{M}f(x)\,dx=\left[\int f^{*}(x)\hat{M}g(x)\,dx\right]^{*}$$

We can rewrite the right hand side and a simple rearrangement leads to

$$\int\hat{g}(x)\hat{M}f(x)\,dx=\int\{\hat{M}g(x)\}^{*}f(x)\,dx$$

which is a common statement of Hermiticity in integral form.

Suppose $$ {\vert \psi_{n}\rangle}$$ is a normalized eigenvector of the Hermitian operator $$ {\hat{M}}$$ with eigenvalue $$ {\mu_{n}}$$. Then by definition

$$\hat{M}\vert \psi_{n}\rangle=\mu_{n}\vert \psi{n}\rangle$$

Therefore

$$\langle\psi_{n}\vert \hat{M}\vert \psi_{n}\rangle=\mu_{n}\langle\psi_{n}\vert \psi_{n}\rangle=\mu_{n}$$

But from the Hermiticity of $$ {\hat{M}}$$ we know

$$\langle\psi_{n}\vert \hat{M}\vert \psi_{n}\rangle=(\langle\psi_{n}\vert \hat{M}\vert \psi_{n}\rangle)^{*}=\mu_{n}^{*}$$

And hence $$ {\mu_{n}}$$ must be real.

Now, let's prove that orthogonality of eigenfunctions for different eigenvalues

$$\begin{array}{rcl}  0&=&\langle\psi_{m}\vert \hat{M}\vert \psi_{n}\rangle-\langle\psi_{m}\vert \hat{M}\vert \psi_{n}\rangle \\ 0&=&(\langle\psi_{m}\vert \hat{M})\vert \psi_{n}\rangle-\langle\psi_{m}\vert (\hat{M}\vert \psi_{n}\rangle) \\ 0&=&(\hat{M}^{\dag}\vert \psi_{m}\rangle)^{\dag}\vert \psi_{n}\rangle-\langle\psi_{m}\vert (\hat{M}\vert \psi_{n}\rangle) \\ 0&=&(\hat{M}\vert \psi_{m}\rangle)^{\dag}\vert \psi_{n}\rangle-\langle\psi_{m}\vert (\hat{M}\vert \psi_{n}\rangle) \\ 0&=&(\mu_{m}\vert \psi_{m}\rangle)^{\dag}\vert \psi_{n}\rangle-\langle\psi_{m}\vert \mu_{n}\vert \psi_{n}\rangle \\ 0&=&\mu_{m}\vert (\psi_{m}\rangle)^{\dag}\vert \psi_{n}\rangle-\mu_{n}\langle\psi_{m}\vert \psi_{n}\rangle \\ 0&=&(\mu_{m}-\mu_{n})\langle\psi_{m}\vert \psi_{n}\rangle \\ \end{array}$$

But $$ {\mu_{m}}$$ and $$ {\mu_{n}}$$ are different, so $$ {0=\langle\psi_{m}\vert \psi_{n}\rangle}$$, i.e., orthogonality, presuming we are working with non-zero functions.

It is quite possible and common in symmetric problems to have more than one eigenfunction associated with a given eigenvalue. This situation is known as degeneracy. It is provable that the number of such degenerate solutions for a given finite eigenvalue is itself finite.

####2.3. Matrix from of derivative operators

Returning to our original discussion of functions as vectors, we can postulate a form for the differential operator

$$\frac{d}{dx}\equiv\left[\begin{array}{cccccc} & \ddots & & & & \\ \cdots & -\frac{1}{2\delta x} & 0 & \frac{1}{2\delta x} & 0 & \cdots \\ \cdots & 0 & -\frac{1}{2\delta x} & 0 & \frac{1}{2\delta x} & \cdots \\ & & & & \ddots & \end{array}\right]$$

where we presume we can take the limits as $$ {\delta x\rightarrow 0}$$.

If we multiply the column vector whose elements are the values of the function then

$$\left[\begin{array}{cccccc} & \ddots & & & & \\ \cdots & -\frac{1}{2\delta x} & 0 & \frac{1}{2\delta x} & 0 & \cdots \\ \cdots & 0 & -\frac{1}{2\delta x} & 0 & \frac{1}{2\delta x} & \cdots \\ & & & & \ddots & \end{array}\right]\left[\begin{array}{c}\vdots \\ f(x_{i}-\delta x) \\ f(x_{i})\\ f(x_{i}+\delta x) \\f(x_{i}+2\delta x) \\ \vdots\end{array}\right]=\left[\begin{array}{c}\vdots \\ \frac{f(x_{i}-\delta x)-f(x_{i}+\delta x)}{2\delta x} \\\frac{f(x_{i}+2\delta x)-f(x_{i})}{2\delta x}\\ \vdots\end{array}\right]=\left[\begin{array}{c}\vdots \\ \left.\frac{df}{dx}\right\vert _{x_{i}} \\ \left.\frac{df}{dx}\right\vert _{x_{i}+\delta x} \\ \vdots\end{array}\right]$$

Note this matrix is antisymmetric reflection about the diagonal and it is not Hermitian. By similar arguments, though $$ {d^{2}/dx^{2}}$$ gives a symmetric matrix and is Hermitian.

We can formally "operate" on the function $$ {f(x)}$$ by multiplying it by the function $$ {V(x)}$$ to generate another function

$$g(x)=V(x)f(x)$$

Since $$ {V(x)}$$ is performing the role of an operator. We can if we wish represent it as a (diagonal) matrix whose diagonal elements are the values of the function at each of the different points.

If $$ {V(x)}$$ is real then its matrix is Hermitian as required for $$ {\hat{H}}$$.

###3. Operators and Quantum Mechanics

####3.1. Hermitian operators in quantum mechanics

For Hermitian operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$ representing physical variables. It is very important to know if they commute, i.e., $$ {\hat{A}\hat{B}=\hat{B}\hat{A}}$$. Remember that because these linear operators obey the same algebra as matrices in general operators do not commute.

For quantum mechanics, we formally define an entity

$$[\hat{A},\hat{B}]=\hat{A}\hat{B}-\hat{B}\hat{A}$$

This entity is called the commutator.

An equivalent statement to saying $$ {\hat{A}\hat{B}=\hat{B}\hat{A}}$$ is then $$ {[\hat{A},\hat{B}]=0}$$. Strictly, this should be written

$$[\hat{A},\hat{B}]=0\hat{I}$$

where $$ {\hat{I}}$$ is the identity operator but this is usually omitted.

If the operator do not commute, then $$ {[\hat{A},\hat{B}]}$$ does not hold an in general we can choose to write

$$[\hat{A},\hat{B}]=i\hat{C}$$

where $$ {\hat{C}}$$ is sometimes referred to the reminder of commutation or the commutation rest.

Operators that commute share the same set of eigenfunctions and operators that share same set of eigenfunctions commute.

Suppose that operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$ commute and suppose that $$ {\vert \psi_{n}\rangle}$$ are the eigenfunctions of $$ {\hat{A}}$$ with eigenvalues $$ {A_{i}}$$, then

$$\hat{A}\hat{B}\vert \psi_{i}\rangle=\hat{B}\hat{A}\vert \psi_{i}\rangle=\hat{B}A_{i}\vert \psi_{i}\rangle=A_{i}\hat{B}\vert \psi_{i}\rangle$$

So,

$$\hat{A}[\hat{B}\vert \psi_{i}\rangle]=A_{i}[\hat{B}\vert \psi\rangle]$$

This means that the vector $$ {\hat{B}\vert \psi_{i}\rangle}$$ is also the eigenvector $$ {\vert \psi\rangle}$$ or is proportional to it. i.e., for some number $$ {B_{i}}$$

$$\hat{B}\vert \psi_{i}\rangle=B_{i}\vert \psi_{i}\rangle$$

This kind of relation holds for all the eigenfunctions $$ {\vert \psi_{i}\rangle}$$. So these eigenfunctions are also the eigenfunctions of the vector $$ {\hat{B}}$$ with associated eigenvalues $$ {B_{i}}$$. Hence we have proved the first statement that operators that commute share the same set of eigenfunctions. Note that the eigenvalues $$ {A_{i}}$$ and $$ {B_{i}}$$ are not in general equal to one another.

Now we consider the statement: operators that share the same set of eigenfunctions commute. Suppose that the Hermitian operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$ share the same complete set $$ {\vert \psi_{i}\rangle}$$ of eigenfunctions with associated sets of eigenvalues $$ {A_{n}}$$ and $$ {B_{n}}$$ respectively. Then

$$\hat{A}\hat{B}\vert \psi_{i}\rangle=\hat{A}B_{i}\vert \psi_{i}\rangle=A_{i}B_{i}\vert \psi_{i}\rangle$$

and similarly

$$\hat{B}\hat{A}\vert \psi_{i}\rangle=\hat{B}A_{i}\vert \psi_{i}\rangle=B_{i}A_{i}\vert \psi_{i}\rangle$$

Hence, for any function $$ {\vert f\rangle}$$ which can always be expanded in this complete set of function $$ {\vert \psi_{n}\rangle}$$, i.e., $$ {\vert f\rangle=\sum_{i}c_{i}\vert \psi_{i}\rangle}$$, we have

$$\hat{A}\hat{B}\vert f\rangle=\sum_{i}c_{i}A_{i}B_{i}\vert \psi_{i}\rangle=\sum_{i}c_{i}B_{i}A_{i}\vert \psi_{i}\rangle=\hat{B}\hat{A}\vert f\rangle$$

Since we have proved this for an arbitrary function, we have proved that the operators commute hence proving the statement operators that share the same set of eigenfunctions commute.

####3.2. General form of the uncertainty principle

First, we need to set up the concepts of the mean and variance of an expectation value. Using $$ {\bar{A}}$$ to denote the mean value of a quantity $$ {\hat{A}}$$. We have, in the bra-ket notation, for a measurable quantity associated with the Hermitian operator $$ {\hat{A}}$$ when the state of the system is $$ {\vert f\rangle}$$

$$\bar{A}\equiv\langle A\rangle=\langle f\vert \hat{A}\vert f\rangle$$

Let us define a new operator $$ {\Delta\hat{A}}$$ associated with the difference between the measured value of $$ {A}$$ and its average value

$$\Delta\hat{A}=\hat{A}-\bar{A}$$

Strictly, we should write $$ {\Delta\hat{A}=\hat{A}-\bar{\hat{I}}}$$, but we take such an identity operator to be understood. Note that this operator is also Hamiltonian.

Variance in statistics is the "mean square" deviation from the average. To examine the variance of the quantity $$ {A}$$, we examine the expectation value of the operator $$ {(\Delta\hat{A})^{2}}$$. Expanding the arbitrary function $$ {\vert f\rangle}$$ on the basis of the eigenfunction $$ {\vert \psi_{i}\rangle}$$ of $$ {\hat{A}}$$.

$$\vert f\rangle=\sum_{i}c_{i}\vert \psi_{i}\rangle$$

We can formally evaluate the expectation value of $$ {(\Delta\hat{A})^{2}}$$ when the system is in the state $$ {\vert f\rangle}$$.

$$\begin{array}{rcl}  \langle(\Delta\hat{A})^{2}\rangle&=&\langle f\vert (\Delta\hat{A})^{2}\vert f\rangle=\left(\sum_{i}c_{i}^{*}\langle\psi_{i}\vert \right)(\hat{A}-\bar{A})^{2}\left(\sum_{j}c_{j}\vert \psi_{j}\rangle\right) \\ &=&\left(\sum_{i}c_{i}^{*}\langle\psi_{i}\vert \right)(\hat{A}-\bar{A})\left(\sum_{j}c_{j}(A_{j}-\bar{A})\vert \psi_{j}\rangle\right) \\ &=&\left(\sum_{i}c_{i}^{*}\langle\psi_{i}\vert \right)\left(\sum_{j}c_{j}(A_{j}-\bar{A})^{2}\vert \psi_{j}\rangle\right)=\sum_{i}\vert c_{i}\vert ^{2}(A_{i}-\bar{A})^{2} \end{array}$$

Because the $$ {\vert c_{i}\vert ^{2}}$$ are the probabilities that the system is found, on measurement, to be in the state $$ {\vert \psi_{i}\rangle}$$ and $$ {(A_{i}-\bar{A})^{2}}$$ for that state simply represents the squared deviation of the value of the quantity $$ {A}$$ from its average value then by definition

$$\overline{(\Delta A)^{2}}\equiv\langle(\Delta\hat{A})^{2}\rangle=\langle(\hat{A}-\bar{A})^{2}\rangle=\langle f\vert (\hat{A}-\bar{A})^{2}\vert f\rangle$$

is the mean squared deviation for the quantity $$ {A}$$ on repeatedly measuring the system prepared in state $$ {\vert f\rangle}$$.

In statistical language, the quantity $$ {\overline{(\Delta A)^{2}}}$$ is called the variance, and the square root of the variance which we can write as $$ {\Delta A=\sqrt{\overline{(\Delta A)^{2}}}}$$ is the standard deviation. In statistics, the standard deviation gives a well-defined measure of the width of a distribution.

We can also consider some other quantity $$ {B}$$ associated with the Hermitian operator $$ {\hat{B}}$$ and, with similar definitions

$$\overline{(\Delta B)^{2}}\equiv\langle(\Delta\hat{B})^{2}\rangle=\langle f\vert (\hat{B}-\bar{B})^{2}\vert f\rangle$$

So we have ways of calculating the uncertainty in the measurements of the quantities $$ {A}$$ and $$ {B}$$ when the system is in the state $$ {\vert f\rangle}$$ to use in a general proof of the uncertainty principle.

Suppose two Hermitian operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$ do not commute and have commutation rest $$ {\hat{C}}$$ as defined above in $$ {[\hat{A},\hat{B}]=i\hat{C}}$$. Consider, for some arbitrary real number $$ {\alpha}$$, the number

$$G(\alpha)=\langle(\alpha\Delta\hat{A}-i\Delta\hat{B})f\vert (\alpha\Delta\hat{A}-i\Delta\hat{B})f\rangle\geq 0$$

By $$ {\vert (\alpha\Delta\hat{A}-i\Delta\hat{B})f\rangle}$$ we mean the vector $$ {(a\Delta\hat{A}-i\Delta\hat{B})\vert f\rangle}$$ written this way to emphasize it is simply a vector so it must have an inner product with itself that is greater than or equal to zero. So,

$$\begin{array}{rcl}  G(\alpha)&=&\langle f\vert (\alpha\Delta\hat{A}-i\Delta\hat{B})^{\dag}(\alpha\Delta\hat{A}-i\Delta\hat{B})\vert f\rangle(\geq 0) \\ &=&\langle f\vert (\alpha\Delta\hat{A}^{\dag}+i\Delta\hat{B}^{\dag})(\alpha\Delta\hat{A}-i\Delta\hat{B})\vert f\rangle \\ &=&\langle f\vert (\alpha\Delta\hat{A}+i\Delta\hat{B})(\alpha\Delta\hat{A}-i\Delta\hat{B})\vert f\rangle \\ &=&\langle f\vert \alpha^{2}(\Delta\hat{A})^{2}+(\Delta\hat{B})^{2}-i\alpha(\Delta\hat{A}\Delta\hat{B}-\Delta\hat{B}\Delta\hat{A})\vert f\rangle \\ &=&\langle f\vert \alpha^{2}(\Delta\hat{A})^{2}+(\Delta\hat{B})^{2}-i\alpha[\Delta\hat{A},\Delta\hat{B}]\vert f\rangle \\ &=&\langle f\vert \alpha^{2}(\Delta\hat{A})^{2}+(\Delta\hat{B})^{2}+\alpha\hat{C}\vert f\rangle \\ &=&\alpha^{2}\overline{(\Delta A)^{2}}+\overline{(\Delta B)^{2}}+\alpha\bar{C} (\geq 0) \end{array}$$

where $$ {\bar{C}\equiv\langle C\rangle=\langle f\vert \hat{C}\vert f\rangle}$$.

By a simple (though not obvious) rearrangement

$$G(\alpha)=\overline{(\Delta A)^{2}}\left[\alpha+\frac{\bar{C}}{2\overline{(\Delta A)^{2}}}\right]^{2}+\overline{(\Delta B)^{2}}-\frac{(\bar{C})^{2}}{4\overline{(\Delta A)^{2}}}\geq 0$$

But the equation above must be true for arbitrary $$ {\alpha}$$, so it is true for

$$\alpha=-\frac{\bar{C}}{2\overline{(\Delta A)^{2}}}$$

which sets the first term equal to zero, so

$$\overline{(\Delta A)^{2}}\,\overline{(\Delta B)^{2}}\geq\frac{(\bar{C})^{2}}{4}$$

So, for two operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$, corresponding to measurable quantities $$ {A}$$ and $$ {B}$$ for which $$ {[\hat{A},\hat{B}]=i\hat{C}}$$ in some state $$ {\vert f\rangle}$$ for which $$ {\bar{C}\equiv\langle C\rangle=\langle f\vert \hat{C}\vert f\rangle}$$, we have the uncertainty principle

$$\Delta A\Delta B\geq\frac{\vert \bar{C}\vert }{2}$$

where $$ {\Delta A}$$ and $$ {\Delta B}$$ are the standard deviations of the values of $$ {A}$$ and $$ {B}$$ we would measure.

The conclusion above is generally true. Only if the operators $$ {\hat{A}}$$ and $$ {\hat{B}}$$ commute. or if they do not commute, but we are in a state $$ {\vert f\rangle}$$ for which $$ {\langle f\vert \hat{C}\vert f\rangle=0}$$. Only in those cases it is possible for both $$ {A}$$ and $$ {B}$$ simultaneously to have exact measurable values.

####3.3. Specific uncertainty principles

We now formally derive the position-momentum relation. Consider the commutator of $$ {\hat{p}_{x}}$$ and $$ {x}$$ (we treat the function $$ {x}$$ as the operator for position). To be sure we are taking derivatives correctly, we have the commutator operate on an arbitrary function:

$$\begin{array}{rcl}  [\hat{p}_{x},x]\vert f\rangle&=&-i\hbar\left(\frac{d}{dx}x-x\frac{d}{dx}\right)\vert f\rangle=-i\hbar\left\{\frac{d}{x}(x\vert f\rangle)-x\frac{d}{dx}\vert f\rangle\right\} \\ &=&-i\hbar\left\{\vert f\rangle+x\frac{d}{dx}\vert f\rangle-x\frac{d}{dx}\vert f\rangle\right\}=-i\hbar\vert f\rangle \end{array}$$

Since $$ {\vert f\rangle}$$ is arbitrary, we can write $$ {[\hat{p}_{x},x]=-i\hbar}$$ and the commutation rest operator $$ {\hat{C}}$$ is simply the number $$ {\hat{C}=-\hbar}$$. And so, from $$ {\Delta A\Delta B\geq\vert \bar{C}\vert /2}$$, we have

$$\Delta\hat{p}_{x}\Delta x\geq\frac{\hbar}{2}$$

The energy operator is the Hamiltonian $$ {\hat{H}}$$ and from Schroedinger's equation

$$\hat{H}\vert \psi\rangle=i\hbar\frac{\partial}{\partial t}\vert\psi\rangle$$

so we use $$ {\hat{H}=i\hbar\partial/\partial t}$$.

If we take the time operator to be just $$ {t}$$ then using essentially identical algebra as used for the momentum-position uncertainty principle.

$$[\hat{H},t]=i\hbar\left(\frac{\partial}{\partial t}t-t\frac{\partial}{\partial t}\right)=i\hbar$$

so, similarly we have

$$\Delta E\Delta t\geq\frac{\hbar}{2}$$

We can relate this result mathematically to the frequency-time uncertainty principle that occurs in Fourier analysis. Noting the $$ {E=\hbar\omega}$$ in quantum mechanics, we have

$$\Delta\omega\Delta t\geq\frac{1}{2}$$
