import pygame

pygame.init()

screen = pygame.display.set_mode()
screen.fill("red")
pygame.display.flip()
input("Press enter to continue...")
screen.fill("green")
pygame.display.flip