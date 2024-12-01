"""
CP1404 - PRAC 05
Colour Lookup
"""

COLOUR_TO_CODE = {"Harlequin": "#3fff00", "Mauvelous": "#ef98aa", "Zomp:": "#39a78e", "Wild Strawberry": "#ff43a4",
                  "Vermillion": "#e34234", "Sapphire": "#0f52ba", "Rose Bonbon": "#f9429e", "Pistachio": "#93c572",
                  "Peach": "#ffe5b4", "Mandarin": "#f37a48"}
colour = input("Enter colour: ").title()
while colour != "":
    try:
        print(f"The hex code for {colour} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").title()
