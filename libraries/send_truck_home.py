from datetime import timedelta


def send_truck_home(truck_obj, distance_table):
    distance_to_hub = distance_table[truck_obj.curr_location]['HUB']
    truck_obj.curr_mileage += distance_to_hub
    time_traveled_1 = truck_obj.calc_time_traveled(distance_to_hub)
    truck_obj.curr_time += timedelta(seconds=time_traveled_1)
    truck_obj.visited_addresses.append('HUB')
    truck_obj.curr_location = 'HUB'
