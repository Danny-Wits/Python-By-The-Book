# List and Strings :
# Lists and strings are both sequences,
# but lists are mutable, while strings are immutable.
# You can convert between them.

string = "Hello World"

# converting a string into list with each character as an element
my_list = list(string)
# Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(my_list)

# splits the string into a list using a string as a separator
# whitespace by default
my_list = string.split()
print(my_list)
# Output: ['Hello', 'World']


_list = ["hi", "hello", "bye"]
# converting a list into string using .join a the separator string
string = " | ".join(_list)
print(string)
