import unittest

from data_structures_practice import hash_table, linked_list


class TestMain(unittest.TestCase):
    def test_linked_list(self):
        ll = linked_list.LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        assert ll.head.value == 1
        assert ll.head.next.value == 2
        assert ll.head.next.next.value == 3


if __name__ == "__main__":
    unittest.main()
