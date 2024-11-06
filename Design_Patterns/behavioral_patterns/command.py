"""
Too many commands will be executed sequentially, so invoke a Invoker that collects the commands and execute by run
e.g. Trainer

Comparison:
Proxy is for multiple user. Command is for single user.
"""
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing ({self._payload})")


class ComplexCommand(Command):
    def __init__(self, a: str, b: str) -> None:
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        print(f"\nReceiver: Working on ({self._a})", end="")
        print(f"\nReceiver: Also working on ({self._b})", end="")


class Invoker:  # commands collector
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:  # consume all colleted commands (run)
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize an invoker with any commands.
    """
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    invoker.set_on_finish(ComplexCommand("Send email", "Save report"))
    invoker.do_something_important()