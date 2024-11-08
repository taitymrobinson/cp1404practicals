"""
CP1404 - PRAC 07
READING FILE
Estimate (all parts): 1 hour 5:53
Actual:
"""
from prac_06.guitar import Guitar


def main():
    """Reads file of guitar details, storing as list of Guitar objects."""
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(parts[0], year, cost))

    for guitar in guitars:
        print(guitar)
main()