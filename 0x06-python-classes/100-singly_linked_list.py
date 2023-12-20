#!/usr/bin/python3
"""Represents a Node of a singly linked list"""


class Node:
    """This class defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node instance with data and next_node.

        Args:
            data: The data value for the node.
            next_node: The next node in the linked list.

        Raises:
            TypeError: If data is not an integer or
            next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node.

        Args:
            value: The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next node in the linked list.

        Args:
            value: The next node to set.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list."""

    def __init__(self):
        """Initializes a SinglyLinkedList instance with an empty list."""
        self.head = None

    def __str__(self):
        """Returns a string representation of the entire linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value: The value for the new Node.
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


# Example usage:
linked_list = SinglyLinkedList()
linked_list.sorted_insert(5)
linked_list.sorted_insert(3)
linked_list.sorted_insert(7)
print(linked_list)
