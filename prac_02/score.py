"""
CP1404 - PRACTICAL
"""
from random import randint

def main():
    """Determine the result based on score. """
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    """Determine the result based on score. """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"



main()
