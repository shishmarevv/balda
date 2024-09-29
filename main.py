import os, threading

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
    str = ''
    for key, value in dict:
        str = str + key + ':' + str(value) + '\n'
    file.write(str)
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

def AIthread(words, iterations):
    global dict


def aiVSai(words):
    print("AI vs AI")
    iterations = int(input("Type in a number of iterations "))
    thread_number = int(input("Type a number of threads "))
    thread_list = []
    for i in range(thread_number):
        thread_list.append(threading.Thread(target = AIthread(words, iterations//thread_number)))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    
    
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