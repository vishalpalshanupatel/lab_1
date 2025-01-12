"""
This script calculates and prints the multiplication table for a number.
"""

def multiplication_table(n):
    """
    Prints the multiplication table for a non-negative integer n.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
multiplication_table(num)
