# List Map, Filter, and Reduce
# These are functional programming tools to process lists.
from functools import reduce  # need for reduce function

# Map applies a function to every element.


list1 = [1, 2, 3, 4, 5]

# return a map object so need to cast is back to a list , same goes for filter
list2 = map(lambda x: x*2, list1)
list2 = list(list2)
print(list2)

# Filter retains elements that satisfy a condition.

list1 = [1, 2, 3, 4, 5]

list2 = filter(lambda x: x % 2 == 1, list1)
list2 = list(list2)
print(list2)

# Reduce aggregates elements into a single value.
# need to import it form functools package
list1 = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


sum = reduce(add, list1, 0)  # using function
print(sum)

sum = reduce(lambda x, y: x+y, list1, 0)  # using lambda
print(sum)
# Output: 15
