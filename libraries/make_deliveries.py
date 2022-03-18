from datetime import timedelta
import sys


# This method will execute the Nearest Neighbor solution.  Each time a package is delivered, the
# address of the delivered package will be added to the visited_addresses list. The method uses a
# while loop that will run until the length of address list is the same as the length of the package list.
# O(n^2) time complexity because of the while and nested for loop
def make_deliveries(truck_obj, package_list, distance_table, time_limit):
    total_time_traveled = 0

    while len(truck_obj.visited_addresses) < len(package_list):
        min_index = -1
        min_address = ''
        min_dist = sys.float_info.max

        origin = truck_obj.curr_location
        distance_obj = distance_table[origin]

        # For loop will loop through each package object in the package list.  If the package has not
        # yet been delivered and the distance to the address on that package is the lowest distance seen
        # so far, then this loop will save that package's delivery information.
        # O(n) time complexity
        for index, package in enumerate(package_list):
            destination = package.address
            if not package.is_delivered() and distance_obj[destination] < min_dist:
                min_index = index
                min_address = destination
                min_dist = distance_obj[destination]

        # Once the above for loop is finished, the data for the next closest, valid destination will
        # saved.  And the code below will now update truck related data.
        time_traveled = truck_obj.calc_time_traveled(min_dist)
        total_time_traveled += time_traveled

        if total_time_traveled >= time_limit:
            break

        truck_obj.curr_time += timedelta(seconds=time_traveled)
        truck_obj.curr_mileage += min_dist
        truck_obj.curr_location = min_address

        # This for loop will update data at the package level as well as the truck's visited_addresses list
        # O(n) time complexity
        for index in range(min_index, len(package_list)):
            if package_list[index].address == min_address:
                package_list[index].update_status('DELIVERED')
                package_list[index].miles_driven += min_dist
                package_list[index].time_delivered = truck_obj.curr_time
                truck_obj.visited_addresses.append(min_address)
