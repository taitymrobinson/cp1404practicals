"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When an invalid character is entered (not an integer)
2. When will a ZeroDivisionError occur?
    When zero is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Have a get valid number function
"""

def main():
    """A program to calculate a fraction"""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_valid_number("Enter a denominator: ")
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_valid_number(prompt):
    number = int(input(prompt))
    while number == 0:
        print("Cannot divide by zero!")
        number = int(input(prompt))
    return number

main()
