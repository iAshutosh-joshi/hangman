import random
words = ['python', 'java', 'kotlin', 'javascript']
password = random.choice(words)
letterpass = list()
i = 0
for _ in range(len(password)):
    letterpass += '-'
    i += 1
letterlist = list(letterpass)
i = 1
b = 0
print("H A N G M A N")
t = input(print('Type "play" to play the game, "exit" to quit:'))
if (t == "exit"):
    exit()
else:
    print()
    lutter = []
    while i <= 8:
        word = ''
        for _ in range(len(password)):
            word += letterpass[b]
            b += 1
        print()
        print(word)
        if word.find('-') == -1:
            print("You guessed the word!")
            print("You survived!")
            exit()
        letter = str(input("Input a letter: "))
        if len(letter) != 1:
            print("You should input a single letter")
        elif ((letter.isalpha() and letter.islower())== False):
            print("Please enter a lowercase English letter")
        elif letter in word:
            print('You\'ve already guessed this letter')
        elif (letter in lutter):
            print('You\'ve already guessed this letter')
        elif letter in password:
            letterpass[password.find(letter)] = letter
            letterpass[password.rfind(letter)] = letter
        elif letter not in password:
            print("That letter doesn't appear in the word")
            i += 1
        lutter.append(letter)
        b = 0
    print("You lost!")
