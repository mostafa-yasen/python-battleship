
class Game():
    def __init__(self, ships: list, board_size: int = 10) -> None:
        self.ships = ships
        self.board_size = board_size


    def get_game_status(self) -> str:
        pass


    def hit(self, piece) -> object:
        pass


    def delete(self) -> bool:
        pass
