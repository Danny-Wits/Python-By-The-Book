# Searching in strings

# using `in` and `not in` operators


s = "Hello World"
print("World" in s)  # True
print("World" not in s)  # False

# using find() and index() methods : both return the lowest index the substring is found


s = "Hello World"
print(s.find("World"))  # return -1 if not found

try:
    # throws a value error if not found ... so try except is used
    print(s.index("x"))
except ValueError:
    print("Not found")


# using startswith() and endswith() methods
s = "Hello World"
print(s.startswith("Hello"))  # True
print(s.endswith("World"))  # True


# String Counting
# using count() method : return the number of times the substring is found
s = "Hello World"
print(s.count("x") > 0)  # False
print(s.count("o"))  # 2
print(s.count("World"))  # 1

# how many r are there in a strawberry :
s = "strawberry"
print(s.count("r"))
