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
curIndex = 0

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


# Sprite
# sans 
SpriteSans = [pygame.image.load(f"assets\\sans\\{index}.gif") for index in range(0, 13)]
# sans dance
SpriteSansDance = [pygame.image.load(f"assets\\sans-dance\\{index}.gif") for index in range(0, 14)]
# sans shrug
SpriteSansShrug = [pygame.image.load(f"assets\\sans-shrug\\{index}.gif") for index in range(0, 13)]


# cursor
# Chargez l'image du curseur personnalisé et redimensionnez-la
new_cursor = pygame.image.load(Pathcursor)
new_cursor = pygame.transform.scale(new_cursor, (35, 35))

# Cachez le curseur par défaut de la souris
pygame.mouse.set_visible(False)

# Créez une surface pour afficher le curseur personnalisé
cursor_surface = pygame.Surface((35, 35), pygame.SRCALPHA)
cursor_surface.blit(new_cursor, (0, 0))


letterUsed = []
alert = "Enter a Letter :"

a = 100
b = 100
amount = .25

score = 10

music = pygame.mixer.music.load(PathMusic)
pygame.mixer.music.play(-1)
pygame.mixer.Sound.play(pygame.mixer.Sound(PathStartSFX))

win = False
lose = False

# assets\\sans\\
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == CHANGE_IMAGE_EVENT:
            curIndex = (curIndex + 1) % len(SpriteSans)  # Passer à l'image suivante, revenir à 0 si la limite est atteinte

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
                    # displayWin(alert)
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathWinSFX))

                    # heart = pygame.image.load("assets\\heart.png")
                    # root.blit(heart, (100, 100))
                    win = True

                    break

            if score == 0:
                pygame.mixer.Sound.play(pygame.mixer.Sound(PathLoseSFX))
                lose = True


        # Sans
        # Contrôlez la visibilité des images
        ShowCorrectFrame(SpriteSans,curIndex)
        root.fill((0, 0, 0))
        root.blit(SpriteSans[curIndex], (465, 90))
        pygame.display.flip()

        # Title
        PLAY_TEXT = get_font(45).render("HANGMAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 40))
        root.blit(PLAY_TEXT, PLAY_RECT)

        if win :
            PLAY_TEXT = get_font(25).render("Vivtory !", True, "orange")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 570))
            root.blit(PLAY_TEXT, PLAY_RECT)
        elif lose :
            PLAY_TEXT = get_font(25).render("You Lose !", True, "red")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 570))
            root.blit(PLAY_TEXT, PLAY_RECT)
        else:
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


        # Obtenez la position de la souris
        pos = pygame.mouse.get_pos()

        # Affichez le curseur personnalisé à la position de la souris
        root.blit(cursor_surface, pos)
        pygame.display.flip()

        # TV
        bg = pygame.image.load(PathOldTV)
        bg = pygame.transform.scale(bg, (1280, 720))
        root.blit(bg, (0, 0))


    pygame.display.flip()