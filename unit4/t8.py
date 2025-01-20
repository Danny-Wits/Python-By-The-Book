# List and Dictionary in Python

# list : mutable collection of items of different types

# Dictionary : mutable collection of key value pairs with unique keys

# initialization
_list = [1, 2, 3, 4, 5]  # Square Brackets
_dict = {1: "Danny", 2: "Sam", 3: "Raju"}  # curly Braces

print(_list)
print(_dict)
# insertion
print("After Insertion:")
_list.append(6)
_dict.update({4: "Audi"})

print(_list)
print(_dict)

# updation
print("After Updation:")
_list[0] = 10
_dict.update({4: "Andy"})

print(_list)
print(_dict)

# deletion
print("After Deletion:")
del _list[0]    # by index
del _dict[4]    # by key

_list.pop(0)  # by index
_dict.pop(2)  # by key

print(_list)
print(_dict)
