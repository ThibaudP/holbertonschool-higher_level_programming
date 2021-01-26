#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """sets string behavior of Rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validator method for all Rectangle attributes"""
        if type(value) is not int:
            raise TypeError(name+" must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(name+" must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(name+" must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """Displays a rectangle"""
        for x in range(self.y):
            print('')
        for x in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """updates the value of a given instance"""
        labels = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                if i > 4:
                    raise TypeError("Rectangle.update() takes 5 arguments\
                                    or less")
                if labels[i] is "id" and args[i] is not None:
                    self.id = args[i]
                elif args[i] is not None:
                    setattr(self, labels[i], args[i])
        else:
            for k, v in kwargs.items():
                if k is "id" and v is not None:
                    self.id = v
                elif k in labels and v is not None:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle object"""
        return {"id": self.id, "x": self.x, "y": self.y,
                "width": self.width, "height": self.height}
