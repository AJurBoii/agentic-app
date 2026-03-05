import linked_list


class hash_table:
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
    
    def remove(self, key: str) -> bool:
        hash_value = self.encode(key)
        if self.search(key):
            current = self.dictionary[hash_value].head
            prev = None
            while current:
                if current.value == key:
                    if prev:
                        prev.set_next(current.next)
                    else:
                        self.dictionary[hash_value].head = current.next
                    return True
                prev = current
                current = current.next
        return False

if __name__ == "__main__":
    hash_obj = hash_table()