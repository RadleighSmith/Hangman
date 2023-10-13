# Hangman - A Python Game

Welcome to a classic game of Hangman, a text-based Python game that challenges your word-guessing prowess. This interactive console application invites players to decipher a concealed word within a limited number of attempts. Choose your level of difficulty. Will you opt for an easy warm-up or dive straight into a more demanding experience? Exercise caution with hints, as you have only one invaluable clue to use throughout each game. Embrace the challenge, expand your vocabulary, and enjoy the thrill of unraveling words. Best of luck, and may your hangman skills be unmatched! 

<img src = "docs/read-me-images/main menu.png">


## Contents

[Planning]()

[Features]()

[Testing]()

[Bugs]()

[Deployment]()

[Credits]()

## Planning

### Key Audience Characteristics:

* Casual gamers seeking an entertaining word-guessing experience.
* Language learners looking to enhance their vocabulary skills.
* Parents and educators in search of an educational tool to aid in language learning for children
* Individuals wanting a fun way to challenge logical thinking.

### Age Group:

* Suitable for all ages.

### Accessibility:

Intuitive user interface suitable for players of all experience levels.

### User Stories:

* As a user, I want the option to choose from different difficulty levels so that I can enjoy playing the game that suits my skill level.
* As a user, I expect clear and concise instructions on how to play Hangman, ensuring a smooth start to the game.
* As a user, I want to receive immediate feedback on my guesses to help me understand which letters I guessed correctly or incorrectly.
* As a user, I want the ability to replay the game after completing it, so I can continue to enjoy playing and test my knowledge.
* As a user, I look forward to encountering a diverse range of words to guess, ensuring an engaging and comprehensive gaming experience.
* As a user, I anticipate an intuitive and user-friendly interface that makes it easy for me to navigate and interact with the game, ultimately enhancing my overall experience.
* As a user, I want the option to use a hint to get assistance with guessing the word, understanding that it will come at the cost of a life. This feature should only be available when I have more than one life remaining.

### Lucid Chart

