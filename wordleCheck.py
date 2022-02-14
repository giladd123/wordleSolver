from distutils.log import error
from operator import truediv
import random
from wordlesolver import getWord
from wordList import words
from wordlesolver import useWordleAnswer
from wordlesolver import lettersToNotUse, yellowLetters, greenLetters


def round(wordToFind, printRegex):
    word = getWord(printRegex)
    wordleAnswer = getWordleAnswer(word, wordToFind)

    if(printRegex):
        print("word: " + word)
        print("wordleAnswer: " + wordleAnswer)
    if(wordleAnswer=="rrrrr"):
        return True
    won = useWordleAnswer(wordleAnswer, word)
    if(won):
        return True
    return False


def getWordleAnswer(word, wordToFind):
    toReturn = "01234"
    for i in range(len(word)):
        if(word[i] == wordToFind[i]):
            toReturn = toReturn.replace(str(i), "r")
        elif(word[i] in wordToFind):
            toReturn = toReturn.replace(str(i), "y")
        else:
            toReturn = toReturn.replace(str(i), "g")
    return toReturn


def seeProcess(wordToFind):
    lettersToNotUse.clear()
    yellowLetters.clear()
    greenLetters.clear()
    print("word to find: " + wordToFind)
    tryCount = 0
    while(not round(wordToFind, True)):
        tryCount += 1
        if(tryCount == 6):
            print("failed to find word: " + wordToFind)
            break
    lettersToNotUse.clear()
    yellowLetters.clear()
    greenLetters.clear()


def main():
    amountOfEach = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(words)):
        wordToFind = words[i]
        tryCount = 0
        while(not round(wordToFind, False)):
            tryCount += 1
            if(tryCount == 6):
                amountOfEach[6] += 1
                seeProcess(wordToFind)
                break
        amountOfEach[tryCount] += 1
        lettersToNotUse.clear()
        yellowLetters.clear()
        greenLetters.clear()
    print(amountOfEach)


main()
