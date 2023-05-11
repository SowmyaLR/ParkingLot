from constants import constants
from vehicles import Car, Truck, Scooter
import math


class Calculator:
    def __init__(self):
        self.place_capacity = 0
        self.lr_slot_no = 0
        self.init_capacity = 0
        self.slot_usage = {}
        self.scooter = None
        self.truck = None
        self.car = None
        self.type_obj = {
            constants.SCOOTER: Scooter,
            constants.TRUCK: Truck,
            constants.CAR: Car
        }

    def set_capacity(self, type, capacity):
        import copy
        if type == constants.SCOOTER:
            self.scooter = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.CAR:
            self.car = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.TRUCK:
            self.truck = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        print("capacity: ", self.place_capacity)

    def _is_full(self):
        return self.place_capacity <= 0

    def _generate_slot_no(self):
        if self.lr_slot_no + 1 <= self.init_capacity and \
                self.lr_slot_no + 1 not in self.slot_usage:
            self.lr_slot_no += 1
            self.slot_usage[self.lr_slot_no] = self.lr_slot_no
            return self.lr_slot_no
        else:
            for i in range(1, self.init_capacity + 1):
                if i not in self.slot_usage:
                    self.lr_slot_no = i
                    self.slot_usage[i] = i
                    return self.lr_slot_no

    def __allot_slot(self):
        if not self._is_full():
            return self._generate_slot_no()
        else:
            print("Parking is full")

    def _park_scooter(self, slot_no, entry_time):
        return self.scooter.park(slot_no, entry_time)

    def _park_truck(self, slot_no, entry_time):
        return self.truck.park(slot_no, entry_time)

    def _park_car(self, slot_no, entry_time):
        return self.car.park(slot_no, entry_time)

    def _unpark_scooter(self, ticket_no, exit_time):
        return self.scooter.unpark(ticket_no, exit_time)

    def _unpark_car(self, ticket_no, exit_time):
        return self.car.unpark(ticket_no, exit_time)

    def _unpark_truck(self, ticket_no, exit_time):
        return self.truck.unpark(ticket_no, exit_time)

    def print_parking_receipt(self, ticket_no, et):
        print(f"Parking Receipt:\n Receipt No: R-{ticket_no}\n Entry Time: {et[1]}\n Exit Time: {et[2]}\n")

    def park(self, type, entry_time):
        slot_no = self.__allot_slot()
        if slot_no:
            ticket_no = getattr(self, "_park" + "_%s" % type.lower())(slot_no, entry_time)
            self.place_capacity -= 1
            self.slot_usage[slot_no] = ticket_no

    def _remove_ticket_from_slot(self, ticket_no):
        for slot_no, ticket in self.slot_usage.items():
            if ticket == ticket_no:
                del (self.slot_usage[ticket])
                return

    def unpark(self, type, ticket_no, exit_time):
        et = getattr(self, "_unpark" + "_%s" % type.lower())(ticket_no, exit_time)
        if et:
            self.print_parking_receipt(ticket_no, et)
            fee = getattr(self, "_calculate_" + "%s" % type.lower() + "_fee")(math.ceil(et[0]))
            print("Fee: ", fee)
            self._remove_ticket_from_slot(ticket_no)


class MallCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def set_capacity(self, type, capacity):
        super().set_capacity(type, capacity)

    def park(self, type, entry_time):
        super().park(type, entry_time)

    def _calculate_car_fee(self, et):
        return constants.MallFee.CAR_FEE * et

    def _calculate_scooter_fee(self, et):
        return constants.MallFee.SCOOTER_FEE * et

    def _calculate_truck_fee(self, et):
        return constants.MallFee.TRUCK_FEE * et

    def unpark(self, type, ticket_no, exit_time):
        super().unpark(type, ticket_no, exit_time)

