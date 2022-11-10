import random
words = ['дуб','осина','берёза']
i = 0
health = 5
used_letters = ''
word = words[random.randrange(3)]
win_word = []

for w in range(len(word)):
    win_word.append('_')
while health > 0:
    test = False
    letter = input('введите букву ')
    if letter in used_letters:
        print('эту буквы Вы уже использовали')
    else:
        used_letters += letter
    for a in word:
        if letter == a:
            o = word.index(letter)
            win_word[o] = letter
            test = True
    if test == False:
        health -= 1
        print('Вы ввели неверную букву.')
        print('Оставшееся кол-во попыток = ', health)
    else:
        print('Вы ввели верную буву')
        print(win_word)
    if word == (''.join(win_word)):
        print('Вы победили')
        break
    elif health == 0:
        print('Вы проиграли')
        break




 HANGMANPICS = ['''

    +---+
    |   |
    |
        |
        |
        |
 =========''','''
 
    +---+
    |   |
    O   |
        |
        |
        |
 =========''','''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']
