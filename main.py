from pprint import pprint
from datetime import time

from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data
from model.truck import Truck
from libraries.load_packages_on_truck import *

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'
GLOBAL_TIME = time(8, 0, 0)

# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)


# print("Packages from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(package_hash.table)):
#     print("{:<2}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))  # 1 to 40 is sent to my_hash.search()

#pprint(distance_table)

# Develop a property to track early shipments upon results from testing
package_id_list_1a = [14, 15, 16, 34, 20, 21, 31, 32, 40, 4, 27, 7, 1]
package_id_list_2 = [3, 13, 39, 30, 8, 37, 9, 38, 5, 10, 36, 17, 12, 23, 18, 11]

undelivered_package_list_1 = load_packages_on_truck(package_id_list_1a, package_hash)
delivered_package_list_1 = []
visited_addresses_1 = []
undelivered_package_list_2 = load_packages_on_truck(package_id_list_2, package_hash)
delivered_package_list_2 = []
visited_addresses_2 = []

curr_location = "HUB"
curr_mileage = 0
curr_time = GLOBAL_TIME

truck_1 = Truck(1, undelivered_package_list_1, delivered_package_list_1, visited_addresses_1, curr_location, curr_mileage, curr_time)

print_packages_on_truck(undelivered_package_list_1)