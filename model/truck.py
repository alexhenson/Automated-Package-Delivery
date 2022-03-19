# This class shows the attribute information of a Truck object
class Truck:
    """The Package class provides information on how to build Package objects to be delivered

    Attributes:
        truck_id: A string indicating one of three truck ID numbers
        package_list: A list of packages specific to current truck object
        visited_addresses: A list of addresses that grows with each completed package delivery
        curr_location: A string containing the current address of the truck
        curr_mileage: A floating point value containing the cumulative mileage of the truck
        curr_time: A datetime object with the current time for the current truck
        SPEED: An integer with the constant truck speed of 18 MPH
    """
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
