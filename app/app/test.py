"""
Sample Test """

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test Calc modulde"""
    def test_add_module(self):
        """Adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_module(self):
        """Subtracting numbers together"""
        res = calc.subtract(7, 6)
        self.assertEqual(res, 1)
