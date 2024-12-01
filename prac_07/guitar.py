"""
CP1404 - PRAC 07
Estimate (all parts): 1 hour 5:53
Actual:
"""

CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Represents a guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of the object."""
        return f"{self.name} ({self.year}) : ${self.cost:,}"

    def __lt__(self, other):
        """Overloads the lt function use 'year' for comparison."""
        return self.get_age() < other.get_age()

    def get_age(self):
        """Gets the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Checks if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE


if __name__ == '__main__':
    jameson = Guitar("Jameson", 2001, 238)
    fender = Guitar("Fender", 2000, 450)
    print(jameson > fender)
    print(jameson < fender)
