
class InvalidShipsCount(Exception):
    msg = "Ships list must be more than 0"


class ShipOverlapingError(Exception):
    msg = "Can not create game, there is a ship overlap"


class ShipOverflowError(Exception):
    msg = "Can not create game, there is a ship place outside the board"


class InvalidHitError(Exception):
    msg = "Can not hit this point, it's outside the board"
