import cv2 as cv
import pygame
import numpy as np

class Display:
    def __init__(self, W:int, H:int) -> None:
        pygame.init()
        self.W, self.H = W, H 
        self.window = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption('road')
        

    def draw(self,img:object) -> None:
        img = np.rot90(img)
        surface = pygame.Surface((self.W,self.H))
        pygame.surfarray.blit_array(surface, cv.cvtColor(img, cv.COLOR_GRAY2BGR))
        self.window.blit(surface, (0,0))
        pygame.display.update()

