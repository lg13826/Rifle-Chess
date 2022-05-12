#!/usr/bin/env python3
from piece import GamePiece

def square_position_equation(row, column, row_length):
    return (column * row_length) + row

class Board:
    game_piece = GamePiece()
    piece = game_piece.return_pieces()
    fen_dict = {
            'k' : piece["King"],
            'p' : piece["Pawn"],
            'n' : piece["Knight"],
            'b' : piece["Bishop"],
            'r' : piece["Rook"],
            'q' : piece["Queen"]
        }

    def __init__(self):
        self._square = [x for x in range(int(64))]
        self._board_dimension = 8

    def squares(self):
        return self._square

    def fen_load(self, fen_string, fen_dict = fen_dict):
        #parse through string
        row = 0
        for i in range(len(fen_string)):
            #check for line break
            if (fen_string[i] == '/'):
                        break;
            #check for number
            if (fen_string[i].isnumeric()):
                
                continue
            #check for letter
            if 
                
            for j in range(self._board_dimension):
                for k in range(self._board_dimension):
                    
                    elif fen_string[i] in fen_dict:
                        if (fen_string[i].isupper()):
                            self._square[square_position_equation(k, j, self._board_dimension)] = fen_dict[fen_string[i]][0]
                            break;
                        else:
                            self._square[square_position_equation(k, j, self._board_dimension)] = fen_dict[fen_string[i]][1]
                            break;

    def board_dimension(self):
        return self._board_dimension

if __name__ == "__main__":
    b = Board()
    b.fen_load("7k/3R")