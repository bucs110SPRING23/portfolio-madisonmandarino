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
    
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 0.5, height * 0.5))
    max_so_far = 0
    max_num = 0
    for (p,z) in threenplus1_iters_dict:
        if z > max_so_far:
            max_so_far = z
            max_num = p
    font = pygame.font.Font(None, 35)
    msg = font.render(f"{max_num} is the max so far", True, "pink")
    window.blit(new_display, (0,0))
    window.blit(msg, (100,100))
    pygame.display.flip()
    pygame.time.wait(1000)

def main():
    upper_limit = 50
    output = threenp1range(upper_limit)
    graph_coordinates(output)
    pygame.display.flip()
    pygame.time.wait(3000)

main()