#!/usr/bin/python3
""" Rectangle Class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init Variables

        :param width: of the rectangle
        :param height: of the rectangle
        :param x: position
        :param y: position
        :param id: of the rectangle
        """

        self.height = height
        self.width = width

        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def height(self):
        """ Get __height value """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set __height value """

        if not isinstance(value, (int, float, bool)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def width(self):
        """ Get __width value """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set __width value """

        if not isinstance(value, (int, float, bool)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def x(self):
        """ Get __x value """

        return self.__x

    @x.setter
    def x(self, value):
        """ Set __x value """

        if not isinstance(value, (int, float, bool)):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @property
    def y(self):
        """ Get __y value """

        return self.__y

    @y.setter
    def y(self, value):
        """ Set __y value """

        if not isinstance(value, (int, float, bool)):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")

        self.__y = value

    def area(self):
        """ Return area of the a rectangle """

        return self.__width * self.__height

    def display(self):
        """ Displays the rectangle with a # sign """

        print("\n" * self.__y, end="")

        print((" " * self.__x + "#" * self.__width + "\n") *
              self.__height, end="")

    def __str__(self):
        """ Str Method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Update attributes of the class """

        args = list(args)

        try:
            if len(args) > 0:
                self.id = args[0]

                self.width = args[1]
                self.height = args[2]

                self.x = args[3]
                self.y = args[4]
            else:
                for key in kwargs.keys():
                    setattr(self, key, kwargs[key])

        except IndexError:
            pass

    def to_dictionary(self):
        """
        Return dictionary as representation of allí attributes of a triangle
        """

        dictionary = {'id': self.id, 'width': self.__width,
                      'height': self.__height, 'x': self.__x, 'y': self.__y}

        return dictionary
