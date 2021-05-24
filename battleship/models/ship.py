from .point import Point
from uuid import uuid1


class Ship():
    def __init__(self, point: Point, direction: str, size: int = 1, id: str = "") -> None:
        self.point = point
        self.direction = direction
        self.size = size
        self.id = id or uuid1().hex[:6]


    def get_ship(self):
        """yields a list of coordinates of this ship"""
        if self.direction.upper() == "V":
            for i in range(0, self.size):
                yield (self.point.x, self.point.y + i)
        else:
            for i in range(0, self.size):
                yield (self.point.x + i, self.point.y)


    def __eq__(self, o: object) -> bool:
        return self.id == o.id


    def serialize(self):
        return {
            "id": self.id,
            "direction": self.direction,
            "size": self.size,
            "point": self.point.serialize()
        }