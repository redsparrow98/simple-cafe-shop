# Read the README.txt file for the code explanation

#================  First task  ===================

# Asks the user to input the word they want to manipulate
string = input("Enter a word: ")

# Makes a list of letter in the given input word 
letters_in_string = list(string)

# Makes every alternate char in to an upper one and each other alt
# char in ot a lower
alteration1 = ""
char = 1

# Uses a for loop to iterate trough the char(letters) in the list
# and increases the char by 1 every time it runs an iteration
# If the char is cleanly divisible by 2 it means the program is
# iterating trough every other character(letter) in the list and it need to be lower
# otherwise it turns it to upper and appends to the empty result string alteration2

for letter in letters_in_string:
    if char % 2 == 0:
        alteration1 += letter.lower()
    else:   
        alteration1 += letter.upper()
        char += 1

# Prints out the final alteration1 of the first task
print(alteration1)

#============  second Task  ======================

# Uses the same input but split the words in the input
# instead of the individual characters
words_in_string = string.split()

# Makes every alternate word in to an upper one and each other alt
# word in ot a lower
alteration2 = ""
wrd = 1

# Uses a for loop to iterate trough the words in the list
# and increases the wrd by 1 every time it runs an iteration
# I the wrd is cleanly divisible by 2 it means the program is
# iterating trough the other alt word in the list and it need to be upper
# otherwise it turns it to lower and appends to the empty result string alteration2
for word in words_in_string:
    if wrd != 1:
        alteration2 += " "
    if wrd % 2 == 0:
        alteration2 += word.upper()
    else:   
        alteration2  += word.lower()
        wrd += 1

# Prints out the final alteration2 of the first task
print(alteration2)
