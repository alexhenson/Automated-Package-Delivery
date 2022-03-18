# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        # O(n) time and space complexity
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # This hash function takes the ID of the package subtracts 1 and then inserts it into the index that is
    # the result mod the length of the table
    def hash_func(self, key):
        return int(key) % len(self.table)

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = self.hash_func(key)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        # O(n) time and space complexity
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = self.hash_func(key)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        # O(n) time and space complexity
        for k, v in bucket_list:
            if int(k) == key:
                return v  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = self.hash_func(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        # O(n) time and space complexity
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Returns entire bucket where the matching key is
    def get_bucket(self, key):
        # get the bucket list where this key would be.
        bucket = self.hash_func(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list
