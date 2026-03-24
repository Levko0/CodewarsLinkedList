def stringify(node):
    result = ''

    if not node:
        return "None"
    while node:
        current = node.data
        result += str(current) + ' -> '
        node = node.next

    return result + 'None'
