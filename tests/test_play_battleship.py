import unittest
from battleship import api


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



    def test_shot_misses_ship(self):
        client = api.app.test_client(self)
        response = client.put("/battleship", json=self.shot_misses_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.data["result"], "WATER")


    def test_shot_hits_ship(self):
        client = api.app.test_client(self)
        response = client.put("/battleship", json=self.shot_hits_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.data["result"], "WATER")


    def test_can_sink_a_ship(self):
        client = api.app.test_client(self)
        response = None
        for row in self.can_sink_a_ship_sample:
            response = client.put("/battleship", json=row)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["result"], "SINK")


    def test_hitting_a_sinked_ship(self):
        client = api.app.test_client(self)
        response = client.put("/battleship", json=self.hitting_a_sinked_ship_sample)
        response = client.put("/battleship", json=self.hitting_a_sinked_ship_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.data["result"], "HIT")


    def test_out_of_bounds_shot(self):
        client = api.app.test_client(self)
        response = client.put("/battleship", json=self.out_of_bounds_shot_sample)
        status_code = response.status_code
        self.assertEqual(status_code, 400)
        self.assertEqual(response.status.upper(), "BAD_REQUEST")
