import time


def isPrimev1(n):
    """Return True if n is prime
    False Otherwise. PS:Docstring"""
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    print(n, " is Prime")
    return True


# ===== Time Fuction =====
t0 = time.time()
for n in range(1, 100000):
    isPrimev1(n)
t1 = time.time()
print("Time required: ", t1 - t0)
