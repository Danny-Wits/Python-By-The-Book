# String traversal
# using for loop

s = "Hello World"
for i in s:
    print(i, end=",")
print()

# using while loop
index = 0
while index < len(s):
    print(s[index], end=",")
    index += 1
print()

# using range
for i in range(len(s)):
    print(s[i], end=",")
print()

# String Comparison
# String comparison is used to check if two strings are equal
# or determine their lexicographical order.

# Operators:
# == : Checks if two strings are equal.
# != : Checks if two strings are not equal.
# <, <=, >, >= : Lexicographical comparison.

str1 = "apple"
str2 = "banana"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 < str2)   # True (lexicographically "apple" comes before "banana")
