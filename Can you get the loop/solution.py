def loop_size(node):

    slow = node.next
    fast = node.next.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    length = 1
    current = slow.next
    while current != slow:
        current = current.next
        length += 1

    return length
