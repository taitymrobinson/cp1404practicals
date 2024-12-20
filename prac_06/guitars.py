"""
CP1404 - PRAC 06
"""
from prac_06.guitar import Guitar

def main():
    """A program to store a user's guitar collection data"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = (Guitar(name, year, cost))
        guitars.append(new_guitar)
        print(f"{new_guitar.__str__()} added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("-" * 20) # Used to improve readability

    for i, guitar in enumerate(guitars, 1):
        vintage_string = "vintage" if guitar.is_vintage() else "not vintage"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}, {vintage_string}")

main()