def draw_hangman(attempts):
    hangman_graphics = [
        """
         ------
         |    |
              |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
        """
    ]
    
    return hangman_graphics[attempts]