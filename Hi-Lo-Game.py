# The binary search algorithm is the most efficient way of finding an item in an ordered list
# Allows very fast searching of the data
# 'Pass' keyword doesn't do anything, but makes the code syntactically correct
# This program lets you think up a random number, the computer guesses your number using binary search algo
# and finds the number you have thought of in less than 10 moves in the range is 1 to 1024.

low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:

    print("Guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("\tMy guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses = guesses + 1    # guesses += 1  ---> Known as augmented assignment, better solution

else:
    print("You thought of the number {}".format(low))
    print("i got it in {} guesses".format(guesses))
