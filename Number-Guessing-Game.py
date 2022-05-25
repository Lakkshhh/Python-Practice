import random

answer = random.randint(1, 1000)    # Generates a random number between 1 and 1000
print(answer)    # TODO: Remove after testing
print("Choose a number between 1 to 1000: ")
number = 0    # Initialize to any number that doesn't equal the answer
i = 1
while number != answer:
    number = int(input())
    if number == 0:
        print("Game Over")
        break
    if number < answer:
        print("Entered number lower than answer. Try again: ")
    elif number > answer:
        print("Entered number higher than answer. Try again: ")
    else:
        if i == 1:
            print("You guessed it right the first time!")
            break
        else:
            print("You got it right in {0} chances.".format(i))
            break
    i += 1
