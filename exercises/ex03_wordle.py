"""Ex03: Wordle."""

__author__ = "730394484"


def contains_char(guess: str, character: str) -> bool:
    """Determines if character is in an index of guess."""
    assert len(character) == 1
    index: int = 0
    chr_exists: bool = False
    while index < len(guess):  
        if guess[index] == character:
            chr_exists = True
        index = index + 1
    return chr_exists


def emojified(guess: str, secret_word: str) -> str:
    """Gives each letter in the guessed word a colored emoji depending on if and/or where it is in the secret word."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0 
    emoji: str = ""
    while index < len(secret_word):
        if guess[index] == secret_word[index]:
            emoji = emoji + GREEN_BOX
        else:    
            if contains_char(secret_word, guess[index]) is True:  
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        index = index + 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Make sure that the player's guess is the right length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    turn: int = 1
    result: bool = False
    while turn < 7 and result is False:   # while the player is still playing and has not won yet
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:  
            result = True
        else: 
            turn += 1
    if result is True:
        print(f"You won in {turn} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()