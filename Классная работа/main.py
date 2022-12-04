HANGMANPICS0 = ['''

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

HANGMANPICS1 = ['''

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
   / \  |
        |
 =========''']

HANGMANPICS2 = ['''

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
   /|\  |
   / \  |
        |
 =========''']



def HANGMANPICSdef():
    import random
    words = [['дуб','тополь','берёза'],['хомяк','крыса','мышка'],['гитара','фортепиано','скрипка']]
    help = [['У Лукоморья ... зелёный','... пух','символ России'],['щекастый зверёк','подлый человек','сыр'],['струнный щипковый','Громко и тихо','звук похож на скрип']]
    i = 0
    t = 0
    g = 0
    health = 7
    used_letters = ''
    win_word = []

    print('Выберите уровень сложности:', '(0) - начальный','(1) - средний','(2) - ультрасложный',sep = '\n')
    r = int(input())
    if r == 0:
        health = 7
    elif r==1:
        health = 5
    elif r==2:
        health = 3

    print('Выберите тему и введите цифру:', '(0) - деревья','(1) - грызуны','(2) - музыкальные инструменты',sep = '\n')
    p = input()
    e = 0
    while e ==0:
        try:
            p = int(p)
            if p > 2:
                print('введите нужное ЧИСЛО')
                p = input()
            else:
                p = int(p)
                for q in range(3):
                    if p == q:
                        word = words[q][random.randrange(3)]
                        e = 1
        except ValueError: #человек вводит именно число
            print('введите нужное ЧИСЛО')
            p = input()

    for w in range(len(word)):
        win_word.append('_')
    while health > 0:
        test = False
        letter = input('введите букву, или если хотите использовать подсказку, напишите "подcказка" ')
        d = 0
        if letter == 'подсказка':
            help_index = words[p].index(word)
            print(help[p][help_index])
        while d == 0:
            if len(letter) > 1:
                print('Введите одну букву')
                letter = input()
            else:
                d = 1
        if letter in used_letters:
            print('эту букву Вы уже использовали')
            g = 1
        else:
            used_letters += letter
        for a in word:
            if letter == a:
                k = word. count(a)
                if k == 1:
                    o = word.index(letter)
                    win_word[o] = letter
                    test = True
                else:
                    for r in range(len(word)):
                        if letter == word[r]:
                            win_word[r] = letter
                            test = True

        if r == 0:
            if test == False:
                if g == 0:
                    health -= 1
                    t = t+1
                g = 0
                print('Вы ввели неверную букву.')
                print(HANGMANPICS0[t-1])
                print('Оставшееся кол-во попыток = ', health)
            else:
                print('Вы ввели верную буву')
                print(win_word)
        elif r == 1:
            if test == False:
                if g == 0:
                    health -= 1
                    t = t+1
                g = 0
                print('Вы ввели неверную букву.')
                print(HANGMANPICS1[t-1])
                print('Оставшееся кол-во попыток = ', health)
            else:
                print('Вы ввели верную буву')
                print(win_word)
        elif r == 2:
            if test == False:
                if g == 0:
                    health -= 1
                    t = t+1
                g = 0
                print('Вы ввели неверную букву.')
                print(HANGMANPICS2[t-1])
                print('Оставшееся кол-во попыток = ', health)
            else:
                print('Вы ввели верную буву')
                print(win_word)

        if word == (''.join(win_word)):
            print('Вы победили')
            print('Хотите сыграть ещё раз?','да/нет',sep = '\n')
            b = input()
            if b == 'да':
                return HANGMANPICSdef()
            break
        elif health == 0:
            print('Вы проиграли')
            print('Хотите сыграть ещё раз?', 'да/нет', sep='\n')
            b = input()
            if b == 'да':
                return HANGMANPICSdef()
            break
HANGMANPICSdef()