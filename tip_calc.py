bill_amount = float(input("Total bill amount? "))
service_level = input("Level of service? ")

if service_level == 'bad':
    tip = bill_amount * 0.1
    total = bill_amount + tip
    print("Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)
elif service_level == 'fair':
    tip = bill_amount * 0.15
    total = bill_amount + tip
    print("Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)
else:
    tip = bill_amount * 1.25
    total = bill_amount + tip
    print("Tip amount: $%.2f" % tip)
    print("Total amount: $%.2f" % total)