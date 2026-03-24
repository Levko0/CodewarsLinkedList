# from preloaded import Node
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None' or list_repr == 'null':
        return None
    parts = list_repr.split(' -> ')

    values = parts[:-1]

    head = None

    for val in reversed(values):
        head = Node(int(val), head)

    return head
