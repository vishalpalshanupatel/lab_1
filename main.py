# Program to calculate the factorial of a number
# This program takes an integer input from the user and calculates its factorial.
# It handles both valid and invalid inputs gracefully.

def calculate_factorial(num):
    """
    Calculate the factorial of a non-negative integer.

    Args:
    num (int): A non-negative integer.

    Returns:
    int or str: The factorial of the number, or a message if the number is negative.
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
    print(
        f"The factorial of {user_input} is {result}."
    )  # This line has been split to fit within the 100-character limit
except ValueError:
    print("Invalid input! Please enter a valid integer.")
