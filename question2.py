""" If the function f is dened as:
def f(x, y):
if x == y:
return 0
else:
return f(x - 1, y) + 2 * 2
(a) For each of the following what value is returned by the call?
i. f(2,2)
ii. f(7,3)
(b) What happens if x is less than y (e.g., f(1,3))? """


def f(x, y):
    if x == y:
        return 0
    else:
        return f(x - 1, y) + 2 * 2

print(f(2, 2))
print(f(7, 3))
print(f(1, 3))