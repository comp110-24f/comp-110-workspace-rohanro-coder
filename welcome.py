x: int = 5


def g(n: int) -> int:
    n += 3
    print(n)
    return n


def f(y: int) -> int:
    print(y)
    return y + 1


y: int = f(x)
print(y)
z: int = g(x) + 1
print(z)
