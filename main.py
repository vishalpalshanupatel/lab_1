# Program to calculate the factorial of a number

def calculate_factorial(num):
    """
    Calculate the factorial of a non-negative integer.
    """
    if num < 0:
        return "Factorial is not defined for negative numbers."
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

# Input from the user
try:
    user_input = int(input("Enter a number: "))  # Renamed variable to avoid conflict with the function parameter
    result = calculate_factorial(user_input)
    print(f"The factorial of {user_input} is {result}.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
