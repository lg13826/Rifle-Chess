import pygame
from pygame.locals import *
 

class Game:
    
    def __init__(self):
        pygame.init()
        vec = pygame.math.Vector2  # 2 for two dimensional
        self._height = 800
        self._width = 800
        self._square = []
        for i in range(63):
            row_pixel = 0
            column_pixel = 0
            #use rect.draw instead
            self._square.append(pygame.Rect(row_pixel, column_pixel, self._width//8, self._height//8))
            self._square[i].fill
            if (row_pixel > self._width - 1):
                row_pixel += self._width//8
            else: 
                column_pixel += self._height//8
                row_pixel = 0
        
        self._displaysurface = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Rifle Chess")
    
    
    

