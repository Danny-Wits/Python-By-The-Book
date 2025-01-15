# Break and continue

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# list of alphabets
alphabet = [chr(a) for a in range(ord("a"), ord("z")+1)]  # list comprehension
vowels = ["a", "e", "i", "o", "u"]
for i in alphabet:
    if i in vowels:
        continue
    print(i)
