parrot = "Norwegian Blue"

for character in parrot:
    print(character)

print("-" * 80)    # This means I will be moving onto a different problem/concept

number = "9,224;338:901 764,862;684"   # Input can also be taken from the user.
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char    # Basically adding all non-numeric values to variable 'separators'

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(sum([int(val) for val in values]))

print("-" * 80)

for i in range(0, 10, 2):            # range(start value, end value, step value)
    print("i is now {}".format(i))   # From 0 up to, but not including 10

print()

for i in range(10, 0, -2):
    print("i is now {}".format(i))   # From 10 up to, but not including 0

print("-" * 80)

# Nested for loop

for i in range(1, 11):
    for j in range(1, 11):
        print("{0} times {1} = {2}".format(i, j, i * j))
    print("=" * 17)

# 'continue' statement

shopping_list = ["Milk", "Shampoo", "Cereal", "Chocolates", "Bread", "Coffee", "Chips", "Toothpaste"]   # This is a list

for item in shopping_list:
    if item == "Bread":
        continue
    print("{} has been bought from the shop".format(item))

print("-" * 80)

# 'break' statement

item_to_find = "Bread"
found_at = None         # 'None' means like empty. 'found_at' exists but it doesn't have a valur for now.

for index in range(len(shopping_list)):     # len() calculates the length of the given sequence
    if shopping_list[index] == item_to_find:
        found_at = index
        break        # breaks out of for loop after this statement executes

# Better code for same previous problem
# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)

print("Item found at position {}".format(found_at + 1))     # + 1 because iterations start from 0 instead of 1
