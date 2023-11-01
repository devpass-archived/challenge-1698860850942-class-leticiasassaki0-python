import unittest
from main import Circle


class TestCircle(unittest.TestCase):
    def test_calculate_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), 78.54, places=2)

        circle = Circle(8)
        self.assertAlmostEqual(circle.calculate_area(), 201.06, places=2)


if __name__ == '__main__':
    unittest.main()
