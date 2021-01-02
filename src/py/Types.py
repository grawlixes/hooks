import enum

class Annotation:
    # match (callable that takes an iterable of integers, and returns a string) -> function that determines whether a row or column matches its annotation
    def __init__(self, match):
        self.match = match

class Hook(enum.Enum):
    TOP_RIGHT = 1
    TOP_LEFT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4
