import pygame

# Initalize the pygame

pygame.init()

# creating the screen
screen = pygame.display.set_mode((1200, 900))

# title and icon
pygame.display.set_caption("Mega Destroyers")
icon = pygame.image.load('pikachu.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('superhero.png')
playerImg = pygame.transform.scale(playerImg, (32, 32))
playerX = 100
playerY = 800

def player():
    screen.blit(playerImg, (playerX, playerY))

# game loop
running = True
while running:

    # RGB
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    player()
    pygame.display.update()

# <div>Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>