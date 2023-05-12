from service.parkinglot_service import ParkingLotService
import sys


def main():
    input_file = sys.argv[1]
    parking_srv = ParkingLotService()
    parking_srv.calculate_bill(input_file)


if __name__ == "__main__":
    main()
