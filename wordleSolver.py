from inspect import getblock
import re
from wordList import words


def askForInput():
    print("Please enter a word to be solved:")
    word = input()
    while(len(word) != 5):
        print("Please enter a valid word to be solved (5 letters):")
        word = input()
    return word


def getIsAnswerValid(answer):
    if(len(answer) != 5):
        return False
    for letter in answer:
        if(letter != "g" and letter != "y" and letter != "r"):
            return False
    return True


def askForWordleAnswer():
    print("Please enter your wordle answer (g-gray,y-yellow,r-green):")
    answer = input()
    while(not getIsAnswerValid(answer)):
        print("Please enter a valid wordle answer (5 letters only g y and r)(g-gray,y-yellow,r-green):")
        answer = input()
    return answer


def useWordleAnswer(answer, word):
    flag = True
    for i in range(len(answer)):
        if(answer[i] == "g"):
            lettersToNotUse.append(word[i])
            flag = False
        elif(answer[i] == "y"):
            yellowLetters.append({"letter": word[i], "index": i})
            flag = False
        elif(answer[i] == "r"):
            greenLetters.append({"letter": word[i], "index": i})
    return flag


def round():
    word = askForInput()
    answer = askForWordleAnswer()
    won = useWordleAnswer(answer, word)
    if(won):
        return True
    print("next word to use is: " + getWord())
    return False


def getLetterDictionary():
    firstLetter = list(x for x in greenLetters if x["index"] == 0)
    secondLetter = list(x for x in greenLetters if x["index"] == 1)
    thirdLetter = list(x for x in greenLetters if x["index"] == 2)
    fourthLetter = list(x for x in greenLetters if x["index"] == 3)
    fifthLetter = list(x for x in greenLetters if x["index"] == 4)
    dictionary = {"firstLetter": getFirstValueIfExists(firstLetter), "secondLetter": getFirstValueIfExists(secondLetter),
                  "thirdLetter": getFirstValueIfExists(thirdLetter), "fourthLetter": getFirstValueIfExists(fourthLetter), "fifthLetter": getFirstValueIfExists(fifthLetter)}
    return dictionary


def getFirstValueIfExists(list):
    if(len(list) > 0):
        return list[0]
    return ""


def getNotLetterDictionary():
    notFirstLetter = [*lettersToNotUse]
    notSecondLetter = [*lettersToNotUse]
    notThirdLetter = [*lettersToNotUse]
    notFourthLetter = [*lettersToNotUse]
    notFifthLetter = [*lettersToNotUse]
    if(len(yellowLetters) > 0):
        notFirstLetter.extend(list(map(lambda x: x["letter"]
                                       if x["index"] == 0 else "", yellowLetters)))
        notSecondLetter.extend(list(map(lambda x: x["letter"]
                                        if x["index"] == 1 else "", yellowLetters)))
        notThirdLetter.extend(list(map(lambda x: x["letter"]
                                       if x["index"] == 2 else "", yellowLetters)))
        notFourthLetter.extend(list(map(lambda x: x["letter"]
                                        if x["index"] == 3 else "", yellowLetters)))
        notFifthLetter.extend(list(map(lambda x: x["letter"]
                                       if x["index"] == 4 else "", yellowLetters)))
        dictionary = {"notFirstLetter": notFirstLetter, "notSecondLetter": notSecondLetter,
                      "notThirdLetter": notThirdLetter, "notFourthLetter": notFourthLetter, "notFifthLetter": notFifthLetter}
    else:
        dictionary = {"notFirstLetter": notFirstLetter, "notSecondLetter": notSecondLetter,
                      "notThirdLetter": notThirdLetter, "notFourthLetter": notFourthLetter, "notFifthLetter": notFifthLetter}
    return dictionary


def getWord(printRegex):
    regex = createRegex()
    if(regex == "[^][^][^][^][^]"):
        return "crane"
    regex = regex.replace("[^]", "[.]")
    if(printRegex):
        print(regex)
    for word in words:
        if(re.match(regex, word)):
            flag = True
            for letter in yellowLetters:
                if(not letter["letter"] in word):
                    flag = False
            if(flag):
                return word
    return ""


def createRegex():
    letterDictionary = getLetterDictionary()
    notLetterDictionary = getNotLetterDictionary()
    regex = ""
    if(letterDictionary["firstLetter"] != ""):
        regex += getLetter(letterDictionary, "firstLetter")
    else:
        regex += getBracket(notLetterDictionary["notFirstLetter"])
    if(letterDictionary["secondLetter"] != ""):
        regex += getLetter(letterDictionary, "secondLetter")
    else:
        regex += getBracket(notLetterDictionary["notSecondLetter"])
    if(letterDictionary["thirdLetter"] != ""):
        regex += getLetter(letterDictionary, "thirdLetter")
    else:
        regex += getBracket(notLetterDictionary["notThirdLetter"])
    if(letterDictionary["fourthLetter"] != ""):
        regex += getLetter(letterDictionary, "fourthLetter")
    else:
        regex += getBracket(notLetterDictionary["notFourthLetter"])
    if(letterDictionary["fifthLetter"] != ""):
        regex += getLetter(letterDictionary, "fifthLetter")
    else:
        regex += getBracket(notLetterDictionary["notFifthLetter"])
    return regex


def getBracket(letters):
    regex = "[^"
    for letter in letters:
        regex += letter
    regex += "]"
    return regex


def getLetter(dictionary, index):
    return "[{}]".format(dictionary[index]["letter"])


def main():
    while(not round()):
        pass
    print("You won!")


lettersToNotUse = []
yellowLetters = []
greenLetters = []
if(__name__ == "__main__"):
    main()
