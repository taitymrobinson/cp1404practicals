"""CP1404 PRACTICAL 04"""
import random

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    """Program to generate an amount of 6 different random numbers in line """
    number_of_quick_picks = int(input("How many quick picks? "))
    for quick_pick in range(number_of_quick_picks):
        quick_pick_line = []
        for number in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick_line:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick_line.append(number)
        print(" ".join(f"{number:5}" for number in quick_pick_line))
main()
