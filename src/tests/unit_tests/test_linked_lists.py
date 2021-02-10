from unittest import TestCase
from unittest.mock import call, patch

from linked_lists.linked_lists import LinkedList, LinkedListNode


class LinkedListNodeClass(TestCase):
    def setUp(self):
        self.linked_list_node = LinkedListNode(None, 2)

    def test_instance(self):
        self.assertEqual(self.linked_list_node.next_node, None)
        self.assertEqual(self.linked_list_node.value, 2)

    def test_repr(self):
        self.assertEqual(
            repr(self.linked_list_node),
            "LinkedListNode(next_node=None, value=2)",
        )

    def test_str(self):
        self.assertEqual(str(self.linked_list_node), "2")


class LinkedListClassTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_instance(self):
        self.assertEqual(self.linked_list.head, None)

    def test_repr(self):
        self.linked_list.head = LinkedListNode(None, 2)
        self.assertEqual(
            repr(self.linked_list),
            "LinkedList(head=2)",
        )

    def test_str(self):
        self.linked_list.head = LinkedListNode(None, 2)
        self.assertEqual(str(self.linked_list), "2")


class LinkedListAddTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_add_first_node(self):
        self.linked_list.add(2)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.head.next_node, None)

    def test_add_two_nodes(self):
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.head.next_node.value, 3)
        self.assertEqual(self.linked_list.head.next_node.next_node, None)


class LinkedListAppendTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append_first_node(self):
        self.linked_list.append(2)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.head.next_node, None)

    def test_append_two_nodes(self):
        self.linked_list.append(2)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.head.next_node.value, 3)
        self.assertEqual(self.linked_list.head.next_node.next_node, None)


class LinkedListRemoveFirstTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.head = LinkedListNode(None, 2)

    def test_remove_node_with_empty_tree(self):
        self.linked_list = LinkedList()
        with self.assertRaises(AttributeError):
            self.linked_list.remove_first()

    def test_remove_only_node(self):
        self.linked_list.remove_first()
        self.assertEqual(self.linked_list.head, None)

    def test_remove_first(self):
        last_node = LinkedListNode(None, 4)
        self.linked_list.head.next_node = LinkedListNode(last_node, 3)

        self.linked_list.remove_first()
        self.assertEqual(self.linked_list.head.value, 3)
        self.assertEqual(self.linked_list.head.next_node.value, 4)
        self.assertEqual(self.linked_list.head.next_node.next_node, None)


class LinkedListRemoveLastTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.head = LinkedListNode(None, 2)

    def test_remove_node_with_empty_tree(self):
        self.linked_list = LinkedList()
        with self.assertRaises(AttributeError):
            self.linked_list.remove_last()

    def test_remove_only_node(self):
        self.linked_list.remove_last()
        self.assertEqual(self.linked_list.head, None)

    def test_remove_first(self):
        last_node = LinkedListNode(None, 4)
        self.linked_list.head.next_node = LinkedListNode(last_node, 3)

        self.linked_list.remove_last()
        self.assertEqual(self.linked_list.head.value, 2)
        self.assertEqual(self.linked_list.head.next_node.value, 3)
        self.assertEqual(self.linked_list.head.next_node.next_node, None)


class LinkedListPrintTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        third_node = LinkedListNode(None, 3)
        second_node = LinkedListNode(third_node, 2)
        first_node = LinkedListNode(second_node, 1)
        self.linked_list = LinkedList()
        self.linked_list.head = first_node

    @patch("builtins.print")
    def test_print(self, print_mock):
        self.linked_list.print()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 4)]
        )
