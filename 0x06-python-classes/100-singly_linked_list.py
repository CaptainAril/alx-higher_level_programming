#!/usr/bin/python3
"""This module defines classes for singly linked lists."""


class Node:
    """Creates a class for signly linked lists nodes."""

    def __init__(self, data, next_node=None):
        """Defines the attributes for each Node instance.

        Args:
            data (int): The data of the new Node.
            next_node (Node): Next Node of node. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the Node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the Node data.

        Args:
            value (int): The Node data.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Creates a singly-linked list class."""

    def __init__(self):
        """Initializes a new Singly-Linked List instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted position.

        Args:
            value (int): New node to be inserted.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of a Singly-Linked List."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
