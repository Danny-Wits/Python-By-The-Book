# For

# classic for loop i.e. ranged loop
for i in range(5):
    print(i, end=",")  # prints 0,1,2,3,4,

# range(start, stop, step)
for i in range(2, 10, 2):
    print(i, end=",")  # prints 2,4,6,8

#!empty for  using pass : to avoid error
for i in []:
    pass

# for to iterate over a list/tuple/string/set/dictionary

print()  # print to get to the next line
list = [1, 2, 3, 4, 5]
for i in list:
    print(i, end=",")  # prints 1,2,3,4,5,
print()

tuple = (1, 2, 3, 4, 5)
for i in tuple:
    print(i, end=",")  # prints 1,2,3,4,5,
print()

string = "hello"
for i in string:
    print(i, end=",")  # prints h,e,l,l,o,
print()

dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
for [key, value] in dictionary.items():
    # prints key1 : value1 |  key2 : value2 | key3 : value3
    print(f" {key} : {value}  ", end=" | ")

print()
set = {1, 2, 3, 2, 1}
for i in set:
    print(i, end=",")  # prints 1,2,3,
