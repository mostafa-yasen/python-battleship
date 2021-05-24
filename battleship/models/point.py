from uuid import uuid1


class Point():
    def __init__(self, x, y, id: str = "") -> None:
        self.id = id or uuid1().hex[:6]
        self.x = x
        self.y = y


    def __eq__(self, other: object) -> bool:
        return self.id == other.id


    def serialize(self):
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y
        }
