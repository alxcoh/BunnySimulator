'''
Created on Jan 30, 2014

@author: alxcoh
'''
from commonPygame import *

fpsClock=pygame.time.Clock()
FPS=60

loopingGame=True

while loopingGame:
    
    #game loop here
    
    for event in pygame.event.get():
        if event.type == QUIT:
            loopingGame=False
            break
    
    
    screen.blit(background, (0,0))    # (0,0) are the top-left coordinates
    pygame.display.flip()
    pygame.display.update()
    fpsClock.tick(FPS)