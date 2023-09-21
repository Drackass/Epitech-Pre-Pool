# Import
import pygame, random

# data
import data as data

# Path
# Font
Pathfont = "assets\\font\\font.ttf"

# Image
PathIcon = 'assets\\heart.png'
Pathcursor = "assets\\cursor.png"
PathOldTV = "assets\\TV.png"

# music & sound
PathMusic = 'assets\\sound\\megalovania.mp3'
PathStartSFX = 'assets\\sound\\snd_levelup.wav'
PathMistakeSFX = 'assets\\sound\\snd_fall2.wav'
PathGoodSFX = 'assets\\sound\\snd_tempbell.wav'
PathBadSFX = 'assets\\sound\\snd_damage_c.wav'
PathWinSFX = 'assets\\sound\\snd_dumbvictory.wav'
PathLoseSFX = 'assets\\sound\\mus_f_newlaugh_low.ogg'

# settings
rootSize = (1280, 720)
rootTitle = "Epitech Pre-Pool - HANGMAN"

# Utils
def display_word(letters): #return the secret word
    displayWord = ""
    for caractere, truth in letters:
        if truth:
            displayWord += caractere
        else:
            displayWord += "_"
    return displayWord

def lerp(a,b,amount): # return the interpolation between two point
    return ((b-a)*amount)+a

def get_font(size): # Returns Press-Start-2P font in the desired size
    return pygame.font.Font(Pathfont, size)

# hides all Frame except the selected one
def ShowCorrectFrame(Sprites,index):
    for i, Frame in enumerate(Sprites):
        if i == index:
            Frame.set_alpha(255)  # Rendre l'image visible
        else:
            Frame.set_alpha(0)  # Rendre l'image invisible

# init
pygame.init()

# start the mixer process
pygame.mixer.init()

# root size
root = pygame.display.set_mode(rootSize)

# root icon
pygame_icon = pygame.image.load(PathIcon)
pygame.display.set_icon(pygame_icon)

# root title
pygame.display.set_caption(rootTitle)

# Event to change the frame
CHANGE_IMAGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_IMAGE_EVENT, 100)

# Sprite
# sans 
SpriteSans = [pygame.image.load(f"assets\\sans\\{index}.gif") for index in range(0, 13)]
# sans dance
SpriteSansDance = [pygame.image.load(f"assets\\sans-dance\\{index}.gif") for index in range(0, 14)]
# sans shrug
SpriteSansShrug = [pygame.image.load(f"assets\\sans-shrug\\{index}.gif") for index in range(0, 13)]

music = pygame.mixer.music.load(PathMusic)
pygame.mixer.music.play(-1)
pygame.mixer.Sound.play(pygame.mixer.Sound(PathStartSFX))

def win(word):
    curIndex = 0

    while True:
        root.fill("black")

        # Title
        PLAY_TEXT = get_font(45).render("HANGMAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 40))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # Sprite
        ShowCorrectFrame(SpriteSansDance,curIndex)
        root.blit(SpriteSansDance[curIndex], (390, 50))

        PLAY_TEXT = get_font(25).render("Vivtory!", True, "orange")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 600))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # Letter
        PLAY_TEXT = get_font(70).render(word, True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 670))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # TV
        bg = pygame.image.load(PathOldTV)
        bg = pygame.transform.scale(bg, (1280, 720))
        root.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSansDance)
            elif event.type == pygame.KEYDOWN:
                main() 

        pygame.display.update()

def lose(word):
    curIndex = 0

    while True:
        root.fill("black")

        # Title
        PLAY_TEXT = get_font(45).render("HANGMAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 40))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # Sprite
        ShowCorrectFrame(SpriteSansShrug,curIndex)
        root.blit(SpriteSansShrug[curIndex], (385, 70))

        PLAY_TEXT = get_font(25).render("you lose, the word was:", True, "red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 600))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # Letter
        PLAY_TEXT = get_font(70).render(word, True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 670))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # TV
        bg = pygame.image.load(PathOldTV)
        bg = pygame.transform.scale(bg, (1280, 720))
        root.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSansShrug)
            elif event.type == pygame.KEYDOWN:
                main() 


        pygame.display.update()

def main():
    # pick random word
    word = data.words[random.randint(0,len(data.words))-1]

    # Create a list of letters
    letters = []
    for letter in word:
        letters.append((letter, False))

    # Show the first and last letters
    letters[0] = (letters[0][0], True)
    letters[-1] = (letters[-1][0], True)

    # show all spaces
    for i, (caractere, truth) in enumerate(letters):
        if caractere == " ":
            letters[i] = (caractere, True)
            
    # lerp init
    a = 0
    b = 100
    amount = .25

    # sprite index init
    curIndex = 0

    # score init
    score = 10

    letterUsed = []
    alert = "Enter a Letter :"

    while True:
        root.fill("black")

        # Title
        PLAY_TEXT = get_font(45).render("HANGMAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 40))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # Sprite
        ShowCorrectFrame(SpriteSans,curIndex)
        root.blit(SpriteSans[curIndex], (465, 90))

        # alert
        PLAY_TEXT = get_font(25).render(alert, True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 570))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # HQ Bar
        b = (score*610)/10
        a = lerp(a,b,amount)
        pygame.draw.rect(root, "red", pygame.Rect(350, 595, 600, 20))
        pygame.draw.rect(root, "green", pygame.Rect(350, 595, a, 20))

        # Letter
        PLAY_TEXT = get_font(70).render(display_word(letters), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 670))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # TV
        bg = pygame.image.load(PathOldTV)
        bg = pygame.transform.scale(bg, (1280, 720))
        root.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()

            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSans)

            elif event.type == pygame.KEYDOWN:
                # Vérifier si une touche de lettre a été appuyée
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    playerInput = chr(event.key)

                    if playerInput in letterUsed:
                        alert = f"letter '{playerInput}' already used"
                        pygame.mixer.Sound.play(pygame.mixer.Sound(PathMistakeSFX))

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
                            alert = f"Found {data.numbers[findCount]} '{playerInput}'"
                            pygame.mixer.Sound.play(pygame.mixer.Sound(PathGoodSFX))   

                        else:
                            score -= 1
                            alert =f"No '{playerInput}' found"     
                            pygame.mixer.Sound.play(pygame.mixer.Sound(PathBadSFX))   
                    currentWord = display_word(letters)

                    if "_" not in currentWord:
                        pygame.mixer.Sound.play(pygame.mixer.Sound(PathWinSFX))
                        win(word)
                        # break

                if score == 0:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathLoseSFX))
                    lose(word)
                
        pygame.display.update()

main()