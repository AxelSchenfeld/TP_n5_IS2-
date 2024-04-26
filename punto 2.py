# Implemente una clase bajo el patrón iterator que almacene una cadena de caracteres y permita 
# recorrerla en sentido directo y reverso.
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class CharIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: str, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self):
        if 0 <= self._position < len(self._collection):
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
            return value
        else:
            raise StopIteration()


class CharCollection(Iterable):
    def __init__(self, collection: str = "") -> None:
        self._collection = collection

    def __iter__(self) -> CharIterator:
        return CharIterator(self._collection)

    def get_reverse_iterator(self) -> CharIterator:
        return CharIterator(self._collection, reverse=True)

    def append(self, char: str):
        self._collection += char


if __name__ == "__main__":
    collection = CharCollection()
    collection.append("Hello, World!")

    print("Directo:")
    print("".join(collection))

    print("\nReverso:")
    print("".join(collection.get_reverse_iterator()))