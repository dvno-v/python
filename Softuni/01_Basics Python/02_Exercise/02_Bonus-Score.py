points = int(input())

bonus = 0

if points > 1000:
    bonus = points * 0.10
elif points > 100:
    bonus = points * 0.20
else:
    bonus = 5

if points % 2 == 0:
    bonus += 1
elif points % 5 == 0:
    bonus += 2

print(bonus)
print(points + bonus)
