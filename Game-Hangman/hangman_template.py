# Complete this template

image_win = """
  \\O/  
   |
  / \ 
"""
images= [

"""
       |
       |
       |
       |
 ______|
""",
"""
    ---|
       |
       |
       |
 ______|
""",
"""
   |---|
       |
       |
       |
 ______|
""",
"""
   |---|
   O   |
       |
       |
 ______|
""",
"""
   |---|
   O   |
   |   |
       |
 ______|
""",
"""
   |---|
   O   |
  /|   |
       |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
       |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
  /    |
 ______|
""",
"""
   |---|
   O   |
  /|\  |
  / \  |
 ______|
"""
]

main_menu = """

1. Play
2. Rules
3. Exit
"""

def play_game():
	"""
	- Write the Game Logic here
	- set the number of max turns to the number of images available.
	- get a random word using the get_word() function.
	- mantain the gusses (_ _ a _ _ b _) as a list of strings
	- Print one image and current status using print stats and ask user to enter an alphabet 
	- Use input_word() from my_lib to input one or more character
	- If user enter a character, check depending on whether it exists in the word, update correct and incorrect guess lists.
	- If user enters a word, user wins if the word is correct and looses directly if the word is wrong, irrespective of the number of remaining lives/chances.
	- If user enters a character that has already been entered, ignore it irrespective of correct or incorrect
	- Increase the turn count each time user guesses wrong.
	- Repeat till user wins or looses(guesses wrong or number of turns becomes 0)
	"""
	pass
	
def print_rules():
	"""
	Read rules from file rules.txt and print on the screen
	Use file handling for this
	"""
	pass