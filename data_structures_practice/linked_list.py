class LinkedListNode:
    def __init__(self, value: any) -> None:
        self.value = value
        self.next = None

    def set_next(self, next_node: "LinkedListNode") -> None:
        self.next = next_node

    def __repr__(self) -> str:
        return f"Node({self.value})"


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value: any) -> None:
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.set_next(new_node)

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return " -> ".join(nodes)
