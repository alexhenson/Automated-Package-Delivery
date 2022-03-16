from datetime import datetime


class Truck:
    def __init__(self, truck_id, package_list, curr_time):
        self.truck_id = truck_id
        self.package_list = package_list
        self.visited_addresses = []
        self.curr_location = 'HUB'
        self.curr_mileage = 0
        self.curr_time = curr_time
        self.speed = 18

    # need current location, current mileage, current time (current time can be the delivery time for the package)
    def __str__(self):
        return "Truck ID:{:<5} Undelivered Packages: {:<40} Visited Addresses: {:<3} " \
               "Current Location: {} Current Mileage: {} Current Time {}".format(
            self.truck_id,
            self.package_list,
            self.visited_addresses,
            self.curr_location,
            self.curr_mileage,
            self.curr_time)

    def calc_time_traveled(self, distance):
        return int((distance / self.speed) * 3600)


