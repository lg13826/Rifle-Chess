#!/usr/bin/env python3
import pygame
import board
from pygame.locals import *

class Game:

    def __init__(self):
        pygame.init()
        self._color = pygame.Color(255,255,0)
        self._height = 800
        self._width = 800
        self._square = []
        self._pieces = []
        self._displaysurface = pygame.display.set_mode((self._width, self._height))
        #load images
        self._rookimg = pygame.image.load('images/bR.svg').convert_alpha()
        self._pawnimg = pygame.image.load('images/bP.svg').convert_alpha()
        self._kingimg = pygame.image.load('images/bK.svg').convert_alpha()
        self._knightimg = pygame.image.load('images/bN.svg').convert_alpha()
        self._queenimg = pygame.image.load('images/bQ.svg').convert_alpha()
        self._bishopimg = pygame.image.load('images/bB.svg').convert_alpha()

    def draw_board(self):
        row_pixel = 0
        column_pixel = 0
        swap_color = False
        for i in range(64):
            self._square.append(pygame.Rect(row_pixel, column_pixel, self._width//8, self._height//8))
            pygame.draw.rect(self._displaysurface, self._color, self._square[i])
            
            if (row_pixel > self._width - 101):
                column_pixel += self._height//8
                row_pixel = 0
                continue;
            else:
                row_pixel += self._width//8
            if swap_color == 0:
                self._color.g = self._color.g - 40
                swap_color = True
            else: 
                self._color.g = self._color.g + 40
                swap_color = False
        pygame.display.flip()
        pygame.display.set_caption("Rifle Chess")

    def draw_pieces(self):
        # draw pieces here
        rook = self._rookimg.get_rect()
        knight = self._knightimg.get_rect()
        queen = self._queenimg.get_rect()
        king = self._kingimg.get_rect()
        bishop = self._bishopimg.get_rect()
        pawn = self._pawnimg.get_rect()
        curr_board = board.Board()
        for i in range(64):
            if (curr_board.square_index(i) != None):
                if (curr_board.square_index(i) == 'k'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._kingimg, king)
                if (curr_board.square_index(i) == 'q'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._queenimg, queen)
                if (curr_board.square_index(i) == 'r'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._rookimg, rook)
                if (curr_board.square_index(i) == 'n'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._knightimg, knight)
                if (curr_board.square_index(i) == 'p'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._pawnimg, pawn)
                if (curr_board.square_index(i) == 'b'):
                    king.fit(self._square[i])
                    self._displaysurface.blit(self._bishopimg, bishop)


if __name__ == '__main__':
    g = Game()
    g.draw_board()
    g.draw_pieces()
    while True:
        pass