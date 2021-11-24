# def f():
#     return 1
#     return 2
#     return 3


# print(f())

def g():
    yield 1
    yield 2
    yield 3


for x in g():
    print(x)
