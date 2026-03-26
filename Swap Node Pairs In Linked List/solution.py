# from preloaded import Node

def swap_pairs(head):
    head2 = Node(next=head)
    prev = head2
    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first

    return head2.next
