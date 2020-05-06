class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return (f"('{self.key}','{self.value}')")


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity

        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # find hash index:
        index = self.hash_index(key)
        # variable to create new node:
        new_node = HashTableEntry(key, value)
        # current node will be the index location:
        current = self.storage[index]
        # check if something is at index, if there isn't, add the node:
        if current is None:
            self.storage[index] = new_node
        else:
            # as long as the next node is not None and not matching key:
            while current.next is not None and current.key != key:
                # keep moving
                current = current.next
                # if key is already there, override its value:
            if current.key == key:
                current.value = value
                # otherwise, create a new node at the end:
            else:
                current.next = new_node

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]
        #special case if cell is empty
        if current is None:
            print('Key not found')
        #search for key until found
        while current.key is not key:
            #if key doesnt exist
            if current == None:
                print('Key not found')
                break
            current = current.next
        #once found repace value with none
        current.value = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]

        #if index is valid search for value
        if self.storage[index] is not None:
            #search for the key
            while current is not None:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
            #if not not found return none
            return None
        #if invalid index return none
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # self.capacity = self.capacity * 2
        # for value in self.storage:
        #     index = self.hash_index(value)
        #     self.put(index, value)

if __name__ == "__main__":
    ht = HashTable(10)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_1", "Filled beyond capacity")
    ht.put("line_2", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_1"))
    print(ht.get("line_2"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_1"))
    print(ht.get("line_2"))

    print("")
