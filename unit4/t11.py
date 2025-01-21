# List vs tuple
from timeit import timeit


# List : Mutable
# Tuple : Immutable
# conversion

_list = [1, 2, 3]
_tuple = tuple(_list)

print(type(_tuple))

# performance difference using timeit
list_snippet = "_list=[1,2,3]"

tuple_snippet = "_tuple=(1,2,3)"

list_time = timeit(list_snippet, number=100000)

tuple_time = timeit(tuple_snippet, number=100000)

print("list is faster" if list_time < tuple_time else "tuple is faster")


# Tuple vs Dictionary

dictionary = {1: "Danny", 2: "Sam", 3: "Raju"}
_tuple = tuple(dictionary)  # convert dictionary keys to tuple

print(type(_tuple))
print(_tuple)

# performance difference using timeit
dictionary_snippet = "dictionary={1:'Danny',2:'Sam',3:'Raju'}"

tuple_snippet = "_tuple=(1,'Danny',2,'Sam',3,'Raju')"

dictionary_time = timeit(dictionary_snippet, number=100000)

tuple_time = timeit(tuple_snippet, number=100000)

print("dictionary is faster" if dictionary_time <
      tuple_time else "tuple is faster")
