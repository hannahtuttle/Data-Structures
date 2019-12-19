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
        # if inserting we must already have a tree/root
        # if value is less that self.value go left, make a new node/tree if its empty, otherwise keep going (recursion)
        # if greater that/equal to the go right, make a new tree/node if epty otherwise keep going (recursion)

        def recurse_inner(node, value):
            new_node = BinarySearchTree(value)
            current = node
            if value >= node.value and node.right == None:
                node.right = new_node
                return
            elif value < node.value and node.left == None:
                node.left = new_node
                return
            elif value >= node.value and node.right != None:
                current = node.right
            elif value < node.value and node.left != None:
                current = node.left
            recurse_inner(current, value)

        return recurse_inner(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target, node='friend'):
        # if target == self.value return it
        #go left or right based on smaller or greater
        if node == 'friend':
            node = self
       
        if node == None:
            return False
        elif node.value == target:
            # print('something else')
            # print('value', node.value, target)
            return True
        else:
            if target < node.value:
                node = node.left
            elif target >= node.value:
                node = node.right
                # print('check')

            
        # print('hello', self.value)
        # print(inner(self, target))
        return self.contains(target, node)


    # Return the maximum value found in the tree
    def get_max(self):
        # if right exisits go right
        #otherwise return self.value
        max_value = self.value
        def inner(node):
            nonlocal max_value
            if node == None:
                return
            else:
                max_value = node.value
                node = node.right
            return inner(node)
        inner(self)
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        def inner(node, cb):
            if node == None:
                return
            cb(node.value)
            # print(node.value)
            inner(node.left, cb)
            inner(node.right, cb)
        
        return inner(self, cb)

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

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
