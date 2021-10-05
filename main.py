import pygame
import random

# Initalize the pygame

pygame.init()

# creating the screen
screen = pygame.display.set_mode((1200, 900))

# background
background = pygame.image.load('2440.jpg')
background = pygame.transform.scale(background, (1200, 900))

# title and icon
pygame.display.set_caption("Mega Destroyers")
icon = pygame.image.load('pikachu.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('superhero.png')
playerImg = pygame.transform.scale(playerImg, (32, 32))
playerX = 100
playerY = 800
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = pygame.image.load('predator-head.png')
enemyImg = pygame.transform.scale(enemyImg, (32, 32))
enemyX = random.randint(0, 1168)
enemyY = random.randint(50, 200)
enemyX_change = 0
enemyY_change = 0

# laser
laserImg = pygame.image.load('laser.png')
laserImg = pygame.transform.scale(laserImg, (32, 32))
laserX = playerX
laserY = playerY
laserX_change = 1
laserY_change = 0
# ready not visable fire, laser in motion
laser_state = "ready"

# player on screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# enemy on screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_laser (x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))


# game loop
running = True
while running:

    # RGB
    screen.fill((255, 0, 0))
    # background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke
        if event.type == pygame.KEYDOWN:
            print('Keystroke pressed')
            if event.key == pygame.K_LEFT:
                playerX_change = -.4
                enemyX_change = -.5

            if event.key == pygame.K_RIGHT:
                playerX_change = .4
                enemyX_change = .5

            if event.key == pygame.K_UP:
                playerY_change = -.4
                enemyY_change = -.5

            if event.key == pygame.K_DOWN:
                playerY_change = .4
                enemyY_change = .5

            if event.key == pygame.K_SPACE:
                fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print('Left')
            if event.key == pygame.K_RIGHT:
                print('Right')
            if event.key == pygame.K_UP:
                print('Up')
            if event.key == pygame.K_DOWN:
                print('Down')

    # players movement
    playerY += playerY_change
    playerX += playerX_change

    # enemy movement
    enemyX += enemyX_change
    enemyY += enemyY_change
    enemyX += random.randint(-5, 5)
    enemyY += random.randint(-5, 5)

    # laser movement
    if laser_state == "ready":
        laserX = playerX
        laserY = playerY

    if laser_state == "fire":
        fire_laser(laserX, laserY)
        laserX += laserX_change

    # X boundaries for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1168:
        playerX = 1168

    # Y boundaries for player
    if playerY <= 0:
        playerY = 0
    elif playerY >= 868:
        playerY = 868

    # X boundaries for enemy
    if enemyX <= 0:
        enemyX = 0
    elif enemyX >= 1168:
        enemyX = 1168

    # Y boundaries for enemy
    if enemyY <= 0:
        enemyY = 0
    elif enemyY >= 868:
        enemyY = 868



    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# <div>Icons made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# <a href='https://www.freepik.com/vectors/business'>Business vector created by vectorpocket - www.freepik.com</a>
# <a href='https://www.freepik.com/vectors/car'>Car vector created by upklyak - www.freepik.com</a>
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>