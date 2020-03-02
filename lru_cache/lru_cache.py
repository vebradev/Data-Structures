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
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key exists in storage:
        #   move node to the front of dll
        #   return node value
        if key in self.storage:
            node = self.storage[key]
            self.cache.move_to_front(node)
            return node.value[1]
        else:
            return

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
    def set(self, key, value):
        # if key exists in storage:
        #   replace node value with new arguments
        #   move node to front of dll
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.cache.move_to_front(node)
            return node
        
        # if cache is at limit: 
        #   delete entry from storage, 
        #   remove last element from dll, 
        #   decrement size
        if self.size == self.limit:
            del self.storage[self.cache.tail.value[0]]
            self.cache.remove_from_tail()
            self.size -= 1
        
        # add new element to cache:
        #   - new node at head, args passed
        #   - create record in storage with key pointing to new node
        #   - increment size
        self.cache.add_to_head((key, value))
        self.storage[key] = self.cache.head      
        self.size += 1
        
# for testing purposes using debugger
# c = LRUCache(5)
# c.set('item-one', 'ORANGES')
# c.set('item-two', 'APPLES')
# c.set('item-three', 1)
# c.get('item-two')
# c.set('item-four', 'BANANAS')
# c.set('item-five', 'GRAPES')
# c.set('item-six', 'CARROTS')
# c.get('item-one')