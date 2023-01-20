pencils = int(input())
pens = int(input())
litres_windex = int(input())
discount = int(input())

price = pencils * 5.80 + pens * 7.20 + litres_windex * 1.20

discounted_price = price - (price * discount / 100)

print(discounted_price)
