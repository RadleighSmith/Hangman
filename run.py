import gspread
import random
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

    CREDS = Credentials.from_service_account_file(
        'words.json',
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

    # Initialize the guessed word with underscores
    guessed_word = ['_'] * len(random_word)

    max_attempts = 0

    if difficulty == 'easy':
        max_attempts = 6
    elif difficulty == 'mediun':
        max_attempts = 5
    elif difficulty == 'hard':
        max_attempts = 4

    return random_word, guessed_word, max_attempts

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
    guessed_letters = []

    while current_attempts < max_attempts:
        print(' '.join(guessed_word))
        print(f"Guessed Letters: {' '.join(guessed_letters)}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in random_word:
            for i, letter in enumerate(random_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            current_attempts += 1
            print(f"Incorrect guess! Attempts remaining: {max_attempts - current_attempts}")

        if '_' not in guessed_word:
            print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
            return True

    print(f"Sorry! The word was: {random_word}")
    return False

def main():
    """
    The main function that manages the execution of the Hangman game.

    This function prompts the user to choose a difficulty level (easy, medium, or hard).
    It then initializes the game with a random word, sets up the initial guessed word,
    and establishes the maximum number of attempts based on the chosen difficulty.
    The game loop is then started.
    """
    print("Welcome to Hangman!")
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        return

    random_word, guessed_word, max_attempts = initialize_game(difficulty)
    play_game(random_word, guessed_word, max_attempts)

if __name__ == "__main__":
    main()