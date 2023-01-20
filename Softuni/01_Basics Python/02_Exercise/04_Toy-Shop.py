price_trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_toys = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
amount_toys = puzzles + dolls + bears + minions + trucks

# discount
if amount_toys >= 50:
    price_toys = price_toys * 0.75

# rent
price_toys = price_toys * 0.9

amount_left = price_toys - price_trip

if amount_left >= 0:
    print(f'Yes! {amount_left:.2f} lv left.')
else:
    print(f'Not enough money! {abs(amount_left):.2f} lv needed.')
