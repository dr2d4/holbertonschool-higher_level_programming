#!/usr/bin/python3
""" Square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Init Variables

        :param size: of the square
        :param x: position
        :param y: position
        :param id: of the square
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Str Method """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ Get size value """

        return self.width

    @size.setter
    def size(self, value):
        """ Set size value """

        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """ Update attributes of the class """

        args = list(args)

        try:
            if len(args) > 0:
                self.id = args[0]

                self.size = args[1]

                self.x = args[2]
                self.y = args[3]
            else:
                for key in kwargs.keys():
                    setattr(self, key, kwargs[key])

        except IndexError:
            pass

    def to_dictionary(self):
        """ Returns attributes of the object """

        dictionary = {'id': self.id, 'size': self.size, 'x': self.x,
                      'y': self.y}

        return dictionary
