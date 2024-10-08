#!/usr/bin/python3
"""
include basegeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangele
    """

    def __init__(self, width, height):
        """
        check from 7th file
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return str
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
