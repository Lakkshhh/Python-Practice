pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)    # sorted is a function, doesn't affect the original list
print(sorted_numbers)
print(numbers)

numbers.sort()    # .sort() is a method, it changes/sorts the original list
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)    # The sorting function will now give same priority to "T" and "t"
print(missing_letter)
