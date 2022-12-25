#!/usr/bin/python3

""" A script to implement Linked List Data Structure in Python """


class Node:
    """ defines a node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ Initialize a node instance.
        Args:
            data (integer): Value of the new node.
            next_node (Node): next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter Method to retrieve node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter Method to set node value """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter Method to retrieve address of next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Setter Method to set next node address"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        """Sets the necessary attributes for the SinglyLinkedList object."""
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
