import itertools
import sys

squares = (x**2 for x in itertools.count(1))

for x in squares:
    print(x)

    if x > 5000:
        squares.close()

print(type(squares))
print(sys.getsizeof(squares))
