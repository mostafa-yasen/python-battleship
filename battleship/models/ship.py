from .point import Point

class Ship():
    def __init__(self, point: Point, direction: str, size: int = 1) -> None:
        self.point = point
        self.direction = direction
        self.size = size


    def get_ship(self):
        """yields a list of coordinates of this ship"""
        if self.direction.upper() == "V":
            for i in range(0, self.size):
                yield (self.point.x, self.point.y + i) 
        else:
            for i in range(0, self.size):
                yield (self.point.x + i, self.point.y)
