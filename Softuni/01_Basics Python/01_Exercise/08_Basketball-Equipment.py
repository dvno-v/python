price_per_year = int(input())

price_sneakers = price_per_year - price_per_year * 0.4
price_outfit = price_sneakers - price_sneakers * 0.20
price_baseball = price_outfit / 4
price_accessories = price_baseball / 5

price = price_accessories + price_baseball + price_outfit + price_sneakers + price_per_year

print (price)