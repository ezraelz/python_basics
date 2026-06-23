import pygame as pyg
pyg.init()

win = pyg.display.set_mode((500, 500))

pyg.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

running = True
while running:
    pyg.time.delay(100)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    keys = pyg.key.get_pressed()
    if keys[pyg.K_LEFT]:
        x -= vel
        
    if keys[pyg.K_RIGHT]:
        x += vel
    if keys[pyg.K_UP]:
        y -= vel
    if keys[pyg.K_DOWN]:
        y += vel
        
    win.fill((0, 0, 0))
    pyg.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pyg.display.update()

pyg.quit()
