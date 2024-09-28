"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

PSEUDOCODE ver 1:
get sales
if sales < 1000
    bonus_rate = 0.1
else
    bonus_rate = 0.15
bonus_amount = sales * bonus_rate
print bonus_amount


PSEUDOCODE ver 2:
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus_rate = 0.1
    else:
        bonus_rate = 0.15
    bonus_amount = sales * bonus_rate
    print(f"Bonus is ${bonus_amount:.2f}")
    sales = float(input("Enter sales: $"))
print("Goodbye.")