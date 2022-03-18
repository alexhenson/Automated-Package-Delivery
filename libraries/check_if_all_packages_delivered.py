# This method will loop through a list to check the delivery status
# O(n) time complexity
def check_if_all_packages_delivered(package_list):
    for package in package_list:
        if not package.is_delivered():
            return False
    return True


# This method will loop through a hashtable to check the delivery status
# O(n) time complexity
def check_if_all_packages_delivered_hash(package_hash):
    for i in range(40):
        if not package_hash.search(i + 1).is_delivered():
            return False
    return True
