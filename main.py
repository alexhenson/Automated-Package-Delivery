from pprint import pprint

from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data
from model.truck import Truck

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'

# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)


print("Packages from Hashtable:")
# Fetch data from Hash Table
for i in range(len(package_hash.table)):
    print("{:<2}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))  # 1 to 40 is sent to my_hash.search()

#pprint(distance_table)

# Develop a property to track early shipments upon results from testing
package_id_list_1 = [14, 15, 16, 34, 20, 21, 31, 32, 40, 4, 27, 7, 1]
package_id_list_2 = [3, 13, 39, 30, 8, 37, 9, 38, 5, 10, 36, 17, 12, 23, 18, 11]

undelivered_package_list_1 = []

for package_id in package_id_list_1:
    undelivered_package_list_1.append(package_hash.search(package_id))

print(package_id_list_1)
print(undelivered_package_list_1)
# truck_1 = Truck(1, undelivered_package_list_1, delivered_package_list, visited_addresses, curr_location, curr_mileage, curr_time)