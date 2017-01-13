Title: Thermoplastic crystallization
Date: 2016-10-10
Category: Notes
Tags: simulation
Slug: 
Authors: Amit

$\alpha(t)$ - degree of crystallization

$$\alpha = \frac{\text{crystallized volume}}{\text{ultimate crystallizable volume}} = \frac{x_c(t,T)}{x_\infty}$$

The [Avrami equation][wiki] describes how solids transform from one phase (state of matter) to another at constant temperature. It can specifically describe the kinetics of crystallisation, but can be applied generally to other changes of phase in materials, like chemical reaction rates:

$$\alpha(t) = 1 - \exp\left[ -k(T).t^n \right] $$

where n is the Avrami exponent. 

For non-isothermal processes, the Nakamura equation can be used:

$$\alpha(t) = 1 - \exp\left[ -\left\{ \int_0^t k(T,\tau) \mathrm{d}\tau \right\}^n \right] $$

or:

$$\frac{\mathrm{d}\alpha}{\mathrm{d}t} = nk(T)(1-\alpha) \left[ \ln\left( \frac{1}{1-\alpha} \right) \right]^{(n-1)/n} $$

[wiki]: https://en.wikipedia.org/wiki/Avrami_equation
