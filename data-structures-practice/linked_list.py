class linked_list_node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value})"

class linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = linked_list_node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.set_next(new_node)

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return " -> ".join(nodes)