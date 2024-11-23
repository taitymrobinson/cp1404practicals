"""
CP1404 - PRAC 09
Intermediate Exercise
ESTIMATE: 20 mins
ACTUAL: 20 mins
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Run tests on Silver Service Taxi, all test should pass."""
    taxi =  SilverServiceTaxi("Test Taxi", 100, 2)
    assert taxi.fanciness == 2
    assert taxi.flagfall == 4.50
    assert taxi.price_per_km == 2.46
    taxi.drive(18)
    assert taxi.get_fare() == 48.78


main()