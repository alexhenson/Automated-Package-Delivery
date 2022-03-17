# This class shows the attribute information of a Truck object
class Truck:
    def __init__(self, truck_id, package_list, curr_time):
        self.truck_id = truck_id
        self.package_list = package_list
        self.visited_addresses = []
        self.curr_location = 'HUB'
        self.curr_mileage = 0
        self.curr_time = curr_time
        self.SPEED = 18

    def __str__(self):
        return "Truck ID:{:<5} Undelivered Packages: {:<40} Visited Addresses: {:<3} " \
               "Current Location: {} Current Mileage: {} Current Time {}".format(
            self.truck_id,
            self.package_list,
            self.visited_addresses,
            self.curr_location,
            self.curr_mileage,
            self.curr_time)

    # Uses the constant SPEED of 18 mph to determine elapsed time by miles driven
    def calc_time_traveled(self, distance):
        return int((distance / self.SPEED) * 3600)


