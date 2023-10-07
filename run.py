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

random_word, guessed_word, max_attempts = initialize_game('hard')
print(random_word)
print(' '.join(guessed_word))
print(max_attempts)