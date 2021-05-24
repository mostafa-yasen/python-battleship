from datetime import timedelta
from battleship.models.point import Point
from http import HTTPStatus

from flask import Flask, jsonify, request, session
from battleship.models.game import Game

from battleship.exceptions import InvalidHitError, InvalidShipsCount, ShipOverflowError, ShipOverlapingError

from traceback import print_exc

from uuid import uuid4

app = Flask(__name__)
app.secret_key = str(uuid4())

GAME = None

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    body = request.json

    try:
        # BUG: should be stored in the session storage or a sqlite database 
        session["GAME"] = Game(body.get("ships")).serialize()

    except InvalidShipsCount as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.BAD_REQUEST

    except ShipOverflowError as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.BAD_REQUEST

    except ShipOverlapingError as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({"message": "Game created successfully"}), HTTPStatus.OK


@app.route('/battleship', methods=['PUT'])
def shot():
    if not session.get("GAME"):
        return jsonify({"message": "Please, create a game first"}), HTTPStatus.EXPECTATION_FAILED

    body = request.json
    if not (body.get("x") and body.get("y")):
        return jsonify({"message": "Invalid coordinate"}), HTTPStatus.BAD_REQUEST

    try:
        game, result = Game(**session["GAME"]).hit(Point(body.get("x"), body.get("y")))
        session["GAME"] = game.serialize()

    except InvalidHitError as e:
        print_exc()
        return jsonify({"message": e.msg}), HTTPStatus.BAD_REQUEST

    except Exception as e:
        print_exc()
        return jsonify({"message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({"result": result}), HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    session.clear()
    return jsonify({}), HTTPStatus.OK


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=1)
