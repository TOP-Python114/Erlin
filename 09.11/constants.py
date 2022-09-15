from enum import Enum


class Pitch(int, Enum):
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    B = 7

class Octave(int, Enum):
    D_CONTRA = -2
    S_CONTRA = -1
    CONTRA = 0
    GREAT = 1
    SMALL = 2
    LINE_1 = 3
    LINE_2 = 4
    LINE_3 = 5
    LINE_4 = 6
    LINE_5 = 7
    LINE_6 = 8

class Accidental(str, Enum):
    D_SHARP = 'double sharp'
    SHARP = 'sharp'
    NATURAL = 'natural'
    FLAT = 'flat'
    D_FLAT = 'double flat'

class Duration(Enum):
    DOUBLE = 0
    WHOLE = 1
    HALF = 2
    QUARTER = 4
    EIGHTH = 8
    SIXTEENTH = 16
    THIRTY_SECOND = 32
    SIXTY_FOURTH = 64
    HUNDRED_TWENTY_EIGHTH = 128
