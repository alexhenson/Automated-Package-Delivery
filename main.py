import math
from pprint import pprint
from datetime import time


from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data
from model.truck import Truck
from libraries.packages_on_truck import *
from libraries.quicksort import quicksort

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

# pprint(distance_table)

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
truck_2 = Truck(2, undelivered_package_list_2, delivered_package_list_2, visited_addresses_2, curr_location, curr_mileage, curr_time)

print('Truck 1:')
print_packages_on_truck(undelivered_package_list_1)
print('Truck 2:')
print_packages_on_truck(undelivered_package_list_2)

sorted_undelivered_package_list_1 = quicksort(undelivered_package_list_1, distance_table)
print(sorted_undelivered_package_list_1)

# # Greedy Algorithm: Min Expenses => Max Profits
# def greedy_distance_algorithm(budget):
#     total = budget
#     c25dollar = 0
#     c10dollar = 0
#     c5dollar = 0
#     c1dollar = 0
#     while (budget >= 25):
#         if c25dollar > 3:  # why 3? 0,1,2,3 will not break so 4 times.
#             break
#         c25dollar += 1
#         budget = budget - 25
#     while (budget >= 10):
#         c10dollar += 1
#         budget = budget - 10
#     while (budget >= 5):
#         c5dollar += 1
#         budget = budget - 5
#     while (budget > 0):
#         if c1dollar > 3:
#             break
#         c1dollar += 1
#         budget = budget - 1
#
#     cDVDs = c25dollar + c10dollar + c5dollar + c1dollar
#
#     # expense calculation
#     eDVDs = 1.00 * cDVDs  # Material cost of DVD: $1.00
#     eLabor = 12.00 * (math.ceil(cDVDs / 10))  # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
#     eShipping = 0.50 * cDVDs  # Shipping cost is $0.50 per DVD
#     eTotal = eDVDs + eLabor + eShipping
#     profit = total - eTotal
#
#     print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total, cDVDs, eTotal, profit))
#     print(" {} x 25 dollar movie = ${:.2f}".format(c25dollar, c25dollar * 25.00))
#     print(" {} x 10 dollar movie = ${:.2f}".format(c10dollar, c10dollar * 10.00))
#     print(" {} x 5  dollar movie = ${:.2f}".format(c5dollar, c5dollar * 5.00))
#     print(" {} x 1  dollar movie = ${:.2f}".format(c1dollar, c1dollar * 1.00))
#
#
# print("\nGreedy Algorithm: Min Expenses => Max Profits")
# greedy_distance_algorithm(102)  # $102.00 budget
# greedy_distance_algorithm(94)  # $94.00 budget
# greedy_distance_algorithm(71)  # $71.00 budget
# greedy_distance_algorithm(200)  # $200.00 budget