HANGMANPICS = ['''

    +---+
    |   |
    |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']

import random
words = [['дуб','осина','берёза'],['хомяк','крыса','мышка'],['гитара','фортепиано','скрипка']]
help = [['У Лукоморья ... зелёный','... пух','символ России'],['щекастый зверёк','подлый человек','сыр'],['струнный щипковый','Громко и тихо','звук похож на скрип']]
i = 0
t = 0
health = 7
used_letters = ''
#word = words[random.randrange(3)]
win_word = []

print('выберите тему и введите цифру:деревья(0),грызуны(1),музыкальные инструменты(2)')
p = int(input())
for q in range(3):
    if p == q:
        word = words[q][random.randrange(3)]

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
        print(HANGMANPICS[t])
        print('Оставшееся кол-во попыток = ', health)
        t = t + 1
        print('есть возможность получить подсказку: да(1),нет(2)')
        a = int(input())
        if a == 1:
            help_index = words[p].index(word)
            print(help[p][help_index])

    else:
        print('Вы ввели верную буву')
        print(win_word)
    if word == (''.join(win_word)):
        print('Вы победили')
        break
    elif health == 0:
        print('Вы проиграли')
        break

#я заметила проблему, если в слове буква повторяется несколько раз(например в слове гитара) програама ломается