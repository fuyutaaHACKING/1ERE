import pygame, sys
from button import Button

pygame.init()
pygame.mixer.init()

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

clock = pygame.time.Clock()
FPS = 60

SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Mettaton's Quizz")

BG = pygame.image.load("assets/sprites/mettatonBg1.png")
BG = pygame.transform.scale(BG, (1280, 720))

all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
                                     # <-- empty line for readabelity
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/sprites/frisk.png").convert_alpha()
        #self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        #self.image = pygame.transform.scale(self.image, (int(self.rect.width/2), int(self.rect.height/2)))
        self.speed_x = 0

        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        #self.rect = pygame.Rect(self.x, self.y, 32, 32)
        #self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def update(self):
        self.rect.x += self.speed_x
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
display_rect = display.get_rect()

player = Player(0, 0)

player.rect.center = display_rect.center
player.speed_x = 0

all_sprites.add(player)

trueLabBackground = pygame.image.load("assets/sprites/trueLab.png").convert()
trueLabBackground = pygame.transform.scale(trueLabBackground, (DISPLAY_WIDTH, DISPLAY_HEIGHT))

# - other -

pygame.mixer.music.load("assets/OST/here-we-are.mp3")
pygame.mixer.music.play(-1)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/fixedsys-monospaced.ttf", size)

def play():
    while True:
        player.update()
        all_sprites.update()

        # - draws (without updates) -

        display.blit(trueLabBackground, (0, 0))

        all_sprites.draw(display)
        
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Mettaton's Quizz Show!", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(250, 675), 
                            text_input="[return to main menu]", font=get_font(20), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    mainMenu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("IMPORT DECKS MENU", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    mainMenu()

        pygame.display.update()

def mainMenu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("METTATON's QUIZ!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        buttonRect = pygame.image.load("assets/sprites/buttonRect.png")
        buttonRect = pygame.transform.scale(buttonRect, (250, 50))

        #SUDDEN_CHANGE_SANS = pygame.sprite.Sprite(image=SUDDEN_CHANGE_SANS_SPRITE, pos=(0, 0))

        PLAY_BUTTON = Button(image=buttonRect, pos=(300, 300), 
                            text_input="Play", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=buttonRect, pos=(900, 300), 
                            text_input="Decks", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=buttonRect, pos=(640, 550),
                            text_input="Exit", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

mainMenu()