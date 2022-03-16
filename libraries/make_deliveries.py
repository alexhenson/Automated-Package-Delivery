from datetime import timedelta
import sys


def make_deliveries(truck_obj, package_list, distance_table):
    while len(truck_obj.visited_addresses) < len(package_list):
        min_index = -1
        min_address = ''
        min_dist = sys.float_info.max

        origin = truck_obj.curr_location
        distance_obj = distance_table[origin]

        for index, package in enumerate(package_list):
            destination = package.address
            if not package.is_delivered() and distance_obj[destination] < min_dist:
                min_index = index
                min_address = destination
                min_dist = distance_obj[destination]

        time_traveled_1 = truck_obj.calc_time_traveled(min_dist)
        truck_obj.curr_time += timedelta(seconds=time_traveled_1)
        print('time traveled in seconds: ' + str(time_traveled_1))

        for index in range(min_index, len(package_list)):
            if package_list[index].address == min_address:
                package_list[index].update_status('DELIVERED')
                package_list[index].miles_driven += min_dist
                package_list[index].time_delivered = truck_obj.curr_time
                truck_obj.visited_addresses.append(min_address)
                print('package delivery time: ' + str(package_list[index].time_delivered))
        truck_obj.curr_mileage += min_dist
        truck_obj.curr_location = min_address