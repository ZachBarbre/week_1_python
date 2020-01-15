# prompt the user for a number 
# compare that number to a predefined value
# if the numbers match tell the user is a mindreader
# else print thanks for paying

user_number = int(input("What number am I thinking of? "))
MAGICNUMBER = 13

if user_number == MAGICNUMBER:
    print("ARE YOU A MINDREADER?!?")
elif user_number > MAGICNUMBER:
    print("Bzzzz!! Too high!")
elif user_number < MAGICNUMBER:
    print("Bzzz!! Too low!")
else:
    print("Nope! Thanks for playing.")