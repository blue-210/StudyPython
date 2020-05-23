import sys
import random
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    sysfont = pygame.font.SysFont(None, 36)
    counter = 0

    while True:
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()

        SURFACE.fill((0, 0, 0))

        pointList = []
        for _ in range(10):
            xpos = random.randint(0,400)
            ypos = random.randint(0,300)
            pointList.append((xpos, ypos))
        
        pygame.draw.lines(SURFACE, (255,255,255), True, pointList,5)


        pygame.display.update()
        FPSCLOCK.tick(5)

if __name__ == '__main__':
    main()