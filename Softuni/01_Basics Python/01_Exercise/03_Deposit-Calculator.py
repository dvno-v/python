#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit = float(input())
term = int(input())
interest = float(input())

price = deposit + term * ((deposit * interest/100) / 12)

print (price)