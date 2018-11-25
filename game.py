import pygame, random, sys, os, time
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
white = (255, 255, 255)
blue = (0, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
BACKGROUNDCOLOR = (50, 50, 50)
FPS = 30
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 12
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 15
count = 3
topScore=0

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # escape quits
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text, font, surface, x, y,Color):
    textobj = font.render(text, 1, Color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def about():
    font = pygame.font.SysFont(None, 60)
    drawText('University Of Sindh Jamshoro', font, windowSurface, (WINDOWWIDTH / 3) - 160, (WINDOWHEIGHT / 3)-130 ,red)
    drawText('University Of Sindh Jamshoro', font, windowSurface, (WINDOWWIDTH / 3) - 158, (WINDOWHEIGHT / 3)-128 ,white)
    drawText('_____________________________', font, windowSurface, (WINDOWWIDTH / 3) - 190, (WINDOWHEIGHT / 3)-117 ,blue)
    font = pygame.font.SysFont(None, 100)
    drawText('SIMPLE CAR  GAME', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3)-15 ,yellow)
    font = pygame.font.SysFont(None, 60)
    drawText('_______________________________', font, windowSurface, (WINDOWWIDTH / 3) - 220, (WINDOWHEIGHT / 3)+15 ,blue)
    font = pygame.font.SysFont(None, 35)
    drawText('Prepared By:', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3)+80 ,white)
    drawText('_______________', font, windowSurface, (WINDOWWIDTH / 3) - 220, (WINDOWHEIGHT / 3)+95 ,blue)
    font = pygame.font.SysFont(None, 70)
    drawText('Muhammad Ismail Soomro', font, windowSurface, (WINDOWWIDTH / 3) - 200, (WINDOWHEIGHT / 3)+160 ,white)
    drawText('(2K18/CSE/74)', font, windowSurface, (WINDOWWIDTH / 3) - 70, (WINDOWHEIGHT / 3)+220 ,white)
    font = pygame.font.SysFont(None, 35)    
    drawText('________________________________________________________', font, windowSurface, (WINDOWWIDTH / 3) - 220, (WINDOWHEIGHT / 3)+270 ,blue)
    font = pygame.font.SysFont(None, 40)
    drawText('Press Esc To Exit Or Any Other Key To Continue', font, windowSurface, (WINDOWWIDTH / 3) - 150, (WINDOWHEIGHT / 3)+340 ,red)
    pygame.display.update()


pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('car race')
pygame.mouse.set_visible(True)

playerImage = pygame.image.load('car1.png')
car3 = pygame.image.load('car3.png')
car4 = pygame.image.load('car4.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('car2.png')
sample = [car3, car4, baddieImage]
wallLeft = pygame.image.load('left.png')
wallRight = pygame.image.load('right.png')

about()

waitForPlayerToPressKey()
zero = 0

while (count > 0):
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0

    while True:
        score += 1

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = 30
            newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                         }
            baddies.append(newBaddie)
            sideLeft = {'rect': pygame.Rect(0, 0, 126, 600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface': pygame.transform.scale(wallLeft, (126, 599)),
                        }
            baddies.append(sideLeft)
            sideRight = {'rect': pygame.Rect(497, 0, 303, 600),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(wallRight, (303, 599)),
                         }
            baddies.append(sideRight)

        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        font = pygame.font.SysFont(None, 38)
        windowSurface.fill(BACKGROUNDCOLOR)
        drawText('Score: %s' % (score), font, windowSurface, 128, 0,yellow)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 128, 21,yellow)
        drawText('Rest Life: %s' % (count), font, windowSurface, 128, 41,yellow)

        windowSurface.blit(playerImage, playerRect)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

    count = count - 1
    time.sleep(1)
    font = pygame.font.SysFont(None, 52)
    if (count == 0):

        drawText('Game Over', font, windowSurface, (WINDOWWIDTH / 3)+40, (WINDOWHEIGHT / 3)+70,red)
        drawText('Press any key to play again.', font, windowSurface, (WINDOWWIDTH /3) - 110, (WINDOWHEIGHT / 3) + 95,white)
        pygame.display.update()
        time.sleep(2)
        waitForPlayerToPressKey()
        count = 3
