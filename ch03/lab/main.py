import random
import pygame
import math
 
#Part A
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill('navy')

screen_size = window.get_size()
center = (screen_size[0]/2, screen_size[1]/2)
width_half= screen_size[0]/2
height_half= screen_size[1]/2
width= screen_size[0]
height= screen_size[1]
vline_start = (200,400)
vline_end = (200, 0)
hline_start = (0,200)
hline_end = (400,200)

    
pygame.draw.circle(window,"black", center, height_half)
pygame.draw.circle(window, "pink", center, width_half)
pygame.draw.line(window, "black", vline_start, vline_end)
pygame.draw.line(window, "black", hline_start, hline_end)
pygame.display.flip()
pygame.time.wait(1000)

# PART B - complete part B here
for _ in range(10):
    randomx = random.randrange(1, screen_size[0])
    randomy = random.randrange(1, screen_size[1])
    distance_from_center = math.hypot(randomx -center[0], randomy- center[1])
    is_in_circle= (distance_from_center  <= 400/2)
    if is_in_circle == True:
        pygame.draw.circle(window, "lime", (randomx, randomy),3)
        print("PASSED", distance_from_center)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.wait(1500)
        
    else:
        pygame.draw.circle(window, "yellow",(randomx,randomy), 3)
        pygame.display.flip()
        pygame.display.update()
        pygame.time.wait(1500)
        print("MISSED")

while 1:
    pygame.event.pump()
    "all your code"

    pygame.time.wait(2000)

pygame.quit()