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
            raise Exception("vehicle already in parking or no spots for parking")

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
            raise Exception("No such vehicle in parking")


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

