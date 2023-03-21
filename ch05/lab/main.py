import pygame



def threenp1(n):
    count = 0
    while n > 1.0:
        count +=1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2,upper_limit + 1):
        b = threenp1(i)
        objs_in_sequence[i] = b
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    pygame.display.init
    window = pygame.display.set_mode( )
    window.fill("lavender")
    new_display = pygame.transform.flip(window, False, True)
    pygame.draw.lines(window,"black", False threenplus1_iters_dict)
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 0.5, height * 0.5))
    window.blit(new_display, (0,0))

    max_so_far = 0

    
   
font = pygame.font.Font(None, 25)


pygame.display.update()
pygame.time.wait(1000)