number_list = [42, 3, -12, 99, 54]
print(number_list)

list_sum = 0
for num in number_list:
    list_sum += num
print("Sum =", list_sum)

max_number = number_list[0]
for num in number_list:
    if num > max_number:
        max_number = num
print("Max =", max_number)

min_number = number_list[0]
for num in number_list:
    if num < min_number:
        min_number = num
print("Min =", min_number)

# for num in number_list:
#     if num % 2 == 0:
#         print(num)

positive_numbers = []
for num in number_list:
    if num % 2 == 0:
        positive_numbers.append(num)
print("Positive numbers =", positive_numbers)

multiplied_list = []
factor = 2
for num in number_list:
    multiplied_list.append(num * factor)
print(f"The list multiplied by {factor} = {multiplied_list}")

duped_list = [42, 3, 42, -12, 99, 54, 3]
print(duped_list)
unduped_list = []
for item in duped_list:
    if item not in unduped_list:
        unduped_list.append(item)
print(unduped_list)
