# Modulus Operator

a = 10
b = 3
remainder = a % b  # modulus operator returns the remainder
print(f"Remainder of {a} % {b} = {remainder}")

# Negative Values
a = 10.1
b = -3


remainder = a % b  # modulus operator returns the remainder
# 10.1 / -3 leaves remainder 1.1
# (1.1) mod -3
# -3+1.1 mod -3    (a) mod b => (a+b) mod b
# -1.9 mod -3
print(f"Remainder of {a} % {b} = {remainder}")
