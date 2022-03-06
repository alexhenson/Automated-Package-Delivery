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
        return "ID: %-1s, Address: %-1s, %s, %s %s, Deadline: %-10s, Mass(kg): %s, Sp. Notes: %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.deadline, self.mass, self.notes)
