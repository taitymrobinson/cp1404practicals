"""
CP1404 - PRAC 07
READING FILE
Estimate (all parts): 1 hour
Actual: 37 mins
"""
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Reads file of guitar details, storing as list of Guitar objects, writes data into file."""
    print("My guitars!")
    guitars = load_file(FILENAME)
    display_guitar_information(guitars)
    add_new_guitars(guitars)
    write_file(FILENAME, guitars)


def load_file(filename):
    """Loads guitar details from file."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            print(parts)
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(parts[0], year, cost))
    return guitars


def display_guitar_information(guitars):
    """Displays guitar details line by line."""
    for guitar in sorted(guitars):
        print(guitar)


def add_new_guitars(guitars):
    """Adds new guitars to the list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = (Guitar(name, year, cost))
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")


def write_file(filename, guitars):
    """Writes guitar details to file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
