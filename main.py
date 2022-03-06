from libraries.hash import ChainingHashTable
from model.package import Package
import csv

# need to figure out the formatting of the strings in package class

bestMovies = [
    [1, "CITIZEN KANE - 1941"],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

# Hash table instance
my_hash = ChainingHashTable()

def load_package_data(fileName):
    with open(fileName) as packages:
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
            p = Package(id, address, city, state, zip, deadline, mass, notes)
            print(p)

            # insert it into the hash table
            my_hash.insert(id, address)

load_package_data('csv_files/package_file.csv')

# print("\nInsert:")
#
# for i in range(len(bestMovies)):
#     my_hash.insert(bestMovies[i][0], bestMovies[i][1])
# print(my_hash.table)
#
# print("\nSearch:")
# print(my_hash.search(1))  # Key=1, item="CITIZEN KANE - 1941"
# print(my_hash.search(2))  # Key=11, item="STAR WARS - 1977"; so same bucket and Chaining is working
#
# print("\nUpdate:")
# my_hash.insert(1, "Star Trek - 1979")  # 2nd bucket; Key=1, item="Star Trek - 1979"
# print(my_hash.table)
#
# print("\nRemove:")
# my_hash.remove(1)  # Key=1, item="Star Trek - 1979" to remove
# print(my_hash.table)
#
# my_hash.remove(1)  # Key=11, item="STAR WARS - 1977" to remove
# print(my_hash.table)table
