# Reverse Look up
from collections import Counter


def reverse_look_up(dictionary: dict, value: any) -> list:
    '''
    Performs a reverse look up on a dictionary in o(n)
        Args:
            dictionary:dict
            value : any

        Returns:
            list of keys
    '''
    keys = list()
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    if len(keys) == 0:
        raise LookupError("No Item Found")
    return keys


# runner
dictionary = {"water": 1, "test": 1, "dance": 2}
dictionary2 = Counter("waterisgoodforhealth")
print(dictionary2.most_common())

print(reverse_look_up(dictionary, 1))
print(reverse_look_up(dictionary2, 2))
