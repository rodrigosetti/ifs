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

This project is a implementation of a kind of IFS. Each system is a stochastic
composition of two-dimensional linear functions.

Why?
---

I wanted to learn more about these beautiful fractal like mathematical
structures.

The system are configured by json files, _e. g._:

    {
        "iterations": 28,
        "width": 800,
        "heigth": 600,
        "transformations": [
            ["1",  "0, .16*y"],
            ["7",  ".2*x -.26*y, .23*x + .22*y + 1.6"],
            ["7",  "-.15*x + .28*y, .26*x + .24*y + .44"],
            ["85", ".85*x + .04*y, -.04*x + .85*y + 1.6"]
        ]
    }

The system is defined by the "transformations" list. It's a mapping of
probability to the transformation function. Each number (first element of each
transformation) is a proportional probability of that transformation to occur,
and each function is an expression transforming a `x` and `y` arguments into
another two-dimensional point (comma separated).

The sum of the probability keys are not necessary to sum to unity, as
the probability is calculated proportionally (_i. e._ roulette wheel).