In the planning stages of my Hangman game, [Lucidchart](https://www.lucidchart.com/) emerged as an invaluable tool. Through Lucidchart's intuitive diagramming capabilities, I meticulously mapped out the game's architecture and flow. Starting with wireframes and flowcharts, I visualized the user interface, game mechanics, and navigation pathways. This allowed for a clear, bird's-eye view of the entire project.

<img src= "docs/read-me-images/lucid-chart.jpeg">

## Features

The Hangman game offers a captivating and interactive gaming experience, pulling random words from Google sheets using the Google API. Players have the flexibility to choose from three distinct difficulty levels, tailored to cater to both novices and players looking for a challenge. The game incorporates a hint feature, providing an extra layer of strategy for players looking to maximize their chances of success. With immediate feedback on guesses, users can track their progress and make informed decisions. The visually engaging interface, coupled with clear instructions, ensures an intuitive user experience. Additionally, the game boasts replayability, allowing players to continually challenge their word-guessing skills.

### Main Menu:

<img src = "docs/read-me-images/main menu.png">

The Hangman game's main menu offers three straightforward options: Play, Instructions, and Quit. Players can quickly jump into the game, learn the rules, or exit with ease. The menu features an intuitive design for seamless navigation, ensuring a smooth and enjoyable user experience.

### Instructions page:

<img src = "docs/read-me-images/instructions.png">

The Instructions section provides players with a clear and comprehensive guide on how to play the Hangman game. It covers the rules, objectives, and mechanics, ensuring that players have a solid grasp of the gameplay. This ensures a smooth start and an enjoyable gaming experience.

### Difficulty choice:

<img src = "docs/read-me-images/difficulty-choice.png">

The Difficulty Choice feature in the Hangman game offers three distinct levels—easy, medium, and hard—catering to players of varying skill levels. This allows users to customize their gameplay experience, ensuring both a fun challenge and an engaging experience for all.

### Game Page and loop:

<img src = "docs/read-me-images/game-loop.png">

The game page in the Hangman experience provides players with an immersive interface where they can engage in a word-guessing challenge. Through an intuitive loop, players enter letters to uncover the hidden word. With each guess, the game offers immediate feedback, keeping players informed about their progress. The loop continues until the player either successfully guesses the word or reaches the maximum attempts. This dynamic gameplay loop ensures an interactive and engaging experience throughout the game.

#### Correct Guess:

<img src = "docs/read-me-images/correct-guess.png">

#### Incorrect Guess:

<img src = "docs/read-me-images/incorrect-guess.png">

### Hint Feature
This Hangman game introduces an intriguing hint feature to aid players. This handy tool allows players to receive a subtle clue, aiding them to uncover the hidden word. Once used or the user is on their last life, the hint prompt is removed from the user interface. Using a hint costs one life, but it cannot be employed on the player's last life otherwise it would end the game.

#### Hint not used:

<img src = "docs/read-me-images/hint-not-used.png">

#### Hint used:

<img src = "docs/read-me-images/hint-used.png">

### Game Win:

<img src = "docs/read-me-images/game-win.png">

When a player successfully guesses the word in the Hangman game, The game promptly celebrates their accomplishment with a winning message and a visual display of the completed word. Players are then presented with the option to replay. This feature encourages replayability,

### Game Lose:

<img src = "docs/read-me-images/game-lose.png">

When a player exhausts their allotted attempts in the Hangman game, the screen displays 'Game Over' with a visual representation of the completed hangman. This signals the conclusion of the current round. However, the game offers players the chance to replay once again encouraging replayability.

### Future Features:

* Leaderboard to track high scores and promote friendly competition among players.
* Expanded word database with categories or themes for a more diverse word selection.
* Customizable themes and visuals to personalize the game's appearance.
* Time-based challenges for players who enjoy a fast-paced gaming experience.
* Integration with educational resources, providing players with information about the words they encounter.

## Testing

### Code Institute's Python Linter:

To ensure clean and consistent code, I utilized the PEP8 checker, an invaluable tool for adhering to Python's style guide. By navigating to [Code Institute's Python Linter](https://pep8ci.herokuapp.com/#), I was able to effortlessly submit my code for examination. The checker meticulously reviewed every aspect of the codebase, from indentation to variable naming. This process not only ensures readability and maintainability but also promotes best practices in Python development. Thanks to the PEP8 checker, my code is not only functional but also adheres to industry-standard coding conventions.

#### Run.py Result

<img src = "docs/read-me-images/run-python-linter.png">

#### Graphics.py Result

<img src = "docs/read-me-images/run-python-linter.png">

### Functional Testing:

#### Main Menu

* Checked each individual option was working as intended:
    * '1' (Play) takes the user to difficulty section.
    * '2' (Instuctions) displays the instructions.
    * '3' (Quit) will quit the game.

* Check that only the correct inputs can be used (1,2,3) or the user will be given the feedback of "Invalid choice. Please enter 1, 2, or 3."

#### Instructions

* Checked if instructions are displayed prominently.
* Confirmed that pressing "Enter" returns the user back to the main menu.

#### Difficulty Section

* Tested each difficulty level (easy, medium, hard) to validate parameter adjustments.
* Tested that only (e,m,h) will be accepted or the user will get a prompt saying "Invalid difficulty level. Please choose from e, m, or h"
* Confirmed corresponding maximum attempts with difficulty levels.
    * 6 for Easy
    * 5 for Medium
    * 4 for Hard

#### Game Loop

* Conducted multiple game sessions to check that the random word feature provides varying words from the google sheet.
* Checked that "Remaining Lives" will decrease when a incorrect letter is guessed.
* Ensured that only one letter can be inputted at a time, except when "hint" is entered.
* Validated that all guessed letters are displayed in the "Guessed Letters" section.
* Checked that correctly guessed letters are revealed in the hidden word.
* Verified that after each guess (except when the user has no lives left or the word has been guessed), the user can make another guess.
* Tested the user feedback system to ensure accurate responses for both correct and incorrect guesses.

#### Hint Feature

* Tested hint feature for providing one clue without errors.
* Ensured that the hint feature is not usable after use or on final life as this would end the game.
* Verified using a hint costs one life.
* Confirmed that once the user has used the hint or is on their final life it removes the prompt.

#### Game Win Page

* Triggered game win condition to evaluate victory screen and options.
* Checked accuracy of displayed screen and replay options.

#### Game Lose Page

* Triggered game lose condition to evaluate game over screen and options.
* Checked accuracy of displayed screen and replay options.

These functional tests were conducted meticulously to ensure a seamless and enjoyable gaming experience for players of all levels. By addressing these aspects, we aim to provide a high-quality Hangman game that meets or exceeds user expectations.

## Bugs

## Deployment

## Credits