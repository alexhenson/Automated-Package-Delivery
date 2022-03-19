from libraries.hash import ChainingHashTable
from model.package import Package
import csv

SIZE_OF_HASH = 20
package_hash = ChainingHashTable(SIZE_OF_HASH)


def load_package_data(file_name):
    """Takes a CSV file and inputs the data into a hashtable

    This method parses out the data from the package_file.csv file into Package objects then the Package objects
    are inserted into the hash table

    Args:
        file_name: This argument is a CSV file to be converted into a hashtable

    Returns:
        package_hash: This function returns a hashtable

    Raises:
        N/A: This function raises no errors/has no error checking

    Time complexity: Because of the for loop, it's time complexity is O(n)
    Space complexity: Because of the chaining hash table the space complexity is O(n)
    """
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
