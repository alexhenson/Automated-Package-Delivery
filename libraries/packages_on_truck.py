# This method inserts package objects into a list
# O(n) space and time complexity
def load_packages_on_truck(package_id_list, package_hash):
    undelivered_package_list = []
    for package_id in package_id_list:
        package_hash.search(package_id).update_status('EN_ROUTE')
        undelivered_package_list.append(package_hash.search(package_id))
    return undelivered_package_list


# This method prints the relevant package information by the truck
# O(n) time complexity
def print_packages_on_truck(undelivered_package_list):
    for i, package_id in enumerate(undelivered_package_list):
        if undelivered_package_list[i].time_delivered is not None:
            print("ID: " + undelivered_package_list[i].package_id +
                  ", Address: " + undelivered_package_list[i].address +
                  ", Status: " + undelivered_package_list[i].status +
                  ", Miles From Last Delivery: " + str(undelivered_package_list[i].miles_driven) +
                  ", Time Delivered: " + str(undelivered_package_list[i].time_delivered.strftime("%H:%M:%S")))
        else:
            print("ID: " + undelivered_package_list[i].package_id +
                  ", Address: " + undelivered_package_list[i].address +
                  ", Status: " + undelivered_package_list[i].status +
                  ", Miles From Last Delivery: " + str(undelivered_package_list[i].miles_driven) +
                  ", Time Delivered: " + str(undelivered_package_list[i].time_delivered))
