# Blocks meaning for loop, if else, while loop etc.

for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))    # Automatically idents 4 spaces after :
    print("*" * 80)   # A colon(:) tells python to expect a code block after it is used, just skips 4 spaces by itself

# Examples

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18:
    print("You are old enough to vote.")
    print("Don't vote for Trump.")
elif age < 5:
    print("Hmmmmmmmm, go watch TV.")
else:
    print("Please come back in {0} years.".format(18 - age))
