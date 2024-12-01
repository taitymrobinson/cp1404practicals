"""
CP1404 PRAC 09
Band class
"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Initialise a band object."""
        self.name = name
        self.members = []
        self.member_to_instrument = {}

    def __str__(self):
        """Return a string of the band object."""
        return f"{self.name} ({str(self.members).lstrip('[').rstrip(']')})"

    def add(self, musician):
        """Adds a musician to the band object."""
        self.member_to_instrument[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        """Returns member to instrument."""
        for member in self.member_to_instrument:
            try:
                print(f"{member} is playing: {self.member_to_instrument[member][0]}")
            except IndexError:
                print(f"{member} needs an instrument!")
