import random

nums_words = [1, 3, 5, 8, 2, 2, 1, 4, 0, 6, 'a', 'm', 'v', 't']

def lottery():
    i = 0
    while i < 4:
        i += 1
        combination = random.choice(nums_words)
        q = print(combination, end=' ')

lottery()
print('\nThis combination is win!')


my_ticket = nums_words[1], nums_words[3], nums_words[6], nums_words[0]

print(my_ticket)
