"""

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

PSEUDOCODE ver 1:
get number_of_items
for item in range of number_of_items
    get item_price
    total_price += item_price
if total_price > 100:
    total_price = total_price * 1.1
print(total_price)

PSEUDOCODE ver 2:
get number_of_items
while number_of_items < 0:
    print Invalid number of items
    get number_of_items
calculate total price and discount
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.9
print(f"Total price for {number_of_items} items is ${total_price:.2f}")