"""
CP1404 Intermediate Exercise
ESTIMATE: 15 mins
ACTUAL: 10 mins
Testing
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Runs tests on Unreliable Car class."""
    ford = UnreliableCar("Broken", 200, 21)
    honda = UnreliableCar("Beaut", 200, 87)
    for i in range(10):
        # These strings from suggested solution were the best formatting option
        print(f"Attempting to drive {i}km:")
        print(f"{ford.name:12} drove {ford.drive(i):2}km")
        print(f"{honda.name:12} drove {honda.drive(i):2}km")


    print(ford)
    print(honda)


main()
