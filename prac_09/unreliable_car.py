"""
CP1404 Intermediate Exercise
Unreliable Car Class
ESTIMATE: 15 mins
ACTUAL: 12 mins
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Represents an unreliable car object."""

    def __init__(self, name, fuel, reliability):
        """Initialises an Unreliable Car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Sometimes drives the car a given distance, depending on the reliability."""
        if randint(0, 100) >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
