# Composition of functions
# Definition: Using the output of one function as the input to another.

def f(x):
    return x + 1


def g(x):
    return x * 2


print(f(g(1)))
# f(1) = 2
# g(2) = 4

# Output: 4


def compose(f, g):
    return lambda x: f(g(x))


fog = compose(f, g)
print(fog(1))
