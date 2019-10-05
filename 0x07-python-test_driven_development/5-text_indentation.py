#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of these characters: ., ? and :

        Parameters:
            :param text: string

        Raises:
            TypeError: if text are not string

        Return:
            None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for sep in ['. ', '? ', ': ']:
        text = text.replace(sep, '{}\n\n'.format(sep[0]))

    print(text, end='')
