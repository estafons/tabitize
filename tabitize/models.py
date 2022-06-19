from enum import Enum


class Octave(str, Enum):
    """Octave Enum"""
    one = 'one'
    two = 'two'
    three = 'three'
    four = 'four'
    five = 'five'
    six = 'six'
    seven = 'seven'

class Pitch(str, Enum):
    """Note Definition"""
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    A = 'A'
    B = 'B'

class Accidental(str, Enum):
    """notes Accidental.(sharp, flat)"""
    sharp = 'sharp'
    flat = 'flat'
    perfect = 'perfect'

class TimeVal(str, Enum):
    pass