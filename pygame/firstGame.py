import pygame as pyg
import os

pyg.init()

win = pyg.display.set_mode((500, 480))

pyg.display.set_caption("First Game")

BASE_DIR = os.path.dirname(__file__)

def load_img(path):
    return pyg.image.load(os.path.join(BASE_DIR, path))

walkRight = [load_img(f'Game/R{i}.png') for i in range(1, 10)]
walkLeft  = [load_img(f'Game/L{i}.png') for i in range(1, 10)]
bg = load_img('Game/bg.jpg')
char = load_img('Game/standing.png')

clock = pyg.time.Clock()

screenWidth = 500
x = 50
y = 400
width = 40
height = 60
vel = 10

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pyg.display.update()

running = True
while running:
    clock.tick(27)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pyg.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
    if not isJump:
        if keys[pyg.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else: 
            isJump = False
            jumpCount = 10
    
    redrawGameWindow()

pyg.quit()