class StadiumCalculator(Calculator):
    def __init__(self):
        '''
        Trucks are not allowed at stadium
        '''
        super().__init__()

    def set_capacity(self, type, capacity):
        import copy
        if type == constants.SCOOTER:
            self.scooter = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.CAR:
            self.car = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.TRUCK:
            raise Exception("Trucks not allowed inside stadium")
        print("capacity: ", self.place_capacity)

    def park(self, type, entry_time):
        super().park(type, entry_time)

    def _calculate_scooter_fee(self, et):
        if constants.NO_FEE <= et < constants.FOUR:
            return constants.StadiumFee.SCOOTER_FIRST_SLAB
        elif constants.FOUR <= et < constants.TWELVE:
            return constants.StadiumFee.SCOOTER_FIRST_SLAB + constants.StadiumFee.SCOOTER_SECOND_SLAB
        elif et >= constants.TWELVE:
            return constants.StadiumFee.SCOOTER_FIRST_SLAB + \
                   constants.StadiumFee.SCOOTER_SECOND_SLAB + math.ceil(et-constants.TWELVE)*constants.StadiumFee.SCOOTER_THIRD_SLAB

    def _calculate_car_fee(self, et):
        if constants.NO_FEE <= et < constants.FOUR:
            return constants.StadiumFee.CAR_FIRST_SLAB
        elif constants.FOUR <= et < constants.TWELVE:
            return constants.StadiumFee.CAR_FIRST_SLAB + constants.StadiumFee.CAR_SECOND_SLAB
        elif et >= constants.TWELVE:
            return constants.StadiumFee.CAR_FIRST_SLAB + \
                   constants.StadiumFee.CAR_SECOND_SLAB + math.ceil(et-constants.TWELVE)*constants.StadiumFee.CAR_THIRD_SLAB

    def unpark(self, type, ticket_no, exit_time):
        super().unpark(type, ticket_no, exit_time)


class AirportCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.truck = None

    def set_capacity(self, type, capacity):
        import copy
        if type == constants.SCOOTER:
            self.scooter = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.CAR:
            self.car = self.type_obj[type](capacity)
            self.place_capacity += capacity
            self.init_capacity = copy.deepcopy(self.place_capacity)
        elif type == constants.TRUCK:
            raise Exception("Trucks not allowed inside airport")

    def _calculate_scooter_fee(self, et):
        if constants.NO_FEE <= et < constants.ONE:
            return constants.NO_FEE
        elif constants.ONE <= et < constants.EIGHT:
            return constants.AirportFee.SCOOTER_FIRST_SLAB
        elif constants.EIGHT <= et < constants.TWENTY_FOUR:
            return constants.AirportFee.SCOOTER_SEC_SLAB
        else:
            return math.ceil(et / constants.TWENTY_FOUR) * constants.AirportFee.SCOOTER_THIRD_SLAB

    def _calculate_car_fee(self, et):
        if constants.NO_FEE <= et < constants.TWELVE:
            return constants.AirportFee.CAR_FIRST_SLAB
        elif constants.TWELVE <= et < constants.TWENTY_FOUR:
            return constants.AirportFee.CAR_SECOND_SLAB
        else:
            return math.ceil(et / constants.TWENTY_FOUR) * constants.AirportFee.CAR_THIRD_SLAB

    def park(self, type, entry_time):
        super().park(type, entry_time)

    def unpark(self, type, ticket_no, exit_time):
        super().unpark(type, ticket_no, exit_time)


if __name__ == "__main__":
    # print("=============== MAll ============")
    # mc = MallCalculator()
    # mc.set_capacity("scooter", 20)
    # mc.set_capacity("truck", 3)
    # mc.set_capacity("car", 30)
    # print(mc.park("scooter", "2023-05-10 13:06:42.195002"))
    # print(mc.park("car", "2023-05-10 14:06:42.195002"))
    # print(mc.park("truck", "2023-05-10 13:06:42.195002"))
    #
    # print(mc.unpark("scooter", "01", "2023-05-10 18:06:42.195002"))
    # print(mc.unpark("car", "02", "2023-05-10 18:06:42.195002"))
    # print(mc.unpark("truck", "3", "2023-05-10 18:06:42.195002"))
    #
    #
    # print(" ===== Airport =======")
    # mc = AirportCalculator()
    # mc.set_capacity("scooter", 20)
    #
    # mc.set_capacity("car", 30)
    # print(mc.park("scooter", "2023-05-10 13:06:42.195002"))
    # print(mc.park("car", "2023-05-10 14:06:42.195002"))
    #
    #
    # print(mc.unpark("scooter", "01", "2023-05-10 18:06:42.195002"))
    # print(mc.unpark("car", "02", "2023-05-12 18:06:42.195002"))

    print("== stadium ===")
    mc = StadiumCalculator()
    mc.set_capacity("scooter", 20)
    # mc.set_capacity("truck", 3)
    mc.set_capacity("car", 30)
    print(mc.park("scooter", "2023-05-10 13:06:42.195002"))
    print(mc.park("car", "2023-05-10 08:06:42.195002"))
    # print(mc.park("truck", "2023-05-10 13:06:42.195002"))

    print(mc.unpark("scooter", "01", "2023-05-10 18:06:42.195002"))
    print(mc.unpark("car", "02", "2023-05-10 22:06:42.195002"))
