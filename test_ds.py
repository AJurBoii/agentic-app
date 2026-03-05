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

        assert str(ll) == "Node(1) -> Node(2) -> Node(3)"

        assert ll.pop() == 1
        assert ll.pop() == 2
        assert ll.pop() == 3
        assert isinstance(ll.pop(), IndexError)


if __name__ == "__main__":
    unittest.main()
