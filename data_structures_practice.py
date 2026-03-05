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

class hash_object:
    def __init__(self):
        self.dictionary = {}
    
    def encode(self, key: str) -> int:
        # custom hash function because using built-in hash() is boring and can also lead to collisions
        hash_value = 0
        for i, char in enumerate(key):
            hash_value += ord(char) * (i + 1)
        return hash_value % (2 ** 32) # prevents absurdly large hash values
    
    def add_bucket(self, hash_value: int, value: any):
        if hash_value not in self.dictionary:
            self.dictionary[hash_value] = linked_list()
        self.dictionary[hash_value].append(value)

    def add(self, key: str):
        hash_value = self.encode(key)
        self.add_bucket(hash_value, key)

    def search(self, key: str) -> bool:
        hash_value = self.encode(key)
        if hash_value in self.dictionary:
            current = self.dictionary[hash_value].head
            while current:
                if current.value == key:
                    return True
                current = current.next
        return False

if __name__ == "__main__":
    hash_obj = hash_object()