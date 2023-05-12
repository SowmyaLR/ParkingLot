from constants import constants
from entities.calculator import MallCalculator, StadiumCalculator, AirportCalculator


class ParkingLotService:
    def __init__(self):
        self.parking_place = None
        self.obj = {
            constants.MALL: MallCalculator,
            constants.STADIUM: StadiumCalculator,
            constants.AIRPORT: AirportCalculator
        }

    def _set_place(self, line):
        place = line.split(" ")
        self.parking_place = self.obj[place[1]]()

    def _set_capacity(self, line):
        values = line.split(" ")
        self.parking_place.set_capacity(values[1], int(values[2]))

    def _park(self, line):
        values = line.split(" ")
        self.parking_place.park(values[1], values[2] + " " + values[3])

    def _unpark(self, line):
        values = line.split(" ")
        self.parking_place.unpark(values[1], values[2], values[3] + " " + values[4])

    def execute_command(self, line):
        commands = line.split(" ")
        getattr(self, "_%s" % commands[0].lower())(line)

    def calculate_bill(self, file_path):
        with open(file_path, "r") as fp:
            content = fp.read()
        lines = content.split("\n")
        for lin in lines:
            self.execute_command(lin)
