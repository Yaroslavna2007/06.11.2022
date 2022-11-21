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

def HANGMANPICS1():
    import random
    words = [['дуб','осина','берёза'],['хомяк','крыса','мышка'],['гитара','фортепиано','скрипка']]
    help = [['У Лукоморья ... зелёный','... пух','символ России'],['щекастый зверёк','подлый человек','сыр'],['струнный щипковый','Громко и тихо','звук похож на скрип']]
    i = 0
    t = 0
    health = 7
    used_letters = ''
    win_word = []

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
        except ValueError:
            print('введите нужное ЧИСЛО')
            p = input()

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
            print('Хотите сыграть ещё раз?','да/нет',sep = '\n')
            b = input()
            if b == 'да':
                return HANGMANPICS1()
            break
        elif health == 0:
            print('Вы проиграли')
            print('Хотите сыграть ещё раз?', 'да/нет', sep='\n')
            b = input()
            if b == 'да':
                return HANGMANPICS1()
            break
HANGMANPICS1()