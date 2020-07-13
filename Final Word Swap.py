# Son of Nuclear Word Swap

def swap(mainString, takeOut, swapIn):

    takeOut = takeOut.lower()
    mainStringLength = len(mainString)
    takeOutLength = len(takeOut)
    swapLength = len(swapIn)
    mainStringPos = 0

    while mainStringPos <= mainStringLength:

        if firstLetterChecker(mainString, takeOut, mainStringPos):

            if mainString[mainStringPos+1:mainStringPos+takeOutLength].lower() == takeOut[1:takeOutLength]:

                mainString = mainString[0:mainStringPos] + swapIn + mainString[mainStringPos+takeOutLength:mainStringLength]

                mainStringPos += swapLength - 1
                mainStringLength += swapLength

        mainStringPos += 1

    return mainString


def firstLetterChecker(mainString, takeOut, mainStringPos):

    if mainString[mainStringPos:mainStringPos+1].lower() == takeOut[0:1]:

        return True

    return False


def main():

    mainString = input("Enter a string: ")
    takeOut = input("Enter a word to be taken out: ")
    swapIn = input("Enter the word to be swapped in: ")

    mainString = swap(mainString, takeOut, swapIn)
    print(mainString)

main()
