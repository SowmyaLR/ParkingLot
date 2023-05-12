import unittest, os

from service.parkinglot_service import ParkingLotService


class TestParkinglotService(unittest.TestCase):
    def test_case1(self):
        file_path = "/".join(os.path.dirname(__file__).split("/")[:-1])
        ps = ParkingLotService()
        ps.calculate_bill(f"{file_path}/inputs/case1")

    def test_case2(self):
        file_path = "/".join(os.path.dirname(__file__).split("/")[:-1])
        ps = ParkingLotService()
        ps.calculate_bill(f"{file_path}/inputs/case2")

    def test_case3(self):
        file_path = "/".join(os.path.dirname(__file__).split("/")[:-1])
        ps = ParkingLotService()
        print(file_path)
        ps.calculate_bill(f"{file_path}/inputs/case3")