"""
We have modules use xml.
Now, we get a new module that use json.
-> define a class that inherits new module to convert the format.

https://refactoring.guru/design-patterns/adapter
"""

class Target:  # raw module use xml
    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:  # new module use json
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):  # inherits new module
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    print(target.request(), end="")
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    print(adapter.request(), end="")