import pygame
pygame.init()

display = pygame.display.set_mode((500,700))
pygame.draw.circle(display,"red", [250, 300], 100)
pygame.display.update()
pygame.draw.circle(display, "green", [250, 175], 50)
pygame.display.update()
pygame.draw.circle(display, "blue", [250, 100], 25)
pygame.display.update()

running = True
while running: 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
     

pygame.quit()