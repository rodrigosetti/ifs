IFS - Iterated function system
==============================

What is it?
-----------

Iterated function systems or IFSs are a method of constructing fractals;
the resulting constructions are always self-similar. IFS fractals,
as they are normally called, can be of any number of dimensions, but
are commonly computed and drawn in 2D. The fractal is made up of the
union of several copies of itself, each copy being transformed by
a function (hence "function system"). The canonical example is the
Sierpinski gasket also called the Sierpinski triangle. The functions
are normally contractive which means they bring points closer together
and make shapes smaller. Hence the shape of an IFS fractal is made
up of several possibly-overlapping smaller copies of itself, each
of which is also made up of copies of itself, ad infinitum. This is
the source of its self-similar fractal nature. (more from Wikipedia:
http://en.wikipedia.org/wiki/Iterated_function_system )

What is this Project?
---------------------

This project is a Haskell implementation of a kind of IFS. Each system
is a stochastic composition of two-dimensional linear functions.

Why?
---

I wanted to learn more about the pure functional Haskell programming
language as well as about this beautiful fractal like mathematical
structures.

The system are configured by JSON files, _e. g._:

    {
        "functions": {
            .1: [0.12, .9,  0  ],
            .7: [1.1 , .25, 0  ],
            .2: [0   , .2,  .16]
        }
        "width" : 800,
        "height": 600
    }

The system is defined by the "functions" object. It's a mapping
of probability to the linear function coefficients. The terms the
coefficients refer to are `x`, `y` and `1` (constant) respectively.

The sum of the probability keys are not necessary to sum to unity, as
the probability is calculated proportionally (_i. e._ roulette wheel).

