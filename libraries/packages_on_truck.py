def load_packages_on_truck(package_id_list, package_hash):
    # Insert package objects into list
    undelivered_package_list = []
    for package_id in package_id_list:
        undelivered_package_list.append(package_hash.search(package_id))
    return undelivered_package_list


def print_packages_on_truck(undelivered_package_list):
    # Print out package info
    for i, package_id in enumerate(undelivered_package_list):
        print("ID: " + undelivered_package_list[i].id + ", Address: " + undelivered_package_list[i].address)