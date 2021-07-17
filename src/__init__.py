"""
Collection utility for Python.
"""


from typing import Any, Callable, Union
from .classes import Nothing


class Kollektor(object):
    """Base class for kollektor.

    Attributes:
        items (tuple): All of the items in the collection.
    """

    def __init__(self, *args: Any) -> None:
        self.items: tuple = args

    @property
    def length(self) -> int:
        """Get collection length.

        Returns:
            int: Collection length.
        """

        return len(self.items)

    def find(self, item: Any) -> Union[Any, Nothing]:
        """Find an object from collection.

        Parameters:
            item: The item will be found.

        Returns:
            Any: Found object.
            kollektor.Nothing`
        """

        for value in self.items:
            if value == item:
                return value

        return Nothing

    def has(self, item: Any) -> bool:
        """Check an object is in collection.

        Parameters:
            item: The item will be checked.

        Returns:
            bool: True or False
        """

        return self.find(item) is not None

    def append(self, *args: Any) -> tuple:
        """Append one or more object to the collection.

        Parameters:
            *args: The item(s) will be added.

        Returns:
            tuple: Added items.
        """

        self.items = (*self.items, *args, )
        return args

    def remove(self, *args: Any) -> tuple:
        """Remove one or more object from the collection.

        Parameters:
            *args: The item(s) will be removed.

        Returns:
            tuple: New items.
        """

        filtered = tuple(value for value in self.items if value not in args)
        self.items = filtered

        return self.items

    def first(self) -> Union[Any, Nothing]:
        """Get first element from the collection.

        Returns:
            Any: object.
            kollektor.Nothing
        """

        return self.items[0] if len(self.items) > 0 else Nothing

    def last(self) -> Union[Any, Nothing]:
        """Get last element from the collection.

        Returns:
            Any: object.
            kollektor.Nothing
        """

        return self.items[-1] if len(self.items) > 0 else Nothing

    def index(self, index: int) -> Union[Any, Nothing]:
        """Find an object from collection with index.

        Returns:
            Any: object.
            kollektor.Nothing
        """

        try:
            return self.items[index]
        except IndexError:
            return Nothing

    def filter(self, fn: Callable) -> tuple:
        """Filter objects from collection.

        Returns:
            tuple: Filtered object(s).
        """

        return tuple(value for value in self.items if fn(value))

    def each(self, fn: Callable) -> list:
        """Iterate objects from collection.

        Returns:
            list: List of returned values.
        """

        return [fn(index, value) for index, value in enumerate(self.items[:])]