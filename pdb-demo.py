#!/usr/bin/env python3
# coding=utf-8

import random

N = 5
RANDOM_RANGE = 0, 10

def float_factorial(j):
    if j <= 0:
        return 1
    return j * float_factorial(j-1)

def random_float(min_val=0, max_val=10):
    return min_val + random.random() * (max_val - min_val)

if __name__ == "__main__":
    for i in range(N):
        rf = random_float(*RANDOM_RANGE)
        ff = float_factorial(rf)
        print(f"float_factorial({rf}) = {ff}")
