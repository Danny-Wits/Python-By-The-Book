# Type Conversion Functions

# Definition : These functions convert data from one type to another

# Common Functions:
# int(): Converts to an integer.
# float(): Converts to a floating-point number.
# str(): Converts to a string.
# bool(): Converts to a Boolean.
# list(), tuple(), set(), etc.: Convert to respective data structures.

text = "12321"
number = int(text)
print(type(number))  # <class 'int'>

flag = 0
flag = bool(flag)  # 0 ,"" ,[] ,() ,{} ... are converted to False else to true
print(flag)

# convert string to list as string is a iterable object too
_list = list("12321")
print(_list)

_set = set("12321")
print(_set)  # same as list but only for unique elements
