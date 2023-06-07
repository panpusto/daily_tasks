import sys
import unittest
from io import StringIO

from model import Node, LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_create_node(self):
        node = Node(10)

        self.assertEqual(node.data, 10)

    def test_append_data_to_linked_list(self):
        self.linked_list.append(1)

        self.assertEqual(self.linked_list.count(), 1)
    
    def test_insert_data_at_position_with_valid_param(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        before_insert = self.linked_list.count()
        self.linked_list.insert(10, 3)

        self.assertEqual(self.linked_list.count(), before_insert + 1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next.data, 2)
        self.assertEqual(self.linked_list.head.next.next.data, 10)
        self.assertEqual(self.linked_list.head.next.next.next.data, 3)

    def test_insert_data_at_position_with_invalid_param(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        with self.assertRaises(IndexError):
            self.linked_list.insert(10, 10)
    
    def test_remove_data_with_value(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)
        before_delete = self.linked_list.count()
        self.linked_list.remove(2)

        self.assertEqual(self.linked_list.count(), before_delete - 1)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next.data, 3)

    def test_count_nodes_in_list(self):
        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.append(3)

        self.assertEqual(self.linked_list.count(), 3)
    
    def test_print_nodes_in_list(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        self.linked_list.append(1)
        self.linked_list.append(2)
        self.linked_list.print()

        sys.stdout = sys.__stdout__

        printed_output = captured_output.getvalue().strip()
        expected_output = "1\n2"
        self.assertEqual(printed_output, expected_output)


if __name__ == '__main__':
    unittest.main()
