import pygame
from constants import *
from gameboard import Gameboard
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(LIGHT)
board = Gameboard(screen)
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    board.draw_board()
    board.draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.check_events()
    board.check_status()




    pygame.display.flip()
