# while loop
i = 0


def should_continue():
    """Should the loop continue?

    Returns:
        bool: True if the loop should continue i.e. i < 5, False otherwise
    """
    global i
    i += 1
    return i < 5


# good to use in case of where we don't know the number of iterations
while should_continue():
    print(i)


# while with else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    # will be printed when i is not less than 5
    print("i is no longer less than 5")
