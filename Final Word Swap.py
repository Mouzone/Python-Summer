# Son of Nuclear Word Swap
# swaps out takeOut with swapIn
# first finds the first letter then checks for rest of takeOut
# if doesn't then increments by one
# if first letter is found it lowercases the length of takeOut and checks
# then puts in swap in and increments by swapLength to go to end of swap
#   somehow doesn't produce an error when len(swapIn) < len(takeOut)
# somehow works even when takeOut[1:...] is camelcase
def swap(mainString, takeOut, swapIn):

    takeOut = takeOut.lower()
    mainStringLength = len(mainString)
    takeOutLength = len(takeOut)
    swapLength = len(swapIn)
    mainStringPos = 0

    while mainStringPos <= mainStringLength:

        if mainString[mainStringPos:mainStringPos+1].lower() == takeOut[0:1]:

            if mainString[mainStringPos+1:mainStringPos+takeOutLength].lower() == takeOut[1:takeOutLength]:

                mainString = mainString[0:mainStringPos] + swapIn + mainString[mainStringPos+takeOutLength:mainStringLength]

                mainStringPos += swapLength - 1
                mainStringLength += swapLength

        mainStringPos += 1

    return mainString


def main():

    # collects the variables to be acted on
    mainString = input("Enter a string: ")
    takeOut = input("Enter a word to be taken out: ")
    swapIn = input("Enter the word to be swapped in: ")

    # takes in 3 strings and returns a string
    mainString = swap(mainString, takeOut, swapIn)
    # shows the output
    print(mainString)

main()
