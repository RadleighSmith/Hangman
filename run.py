import gspread
import random
import os
import json
from graphics import hangman_title, draw_hangman
from google.oauth2.service_account import Credentials

def get_random_word():
    """
    Retrieves a random word from the Google Sheets.

    Returns a random word in string format.
    """

    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_info(
        json.loads(os.environ.get('CREDS')),
        scopes=SCOPE
    )

    CLIENT = gspread.authorize(CREDS)

    SHEET = CLIENT.open('hangman_words').sheet1

    words = SHEET.col_values(1)

    random_word = random.choice(words)

    return random_word

def initialize_game(difficulty):
    """
    Initializes the Hangman game.

    Argument = The difficulty level (easy, medium, or hard) chosen by the user.

    Returns A tuple containing the random word, the initial guessed word, and max_attempts based from the difficulty.
    """
    random_word = get_random_word()

    guessed_word = ['_'] * len(random_word)

    max_attempts = 0

    if difficulty == 'easy':
        max_attempts = 6
    elif difficulty == 'medium':
        max_attempts = 5
    elif difficulty == 'hard':
        max_attempts = 4

    return random_word, guessed_word, max_attempts

def hint(random_word, guessed_word, guessed_letters, max_attempts, hint_used):
    """
    Randomly selects an unguessed letter from the word to provide as a hint.
    If a hint is provided, the corresponding letter is revealed in the guessed word.

    A hint costs a life and can only be used if there is more than 1 letter remaining and
    if the hint hasn't been used before in the game.
    """
    if hint_used or guessed_word.count('_') <= 1:
        print("Sorry, you can't use a hint right now.")
        return False

    unguessed_letters = [letter for letter in random_word if letter not in guessed_letters]
    hint_letter = random.choice(unguessed_letters)

    for i, letter in enumerate(random_word):
        if letter == hint_letter:
            guessed_word[i] = hint_letter

    guessed_letters.add(hint_letter)
    return True

def replay():
    """
    Asks the player if they want to play again, only allowing 'y' or 'n'.

    Returns True if the player wants to play again, False otherwise.
    """
    while True:
        replay_choice = input("Do you want to play again? (y/n): ").strip().lower()
        if replay_choice == 'y':
            return True
        elif replay_choice == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def play_game(random_word, guessed_word, max_attempts):
    """
    Plays a round of the game.

    Arguments:
        random_word (string): The word to guess.
        guessed_word (list): The word with guessed letters.
        max_attempts (interger): The maximum number of attempts.

    Returns True if the game is won, otherwise returns false.
    """
    current_attempts = 0
    guessed_letters = set()
    hint_used = False
    lives = max_attempts

    while current_attempts < max_attempts:
        print(' '.join(guessed_word))
        print(f"Guessed Letters: {' '.join(guessed_letters)}")
        print(f"Lives Remaining: {lives}")

        draw_hangman(current_attempts)

        if not hint_used:
            guess = input("Enter a letter (or type 'hint' for a hint): ").lower()
        else:
            guess = input("Enter a letter: ").lower()

        if guess == 'hint':
            hint_successful = hint(random_word, guessed_word, guessed_letters, max_attempts, hint_used)
            if hint_successful:
                hint_used = True
                lives -= 1
                continue
            else:
                current_attempts += 1
        else:
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            if guess in random_word:
                for i, letter in enumerate(random_word):
                    if letter == guess:
                        guessed_word[i] = guess
            else:
                current_attempts += 1
                lives -= 1
                print(f"Incorrect guess! Attempts remaining: {max_attempts - current_attempts}")

            guessed_letters.add(guess)

            if '_' not in guessed_word:
                print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
                return replay()

    print(f"Sorry! The word was: {random_word}")
    draw_hangman(current_attempts)
    return replay()

def main():
    """
    The main function that manages the execution of the Hangman game.

    This function prompts the user to choose a difficulty level (easy, medium, or hard).
    It then initializes the game with a random word, sets up the initial guessed word,
    and establishes the maximum number of attempts based on the chosen difficulty.
    The game loop is then started.
    """
    hangman_title()
    while True:
        print("\nMenu:")
        print("1. Play")
        print("2. Instructions")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\nDifficulty Levels:")
            print("e - Easy")
            print("m - Medium")
            print("h - Hard")
            difficulty = input("Choose a difficulty (e/m/h): ").lower()

            if difficulty not in ['e', 'm', 'h']:
                print("Invalid difficulty level. Please choose from e, m, or h.")
                continue

            if difficulty == 'e':
                difficulty = 'easy'
            elif difficulty == 'm':
                difficulty = 'medium'
            else:
                difficulty = 'hard'

            random_word, guessed_word, max_attempts = initialize_game(difficulty)
            play_game(random_word, guessed_word, max_attempts)
        elif choice == '2':
            print("\nInstructions:")
            print("PLACEHOLDER INSTRUCTIONS THIS IS A TEST")  
        elif choice == '3':
            break  
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()