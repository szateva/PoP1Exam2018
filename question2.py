def f(x, y):
    if x == y:
        return 0
    else:
        return f(x - 1, y) + 2 * 2

print(f(2, 2))
print(f(7, 3))
print(f(1, 3))