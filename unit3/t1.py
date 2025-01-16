# Function Call
#!Definition: A function call executes a defined function with specific arguments, if any.


# function creation :
# def function_name():
#   function body
#   return value
#! Adding new Functions to our program
def simple_function():
    print("I am a simple function")


# function call : function_name(arguments)
simple_function()  # function call


def is_even(num):
    return num % 2 == 0


print(is_even(5))  # function call with arguments
print(is_even(6))  # function call with arguments


def add_num(num1, num2):
    return num1+num2


print(add_num(num2=5, num1=6))  # function call with named arguments
