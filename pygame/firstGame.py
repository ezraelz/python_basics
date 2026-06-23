import pygame as pyg
pyg.init()

win = pyg.display.set_mode((500, 500))

pyg.display.set_caption("First Game")

screenWidth = 500
x = 50
y = 450
width = 40
height = 60
vel = 15

isJump = False
jumpCount = 10

running = True
while running:
    pyg.time.delay(100)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT] and x > vel:
        x -= vel
    if keys[pyg.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not isJump:
        if keys[pyg.K_UP] and y > vel:
            y -= vel
        if keys[pyg.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pyg.K_SPACE]:
            isJump = True
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

        
    win.fill((0, 0, 0))
    pyg.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pyg.display.update()

pyg.quit()
