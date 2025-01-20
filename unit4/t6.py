# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# Creating a dictionary
# dictionary_name = {key1: value1, key2: value2, ...}

dude = {"name": "John", "age": 30, "city": "New York"}

print(dude)

# Accessing values in a dictionary
print(dude["name"])  # John
print(dude["age"])  # 30
print(dude["city"])  # New York


#! Dictionary as a Counter
string = "Hello World"

counters = dict()


for c in string:
    if (c in counters):
        counters[c] += 1
    else:
        counters[c] = 1

print(counters)

# finding max counters

max_count = max(counters.values())

max_keys = [a for a in counters if counters[a] == max_count]
print(max_keys)


#!Looping over a dictionary

# for keys
for key in counters:
    print(key, end=" ")
print()

# for values
for value in counters.values():
    print(value, end=" ")
print()

# for both
for key, value in counters.items():
    print(f"{key}=> {value}", end=" | ")
print()
