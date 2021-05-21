import unittest
from battleship import api


class TestDeleteBattleship(unittest.TestCase):
    def test_delete_battleship(self):
        client = api.app.test_client(self)
        response = client.delete("/battleship")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
