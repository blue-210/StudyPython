import sys
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

        # 赤 矩形塗りつぶし
        pygame.draw.rect(SURFACE, (255,0,0), (100,100,50,50),3)

        # Rectオブジェクト
        rect1 = Rect(200,60,140,80)
        pygame.draw.rect(SURFACE, (255,0,0), rect1)

        #円を描く
        pygame.draw.circle(SURFACE, (0,255,0), (250,150), 30, 10)

        # 楕円を描く
        pygame.draw.ellipse(SURFACE,(0,0,255), (250,30,90,90))

        # 線を描く
        pygame.draw.line(SURFACE, (10,250,250), (10,80),(200,80))

        # 格子を描く
        for xpos in range(0,400,25):
            pygame.draw.line(SURFACE, 0xFFFFF, (xpos, 0), (xpos,300))
        
        for ypos in range(0,300,25):
            pygame.draw.line(SURFACE, 0xFFFFF, (0,ypos), (400,ypos))


        """
        counter += 1
        SURFACE.fill((0,0,0))
        count_image = sysfont.render(
            "count is {}".format(counter), True, (225,225,225))
        SURFACE.blit(count_image, (50,50))
        """
        pygame.display.update()
        FPSCLOCK.tick(5)

if __name__ == '__main__':
    main()