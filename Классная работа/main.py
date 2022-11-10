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



1. import random
  2. HANGMANPICS = ['''
  3.
  4.    +---+
  5.    |   |
  6.        |
  7.        |
  8.        |
  9.        |
 10. =========''','''
 11.
 12.    +---+
 13.    |   |
 14.    O   |
 15.        |
 16.        |
 17.        |
 18. =========''','''
 19.
 20.    +---+
 21.    |   |
 22.    O   |
 23.    |   |
 24.        |
 25.        |
 26. =========''','''
 27.
 28.    +---+
 29.    |   |
 30     O   |
 31.   /|   |
 32.        |
 33.        |
 34. =========''','''
 35.
 36.    +---+
 37.    |   |
 38.    O   |
 39.   /|\  |
 40.        |
 41.        |
 42. =========''','''
 43.
 44.    +---+
 45.    |   |
 46.    O   |
 47.   /|\  |
 48.   /    |
 49.        |
 50. =========''','''
 51.
 52.    +---+
 53.    |   |
 54.    O   |
 55.   /|\  |
 56.   / \  |
 57.        |
 58. =========''']
