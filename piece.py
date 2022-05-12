
class GamePiece:
    def __init__(self):
        self._colors = ["White" , "Black"]
        self._type = ["King", "Pawn", "Knight", "Bishop", "Rook", "Queen"]
        self._pieces = {x: self._colors for x in self._type for _ in self._colors}

    def return_pieces(self):
        return self._pieces
    