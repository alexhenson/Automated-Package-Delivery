from libraries.load_package_data import load_package_data

PACKAGE_CSV = 'csv_files/package_file.csv'

# Load CSV files into hash tables
package_hash = load_package_data(PACKAGE_CSV)

print()
print("Packages from Hashtable:")
# Fetch data from Hash Table
for i in range(len(package_hash.table)):
    print("{}. {}".format(i + 1, package_hash.search(str(i + 1))))  # 1 to 40 is sent to my_hash.search()

# Need to use zybooks to update insert, search, and remove functions

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
