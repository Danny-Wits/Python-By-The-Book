#  Pre-defined String Functions in Python

s = "Hello World"
# Case Conversion:

# lower(): Converts all characters to lowercase.
# upper(): Converts all characters to uppercase.
# capitalize(): Capitalizes the first character of the string.
# title(): Capitalizes the first character of each word.
# swapcase(): Swaps the case of all character.
print("to Lower: " + s.lower())  # hello world
print("To Upper: " + s.upper())  # HELLO WORLD
print("Capitalized: " + s.capitalize())  # Hello world
print("Title: " + s.title())  # Hello World
print("Swapped: " + s.swapcase())  # hELLO wORLD


s = "__Hello World__"
# Trimming and Padding:
# strip(): Removes whitespace from both ends.
# lstrip(): Removes whitespace from the left.
# rstrip(): Removes whitespace from the right.
# zfill(width): Pads the string with zeros.
print("Strip: " + s.strip("_"))  # Hello World
print("Left Strip: " + s.lstrip("_"))  # Hello World__
print("Right Strip: " + s.rstrip("_"))  # __Hello World
s = "X"
print("Zfill: " + s.zfill(5))  # 0000X

s = "Hi Bro"
# Search and Replace:
# find(substring): Returns the index of the first occurrence of a substring or -1.
# replace(old, new): Replaces all occurrences of a substring with another.
# startswith(prefix): Checks if a string starts with a given prefix.
# endswith(suffix): Checks if a string ends with a given suffix.

print(f"Find: {s.find('Bro')}")  # 2
print("Replace: " + s.replace("Bro", "Brother"))  # Hi Brother
print(f"Starts with: {s.startswith('Hi')}")  # True
print(f"Ends with: {s.endswith('Hi')}")  # False


s = "Hello World"
# Splitting and Joining:
# split(separator): Splits the string into a list based on a separator.
# rsplit(separator): Splits from the right.
# join(iterable): Joins elements of an iterable with the string as a separator.

_list = s.split(" ")  # ['Hello', 'World']
print(_list)

_list = s.rsplit(" ")  # ['Hello', 'World']
print(_list)


s = " | "
string = s.join(["a", "b", "c", "d"])
print(string)  # a | b | c | d


# Validation:
# isalpha(): Checks if all characters are alphabetic.
# isdigit(): Checks if all characters are digits.
# isalnum(): Checks if all characters are alphanumeric.
# isspace(): Checks if all characters are whitespace.
# islower(): Checks if all characters are lowercase.
# isupper(): Checks if all characters are uppercase.


s = "hello world"
print(f"isaplha: {s} : {s.isalpha()}")  # False
print(f"isdigit: {'123'} : {'123'.isdigit()}")  # False
print(f"isalnum: {s} : {s.isalnum()}")  # True
print(f"isspace: {s} : {s.isspace()}")  # False
print(f"islower: {s} : {s.islower()}")  # True
print(f"isupper: {s} : {s.isupper()}")  # False
