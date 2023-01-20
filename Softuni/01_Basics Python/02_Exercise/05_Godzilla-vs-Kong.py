budget = float(input())
statists = int(input())
price_outfit = float(input())

price_decour = budget * 0.1

if statists > 150:
    price_outfit = price_outfit * 0.9

price_statists = statists * price_outfit

price_for_film = price_decour + price_statists

money_left = budget - price_for_film

if money_left >= 0:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(money_left):.2f} leva more.')

