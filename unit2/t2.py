# Boolean Expressions && Logical Operators

#!Boolean : A value that is either True or False
a = True  # a is a bool
b = False  # b is a bool

# Logical operators
# and, or, not

# truth table for logical operators
c1 = [True, True, False, False]
c2 = [True, False, True, False]

# and
print("AND")
for i in range(4):
    print(f"{c1[i]} and {c2[i]} = {c1[i] and c2[i]}")
# or
print("OR")
for i in range(4):
    print(f"{c1[i]} or {c2[i]} = {c1[i] or c2[i]}")
# not
print("NOT")
for i in range(4):
    print(f"not {c1[i]} = {not c1[i]}")
