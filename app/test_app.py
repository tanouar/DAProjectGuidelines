import unittest
from utils import load_json

class TestApp(unittest.TestCase):
    def test_load_json(self):
        data = load_json("data/resources.json")
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
