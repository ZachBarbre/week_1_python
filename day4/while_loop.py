# index = 1
# while index <= 10:
#     print(index)
#     index += 1

# start = int(input('Start? '))
# end = int(input('End? '))

# while start <= end:
#     print(start)
#     start += 1

# index = 1 
# while index < 10:
#     print(index)
#     index += 2

# coins = 0
# while True:
#     print(f"You have {coins} coins.")
#     ans = input("Do you want another coin? ")
#     if ans.lower().strip() == 'yes':
#         coins += 1
#     elif ans.lower().strip() == 'no':
#         print("Bye")
#         break
#     else:
#         pass

# size = int(input("How big is it? "))
# index = 0

# while index < size:
#     print('*'*size)
#     index += 1

# height = int(input('Height? '))
# width = int(input('Width? '))
# index = 0
# while index < height:
#     if index == 0 or index == height - 1:
#         print('*' * width)
#     else:
#         print('*' + ' '*(width-2) + '*')
#     index += 1

# height = int(input('Height? '))
# index = 1
# while index <= height:
#     print(' ' * (height - index) + '*'*(index-1) + '*' + '*'*(index-1) + ' ' * (height - index))
#     index += 1

# first_number = 1
# while first_number <= 10:
#     second_number = 1
#     while second_number <= 10:
#         answer = first_number * second_number
#         print(f"{first_number} X {second_number} = {answer}")
#         second_number += 1
#     first_number += 1

# text = input("Text? ")
# print('*'*(len(text)+4))
# print('* ' + text + ' *')
# print('*'*(len(text)+4))

# index = 1
# triangle_numbers = 1
# while index <= 100:
#     print(triangle_numbers)
#     index += 1
#     triangle_numbers += index

num = int(input('Enter number: '))
index = 1
while index <= num:
    if num % index == 0:
        print(index)
    index += 1