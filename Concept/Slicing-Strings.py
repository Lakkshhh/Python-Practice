# \\\ Slicing for Strings ///

#                   1
#         01234567890123
parrot = "Norwegian Blue"

print(parrot[0:6])     # It extends from position 0 up to, but not including position 6    ---> Output = Norweg
print(parrot[2:5])     # It extends from position 2 up to, but not including position 5    ---> Output = rwe
print(parrot[:9])      # It starts from index(0) since no value is given before colon    ---> Output = Norwegian
print(parrot[10:])     # It ends at last index since no value is given after colon    ---> Output = Blue
print(parrot[:])       # Norwegian Blue
print(parrot[-4:-2])   # Bl
print(parrot[-4:12])   # Bl

print(parrot[0:6:2])   # In steps of 2. Hence 0,2,4.....    ---> Output = Nre
print(parrot[0:6:3])   # In steps of 3. Hence 0,3,6.....    ---> Output = Nw

letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[25:0:-1])    # When slicing backwards, start value > stop value
