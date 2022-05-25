# While loop is used when we want a block of code to execute until a condition is true and stop when it becomes false.
# Useful when you don't know how many times you need to loop
# Let's start with a simple code

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

print("-" * 80)

# Ex2

available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
if chosen_exit.casefold() != "quit":
    print("Aren't you glad you got outta there")
