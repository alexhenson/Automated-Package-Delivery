# while len(truck_1.visited_addresses) < len(package_list_1):
#     min_index = -1
#     min_address = ''
#     min_dist = sys.float_info.max
#
#     origin = curr_location
#     distance_obj = distance_table[origin]
#
#     for index, package in enumerate(package_list_1):
#         destination = package.address
#         if not package.is_delivered() and distance_obj[destination] < min_dist:
#             min_index = index
#             min_address = destination
#             min_dist = distance_obj[destination]
#
#     time_traveled_1 = truck_1.calc_time_traveled(min_dist)
#     truck_1.curr_time += timedelta(seconds=time_traveled_1)
#     print('time traveled in seconds: ' + str(time_traveled_1))
#
#     for index in range(min_index, len(package_list_1)):
#         if package_list_1[index].address == min_address:
#             package_list_1[index].update_status('DELIVERED')
#             package_list_1[index].miles_driven += min_dist
#             package_list_1[index].time_delivered = truck_1.curr_time
#             truck_1.visited_addresses.append(min_address)
#             print('package delivery time: ' + str(package_list_1[index].time_delivered))
#     truck_1.curr_mileage += min_dist
#     curr_location = min_address