# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['name'])
# print(ramit['friends'][1]['interests'][1])

# word = input('Please enter a words: ')
# letter_counts = {}
# for letter in word.lower():
#     if letter in letter_counts:
#         letter_counts[letter] += 1
#     else:
#         letter_counts[letter] = 1
# print(letter_counts)

words = input("Please enter a phrase: ").lower().split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)
