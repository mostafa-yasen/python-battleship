from http import HTTPStatus

from flask import Flask, jsonify, request
from battleship.models.game import Game

from battleship.exceptions import InvalidShipsCount, ShipOverflowError, ShipOverlapingError

from traceback import print_exc

app = Flask(__name__)
GAME = None

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    body = request.json

    try:
        GAME = Game(body.get("ships"))

    except InvalidShipsCount as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.EXPECTATION_FAILED

    except ShipOverflowError as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.EXPECTATION_FAILED

    except ShipOverlapingError as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.EXPECTATION_FAILED
    except Exception as e:
        print_exc()
        return jsonify({"message": e.get("msg")}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({"message": "Game created successfully"}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED
