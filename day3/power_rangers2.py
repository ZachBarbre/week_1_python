power_rangers = ['Jason', 'Trini', 'Billy', 'Zack', 'Kim', 'Tommy']

who_to_remove = input(f"Who gets removed from this list {power_rangers}? ")

if who_to_remove in power_rangers:
    power_rangers.remove(who_to_remove)
    print(who_to_remove, 'is removed.')
else:
    print(who_to_remove, "isn't here")