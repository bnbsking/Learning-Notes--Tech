"""
Decouple RedCircle, RedSquare, BlueCircle, BlueSquare.

The factory is abstract in abstract factory, but can be real here.

https://refactoring.guru/design-patterns/bridge
"""

from abc import ABC, abstractmethod


class Implementation(ABC):  # color
    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):  # red
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):  # blue
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


class Abstraction:  # shape
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):  # Circle
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    print(abstraction.operation(), "\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    print(abstraction.operation())