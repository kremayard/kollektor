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

    def has(self, item: Any) -> bool:
        """
        Check an object is in collection.

        **Parameters**:
        - item (`Any`): The item will be checked.

        **Returns**:
        - `bool`: True or False
        """

        return self.find(item) is not None