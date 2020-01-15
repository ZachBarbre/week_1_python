bill_amount = float(input("Total bill amount? "))
service_level = input("Level of service? ")
number_people = float(input("Split how many ways? "))

if service_level == 'bad':
    tip = bill_amount * 0.1
elif service_level == 'fair':
    tip = bill_amount * 0.15
else:
    tip = bill_amount * 0.25

total = bill_amount + tip
spilt_total = total / number_people
print("Tip amount: $%.2f" % tip)
print("Total amount: $%.2f" % total)
print("Amount per person: $%.2f" % spilt_total)