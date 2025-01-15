# if statement

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult")

# if-else statement

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# inline if-else

print("You are an adult") if (age >= 18) else print("You are not an adult")

# if-elif-else statement

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

# Nested if-else statement

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult", end=" ")
    if age >= 65:
        print("and you are an elder")
    else:
        print("and you are still young")
else:
    print("You are not an adult")
