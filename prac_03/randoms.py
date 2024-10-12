# What did you see on line 1?
# A random integer between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# The smallest number possible is 5, and the largest is 20

# What did you see on line 2?
# A random odd integer between 3 and 10
# What was the smallest number you could have seen, what was the largest?
# The smallest number possible is 3, and the largest is 9
# Could line 2 have produced a 4?
# No, as the range only allows odd numbers

# What did you see on line 3?
# A random float between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# The smallest is 2.5 and the largest is 5.5

from random import randint
print(randint(1, 100))