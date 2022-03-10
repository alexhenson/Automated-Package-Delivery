from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'

# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)



# print()
# print("Packages from Hashtable:")
# # Fetch data from Hash Table
# for i in range(len(package_hash.table)):
#     print("{}. {}".format(i, [str(p) for a, p in package_hash.get_bucket(str(i + 1))]))  # 1 to 40 is sent to my_hash.search()

# print("{}".format(package_hash.search(str(29))))
# print("{}".format(package_hash.get_bucket(str(29))))
