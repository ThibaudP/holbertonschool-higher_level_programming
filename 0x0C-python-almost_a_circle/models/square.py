#!/usr/bin/python3
"""Square module"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """sets the string behavior for Square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        self.integer_validator("size", value)
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method for square class"""
        labels = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                if i > 3:
                    raise TypeError("Square.update() takes 4 arguments\
                                    or less")
                if labels[i] is "id" and args[i] is not None:
                    self.id = args[i]
                else:
                    self.integer_validator(labels[i], args[i])
                    setattr(self, labels[i], args[i])
        else:
            for k, v in kwargs.items():
                if k is "id" and v is not None:
                    self.id = v
                elif k in labels:
                    self.integer_validator(k, v)
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square object"""
        return {"id": self.id, "x": self.x, "y": self.y, "size": self.size}
