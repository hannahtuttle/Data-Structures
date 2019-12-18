import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.DLL = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # find the key/value pair that matches they key, return the value
    # move the node you are vewing to the head.
    # return none if the key does not exist
    def get(self, key):
        current = self.DLL.head
        val = ''
        while current is not None:
            if current.key == key:
                self.DLL.move_to_front(current)
                val = current.value
            current = current.next
        if val == '':
            return None
        else:
            return val

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    # if the size id less than 10:
        # check all the keys and make sure they don't already exist, if the key already exists replace the value, move the nose to the head
        # if the node does not exist and the size is less than 10 just add the node to the head
    #if the size is == 10:
        # check all the keys and make sure they don't already exist, if the key already exists replace the value, move the nose to the head
        #  the add to the head and remove the tail
    def set(self, key, value):
        if self.size == 0:
            self.DLL.add_to_head(key, value)
            self.size += 1
        else:
            current = self.DLL.head
            already_exist = False
            while current is not None:
                if current.key == key:
                    current.value = value
                    already_exist = True
                    self.DLL.move_to_front(current)
                current = current.next
            if already_exist == False and self.size < self.limit:
                self.DLL.add_to_head(key, value)
                self.size += 1
            elif already_exist == False and self.size == self.limit:
                self.DLL.add_to_head(key, value)
                self.DLL.remove_from_tail()

