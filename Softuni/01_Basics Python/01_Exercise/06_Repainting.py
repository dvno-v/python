nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint + paint * 0.1) * 14.50
thinner_price = 5 * thinner
bags = 0.4

price_materials = nylon_price + paint_price + thinner_price + bags

work_price = price_materials * 0.30 * hours

print(price_materials + work_price)
