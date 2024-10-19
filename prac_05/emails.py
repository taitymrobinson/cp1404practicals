"""
CP1404 PRAC 05
Emails
Estimate: 20 minutes
Actual: 16 minutes
"""


def main():
    """Program to create a dictionary of emails to names"""
    email_to_name = {}
    email = input("Enter your email: ")

    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is {name} your name? [Y/n] ").upper()
        if confirmation == "Y":
            email_to_name[email] = name
        else:  # Not else-if as instructions say 'if input isn't y'
            name = input("Enter your name: ")
            email_to_name[email] = name
        email = input("Enter your email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract suspected name from email"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    print(name)
    return name


main()
