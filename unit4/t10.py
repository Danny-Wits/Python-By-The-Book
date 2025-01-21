# Tuples as return values

def swap(a, b) -> tuple:
    return b, a


a = 10
b = 5

print(f"a = {a}, b = {b}")
a, b = swap(a, b)
print(f"a = {a}, b = {b}")

# a = 10, b = 5

# Variable-length argument tuples


# *numbers is a variable arg with any number of values denoted by *
def add(*numbers, limit) -> int:
    sum = 0
    for i in range(limit):
        sum += numbers[i]
    return sum


print(add(1, 2, 3, 4, 5, limit=3))
