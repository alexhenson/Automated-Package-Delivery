from datetime import datetime
from model.truck import Truck
from libraries.packages_on_truck import *
from libraries.make_deliveries import make_deliveries
from libraries.send_truck_home import send_truck_home
from libraries.check_if_all_packages_delivered import *
from libraries.load_package_data import load_package_data
from libraries.load_distance_table_data import load_distance_table_data

PACKAGE_CSV = 'csv_files/package_file.csv'
DISTANCE_CSV = 'csv_files/distance_table.csv'

# Load package_file CSV file into hash table
package_hash = load_package_data(PACKAGE_CSV)

# Load distance_table CSV file into variable
distance_table = load_distance_table_data(DISTANCE_CSV)


# This method will simulate the entire delivery process up until the time limit
# imposed by the user.
# O(n) there is only one for loop in this method to print out package data
def delivery_simulator(time_limit):
    package_id_list_1 = [1, 29, 7, 40, 4, 2, 33, 17, 21, 24]
    package_id_list_2 = [13, 39, 14, 15, 16, 34, 19, 20, 3, 18, 36, 38, 30, 8, 37, 5]
    package_id_list_3 = [6, 9, 10, 11, 12, 22, 23, 25, 26, 27, 28, 31, 32, 35]

    truck_1_2_departure_time = datetime(2022, 3, 18, 8, 0, 0)

    package_list_1 = load_packages_on_truck(package_id_list_1, package_hash)
    package_list_2 = load_packages_on_truck(package_id_list_2, package_hash)

    truck_1 = Truck(1, package_list_1, truck_1_2_departure_time)
    truck_2 = Truck(2, package_list_2, truck_1_2_departure_time)

    make_deliveries(truck_1, package_list_1, distance_table, time_limit)
    make_deliveries(truck_2, package_list_2, distance_table, time_limit)

    # Bring truck 1 back home if all packages delivered and send out truck 3
    if check_if_all_packages_delivered(package_list_1):
        send_truck_home(truck_1, distance_table)
        package_list_3 = load_packages_on_truck(package_id_list_3, package_hash)
        truck_3_departure_time = truck_1.curr_time
        time_difference_dt = (truck_1.curr_time - truck_1_2_departure_time).total_seconds()
        truck_3_time_limit = abs(time_difference_dt - time_limit)
        truck_3 = Truck(3, package_list_3, truck_3_departure_time)
        make_deliveries(truck_3, package_list_3, distance_table, truck_3_time_limit)

    # Print out all package data from hash table
    print()
    print('Package Info')
    for i in range(40):
        print("{:<2}. {}".format(i, package_hash.search(i + 1)))

    # Print out all package data by truck
    print()
    print('Package Info by Truck')
    print('Truck 1:')
    print_packages_on_truck(package_list_1)
    print()
    print('Truck 2:')
    print_packages_on_truck(package_list_2)
    if check_if_all_packages_delivered(package_list_1):
        print()
        print('Truck 3:')
        print_packages_on_truck(package_list_3)

    # If all packages delivered, print out Total Miles and Final Delivery Time
    if check_if_all_packages_delivered_hash(package_hash):
        print()
        print('Total Miles Driven: ' + str(truck_1.curr_mileage + truck_2.curr_mileage + truck_3.curr_mileage))
        print('Time of Final Delivery: ' + str(truck_3.curr_time.strftime("%H:%M:%S")))
