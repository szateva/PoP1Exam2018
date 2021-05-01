def multiply(m, n):
    if n == 0 or m == 0:
        return 0
    elif (m > 0 and n > 0) or (m < 0 and n < 0):
        return m + multiply(m, n-1)
    else:
        m1 = abs(m)
        n1 = abs(n)
        result = m1 + multiply(m1, n1-1)
        return -1 * result

print(multiply(5,2))
print(multiply(2,0))
print(multiply(3,7))
print(multiply(4, -2))
print(multiply(-2, 4))