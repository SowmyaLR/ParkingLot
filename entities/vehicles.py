import datetime

class Vehicles:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.init_cap = capacity
        self.vehicle_data = {}

    def __is_valid_vehicle(self, ticket_no):
        return ticket_no in self.vehicle_data

    def __generate_ticket_no(self, slot_no):
        return "{0:0{width}}".format(slot_no, width=len(str(self.init_cap)))

    def park(self, slot_no, entry_time):
        ticket_no = self.__generate_ticket_no(slot_no)
        if self.capacity > 0 and not self.__is_valid_vehicle(ticket_no):
            self.vehicle_data[ticket_no] = datetime.datetime.strptime(entry_time, '%Y-%m-%d %H:%M:%S.%f')
            self.capacity -= 1
            print(f"Parking Ticket: \n Ticket no: {ticket_no}\n "
                  f"Slot No: {slot_no} \n Entry Time: {entry_time}")
            return ticket_no
        else:
            print("vehicle already in parking or no spots for parking")

    def unpark(self, ticket_no, exit_time):
        if self.__is_valid_vehicle(ticket_no):
            from datetime import timedelta
            exit_time = datetime.datetime.strptime(exit_time, '%Y-%m-%d %H:%M:%S.%f')
            et = exit_time - self.vehicle_data[ticket_no]
            et = et / timedelta(hours=1)
            ent_time = self.vehicle_data[ticket_no]
            del (self.vehicle_data[ticket_no])
            self.capacity += 1
            return (et, ent_time.strftime('%Y-%m-%d %H:%M:%S'),
                    exit_time.strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print("No such vehicle in parking")


class Truck(Vehicles):
    def __init__(self, capacity):
        super().__init__(capacity)

    def park(self, slot_no, entry_time):
        super().park(slot_no, entry_time)

    def unpark(self, ticket_no, exit_time):
        return super().unpark(ticket_no, exit_time)


class Car(Vehicles):
    def __init__(self, capacity):
        super().__init__(capacity)

    def park(self, slot_no, entry_time):
        super().park(slot_no, entry_time)

    def unpark(self, ticket_no, exit_time):
        return super().unpark(ticket_no, exit_time)


class Scooter(Vehicles):
    def __init__(self, capacity):
        super().__init__(capacity)

    def park(self, slot_no, entry_time):
        super().park(slot_no, entry_time)

    def unpark(self, ticket_no, exit_time):
        return super().unpark(ticket_no, exit_time)


if __name__ == "__main__":
    # v = Vehicles(30)
    t = Truck(120)
    c = Car(34)
    # v.park(34,"5556")
    t.park(1, "2023-05-10 13:06:42.195002")
    c.park(2, "2023-05-10 13:54:15.200891")
    # v.unpark(1, 2)
    et = t.unpark("001", "2023-05-10 19:58:10.224214")
    print(et)
    print(c.unpark("02", "2023-05-10 19:58:10.224214"))
