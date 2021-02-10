from unittest import TestCase
from unittest.mock import call, patch

from linked_lists.linked_lists import LinkedList


class LinkedListIntegrationTestCase(TestCase):
    def setUp(self):
        linked_list = LinkedList()
        linked_list.add(3)
        linked_list.add(2)
        linked_list.add(1)
        linked_list.add(0)

        linked_list.append(4)
        linked_list.append(5)
        linked_list.append(6)
        linked_list.append(7)

        linked_list.remove_first()  # remove 0
        linked_list.remove_last()  # remove 7

        self.linked_list = linked_list

    @patch("builtins.print")
    def test_print(self, print_mock):
        self.linked_list.print()
        self.assertEqual(
            print_mock.mock_calls,
            [call(number, end="-") for number in range(1, 7)]
        )
