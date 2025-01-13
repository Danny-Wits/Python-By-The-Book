# Order of operations

# Python follows the PEMDAS Rule
# 1. P: Parentheses ()
# 2. E: Exponentiation **
# 3. M/D: Multiplication *, Division /, Floor Division //, Modulus % (evaluated left to right)
# 4. A/S: Addition + and Subtraction - (evaluated left to right)

result = 10 + 2 * 3 - 4 / 2**2
# 10 + 2 * 3 - 4/4
# 10 + 6 - 1
# 16 - 1
# 15
print(result)  # Output: 14.0

result = (10 + 2) * (3 - 4) / 2
# 12 * (-1) / 2
# -12 / 2
print(result)  # Output: -6.0
