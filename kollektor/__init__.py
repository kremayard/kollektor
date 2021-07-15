"""
Collection utility for Python.
"""


from typing import Any, Union


class Kollektor(object):
    """
    Base class for kollektor.
    """

    def __init__(self, *args) -> None:
        """
        Construct a new 'Kollektor' object.

        **Parameters**:
        - `*args`: items for collection.
        """

        self.items: tuple = args

    def find(self, item: Any) -> Union[Any, None]:
        """
        Find an object from collection.

        **Parameters**:
        - item (`Any`): The item will be found.

        **Returns**:
        - `Any`: Found object.
        - `None`
        """

        for value in self.items:
            if value == item:
                return value

        return None
