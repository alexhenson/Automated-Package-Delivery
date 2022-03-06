class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes

    def __str__(self):  # overwite print(Movie) otherwise it will print object reference
        return "ID:{:<5} Address: {:<40}{:<17} {} {:<6} Deadline: {:<9} Mass(kg): {:<3} Sp. Notes: {:<8}".format(
            self.id, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.notes)