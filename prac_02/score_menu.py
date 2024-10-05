"""
CP1404 - PRACTICAL
"""


def main():
    """Get valid score from user, print corresponding result, print stars equal to score."""
    score = get_valid_score(0, 100)
    print("""
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
    """)
    selection = input(">> ").upper()
    while selection != 'Q':
        if selection == 'G':
            score = get_valid_score(0, 100)
        elif selection == 'P':
            print(f"Result: {determine_result(score)}")
        elif selection == 'S':
            print_stars(score)
        else:
            print("Invalid selection")
        print("""
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
            """)
        selection = input(">> ").upper()


    print("Farewell.")


def get_valid_score(upper, lower):
    """Get a valid score between boundaries."""
    score = int(input("Please enter a score (0-100 inclusive): "))
    while score < lower or score > upper:
        print("Invalid score")
        score = int(input("Please enter a score (0-100 inclusive): "))
    return score


def determine_result(score):
    """Determine the result based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def print_stars(score):
    """Print asterisks equal to score."""
    print("*" * score)


main()
