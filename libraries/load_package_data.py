from libraries.hash import ChainingHashTable
from model.package import Package
import csv

SIZE_OF_HASH = 20

package_hash = ChainingHashTable(SIZE_OF_HASH)


def load_package_data(file_name):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)  # skip header
        for package in package_data:
            id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            mass = package[6]
            notes = package[7]

            # package object
            p = Package(id, address, city, state, zip, deadline, mass, "AT THE HUB", None, notes)
            #print(p)

            # insert it into the hash table
            package_hash.insert(id, p)
        return package_hash
