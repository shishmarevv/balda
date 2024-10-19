import os, random, time

def outFile():
    file = open("C:/Users/Nergigante/Documents/Projects/Balda/memory.txt", 'r')
    dict = {}
    for line in file:
        Tline = line.split(":")
        dict[Tline[0]] = int(Tline[1])
    file.close()
    return dict

def inFile(dict):
    file = open("C:/Users/Nergigante/Documents/Projects/Balda/memory.txt", 'w')
    buffer = ''
    for key in dict.keys():
        buffer = buffer + key + ':' + str(dict[key]) + '\n'
    file.write(buffer)
    file.close()

def check(words, input_word):
    button = 0
    input_word.replace('\n', '')
    for word in words:
        if input_word in word:
            if not(input_word == word):
                button = 2
        if input_word == word:
            button = 1
            break
    return button

def playerVSplayer(words):
    print("Player versus Player")
    buffer = ""
    checker = True
    desider = False
    while checker:
        os.system('cls')
        print("Current word is " + buffer)
        desider = not desider
        if desider:
            print("Player ONE:")
            buffer = buffer + input(buffer)[:1]
        else:
            print("Player TWO:")
            buffer = buffer + input(buffer)[:1]
        switch = check(words, buffer)
        if switch == 0 or switch == 1:
            checker = False
    if switch == 0:
        print("There is no word that incudes " + buffer)
    elif switch == 1:
        print("You completed the word")
    if not desider:
        print("Player ONE won") 
    else:
        print("Player TWO won")
    checker = True
    print("Come back to main menu typing m\nType r to retry")
    while checker:
        m = input()
        if m == 'm':
            checker = False
            main(words)
        elif m == 'r':
            checker = False
            playerVSplayer(words)

def aiVSai(words):
    global dict
    timer = time.time()
    os.system('cls')
    print("AI versus AI")
    iterations = int(input("Type the number of iterations:"))
    for i in range(iterations):
        buffer = chr(97 + random.randint(0, 25))
        if not (buffer in dict.keys()):
            dict[buffer] = 0
        checker = True
        iterator = 1
        cash = []
        while checker:
            cash.append(buffer)
            switch = check(words, buffer)
            if switch == 2:
                dict[buffer] = dict[buffer] + iterator
                weight = 0
                temp = True
                for key in dict.keys():
                    if buffer in key and (len(buffer) + 1 == len(key)):
                        temp = False
                        if dict[key] > weight:
                            weight = dict[key]
                if temp:
                    buffer = buffer + chr(97 + random.randint(0, 25))
                else:
                    temp = []
                    for key in dict.keys():
                        if abs(dict[key] - weight) <= 3*iterator:
                            temp.append(key)
                    buffer = buffer + temp[random.randint(0, len(temp) - 1)]
                if not (buffer in dict.keys()):
                    dict[buffer] = 0
            else:
                checker = False
                for key in cash:
                    dict[key] = dict[key] - 1
            iterator = iterator + 1
        if (i/iterations*100)%10 == 0:
            print("Current progress:" + str(i/iterations*100) + "%")
    print("It took " + str(time.time() - timer) + " seconds")
    stop = input("If you want to come back to main menu type m: ")  
    if stop == 'm':
        main(words)
    
def main(words):
    os.system('cls')
    print("MAIN MENU")
    print("TYPE 1 IF YOU WANT PLAYER VS PLAYER \nTYPE 2 IF YOU WANT PLAYER VS AI \nTYPE 3 IF YOU WANT AI VS AI\nTYPE 4 TO SEE RULES\nTYPE 5 TO EXIT")
    checker = True
    while checker:
        i = input()
        if i == '1':
            checker = False
            playerVSplayer(words)
        elif i == '3':
            checker = False
            aiVSai(words)
        elif i =='5':
            checker = False

WordsFile = open("C:/Users/Nergigante/Documents/Projects/Balda/words.txt", 'r')
words = []
for line in WordsFile:
    temp = line.replace('\n','')
    if len(temp) > 2:
        words.append(temp)
WordsFile.close()
dict = outFile()
main(words)
inFile(dict)