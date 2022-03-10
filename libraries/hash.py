# W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def hash_func(self, key):
        #return hash(key) % len(self.table)
        return (int(key) - 1) % len(self.table)
        # hash_key = 0
        # for char in key:
        #     hash_key += ord(char)
        # return hash_key % len(self.table)

    # Inserts a new item into the hash table.
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = self.hash_func(key)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
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
        #print([str(p) for a, p in bucket_list])

        # search for the key in the bucket list
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
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

            # Searches for an item with matching key in the hash table.
            # Returns the item if found, or None if not found.

    def get_bucket(self, key):
        # get the bucket list where this key would be.
        bucket = self.hash_func(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list



