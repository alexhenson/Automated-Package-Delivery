from pprint import pprint
from datetime import datetime, timedelta

from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data
from model.truck import Truck
from libraries.packages_on_truck import *
from libraries.make_deliveries import make_deliveries
from libraries.send_truck_home import send_truck_home

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'


# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)


print("Packages from Hashtable:")
# Fetch data from Hash Table
for i in range(len(package_hash.table)):
    print("{:<2}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))

print(distance_table)

# Figure out package 13

package_id_list_1 = [1, 29, 7, 40, 4, 2, 33, 17, 21, 24]
package_id_list_2 = [13, 39, 14, 15, 16, 34, 19, 20, 3, 18, 36, 38, 30, 8, 37, 5]
package_id_list_3 = [6, 9, 10, 11, 12, 22, 23, 25, 26, 27, 28, 31, 32, 35]



TRUCK_1_2_DEPARTURE_TIME = datetime(2022, 3, 16, 8, 0, 0)

package_list_1 = load_packages_on_truck(package_id_list_1, package_hash)
package_list_2 = load_packages_on_truck(package_id_list_2, package_hash)
package_list_3 = load_packages_on_truck(package_id_list_3, package_hash)

truck_1 = Truck(1, package_list_1, TRUCK_1_2_DEPARTURE_TIME)
truck_2 = Truck(2, package_list_2, TRUCK_1_2_DEPARTURE_TIME)

print('Truck 1:')
print_packages_on_truck(package_list_1)
print('Truck 2:')
print_packages_on_truck(package_list_2)
print('Truck 3:')
print_packages_on_truck(package_list_3)

# Truck 1 & 2
make_deliveries(truck_1, package_list_1, distance_table)
make_deliveries(truck_2, package_list_2, distance_table)

print()
print('total mileage before HUB for truck 1')
print(truck_1.curr_mileage)

print()
print('current time before HUB for truck 1')
print(truck_1.curr_time)

print()
print('packages after deliveries for truck 1')
print_packages_on_truck(package_list_1)

print()
print('address list for truck 1')
print(truck_1.visited_addresses)

print()
print('total mileage for truck 2')
print(truck_2.curr_mileage)

print()
print('current time for truck 2')
print(truck_2.curr_time)

print()
print('packages after deliveries for truck 2')
print_packages_on_truck(package_list_2)

print()
print('address list for truck 2')
print(truck_2.visited_addresses)

# Bring truck 1 back home
send_truck_home(truck_1, distance_table)

print()
print('total mileage after HUB for truck 1')
print(truck_1.curr_mileage)

print()
print('current time after HUB for truck 1')
print(truck_1.curr_time)

TRUCK_3_DEPARTURE_TIME = truck_1.curr_time
truck_3 = Truck(3, package_list_3, TRUCK_3_DEPARTURE_TIME)
make_deliveries(truck_3, package_list_3, distance_table)

print()
print('total mileage for truck 3')
print(truck_3.curr_mileage)

print()
print('current time for truck 3')
print(truck_3.curr_time)

print()
print('packages after deliveries for truck 3')
print_packages_on_truck(package_list_3)

print()
print('address list for truck 3')
print(truck_3.visited_addresses)

print("Packages from Hashtable:")
# Fetch data from Hash Table
for i in range(len(package_hash.table)):
    print("{:<2}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))