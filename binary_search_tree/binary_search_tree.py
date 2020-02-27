import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # do comparison on value being passed
        # and decide which way to traverse, left or right
        if value < self.value:
            # go left
            # if attr .left is equal to None:
            #   create new node
            # else:
            #   call insert method on node in that position
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            # go right
            # if attr .right is equal to None:
            #   create new node
            # else:
            #   call insert method on node in that position
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # do comparison on value being passed
        # decide which way to traverse, l or r
        if target is self.value:
            return True
        
        if target < self.value:
            # go left
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            # go right
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # can go right? go and run get_max again
        # else: return the value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb passing in value of node
        # if left field is not empty:
            # call for_each on node with cb passed
        # if right field is not empty:
            # call for_each on node with cb passed
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print value if it exists
        # terminate if it doesn't
        if node is None:
            return
        # traverse to the end of left
        node.in_order_print(node.left)
        # print value of last node
        print(node.value)
        # traverse right once finished with left
        node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create new instance of Queue and enqueue node
        bft_queue = Queue()
        bft_queue.enqueue(node)
        # iterate over queue while it has node inside
        while bft_queue.len() > 0:
            # dequeue head and print it's value
            element = bft_queue.dequeue()
            print(element.value)
            # if element has l or r props
                # enqueue them
            if element.left:
                bft_queue.enqueue(element.left)
            if element.right:
                bft_queue.enqueue(element.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(node)
        while dft_stack.len() > 0:
            element = dft_stack.pop()
            print(element.value)
            if element.right:
                dft_stack.push(element.right)
            if element.left:
                dft_stack.push(element.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

tree = BinarySearchTree(5)
tree.insert(7)
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(6)
tree.insert(10)
tree.insert(88)
# tree.contains(88)