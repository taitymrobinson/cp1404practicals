"""CP1403 PRACTICAL 04"""
NUMBER_OF_REPETITIONS_ALLOWED = 5
repetition_counter = 0
numbers = []
while repetition_counter < NUMBER_OF_REPETITIONS_ALLOWED:
    number = float(input("Number: "))
    numbers.append(number)
    repetition_counter += 1

