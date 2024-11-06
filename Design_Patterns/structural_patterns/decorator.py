"""
We have a base class called "Notifier",
and "SMS Notifier", "FB Notifier", "Slack Notifier" inherits it.

However, we need "SMS+FB Notifier", "Slack+SMS Notifier", ...

Solution: Wrapping

https://refactoring.guru/design-patterns/decorator/python/example
"""

class Component:  # Raw interface
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):  # Raw class
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(f"RESULT: {simple.operation()}", end="")
    print("\n")

    # Note how decorators can wrap not only simple components but the other decorators as well.
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    print(f"RESULT: {decorator2.operation()}", end="")