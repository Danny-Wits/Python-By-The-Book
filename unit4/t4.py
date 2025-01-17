# Deleting Elements
# You can delete elements by index, value, or range.

# by index:using del

list1 = [1, 2, 3, 4, 5]

del list1[0]
print(list1)


# by value using remove()


list1 = [1, 2, 3, 4, 5]

list1.remove(3)  # removes only the first occurrence
print(list1)

# by range using del

list1 = [1, 2, 3, 4, 5]

del list1[1:3]
print(list1)
