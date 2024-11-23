"""
CP1404 - PRAC 09
Intermediate Exercise
ESTIMATE: 20 mins
ACTUAL: 20 mins
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness, flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialises a Silver Service Taxi object."""
        super(SilverServiceTaxi, self).__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Returns a string representation of the Silver Service Taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the fare."""
        return self.flagfall + super().get_fare()
