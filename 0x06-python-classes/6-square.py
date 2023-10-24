#!/usr/bin/python3
""" A Class Square that defines a square by
    Private instance attribute: size
    Private instance attirubute: position
    Getter and Setters
    The Instantiation with optional size
    size must be an integer
    Public instance method: def area(self)
    Public instance method: def my_print(self)
"""


class Square:
    """The Class constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """The Position getter"""
    @property
    def position(self):
        return self.__position

    """The Position getter"""
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    """This returns the current square area"""
    def area(self):
        return self.__size ** 2

    """This prints in stdout the square with the character #"""
    def my_print(self):
        if self.size != 0:
            if self.position[1] is not 0:
                print('\n' * self.position[1], end='')
            for char in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
        else:
            print()
