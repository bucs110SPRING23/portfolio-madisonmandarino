import random
import pygame
import math
 
pygame.init()
screen = pygame.display.set_mode((400,400))
screen_size = pygame.display.get_window_size()
width = screen_size[0]
height = screen_size[1]
center = [width/2, height/2]
screen.fill('navy')

rectange_one = pygame.draw.rect(screen,"orange",[110,0,50,50])
rectangle_two = pygame.draw.rect(screen, "purple",[290,0,50,50])

placing_bet = None
while placing_bet is None:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            break
        elif event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
        elif rectangle_one.collidepoint(mouse_pos):
            font = pygame.font.Font(None, 45)
            place_bet1 = font.render("Bet on Player 1", True, "white")
            screen.blit(place_bet1, (110,0))
            placed_bet = 1
            pygame.display.flip()
            pygame.time.wait(5000)
            placing_bet = False
            break
        elif rectangle_two.collidepoint(mouse_pos):
            font = pygame.font.Font(None, 45)
            place_bet2 = font.render("Bet on Player 2", True, "white")
            placed_bet = 2
            screen.blit(place_bet2, (290,0))
            pygame.display.flip()
            pygame.time.wait(5000)
            placing_bet = False
            break

    
player1_hit = ("orange")
player1_miss = ("yellow")
player2_hit = ("purple")
player2_miss = ("pink")

board = (width/2, height/2)
board = pygame.draw.circle(screen, "white", [width/2, height/2])


num_rounds = 10

for i in range(num_rounds):
    dart_1x = random.randrange(0, width/2)
    dart_2x = random.randrange(0, width/2)
    dart_1y = random.randrange(0, height/2)
    dart_2y = random.randrange(0, height/2)
    distance_from_center1 = math.hypot(center[0] -dart_1x, center[1]-dart_1y)
    distance_from_center2 = math.hypot(center[0] -dart_2x, center[1]-dart_2y)
    is_on_board1 = distance_from_center1 <= width / 2
    is_on_board2 = distance_from_center2 <= width / 2

    if is_on_board1 :
        pygame.draw.circle(screen, player1_hit, (dart_1x, dart_1y), 7)
        player1_score +=1
    else: 
        pygame.draw.circle(screen, player1_miss, (dart_1x, dart_1y), 7)

    if is_on_board2:
        pygame.draw.circle(screen, player2_hit, (dart_2x, dart_2y), 7)
        player2_score +=1
    else:
        pygame.draw.circle(screen, player2_miss (dart_2x, dart_2y), 7)
    

    if player1_score > player2_score:
        font=pygame.font.Font(None, 40)
        text= font.render("PLAYER 1 HAS WON", True,"black")
        screen.blit(text, (50,200))
        if placed_bet == 1:
            font = pygame.font.Font(None, 40)
            text = font.render("YOU PLACED A CORRECT BET", True, "black")
            screen.blit(text, (50, 200))
        else: 
            font = pygame.font.Font(None, 40)
            text = font.render("YOU PLACED THE WRONG BET", True, "red")
            screen.blit(text, (50, 200))
    
    elif player1_score < player2_score:
        font=pygame.font.Font(None, 40)
        text= font.render("PLAYER 2 HAS WON", True,"black")
        screen.blit(text, (50,200))
        if placed_bet == 2:
            font = pygame.font.Font(None, 40)
            text = font.render("YOU PLACED A CORRECT BET", True, "black")
            screen.blit(text, (50, 200))
        else: 
            font = pygame.font.Font(None, 40)
            text = font.render("YOU PLACED THE WRONG BET", True, "red")
            screen.blit(text, (50, 200))

pygame.display.flip()
pygame.time.wait(2000)
    





