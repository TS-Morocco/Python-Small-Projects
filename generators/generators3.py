import itertools


def prime_numbers():
    # Handle the first prime_numbers
    yield 2
    prime_cache = [2]  # Cache of primes

    # Loop over positive, odd integers
    for n in itertools.count(3, 2):
        is_prime = True

        # Check to see if any prime number divides n
        for p in prime_cache:
            if n % p == 0:  # p divides n evenly
                is_prime = False
                break

        # Is it prime?
        if is_prime:
            prime_cache.append(n)
            yield n


for p in prime_numbers():
    print(p)
    if p > 100:
        break
