class Truck:
    def __init__(self, truck_id, undelivered_package_list, delivered_package_list, visited_addresses, curr_location,
                 curr_mileage, curr_time):
        self.truck_id = truck_id
        self.undelivered_package_list = undelivered_package_list
        self.delivered_package_list = delivered_package_list #might be extraneous, can use helper to just check for undelivered packages)
        self.visited_addresses = visited_addresses
        self.curr_location = curr_location
        self.curr_mileage = curr_mileage # this should be total miles and be derived
        self.curr_time = curr_time
        self.speed = 18

    # need current location, current mileage, current time (current time can be the delivery time for the package)
    def __str__(self):
        return "Truck ID:{:<5} Undelivered Packages: {:<40} Delivered Packages: {:<9} Visited Addresses: {:<3} " \
               "Current Location: {} Current Mileage: {} Current Time {}".format(
            self.truck_id,
            self.undelivered_package_list,
            self.delivered_package_list,
            self.visited_addresses,
            self.curr_location,
            self.curr_mileage,
            self.curr_time)
