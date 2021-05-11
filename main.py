import pygame
import sys
from game import Game

#init new Game
blockSize = 8 #Set the size of the grid block
g1 = Game(number_of_blops=2000, blocksize=blockSize)

pygame.init()
WIDTH = blockSize * 100
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A simulation")
background_color = pygame.Color("White")
clock = pygame.time.Clock()

running = True

def drawGrid():

    for x in range(WIDTH//blockSize):
        for y in range(WIDTH//blockSize):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(WIN, (0,0,0), rect, 1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    WIN.fill(background_color)
    drawGrid()
    g1.collsion()
    for blop in g1.blopsGreen:
        pygame.draw.rect(WIN, blop.color, (blop.position.get('x'), blop.position.get('y'), blockSize, blockSize))
        blop.move(WIDTH,WIDTH)
    for blop in g1.blopsRed:
        pygame.draw.rect(WIN, blop.color, (blop.position.get('x'), blop.position.get('y'), blockSize, blockSize))
        blop.move(WIDTH,WIDTH)

    pygame.display.update()

