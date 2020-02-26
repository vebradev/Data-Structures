# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

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
        print(f"Target: {target} vs value: {self.value}")
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
    # def get_max(self):
    #     # can go right? go and run get_max again
    #     # else: return the value
    #     if self.right != None:
    #         return self.get_max()
    #     else:
    #         return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

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