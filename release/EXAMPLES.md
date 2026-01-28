# LaTeX Equation Examples

Copy and paste these into the application for quick testing.

## Simple Examples

### Einstein's Equation
```
E = mc^2
```

### Quadratic Formula
```
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
```

### Circle Equation
```
x^2 + y^2 = r^2
```

## Advanced Examples

### Navier-Stokes Equation
```
\frac{\partial u}{\partial t} + \nabla \cdot \mathbf{u} = -\nabla p + \nu \nabla^2 \mathbf{u}
```

### Maxwell's Equations
```
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
```

### Schrödinger Equation
```
i\hbar\frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2 \psi + V\psi
```

### Fourier Transform
```
\mathcal{F}(f) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx
```

### Laplace Transform
```
\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
```

## Matrix Examples

### 2x2 Matrix
```
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
```

### Determinant
```
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix} = ad - bc
```

### 3x3 Matrix
```
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
```

## Calculus Examples

### Limit
```
\lim_{x \to \infty} \frac{1}{x} = 0
```

### Integral
```
\int_{a}^{b} f(x) \, dx
```

### Double Integral
```
\iint_D f(x,y) \, dA
```

### Derivative
```
\frac{d}{dx} f(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
```

### Partial Derivative
```
\frac{\partial}{\partial x} f(x,y,z)
```

## Series & Sums

### Geometric Series
```
\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}
```

### Product Notation
```
\prod_{i=1}^{n} x_i
```

### Binomial Coefficient
```
\binom{n}{k} = \frac{n!}{k!(n-k)!}
```

## Statistical Examples

### Normal Distribution
```
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
```

### Standard Deviation
```
\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
```

### Probability
```
P(A \cap B) = P(A) \cdot P(B|A)
```

## Linear Algebra Examples

### Eigenvalue Equation
```
\mathbf{A}\mathbf{v} = \lambda\mathbf{v}
```

### Trace
```
\text{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii}
```

### Singular Value Decomposition
```
\mathbf{A} = \mathbf{U}\Sigma\mathbf{V}^T
```

## Physics Examples

### Kinetic Energy
```
KE = \frac{1}{2}mv^2
```

### Potential Energy
```
PE = mgh
```

### Work-Energy Theorem
```
W = \Delta KE = \frac{1}{2}m(v_f^2 - v_i^2)
```

### Planck's Equation
```
E = h\nu
```

## Chemistry Examples

### Ideal Gas Law
```
PV = nRT
```

### Enthalpy
```
\Delta H = \Delta U + \Delta(PV)
```

### Equilibrium Constant
```
K = \frac{[C]^c[D]^d}{[A]^a[B]^b}
```

## Greek Letters & Symbols

```
\alpha + \beta + \gamma = \delta
```

```
\epsilon, \varepsilon, \zeta, \eta, \theta, \vartheta
```

```
\iota, \kappa, \lambda, \mu, \nu, \xi, \pi, \rho, \sigma
```

```
\tau, \upsilon, \phi, \varphi, \chi, \psi, \omega
```

## Special Functions

### Bessel Function
```
J_0(x) = \frac{1}{\pi} \int_0^{\pi} \cos(x\sin\theta) d\theta
```

### Gamma Function
```
\Gamma(n) = (n-1)!
```

### Error Function
```
\text{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^{x} e^{-t^2} dt
```

## Complex Examples

### Euler's Formula
```
e^{i\pi} + 1 = 0
```

### Complex Number
```
z = a + bi = r e^{i\theta}
```

### Residue Theorem
```
\oint_C f(z) dz = 2\pi i \sum \text{Res}(f, z_k)
```

## Tips for Best Results

1. **Use `Display` mode** for prominent equations
2. **Use `Inline` mode** for small, text-sized equations
3. **Keep equations concise** for faster compilation
4. **Test complex equations** in Overleaf first
5. **Escape special characters**: `\$`, `\_`, `\{`, `\}`

---

For more LaTeX help, visit: https://www.overleaf.com/learn
