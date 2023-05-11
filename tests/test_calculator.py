import unittest

from entities.calculator import MallCalculator


class TestCalculator(unittest.TestCase):
    def test_mall_calculator(self):
        mc = MallCalculator()
        mc.set_capacity("scooter", 20)
        mc.set_capacity("truck", 3)
        mc.set_capacity("car", 30)
        mc.park("scooter", "2023-05-10 13:06:42.195002")
        mc.park("car", "2023-05-10 14:06:42.195002")
        mc.park("truck", "2023-05-10 13:06:42.195002")

        self.assertEqual(mc.unpark("scooter", "01", "2023-05-10 18:06:42.195002"), 50)
        self.assertEqual(mc.unpark("car", "02", "2023-05-10 18:06:42.195002"), 80)
        self.assertEqual(mc.unpark("truck", "3", "2023-05-10 18:06:42.195002"), 250)