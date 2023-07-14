import unittest
import polygon
import drawing_board

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.p = polygon.RandomPolygon(drawing_board.DrawingBoard(), 3)

    def test_distance(self):
        self.assertEqual(self.p.distance((0, 0), (5, 0)), 5)
        self.assertEqual(self.p.distance((1, 0), (1, 4)), 4)
        self.assertEqual(self.p.distance((1, 1), (4, 5)), 5)

    def test_nearest_neighbor(self):
        self.assertEqual(self.p.get_nearest_neighbor((0, 0), {(1, 1), (2, 2)}), (1, 1))


if __name__ == '__main__':
    unittest.main()