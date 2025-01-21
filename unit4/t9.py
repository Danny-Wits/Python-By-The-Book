
# Tuples
# A tuple is an immutable sequence of values, often used to store collections of heterogeneous data.

person = ("Danny", 1, 5.8)

# Also Tuples can be init without the parenthesis

person = "Danny", 1, 5.8

print(person)

try:
    person[0] = "John"
except Exception as e:
    print("Tuples are immutable")

print(person)


# Tuple Assignment

a, b, c = 1, 2, 3

print(a, b, c)


# var swap using tuple assignment

a = 10
b = 5

print(f"a = {a}, b = {b}")

a, b = b, a

print(f"a = {a}, b = {b}")
