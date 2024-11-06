"""
Adventures: 4 types, e.g. warrior, archer, ....
Equipment: 5 types, e.g. clothes, pants, shoes, hat, weapons
Each adventure can choose multiple equipments

Raw:
subclasses: multiple combinations

Solution:
abstract equipment factory 1 -> 5 equipment factory
abstract adventurer factory 1 -> 4 adventure factory that has serveral methods of equipment
subclasses = 5+4 = 9

Comparison:
Both builder and abstract factory narrow downs the number of subclasses.
builder focus on the step by step permutation to build the result in Director class, (permutations(M,N))
whereas abstract factory focus on the combination that returns the result directly. (M * N)

https://skyyen999.gitbooks.io/-study-design-pattern-in-java/content/abstractFactory1.html
https://refactoring.guru/design-patterns/abstract-factory
"""

from abc import ABC, abstractmethod


class AbstractProductA(ABC):  # clothes
    @abstractmethod
    def useful_function_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):  # clothes 1
    def useful_function_a(self) -> str:
        return "The result of the product A1."

class ConcreteProductA2(AbstractProductA):  # clothes 2
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):  # pants
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

class ConcreteProductB1(AbstractProductB):  # pants 1
    def useful_function_b(self) -> str:
        return "The result of the product B1."

class ConcreteProductB2(AbstractProductB):  # pants 2
    def useful_function_b(self) -> str:
        return "The result of the product B2."


class AbstractFactory(ABC):  # character factory
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):  # warrior factory
    def create_product_a(self) -> AbstractProductA:  # clothes
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:  # pants
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):  # archer factory
    def create_product_a(self) -> AbstractProductA:  # clothes
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:  # pants
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())