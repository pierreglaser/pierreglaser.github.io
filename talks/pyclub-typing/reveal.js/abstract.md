Current modern scientific computing frameworks such as `numpy` or `pytorch`
offer an attractive trade-off between ease of use and performance by exposing
a set of highly optimized, common numerical subroutines (implemented in
low-level languages) via a high-level Python API. However, not much is done in
these frameworks to optimize performance at a program level.

`jax` fills this gap by defining and implementing a system of
function transformations, which can be operated on *pure and statically composed* (PSC)
Python programs allowed to call a large set of `numpy`-like subroutines.
These function transformations encompass in a unified manner operations as varied
Just In Time (JIT) compilation, Automatic Differentiation, Vectorization and
more, making programs written in `jax` both highly-optimized and often less
complex than their pytorch counterpart.

In this tutorial, we will go through a high-level introduction to `jax`,
discuss its most common features and how to write idiomatic `jax` code through a
series of examples. Finally, we will also consider the potential limitations
of `jax`, and in particular the "compiled language creep", e.g the additional
structural constraints that `jax`-compatible programs must verify.
