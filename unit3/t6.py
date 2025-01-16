# Recursion
# Definition : A function that calls itself again and again until it reaches a base case


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)  # factorial calls itself


print(factorial(5))

# Stack Diagram for Recursive Functions
# visualizing using console


def factorial(n):
    print(f"factorial({n}) running")
    if n == 1:
        print(f"factorial({n}) returns 1")
        return 1
    else:
        print(f"factorial({n}) called factorial({n-1})")
        result = n * factorial(n-1)
        print(f"factorial({n}) returns {result} ")
        return result


print("Stack Diagram for Recursive Functions")
print(factorial(3))
