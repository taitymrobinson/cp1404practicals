"""CP1403 PRACTICAL 04"""
NUMBER_OF_REPETITIONS_ALLOWED = 5
repetition_counter = 0
numbers = []
while repetition_counter < NUMBER_OF_REPETITIONS_ALLOWED:
    number = float(input("Number: "))
    numbers.append(number)
    repetition_counter += 1

print(f"First number is: {numbers[0]}")
print(f"Last number is: {numbers[-1]}")
print(f"The smallest number is: {min(numbers)}")
print(f"The largest number is: {max(numbers)}")
print(f"The average number is: {sum(numbers) / len(numbers)}")