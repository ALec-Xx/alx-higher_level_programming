#!/usr/bin/python3
"""Define classes for a singly-linked list"""

class Node: 
    """Represent a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation of new Node

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return (self.__data)

    @property
    def next_node(self):
        """property to retrieve next node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """Property setter to set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Property setter to set next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Simple instantiation of single linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted 
        position in the list (increasing order)

        Args:
            value (Node): The new Node to insert.
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
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
