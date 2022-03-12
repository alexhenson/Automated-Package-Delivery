class Package:
    def __init__(self, id, address, city, state, zip_code, deadline, mass, status, time_delivered, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.status = status
        self.time_delivered = time_delivered
        self.notes = notes
        self.mileage = 0  #distance traveled from the previous delivery to have the truck add up all the mileage at the end to know distance traveled so far

    def __str__(self):
        return "ID: {:<3} Address: {:<40}{:<17} {} {:<6} Deadline: {:<9} Mass(kg): {:<3} Status: {:<11} Time Delivered: {} Sp. Notes: {:<60}".format(
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip_code,
            self.deadline,
            self.mass,
            self.status,
            self.time_delivered,
            self.notes)

    def update_status(self, new_status):
        if new_status not in ['EN_ROUTE', 'DELIVERED']:
            raise ValueError("You may only change status to 'En Route' or 'Delivery Time'")
        else:
            self.status = new_status

    def update_time_delivered(self, new_time_delivered):
        self.time_delivered = new_time_delivered

# helper, is_delivered (and ! for the other one or maybe just code the inverse the explicitly)
