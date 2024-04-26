# Implemente una clase bajo el patrón observer donde una serie de clases están subscriptas, cada clase 
# espera que su propio ID (una secuencia arbitraria de 4 caracteres) sea expuesta y emitirá un mensaje 
# cuando el ID emitido y el propio coinciden. Implemente 4 clases de tal manera que cada una tenga un ID
# especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con ID para el que tenga una 
# clase implementada.
from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice
from string import ascii_uppercase
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, id_: str) -> None:
        pass


class ConcreteSubject(Subject):
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Adjuntó un observador.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, id_: str) -> None:
        print(f"Subject: Notificando observadores para el ID: {id_}")
        for observer in self._observers:
            observer.update(id_)


class Observer(ABC):
    @abstractmethod
    def update(self, id_: str) -> None:
        pass


class ConcreteObserverA(Observer):
    _id: str

    def __init__(self, id_: str) -> None:
        self._id = id_

    def update(self, id_: str) -> None:
        if id_ == self._id:
            print(f"ConcreteObserverA: Reaccionó al ID {id_}")


class ConcreteObserverB(Observer):
    _id: str

    def __init__(self, id_: str) -> None:
        self._id = id_

    def update(self, id_: str) -> None:
        if id_ == self._id:
            print(f"ConcreteObserverB: Reaccionó al ID {id_}")


class ConcreteObserverC(Observer):
    _id: str

    def __init__(self, id_: str) -> None:
        self._id = id_

    def update(self, id_: str) -> None:
        if id_ == self._id:
            print(f"ConcreteObserverC: Reaccionó al ID {id_}")


class ConcreteObserverD(Observer):
    _id: str

    def __init__(self, id_: str) -> None:
        self._id = id_

    def update(self, id_: str) -> None:
        if id_ == self._id:
            print(f"ConcreteObserverD: Reaccionó al ID {id_}")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA("ABCD")
    subject.attach(observer_a)

    observer_b = ConcreteObserverB("WXYZ")
    subject.attach(observer_b)

    observer_c = ConcreteObserverC("1234")
    subject.attach(observer_c)

    observer_d = ConcreteObserverD("ABCD")
    subject.attach(observer_d)

    # Emitir 8 IDs y notificar a los observadores
    for _ in range(8):
        id_ = ''.join(choice(ascii_uppercase) for _ in range(4))
        subject.notify(id_)