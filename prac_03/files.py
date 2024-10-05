# Question 1
FILENAME = "name.txt"
name = input("Enter your name: ")
in_file = open(FILENAME, "w")
print(name, file=in_file)
in_file.close()

# Question 2
FILENAME = "name.txt" # This is repeated as instructions state to treat as separate programs.
in_file = open(FILENAME, "r")
for name in in_file:
    print(f"Hi {name.strip()}!")
in_file.close()

# Question 3
FILENAME = "numbers.txt"
with open(FILENAME, "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)