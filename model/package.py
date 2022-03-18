# This class shows the attribute information of a Package object
class Package:
    def __init__(self, package_id, address, city, state, zip_code, deadline, mass, status, time_delivered, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.status = status
        self.time_delivered = time_delivered
        self.notes = notes
        self.miles_driven = 0  # May not use this

    def __str__(self):
        if self.time_delivered is not None:
            time = self.time_delivered.strftime("%H:%M:%S")
            return "ID: {:<3} " \
                   "Address: {:<40}{:<17} {} {:<6} " \
                   "Deadline: {:<9} " \
                   "Mass(kg): {:<3} " \
                   "Status: {:<11} " \
                   "Time Delivered: {} " \
                   "Sp. Notes: {:<60}".format(
                    self.package_id,
                    self.address,
                    self.city,
                    self.state,
                    self.zip_code,
                    self.deadline,
                    self.mass,
                    self.status,
                    time,
                    self.notes)
        else:
            return "ID: {:<3} " \
                   "Address: {:<40}{:<17} {} {:<6} " \
                   "Deadline: {:<9} " \
                   "Mass(kg): {:<3} " \
                   "Status: {:<11} " \
                   "Time Delivered: {} " \
                   "Sp. Notes: {:<60}".format(
                self.package_id,
                self.address,
                self.city,
                self.state,
                self.zip_code,
                self.deadline,
                self.mass,
                self.status,
                self.time_delivered,
                self.notes)

    # Updates the status of the package from AT_HUB -> EN_ROUTE -> DELIVERED
    def update_status(self, new_status):
        if new_status not in ['EN_ROUTE', 'DELIVERED']:
            raise ValueError("You may only change status to 'En Route' or 'Delivery Time'")
        else:
            self.status = new_status

    # Returns a boolean value checking if the status of the package is DELIVERED
    def is_delivered(self):
        return self.status == "DELIVERED"
