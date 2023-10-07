import gspread 
from google.oauth2.service_account import Credentials

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

SHEET = CLIENT.open('hangman_words').get_worksheet(0)

words = SHEET.col_values(1)

print(words)