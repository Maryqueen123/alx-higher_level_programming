#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """Invert int operators == and !=."""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, mother):
        """what was != is now =="""
        return int(self) != mother

    def __ne__(self, mother):
        """override != operatior with == operator"""
        return int(self) == other
