"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730394484"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters") 
    exit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + word)

number_of_matching_characters: int = 0

if single_character == word[0]:
    print(single_character + " found at index 0")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == word[1]:
    print(single_character + " found at index 1")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == word[2]:
    print(single_character + " found at index 2")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == word[3]:
    print(single_character + " found at index 3")
    number_of_matching_characters = number_of_matching_characters + 1

if single_character == word[4]:
    print(single_character + " found at index 4")
    number_of_matching_characters = number_of_matching_characters + 1

if number_of_matching_characters == 1:
    print("1 instance of " + single_character + " found in " + word)
else: 
    if number_of_matching_characters > 1:
        print(str(number_of_matching_characters) + " instances of " + single_character + " found in " + word)
    
if number_of_matching_characters == 0:
    print("No instances of " + single_character + " found in " + word)
