from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length > 0:
            return self.storage.remove_from_head()
        return

    def len(self):
        return self.storage.length
