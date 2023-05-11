SCOOTER = 'scooter'
TRUCK = 'truck'
CAR = 'car'


class MallFee:
    SCOOTER_FEE = 10
    CAR_FEE = 20
    TRUCK_FEE = 50


class AirportFee:
    def get_scooter_fee(self, et):
        if 0 <= et < 1:
            return 0
        elif 1 <= et < 8:
            return