from libraries.hash import ChainingHashTable
from model.package import Package
import csv

SIZE_OF_HASH = 20

package_hash = ChainingHashTable(SIZE_OF_HASH)


# This method parses out the data from the package_file.csv file into Package objects
# Then the Package objects are inserted into the hash table
# O(n) time and space complexity
def load_package_data(file_name):
    with open(file_name) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)  # skip header
        for package in package_data:
            package_id = package[0]
            address = package[1]
            city = package[2]
            state = package[3]
            zip_code = package[4]
            deadline = package[5]
            mass = package[6]
            notes = package[7]

            # package object
            p = Package(package_id, address, city, state, zip_code, deadline, mass, "AT_HUB", None, notes)

            # insert it into the hash table
            package_hash.insert(package_id, p)
    return package_hash
