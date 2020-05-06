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
        self.count = 0

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
            self.count += 1
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
                self.count += 1
        #auto resize feature
        #self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # find hash index:
        index = self.hash_index(key)
        # if current is None, print key not found:
        if self.storage[index] is None:
            print('Key not found')
        else:
            # set previous and current variables:
            previous = None
            current = self.storage[index]
            # while there's more than 1 node in the linked list:
            while current.next is not None:
                # if keys match, skip over node so previous points to next:
                if current.key == key:
                    if previous is None:
                        self.storage[index] = current.next
                        self.count -= 1
                    else:
                        previous.next = current.next
                        self.count -= 1
                    break
                else:
                    # keep moving down the list looking for matching key
                    previous = current
                    current = current.next
            # if only 1 item in the list and keys match, replace with None
            if previous is None and current.key == key:
                self.storage[index] = None
                self.count -= 1
        #auto resize feature
        #self.resize()



    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        current = self.storage[index]

        #if index is valid search for value
        if current is not None:
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

    def resize(self, length=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        #find the load
        load_factor = (self.count / self.capacity)
        og_storage = self.storage

        if length is not None:
            self.capacity = length
            self.storage = [None] * length
            for index in og_storage:
                #if there is data in that cell rehash them
                if index is not None:
                    #establish the head node for that cell
                    current = index
                    #keep going till end of linked list
                    while current is not None:
                        self.put(current.key, current.value)
                        # go to next
                        current = current.next

        #if space used is greater than .7 double space
        elif load_factor >= .7:
            self.capacity *= 2
            self.storage = [None] * self.capacity
            #rehash the table
            for index in og_storage:
                #if there is data in that cell rehash them
                if index is not None:
                    #establish the head node for that cell
                    current = index
                    #keep going till end of linked list
                    while current is not None:
                        self.put(current.key, current.value)
                        # go to next
                        current = current.next

        #if space used is less than .2 halve space
        elif load_factor <= .2:
            self.capacity = int(self.capacity/2)
            self.storage = [None] * self.capacity
            #rehash the table
            for index in og_storage:
                #if there is data in that cell rehash them
                if index is not None:
                    #establish the head node for that cell
                    current = index
                    #keep going till end of linked list
                    while current is not None:
                        self.put(current.key, current.value)
                        # go to next
                        current = current.next
        else:
            return





if __name__ == "__main__":
    ht = HashTable(2)
    old_capacity = len(ht.storage)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_1", "Filled beyond capacity")
    ht.put("line_2", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_1"))
    print(ht.get("line_2"))

    # Test resizing
    #old_capacity = len(ht.storage)
    #ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_1"))
    print(ht.get("line_2"))

    print("")
