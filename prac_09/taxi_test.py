"""
CP1404 WALKTHROUGH
ESTIMATE - 5 mins
ACTUAL: 7 mins
"""

from prac_09.taxi import Taxi


def main():
    """Tests the Taxi class"""
    taxicab = Taxi("Prius 1", 100)
    taxicab.drive(40)
    print(taxicab)
    taxicab.start_fare()
    taxicab.drive(100)
    print(taxicab)


main()
