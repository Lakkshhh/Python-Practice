# 1. This section talks about 'and' and 'or' conditions

# 2. For 'and', both conditions should be true, then only will the code block execute. If either one is false, it will
#    not execute. For 'or', if either one of them is true, the code will execute. Even if one statement is false but
#    the other one is true, it will execute.

# 3. 'and' has higher precedence/priority than 'or'.

# 4. 0 is evaluated to False. All empty sequences are evaluated to false. Eg: Apple = ""    //Empty string

age = int(input("How old are you? "))

# if age > 18 and age < 70:
if 18 < age < 70:  # This is the simplified chain expression of the above comment
    print("Have a good day at work!")
else:
    print("Enjoy your free time.")

if age <= 18 or age >= 70:
    print("Enjoy your free time.")
else:
    print("Have a good day at work!")

print("-" * 80)

# \\\ True False Boolean Examples ///

# Ex1
day = "Saturday"
temperature = 32
raining = True

if (day == "Saturday" and temperature > 27) or not raining:  # not True = False
    print("Go swimming")  # not False = True
else:
    print("Learn Python")

print("-" * 80)   # Used to just separate these different example outputs in the run terminal

# Ex2
if 0:
    print("True")
else:
    print("False")

name = input("Enter your name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

print("-" * 80)

# Ex3 ('in' and 'not in' conditions)

parrot = "Norwegian Blue"
letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

print("-" * 80)

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():  # casefold() is used for caseless matching. Converts every string to lower case
    print("But i want to go to cinema")
else:
    print("Sounds fun!")
