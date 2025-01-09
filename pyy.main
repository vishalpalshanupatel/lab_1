# Program to calculate the factorial of a number

# Function to calculate factorial
def calculate_factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Input from the user
try:
    num = int(input("Enter a number: "))
    result = calculate_factorial(num)
    print(f"The factorial of {num} is {result}.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
