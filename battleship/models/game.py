from werkzeug.utils import send_file
from battleship.models.ship import Ship
from battleship.models.point import Point
from battleship.exceptions import InvalidHitError, InvalidShipsCount, ShipOverflowError, ShipOverlapingError


class Game():
    def __init__(self, ships: list, board_size: int = 10) -> None:
        self.board = []
        self.json_ships = ships
        self.board_size = board_size
        self.validate()
        self.setup()


    def setup(self) -> None:
        """Configures the game board and takes each of the ships and places
        them on the board"""
        for _ in range(self.board_size):
            # The board will always be a square.
            self.board.append([None] * self.board_size)

        self.ships = [
            Ship(
                Point(s["x"], s["y"]), s["direction"], s["size"]
            ) for s in self.json_ships
        ]

        for ship in self.ships:
            self.place_on_board(ship)


    def place_on_board(self, ship) -> None:
        """Places the ship coordinates on the board"""
        coordinates = list(ship.get_ship())
        for (x, y) in coordinates:
            if x >= self.board_size or y >= self.board_size\
            or x < 0 or y < 0:
                raise ShipOverflowError

            if self.board[x][y]:
                raise ShipOverlapingError

            self.board[x][y] = ship


    def hit(self, point: Point) -> object:
        """Hit a point on the board
        :returns: `str` represents the hit result
        - HIT: for a valid hit shoot
        - MISS: for invalid one
        - SINK: if it hits the last piece of a ship
        """
        if point.x >= self.board_size or point.y >= self.board_size:
            raise InvalidHitError

        if self.board[point.x][point.y] == False:
            return "HIT"

        elif self.board[point.x][point.y] is not None:
            tmp_ship = self.board[point.x][point.y]
            self.board[point.x][point.y] = False
            for i in range(self.board):
                for j in range(len(self.board[i])):
                    # TODO: enhance the looping here
                    # loopin (x * x) times in the worrest case. 
                    if self.board[i][j] == tmp_ship:
                        return "HIT"
            return "SINK"
        else:
            return "MISS"


    def validate(self) -> None:
        """Validates the ships to be placed properly on board"""
        if not len(self.json_ships):
            raise InvalidShipsCount

        # TODO: validate ship dicts are valid and each one 
        # has `x`, `y`, `size`, `direction`.


    def print_board(self) -> None:
        """prints the current board for debugging"""
        print(" = " * self.board_size)
        for row in self.board:
            print(row)
        print(" = " * self.board_size)
