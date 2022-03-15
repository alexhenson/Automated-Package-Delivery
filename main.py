from pprint import pprint
from datetime import time
import sys


from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data
from model.truck import Truck
from libraries.packages_on_truck import *

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'
GLOBAL_TIME = time(8, 0, 0)

# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)


print("Packages from Hashtable:")
# Fetch data from Hash Table
for i in range(len(package_hash.table)):
    print("{:<2}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))  # 1 to 40 is sent to my_hash.search()

print(distance_table)

# Develop a property to track early shipments upon results from testing
package_id_list_1a = [14, 15, 16, 34, 20, 21, 31, 32, 40, 4, 29, 7, 1]
package_id_list_2 = [3, 13, 39, 30, 8, 37, 9, 38, 5, 10, 36, 17, 12, 23, 18, 11]

package_list_1 = load_packages_on_truck(package_id_list_1a, package_hash)
visited_addresses_1 = []
package_list_2 = load_packages_on_truck(package_id_list_2, package_hash)
visited_addresses_2 = []

curr_location = "HUB"
curr_mileage = 0
curr_time = GLOBAL_TIME

truck_1 = Truck(1, package_list_1, visited_addresses_1, curr_location, curr_mileage, curr_time)
truck_2 = Truck(2, package_list_2, visited_addresses_2, curr_location, curr_mileage, curr_time)

print('Truck 1:')
print_packages_on_truck(package_list_1)
print('Truck 2:')
print_packages_on_truck(package_list_2)

# deliver package

#test for distance table

# print('one dimension:' + str(distance_table[0]))
# print('three dimensions:' + str(distance_table[0][0][0]))

# while loop to access truck package list based on length of address list
# variable to hold shortest distance and address info
# use dictionary to instantly access addresses by key and find shortest distance
# save distance if less than current lowest distance
# save address
#
# have truck deliver package to that address
# update current location and mileage
# add to address list

#
while len(truck_1.visited_addresses) < len(package_list_1):
    min_index = -1
    min_address = ''
    min_dist = sys.float_info.max

    origin = curr_location
    distance_obj = distance_table[origin]
    #for origin, distance_obj in distance_table.items():
    #if origin == curr_location:
    for index, package in enumerate(package_list_1):
        destination = package.address
        print("current location: " + origin)
        print("address: " + destination)
        print("distance: " + str(distance_obj[destination]))
        if not package.is_delivered() and distance_obj[destination] < min_dist:
            min_index = index
            min_address = destination
            min_dist = distance_obj[destination]

    for index in range(min_index, len(package_list_1)):
        if package_list_1[index].address == min_address:
            package_list_1[index].update_status('DELIVERED')
            package_list_1[index].miles_driven += min_dist
            truck_1.visited_addresses.append(min_address)
    truck_1.curr_mileage += min_dist
    curr_location = min_address

print()
print('packages after deliveries')
print_packages_on_truck(package_list_1)

print()
print('address list')
print(visited_addresses_1)

print()
print('total mileage')
print(truck_1.curr_mileage)