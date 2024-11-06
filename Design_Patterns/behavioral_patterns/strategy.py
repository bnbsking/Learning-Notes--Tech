"""
Strategy classes defines a family of algorithms.
Main instance use one subclass of interface (remember DIP).
combinations(N,1)

Robustness of Python P.288
"""

from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.do_algorithm(data)

data = [1, 3, 2, 5, 4]

context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # Output: [1, 2, 3, 4, 5]

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # Output: [5, 4, 3, 2, 1]
