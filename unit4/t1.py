# Lists as a Sequence
# Lists are ordered collections of items, which can be of mixed types
# (e.g., integers, strings, or even other lists).

_list = [1, "hello", True]
print(_list)


# Traversing a List
# You can iterate through a list using loops.

_list = [1, 2, 3, 4, 5]
for i in _list:
    print(i, end=",")
print()


# List Operations
# Lists support various operations like concatenation, repetition,comprehension and membership checks.

# concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)  # [1, 2, 3, 4, 5, 6]

# repetition
list1 = [1, 2, 3]
list2 = list1 * 2
print(list2)  # [1, 2, 3, 1, 2, 3]

# comprehension
list1 = [a for a in range(5)]
print(list1)  # [0, 1, 2, 3, 4]
# membership check
list1 = [1, 2, 3]
print(2 in list1)  # True
print(4 not in list1)  # True
