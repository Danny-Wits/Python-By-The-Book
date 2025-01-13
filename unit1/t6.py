# Operators and operands
#!Operands : Values that are used by an operator
#!Operators : Symbols that perform operations on values/ operands
# Arithmetic operators
# +, -, *, /, //, %, **

from colorama import Fore, Style
# using a color coding for terminal using colorama
print(Fore.GREEN + "Arithmetic operators")
a = 5
b = 3
print(f"a + b = {a+b}")  # Addition
print(f"a - b = {a-b}")  # Subtraction
print(f"a * b = {a*b}")  # Multiplication
print(f"a / b = {a/b}")  # Floating point division
print(f"a // b = {a//b}")  # Floor Division (Quotient is floored)
print(f"a % b = {a%b}")  # Modulo
print(f"a ** b = {a**b}")  # a to the power b


# Assignment operators
print(Fore.RED + "Assignment operators")
# =, +=, -=, *=, /=, //=, %=, **=
a = 5  # Assigning 5 to a
a += 3  # Adding 3 to a
a -= 3  # Subtracting 3 from a
a *= 3  # Multiplying a by 3
a /= 3  # Dividing a by 3
a //= 3  # Dividing a by 3 and then floored
a %= 3  # Remainder after dividing a by 3
a **= 3  # a is now a to the power of 3

# Comparison operators
print(Fore.BLUE + "Comparison operators")
# ==, !=, >, <, >=, <=
a = 4
b = 5
print(f"a == b : {a==b}")
print(f"a != b : {a!=b}")
print(f"a > b : {a>b}")
print(f"a < b : {a<b}")
print(f"a >= b : {a>=b}")
print(f"a <= b : {a<=b}")

# Logical operators
print(Fore.YELLOW + "Logical operators")
# and, or, not
t = True
f = False

print(f"t and f : {t and f}")
print(f"t or f : {t or f}")
print(f"not t : {not t}")

# Identity operators
print(Fore.CYAN + "Identity operators")
# is, is not

a = 5
b = 5
print(f"a is b : {a is b}")
print(f"a is not b : {a is not b}")

# Membership operators
print(Fore.MAGENTA + "Membership operators")
# in, not in

a = [1, 2, 3, 4, 5]
print(f"list a : {a}")
print(f"2 in a : {2 in a}")
print(f"10 not in a : {10 not in a}")

# Bitwise operators
print(Fore.LIGHTRED_EX + "Bitwise operators")
# &, |, ^, ~, <<, >>
a = 5
b = 3
print(f"a & b : {a & b}")  # 101 & 011 = 001
print(f"a | b : {a | b}")  # 101 | 011 = 111
print(f"a ^ b : {a ^ b}")  # 101 ^ 011 = 110
print(f"~a : {~a}")  # ~101 = -6
print(f"a << b : {a << b}")  # 101 << 3 = 101000
print(f"a >> b : {a >> b}")  # 101 >> 3 = 1

print(Style.RESET_ALL)
