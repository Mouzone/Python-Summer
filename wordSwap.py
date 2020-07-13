# takes in multiple strings
# returns array
def wordSwap(mainString, takeOut, swapIn, mode):

    position = 0 # The current position in the array
    mainArray = mainString.split(" ") # converts the user's string into an Array

    # If the item in the array equals takeOut we use the countas an indice and put in swapIn
    # If the user wanted scorched earth we use condition mode == "S" which then checks if item == takeOut capitalized
        # only checks for the word with a capitalized first letter
    # then increments posiiton by 1 as the for loop incremented as well
    for item in mainArray:

        if item == takeOut:

            mainArray[count] = swapIn

        if mode == "S":

            if item == takeOut.capitalize():

                mainArray[count] = swapIn

        position += 1

    return mainArray

def main():

    # Where the necessary info is collected
    mainString = input("Enter a string: ") # The string which the function acts on
    mode = input("Enter 'S' for scorched earth: ") # Scorched earth ignores capitals
    takeOut = input("Enter the word you want to swap out: ") # Word you want out
    swapIn = input("Enter the word you want to swap in: ") # Word you want to put in place of takeOut

    # Resulting array of after swapping out the words the user wants
    mainArray = wordSwap(mainString, takeOut, swapIn, mode)

    # prints introduction then uses ".join" to concatenate array into string
    print("Your resulting string is:", " ".join(mainArray))

main()
