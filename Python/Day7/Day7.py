import random

# List of words
words = [
    "apple",
    "banana",
    "cat",
    "dog",
    "elephant",
    "flower",
    "green",
    "house",
    "ice cream",
    "jazz",
    "kite",
    "lemon",
    "mountain",
    "notebook",
    "orange",
    "pizza",
    "queen",
    "rainbow",
    "sun",
    "tree",
    "umbrella",
    "volcano",
    "watermelon",
    "xylophone",
    "yellow",
    "zebra",
    "hello world",
    "lorem ipsum"
]

numbers = ({
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
})

hangman = [
    """      
    =========
    """,
    """
           
          |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
          |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]

# Choose the word to guess
word = words[random.randint(0,len(words))-1]

letters = []

score = 0

# Create the list
for letter in word:
    letters.append((letter, False))

# Show the first and last letters
letters[0] = (letters[0][0], True)
letters[-1] = (letters[-1][0], True)

for i, (caractere, truth) in enumerate(letters):
    if caractere == " ":
        letters[i] = (caractere, True)

# Function to return the secret word
def display_word(letters):
    displayWord = ""
    for caractere, truth in letters:
        if truth:
            displayWord += caractere
        else:
            displayWord += "_"
    return displayWord

def addSpace():
    for _ in range(100):
        print("")

def displayTitle():
        print("""
 _   _    ___    _   _   _____  ___  ___   ___    _   _ 
| | | |  / _ \  | \ | | |  __ \ |  \/  |  / _ \  | \ | |
| |_| | / /_\ \ |  \| | | |  \/ | .  . | / /_\ \ |  \| |
|  _  | |  _  | | . ` | | | __  | |\/| | |  _  | | . ` |
| | | | | | | | | |\  | | |_\ \ | |  | | | | | | | |\  |
\_| |_/ \_| |_/ \_| \_/  \____/ \_|  |_/ \_| |_/ \_| \_/""")

def displayGame(alert=""):
    addSpace()
    displayTitle()
    displayHangman()
    if alert != "":
        print(alert)
    print(display_word(letters))

def displayHangman():
    print(hangman[score])

def displayWin(alert=""):
        addSpace()
        displayTitle()
        displayHangman()
        if alert != "":
            print(alert)
        print(f"{word}: correct guess\nCongratulations !")

def displayLose(alert=""):
        addSpace()
        displayTitle()
        displayHangman()
        if alert != "":
            print(alert)
        print(f"Sorry, you've exhausted all your attempts. The word was : {word}")
    
letterUsed = []
displayGame()
while score < 9:
    playerInput = input("Enter a letter:")
    alert = ""
    if len(playerInput)==1:
        if playerInput in letterUsed:
            alert = f"letter '{playerInput}' already used"
            displayGame(alert)
        else:
            letterUsed.append(playerInput)
            letterFound = False
            findCount = 0
            for i, (caractere, truth) in enumerate(letters):
                if caractere == playerInput and not truth:
                    letters[i] = (caractere, True)
                    findCount +=1
                    letterFound = True

            if letterFound:
                alert = f"Found {numbers[findCount]} '{playerInput}'"
            else:
                score += 1
                alert =f"No '{playerInput}' found"
    else:
        if playerInput == word:
            displayWin(alert)
            break
        else:
            score += 1
            alert =f"{playerInput}: incorrect guess"

    currentWord = display_word(letters)

    if "_" not in currentWord:
        displayWin(alert)
        break
    else:
        displayGame(alert)
         
if score == 9:
    displayLose(alert)