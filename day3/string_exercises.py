words = 'this is a collection of cheeses'

print(words)
print(words.upper())
print(words.title())

words_reverse = ''
for letter in words:
    words_reverse = letter + words_reverse
print(words_reverse)

leet = '4361057'
normal = 'AEGIOST'
leet_words = ''
for letter in words.upper():
    if letter in normal:
        leet_words = leet_words + leet[normal.rindex(letter)]
    else:
        leet_words = leet_words + letter
print(leet_words)

vowels = 'aeiou'
long_vowel_words = ''
for letter in words:
    if letter in vowels and letter == long_vowel_words[-1]:
        long_vowel_words = long_vowel_words + letter * 4
    else:
        long_vowel_words = long_vowel_words + letter
print(long_vowel_words)

