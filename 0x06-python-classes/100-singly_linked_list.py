#!/usr/bin/python3
"""SinglyLinkedList module.

This module contains a recreation of singly linked lists from C, but in Python.
Why bother recreating such an abomination in a language that doesn't need it?
Don't know, but that's what this is, and that's what you get.
No returns or refunds.

"""


class Node:
    """This class is a linked list node

    Attributes:
        __data (int): data stored in node
        __next_node (Node): next Node of the list

    """
    def __init__(self, data=0, next_node=None):
        """__init__ method

        Args:
            data (int): data stored in node
            next_node (Node): next node

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter

        Gets the value of private attribute __data

        Return:
            int: the value of data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter

        Sets the value of private attribute _data

        Args:
            value (int): value to be stored in __data
        Raises:
            TypeError: If ``value`` is not an int

        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter

        Gets the value of private attribute __next_node

        Return:
            Node: the next node in the list

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter

        Sets the value of private attribute __next_node

        Args:
            value (int): the next node
        Raises:
            TypeError: If ``value`` is not a Node class object

        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class is a singly linked list

    Attributes:
        __head (Node): head node of the list
        __next_node (Node): next Node of the list

    """
    def __init__(self):
        """__init__ method for SinglyLinkedList

        """
        self.__head = None
        self.__next_node = None

    def __str__(self):
        """Defines behavior when the object is printed

        Returns:
            str: A string of all elements

        """
        output = ""
        node = self.__head
        if node is not None:
            while node is not None:
                output += str(node.data)+"\n"
                node = node.next_node

        return output[:-1]

    def sorted_insert(self, value):
        """Inserts a new node at sorted position in the list

        Args:
            value (int): value to store at correct index
        """
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
