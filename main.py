from random import *

words = open("words.txt","r")
wordList = words.readlines()
for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

def testWord(word,part):
    if word == "":
        return False
    elif (word in wordList) and (part in word):
        return True
    print(part + " is not in " + word + ".")
    return False


while True:
    randWord = wordList[randint(0,len(wordList)-1)]
    randStart = randint(0,len(randWord)-4)
    part = randWord[randStart:min((randStart + randint(2,3)),len(randWord)-1)]
    givenWord = ""
    while not testWord(givenWord,part):
        givenWord = input("Word with " + part + ": ").lower()