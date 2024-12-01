"""Guessing game with files and exceptions"""

FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()

    while guess != secret:
        print("Guess again!")
        guess = get_valid_number()
    print("Congratulations!")


def load_number(filename):
    try:
        infile = open(filename, "r")
        number = int(infile.read())
    except ValueError:
        print(f"{filename} is not an integer")
        number = 6
    except FileNotFoundError:
        print(f"{FILENAME} is not a file")
        number = 4
    else:
        infile.close()  # no issue with undefined variable
    return number


def get_valid_number():
    is_valid_number = False
    while not is_valid_number:
        try:
            guess = int(input("? "))
            is_valid_number = True
        except ValueError:
            print("Invalid Integer")
    return guess  # no issue with undefined variable


main()
