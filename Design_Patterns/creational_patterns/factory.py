"""
Raw:
   Creator -> Product        -> Product.operate()
or Factory -> transportation -> transportation.transport()

Soulution:
abstract Product

https://refactoring.guru/design-patterns/abstract-factory
"""
from abc import ABC, abstractmethod


class Product(ABC):  # transportation
    @abstractmethod
    def operation(self) -> str:  # transport
        pass


class ConcreteProduct1(Product):  # e.g. Truck
    def operation(self) -> str:  # transport
        return "product 1 operation"


class ConcreteProduct2(Product):  # e.g. Ship
    def operation(self) -> str:  # transport
        return "product 2 operation"


if "Simple factory pattern":
    class SimpleFactoryCreator:
        def __init__(self, product: Product):
            self.product = product

        def product_operation(self) -> None:
            print(self.product.operation())


    def main_simple_factory(product_name: str):
        product = globals()[product_name]()
        SimpleFactoryCreator(product).product_operation()


    main_simple_factory("ConcreteProduct1")
    main_simple_factory("ConcreteProduct2")


if "Factory pattern":
    class Creator(ABC):  # factory
        @abstractmethod
        def factory_method(self):
            pass

        def product_operation(self) -> str:
            product = self.factory_method()
            print(product.operation())
        

    class ConcreteCreator1(Creator):
        def factory_method(self) -> Product:
            return ConcreteProduct1()


    class ConcreteCreator2(Creator):
        def factory_method(self) -> Product:
            return ConcreteProduct2()


    def main(creator: str) -> None:
        globals()[creator]().product_operation()


    main("ConcreteCreator1")
    main("ConcreteCreator2")

