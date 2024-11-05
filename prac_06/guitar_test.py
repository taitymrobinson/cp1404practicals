"""
CP1404 - PRAC 06
"""
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
bass = Guitar("Bass L-5 CES", 1999, 134563.40)

print(f"{gibson.name} get_age() - Expected 102. Got {gibson.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{bass.name} get_age() - Expected 25. Got {bass.get_age()}")
print(f"{bass.name} is_vintage() - Expected False. Got {bass.is_vintage()}")