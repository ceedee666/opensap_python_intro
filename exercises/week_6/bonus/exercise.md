# Week 6 Bonus - Compute π using a random number generator

The number π (Pi) can be calculated using random numbers. Suppose you have a circle
with radius 1 which is inscribed in a square with a side length of 2 (see figure below). Then the square
has an area of 4 (2 \* 2) and the circle has an area of π (r = 1, thus $π\*r^2 = π$).

![Figure1](img1.png)

If thousands of points are randomly created within the square, then some points are
inside the square _and_ inside the circle, others are inside the square and _not_ inside the circle.
The situation can be simplified if you just consider the upper right quadrant of
the above figure. This square has a side length of 1. Each point within the
square can be described by the coordinates `x` and `y`
(0 < x, y < 1). If x\*\*2 + y\*\*2 < 1, then the point specified by (x,y) is
within the circle.

![Figure2](img2.png)

As the relation between the sizes of circle and square is π/4, the relation
between the points in the circle and the points in the square must be π/4 as
well. Using this formula, one can now use a random number generator to calculate π.

## Your Task

Using the library `random` create 10.000 random points inside the square.
That means generate 10.000 random pairs of values for `x` and `y`. The random value must be between 0 and 1
in order for a point to be inside the square.
For each point check if x\*\*2 + y\*\*2 is < 1. If this is the case, then the point is
within the circle. Count the total number of points and the points which are
in the circle. Use these numbers to calculate π.
Finally compare your calculated value of π with
the value of π found in the `math` library. Do this by printing the calculated value of π, the value from
the math library as well as the difference.

Below is an example execution of the program. Note that your values might be different.

```
Calculated value of π: 3.1396
Value of π from math library: 3.141592653589793
Difference: -0.0019926535897929476
```

## Additional Challenge

Can you solve the bonus exercise without a for loop using list comprehension?
