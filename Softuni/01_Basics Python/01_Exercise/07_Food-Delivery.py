chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_price = chicken_menus * 10.35
fish_price = fish_menus * 12.40
vegan_price = vegan_menus * 8.15
desert = (chicken_price + fish_price + vegan_price) * 0.2

price = chicken_price + fish_price + vegan_price + desert + 2.5

print(round(price, 2))
