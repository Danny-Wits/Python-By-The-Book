# List Slices
# Slices allow you to extract portions of a list.

# Slicing syntax: list[start:end:step]

i = [1, 2, 3, 5, 7]

print(i[1:4])  # [2, 3, 5]
print(i[:4])  # [1, 2, 3, 5]
print(i[1:])  # [2, 3, 5, 7]
print(i[:])  # [1, 2, 3, 5, 7]
print(i[0:len(i):2])  # [1, 3, 7]
