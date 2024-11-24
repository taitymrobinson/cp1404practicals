"""
CP1404 PRAC 09
ESTIMATE: 1 hour
ACTUAL: 50 mins
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Program to simulate a taxi service."""
    print("Let's drive")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0.00
    current_taxi = None
    print("(q)uit, (c)hoose taxi, (d)rive")
    choice = input("--> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            except IndexError:
                print("Invalid taxi choice")
                print(f"Bill to date: ${bill_to_date:.2f}")
                current_taxi = None

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill_to_date += fare
                print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

        print("(q)uit, (c)hoose taxi, (d)rive")
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
