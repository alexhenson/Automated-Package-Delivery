def load_packages_on_truck(package_id_list, package_hash):
    # Insert package objects into list
    undelivered_package_list = []
    for package_id in package_id_list:
        package_hash.search(package_id).update_status('EN_ROUTE')
        undelivered_package_list.append(package_hash.search(package_id))
    return undelivered_package_list


# Need to change this to print based on status
def print_packages_on_truck(undelivered_package_list):
    # Print out package info
    for i, package_id in enumerate(undelivered_package_list):
        print("ID: " + undelivered_package_list[i].package_id + ", Address: " + undelivered_package_list[i].address + ", Status: " + undelivered_package_list[i].status + ", Miles Driven: " + str(undelivered_package_list[i].miles_driven) + ", Time Delivered: " + str(undelivered_package_list[i].time_delivered))
