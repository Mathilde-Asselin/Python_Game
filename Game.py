#Exo de fin -> Simple Space Invader

#First install pip game ->  mettre "pip3 install pygame" ds terminal de Visual

import time

#Petite question avant de démarrer le jeu 
name = input("Nom du Joueur: ")
print(f"Bonjour {name}, tu es ready ?")
time.sleep(2)

print("Gooo !")
time.sleep(1)

#Importons pygame ! 
import pygame

#Verifie si tout les modules sont chargés
module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode((500,500))

#Logo du jeu 
pygame.display.set_caption("Simple Space Invador")
image = pygame.image.load("spaceship.png").convert()
pygame.display.set_icon(image)

print(image)

#Background 
WINDOWWIDTH = 480
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

#1 - Initialisation de notre jeu

class SpaceVender:
    ennemies = []
    tirs = []
    lost = False

    # Tout comme l'exo de la class player on utilise def init !
    # On definit une hauteur, une largeur pour notre écran et une durée pour notre jeu
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False

        vaisseau = Vaisseau(self, width / 2, height - 20)
        generateur = Generateur(self)
        tir = None

        #On génère des fonctions pour le background
        background = pygame.image.load('background.jpeg').convert()
        background_rect = background.get_rect()

        #On ajoute la musique !
        #Petit Star Wars pour être dans le thème
        file = 'music.mp3'

        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.


        while not done:
            
            if len(self.ennemies) == 0:
                self.displayText("Bravooo champion !!")

            # Permet de gérer les "mouvements" du vaisseau dont la vitesse 
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  
                vaisseau.x -= 1 if vaisseau.x > 20 else 0  

            elif pressed[pygame.K_RIGHT]:  
                vaisseau.x += 1 if vaisseau.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                # Appuyer sur Spacebar pour tirer 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.tirs.append(Tirs(self, vaisseau.x, vaisseau.y))
                    #time.sleep(0.1)

            pygame.display.flip()

            # Permet de gérer la vitesse de descente
            self.clock.tick(200)

            # On ajoute une image de fond au background 
            DISPLAYSURF.blit(background, background_rect)
            #self.screen.fill((29, 0, 100)) -> Juste couleur de fond ! 

            for ennemie in self.ennemies:
                ennemie.draw()
                
                ennemie.destruction(self)
                if (ennemie.y > height):
                    self.lost = True
                    self.displayText("Retente ta chance !")
            
            if not self.lost: vaisseau.draw()

            for tir in self.tirs:
                tir.draw()
            

    # Pygame Text - font
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 40)
        textsurface = font.render(text, False, (223, 255, 252))
        self.screen.blit(textsurface, (110, 160))

#2 - Création des ennemies

class Ennemie:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 25

    # Pygame Draw - rectangle 
    def draw(self):
        #pygame.draw.circle(self.game.screen, BLUE, (200, 90), 40, 2)
        pygame.draw.rect(self.game.screen,  
                         (55, 104, 167),  
                         pygame.Rect(self.x, self.y, self.size, self.size))

        self.y += 0.1
    
    # Permet la destruction des ennemies
    def destruction(self, game):
        for tir in game.tirs:
            if (tir.x < self.x + self.size and
                    tir.x > self.x - self.size and
                    tir.y < self.y + self.size and
                    tir.y > self.y - self.size):
                game.tirs.remove(tir)
                game.ennemies.remove(self)

#3 - Création du générateur permettant de multiplier les ennemies

class Generateur:

    # Permet de gérer le nombre d'ennemies
    def __init__(self, game):
        margin = 60  
        width = 40  
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.ennemies.append(Ennemie(game, x, y))


#4 - Création du vaisseau

class Vaisseau:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    # Pygame Draw - rectangle
    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (255, 205, 0),
                         pygame.Rect(self.x, self.y, 12, 8))


#5 - Création des tirs

class Tirs:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    # Pygame Draw - rectangle
    def draw(self):
        pygame.draw.rect(self.game.screen,  
                         (0, 255, 243),  
                         pygame.Rect(self.x, self.y, 3, 3))
        self.y -= 1.2


if __name__ == '__main__':
    game = SpaceVender(600, 400)
 
 
 

