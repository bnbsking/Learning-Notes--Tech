"""
Everybody access DB cause low performance.

Solution: use proxy
"""

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):  # real access to DB
    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):  # proxy that accept clients requests and send them to RealSubject 
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.request()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    real_subject.request()

    print()

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    proxy.request()