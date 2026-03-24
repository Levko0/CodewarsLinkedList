from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    my_list = None
    my_list = push(my_list, 3)
    my_list = push(my_list, 2)
    my_list = push(my_list, 1)
    return my_list
