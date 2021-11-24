#!/usr/bin/env python3
import random
print(random.uniform(0, 1))


def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle/num_point_total


print(estimate_pi(100))
print(estimate_pi(1000))
print(estimate_pi(10000))
print(estimate_pi(100000))
print(estimate_pi(1000000))
# print(estimate_pi(10000000))
# print(estimate_pi(100000000))
