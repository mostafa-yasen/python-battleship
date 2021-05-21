
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y
