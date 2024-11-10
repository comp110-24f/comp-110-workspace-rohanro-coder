def funky(i: int) -> int:
    while i < 5:
        if i == 2:
            return i
        print(i)
        i += 1
    return 1000


print(funky(10))
