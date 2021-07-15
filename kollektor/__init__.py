"""
Collection utility for Python.
"""


from typing import Any, Union


class Kollektor(object):
    """
    Base class for kollektor.
    """

    def __init__(self, *args: Any) -> None:
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

    def append(self, *args: Any) -> tuple:
        """
        Append one or more object to the collection.

        **Parameters**:
        - `*args`: The item(s) will be added.

        **Returns**:
        - `tuple`: Added items.
        """

        self.items = (*self.items, *args, )
        return args

    def remove(self, *args: Any) -> tuple:
        """
        Remove one or more object from the collection.

        **Parameters**:
        - `*args`: The item(s) will be removed.

        **Returns**:
        - `tuple`: New items.
        """

        filtered = tuple(value for value in self.items if value not in args)
        self.items = filtered

        return self.items

    def first(self) -> Union[Any, None]:
        """
        Get first element from the collection.

        **Returns**:
        - `Any`: object.
        - `None`
        """

        return self.items[0] if len(self.items) > 0 else None

    def last(self) -> Union[Any, None]:
        """
        Get last element from the collection.

        **Returns**:
        - `Any`: object.
        - `None`
        """

        return self.items[-1] if len(self.items) > 0 else None