# Son of Word Swap
def nuclearProtocol(mainString, takeOut, swapIn, noMercy):

    length = len(takeOut)
    i = 0 # position currently in the mainString

    while i <= len(mainString): # simplfies it as increment will also be position

        # checks if from the current position to the length of the target word is the target word
        # this works bc i+length will go one over, but indices don't include the last position
        if mainString[ i : i + length ] == takeOut:

            # if before is true this takes the past before it and concatenates new word in middle
            # and adds the rest of the string
            # the string will be put back into the loop and acted upon
            mainString = mainString[ 0 : i ] + swapIn + mainString[ i + length : len(mainString)]
            # to prevent rechecking and the possibility of takeOut and swapIn being different lengths
            # the loop continues at the position where the rest of the string is
            i += len(swapIn)

        if noMercy == "Y":

            if mainString[ i : i + length ] == takeOut.capitalize():

                mainString = mainString[ 0 : i ] + swapIn + mainString[ i + length : len(mainString) ]

                i += len(swapIn)

        i += 1

    return mainString

def main():

    # Where the necessary info is collected
    mainString = input("Enter a string: ") # The string which the function acts on
    takeOut = input("Enter the word you want to swap out: ") # Word you want out
    swapIn = input("Enter the word you want to swap in: ") # Word you want to put in place of takeOut
    noMercy = input("THERE IS NO GOING BACK.\nDARE TO ANNIHILATE?\nEnter 'Y' for YES: ")

    # TOTAL TOTAL DESTRUCTION
    # Swap out every instance of a word
    # ex) swap out the with dog, thesaurus -> dogsaurus
    print(nuclearProtocol(mainString, takeOut, swapIn, noMercy.capitalize()))

main()
