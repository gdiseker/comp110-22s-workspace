"""EX02: One Shot Wordle."""

__author__ = "730394484"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0 
emoji: str = ""

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji = emoji + GREEN_BOX    
    else: 
        chr_exists: bool = False
        alt_indices: int = 0
        while chr_exists is False and alt_indices < len(secret_word): 
            if secret_word[alt_indices] == guess[index]:   # Test to see if letter is in another index in the word
                chr_exists = True
            else:
                alt_indices = alt_indices + 1 
        if chr_exists is True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX  
    index = index + 1 

print(emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")