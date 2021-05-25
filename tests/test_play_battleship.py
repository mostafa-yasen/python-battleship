import unittest
from battleship import api


PERFECT_SHIPS_SAMPLE = {
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

class TestPlayBattleship(unittest.TestCase):
    shot_misses_ship_sample = {"x": 4, "y": 8}
    shot_hits_ship_sample = {"x": 3, "y": 5}
    can_sink_a_ship_sample = [
        {"x": 7, "y": 4},
        {"x": 7, "y": 5},
        {"x": 7, "y": 6}
    ]
    hitting_a_sinked_ship_sample = {"x": 7, "y": 6}
    out_of_bounds_shot_sample = {"x": 10, "y": 7}


    @classmethod
    def setUp(cls):
        cls._client = api.app.test_client(cls)
        cls._client.post("/battleship", json=PERFECT_SHIPS_SAMPLE)


    def test_shot_misses_ship(self):
        response = self._client.put("/battleship", json=self.shot_misses_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json["result"], "WATER")


    def test_shot_hits_ship(self):
        response = self._client.put("/battleship", json=self.shot_hits_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json["result"], "HIT")


    def test_can_sink_a_ship(self):
        response = None
        for row in self.can_sink_a_ship_sample:
            response = self._client.put("/battleship", json=row)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], "SINK")


    def test_hitting_a_sinked_ship(self):
        response = self._client.put("/battleship", json=self.hitting_a_sinked_ship_sample)
        response = self._client.put("/battleship", json=self.hitting_a_sinked_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json["result"], "HIT")


    def test_out_of_bounds_shot(self):
        response = self._client.put("/battleship", json=self.out_of_bounds_shot_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 400)
        self.assertEqual(response.status.upper(), "400 BAD REQUEST")

