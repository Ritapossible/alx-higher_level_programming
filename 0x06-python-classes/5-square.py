#!/usr/bin/python3
""" The Class Square that defines a square by
    Private instance attribute: size
    Getter and Setters
    The Instantiation with optional size
    size must be an integer
    Public instance method: def area(self)
    Public instance method: def my_print(self)
"""


class Square:
    """The Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """The Size getter"""
    @property
    def size(self):
        return self.__size

    """The Size setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """Returns the current square area."""
    def area(self):
        return self.__size ** 2

    """This prints in stdout the square with the character #"""
    def my_print(self):
        if self.size != 0:
            for char in range(self.size):
                print('#' * self.size)
        else:
            print()
