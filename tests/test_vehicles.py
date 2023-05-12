import unittest

from entities.vehicles import Truck, Car, Scooter


class TestVehicles(unittest.TestCase):
    def test_case_truck(self):
        t = Truck(120)
        t.park(1, "2023-05-10 13:06:42.195002")
        et = t.unpark("001", "2023-05-10 19:58:10.224214")
        self.assertEqual(len(et), 3)

    def test_case_car(self):
        c = Car(34)
        c.park(2, "2023-05-10 13:54:15.200891")
        et = c.unpark("02", "2023-05-10 19:58:10.224214")
        self.assertEqual(len(et), 3)

    def test_case_scooter(self):
        s = Scooter(45)
        s.park(2, "2023-05-10 13:54:15.200891")
        et = s.unpark("02", "2023-05-10 19:58:10.224214")
        self.assertEqual(len(et), 3)