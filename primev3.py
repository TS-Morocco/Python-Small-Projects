import math
import time


def isPrimev2(n):
    """Return True if n is prime
    False Otherwise. PS:Docstring"""
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1+max_divisor, 2):
        if n % d == 0:
            return False
    print(n, " is Prime")
    return True


# ===== Time Fuction =====
t0 = time.time()
for n in range(1, 100000):
    isPrimev2(n)
t1 = time.time()
print("Time reauired: ", t1 - t0)
