"""
Description: https://code.google.com/codejam/contest/dashboard?c=6234486#s=p1

The equation for position given time is:
    x(t) = x_0 + v_0 * t + (a * t^2)/2
where `x_0` is the initial position, `v_0` is the initial speed,
and `a` is the constant acceleration due to gravity.
For simplicity, we assume x_0 = (0, 0); that is, the rocket starts
at the origin.

The equation for speed given time is:
    v(t) = v_0 + a * t

Vertical component: v_vert = v_0 * sin θ
Horizontal component: v_hor = v_0 * cos θ

The vertical speed goes down until the rocket reaches its peak altitude,
at time t':
    0 = v_vert + a * t' <=> (- a) * t' = v_vert <=> t' = v_vert / (- a)

And we know that at time t' we're supposed to be at half the horizontal distance.
    v_hor * t' = d/2 <=> t' = d/(2 * v_hor)

Putting these equations together:
    (v_0 * sin θ) / (- a) = d / (2 * (v_0 * cos θ))

Extracting the θ terms on one side:
    <=> (v_0 * sin θ) / (- a) = d / (2 * (v_0 * cos θ))
    <=> (v_0 * sin θ * cos θ) / (- a) = d/(2 * v_0)
    <=> sin θ * cos θ = (-a * d) / (2 * (v_0)^2)
    <=> 2 * sin θ * cos θ = (-a * d) / (v^0)^2

Now to get something we can actually solve, we will use a trig identity
for sine of 2x:
    <=> sin 2θ = (-a * d) / (v^0)^2

Therefore:
    2θ = arcsin ((-a * d) / (v^0)^2)
    <=> θ = 1/2 * arcsin((-a * d) / (v^0)^2)

"""

import numpy as np
import sys

fin = sys.stdin
fout = sys.stdout

accel = -9.8

test_cases = int(next(fin))

for case in range(test_cases):
    initial_speed, distance = map(int, next(fin).strip().split())

    arg = (- accel * distance) / (initial_speed ** 2)
    arg = np.clip(arg, -1, 1)
    angle = 0.5 * np.arcsin(arg)
    print(f'Case #{case + 1}:', np.degrees(angle), file=fout)
