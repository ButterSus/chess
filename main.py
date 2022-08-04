import typing
import enum


class Color(enum.Enum):
    White = 0
    Black = 1


class Characters:
    class _Characters(enum.Enum):
        Pawn = 0
        Rook = 1
        Knight = 2
        Bishop = 3
        Queen = 4
        King = 5

    @staticmethod
    def _newClass(character: _Characters):
        class _NewClass:
            type = character
            color: Color

            def __init__(self, color: Color):
                self.color = color

            def move(self, x: int, y: int) -> typing.NewType('isPossibleToMove', bool):
                ...
        return _NewClass

    Pawn = _newClass(_Characters.Pawn)
    Rook = _newClass(_Characters.Rook)
    Knight = _newClass(_Characters.Knight)
    Bishop = _newClass(_Characters.Bishop)
    Queen = _newClass(_Characters.Queen)
    King = _newClass(_Characters.King)



