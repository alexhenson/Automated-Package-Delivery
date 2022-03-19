class Package:
    """The Package class provides information on how to build Package objects to be delivered

    Attributes:
        package_id: A string indicating the package ID number
        address: A string indicating address to be delivered to
        city: A string with the city
        state: A string with the state
        zip_code: A string with the zip code
        deadline: A string with a time delivery deadline
        mass: A string with the mass of the package
        status: A string with one of three delivery statuses
        time_delivered: A datetime object with the final delivery time
        notes: A string with any special notes is applicable
        miles_driven: An integer that represents how many miles since the last delivery once the package has been delivered
    """
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
        # This if statement will remove date information from datetime object before printing
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
