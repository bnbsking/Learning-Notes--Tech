"""
How to design an extenable finite state machine (FSM)?

https://refactoring.guru/design-patterns/state
"""

from abc import ABC, abstractmethod

State = None

class Context:  # the current pointer of user
    _state = None
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):  # can be changed at runtime
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self  # actually, state and context are bidirectional.

    def request1(self):  # State.handle1 can contains changing to next state
        self._state.handle1()

    def request2(self):  # State.handle2 can contains changing to next state
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    print()
    context.request2()