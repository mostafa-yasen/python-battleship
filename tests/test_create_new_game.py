import unittest
from battleship import api


class TestCreateNewGame(unittest.TestCase):
    ships_outside_sample = {
        "ships": [
            {
                "x": 8,
                "y": 1,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }
    perfect_sample = {
        "ships": [
            {
                "x": 2,
                "y": 1,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }
    ships_overlap_sample = {
        "ships": [
            {
                "x": 5,
                "y": 5,
                "size": 4,
                "direction": "H"
            },
            {
                "x": 7,
                "y": 4,
                "size": 3,
                "direction": "V"
            },
            {
                "x": 3,
                "y": 5,
                "size": 2,
                "direction": "V"
            },
            {
                "x": 6,
                "y": 8,
                "size": 1,
                "direction": "H"
            }
        ]
    }
    def test_empty_ships(self):
        client = api.app.test_client(self)
        response = client.post("/battleship", json={"ships": []})
        status_code = response.status_code
        self.assertEqual(status_code, 400)


    def test_create_game(self):
        client = api.app.test_client(self)
        response = client.post("/battleship", json=self.perfect_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    def test_ships_outside(self):
        client = api.app.test_client(self)
        response = client.post("/battleship", json=self.ships_outside_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 400)

    def test_ships_overlap(self):
        client = api.app.test_client(self)
        response = client.post("/battleship", json=self.ships_overlap_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 400)


if __name__=="__main__":
    unittest.main()
