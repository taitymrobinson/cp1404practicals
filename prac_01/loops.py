for i in range(1,21,2):
    print(i, end=" ")
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

number_of_stars = int(input("How many stars do you have? "))
for stars in range(1, number_of_stars + 1):
    print('*', end=" ")
print()

for stars in range(1, number_of_stars + 1):
    print('*' * stars)
print()