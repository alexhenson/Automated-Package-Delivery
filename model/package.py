class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, status, time_delivered, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.status = status
        self.time_delivered = time_delivered
        self.notes = notes

    def __str__(self):
        return "ID: {:<3} Address: {:<40}{:<17} {} {:<6} Deadline: {:<9} Mass(kg): {:<3} Status: {:<11} Time Delivered: {} Sp. Notes: {:<60}".format(
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.deadline,
            self.mass,
            self.status,
            self.time_delivered,
            self.notes)
