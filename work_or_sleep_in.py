day_index = int(input("Day (0-6)? "))

if day_index == 0 or day_index == 6:
    print('Sleep in')
elif day_index > 6 or day_index < 0:
    print('Read the input insructions')
else:
    print('Go to work')