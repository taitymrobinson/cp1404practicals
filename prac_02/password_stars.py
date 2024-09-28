def main():
    """Print asterisks same length as inputted password, that is longer than minimum length"""
    minimum_length = 6
    password = get_valid_password(minimum_length)
    print_asterisks(password)


def get_valid_password(minimum_length):
    """Get valid password based on minimum length"""
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print asterisks same length as password"""
    print("*" * len(password))

main()