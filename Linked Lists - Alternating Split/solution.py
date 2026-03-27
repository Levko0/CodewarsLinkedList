class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes")

    current = head

    first_head = head
    second_head = head.next
    first_tail = first_head
    second_tail = second_head
    current = head.next.next

    while current and current.next:
        first_tail.next = current
        first_tail = first_tail.next

        second_tail.next = current.next
        second_tail = second_tail.next

        current = current.next.next

    if current:
        first_tail.next = current
        first_tail = first_tail.next

    first_tail.next = None
    second_tail.next = None

    return Context(first_head, second_head)
