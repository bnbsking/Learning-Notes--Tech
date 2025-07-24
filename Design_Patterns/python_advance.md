## 1 type annotation

#### 1.1 code

```python
from typing import Callable, Dict, List, Tuple

L: List[Tuple[int, int]] = [(1,2), (3,5), (7,6)]
D: Dict[str, Dict[str, List[int]]] = {"a": {"b": [1,2]}}
def process_a(a: List[Tuple[int, int]]) -> Dict[str, Dict[str, List[int]]]:
    Pass

L: List[Tuple[int]] = [(1,2)]
D: Dict[Tuple[int, int], List[Tuple[int, int, int]]] = {(1, 2): [(3, 4, 5), (6, 7, 8)]}

def wrap(f: Callable[[], int]):
    return f
def f():
    return 1

#—---

from typing import Literal
a: Literal[“apple”, “banana”, “cat”]

#—---

from typing import NewType
sanitized_str = NewType(“SanitizedStr”, output_str)
#E.g.1. prevent sql injection
#E.g.2. Simplify complex type

#—---

from typing import Final # Constant
a: Final = “str”

#—---

from typing import TypedDict

class Range(TypedDict):
    min: float  # can also be nested
    max: float

D: Range = {"min": 5, "max": 10}  # key must same as Range
#print(type(D))  # dict. TypedDict is just for checking

class Range2(TypedDict, total=False):
    min: float
    max: float
    x: Optional[float]  # allow optional key

E: Range2 = {"min": 5, "max": 10}

#—---

#To verify the input type and output type be relative same type (absolute type unknown)

from typing import TypeVar

T = TypeVar('T')
def h(a: T) -> T:
    return a

#—---

from typing import Generic, TypeVar
# Extension of TypedDict into general class type

T2 = TypeVar('T2')

class B(Generic[T2]):  # must used with TypeVar
    val: int = 5  # if not specified, no this attribute

obj: B = B()
print(obj.val)

#—---

#Self-defined type
#From collections import UserDict, UserList, UserString
# or use collections.abc.Set
# remember use self.data.xxx instead of self.xxx
```

#### 1.2 concepts

Function input and output use type annotation is enough.
“Any” is type for anything but it lose the value of type annotation

#### 1.3 tools - mypy

```bash
pip install mypy
mypy xxx.py
```

However, mypy is not omnipotent:
```python
def g():
    return 1 if False else "a"
x: int = g()
print(x)

#—---

from typing import Optional, Union

a: Optional[str] = “a”
b: Union[str, None] = “b” # they are the same

#However, mypy raise error:
a: Optional[str] = "a”
print(a.replace) # "Optional[str]" has no attribute "replace"

#So, it would be better:
#a: Optional[str] = "a”
#if a is not None:
#    print(a.replace)

#—---

#Customize mypy
#E.g. mypy --disallow-any-generics
#Or
#E.g. create file mypy.ini
```

config
```
[mypy]
disallow_any_generics = True
```

#### 1.4 More tools

+ VSCode python extension installs Pylance (just like mypy). Including
    + Annotation check
    + library check
    + links to source code 
    + Jupyter
    + isort (library sort). e.g. isort a.py

+ MonkeyType: auto type annotation
+ PyType: more flexible but more risk

For a large project, do type annotation at the core part.

===

+ Typedict: static time checking
+ Pydantic (3rd party): runtime checking

```python
from pydantic.dataclasses import dataclass

@dataclass
class A:
    X: str
    Y: int

#or

from pydantic import BaseModel

class A(BaseModel, extra=”allow”):
	File_name: str

A.model_validate(x)
```


## 2 Advanced types

#### 2.1 types

```python
#@dataclass(frozen=True) let the class be constant and hashable
# Note that Enum is class-behaved, not object behaved!

from enum import Enum

class C(Enum):
    k1 = 1 # or enum.auto()
    k2 = 1

print(C.k1, C.k1.value) # C.k1, 1
print(C(1)) # C.k1 # inverse

#Or to unique the inversion

from enum import Enum, unique

@unique
class C(Enum):
    k1 = 1
    k2 = 2

print(C.k1, C.k1.value) # C.k1, 1
print(C(1)) # C.k1 # inverse
```

#### 2.2 concepts

+ When to use TypedDict when to use Enum? Static vs Dynamic

+ hashable
    + yes
        + Enum
        + dataclass(frozen=True)
    + no
        + dataclass
        + normal class

+ about dataclass
    + homogeneous data: use dict
    + heterogeneous data: use dataclass
        + dataclass can replace TypeDict since it can define methods
        + dataclass can replace NamedTuple since it can define methods

#### 2.3 more about class

+ class __init__ provides more flexible possibilities e.g. assertion, computation, etc.

+ class attribute testing one by one: trade off between efficiency and safety

+ class attribute constraint (invariant) should be obeyed in run time. 

```python
#Name mangling

class A:
    __abc

obj._A_abc
```

+ When to use @classmethod
```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, s):
        # Parse the string to get x and y values
        x, y = ... 
        return cls(x, y)
```

+ Context manager ???

## 3 design pattern concept

#### 3.1 some techniques

```python
def f(x1, x2, x3, x4):
    states = x1 * x2 * x3 * x4

def f(g(x1, x2), h(x3, x4)):
    state = x1 * x2 + x3 * x4
```

+ Alternative to interface: protocol. It is for type confirming

```python
from typing import Protocol

class Splittable(Protocol):
    Def split_in_half(self) -> tuple[‘Splittable’, ‘Splittable’]

class BLTSandwich:
    Def split_in_half(self) -> tuple[‘Splittable’, ‘Splittable’]

#It cannot use directly use issubclass to check, but can:

from typing import runtime_checkable
@runtime_checkable
class Splittable(Protocol):
    Def split_in_half(self) -> tuple[‘Splittable’, ‘Splittable’]

class BLTSandwich:
    Def split_in_half(self) -> tuple[‘Splittable’, ‘Splittable’]
	Assert issubclass(self, Splittable)
```

+ Dependency
E.g. dependency: pizza payment, pizza making, pizza store seat management
Put “pizza list” in pizza making only, the other two systems reference it!

+ DRY (Don’t Repeat Yourself) rule
    + fixing is time-consuming
    + However, don’t over DRY especially if there are so many exceptions!

+ function programming
    + Decorator: input function (can add args) output function
    + import backoff
    ```python
    @backoff.on_exception …
    ```
    + functools.lru_cache

```python
#Do NOT use [] as default args
def h(L=[], D={}):
    L.append(1)
    D["a"] = D.get("a", 0) + 1
    print(L, D)

h() # [1] {'a': 1}
h() # [1, 1] {'a': 2}
```

#### 3.2 SOLID

###### 2 OCP
Extend by adding function not modified function
Remember to think which part is portable to prevent over-OCP

Risk: 1 Hard to read 2 increase dependency

```python
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def calculate_area(self):
        if self.shape_type == 'rectangle':
            return self.calculate_rectangle_area()
        elif self.shape_type == 'circle':
            return self.calculate_circle_area()

    def calculate_rectangle_area(self):
        return self.width * self.height

    def calculate_circle_area(self):
        return 3.14 * (self.radius ** 2)

#Improve

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
```

###### 3 LSP
subclass must obey all invariants as parent class. (Highly recommended call super)
Subclass must obey all parent methods

```python
#violation
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):  # must override so violate LSP
        return self.width * self.width

#Solution
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
```

+ More about LSP:
    + Inheritance: A is a B
    + Composition (Delegation): A has a B
        + E.g. self.xxx: B = …

###### 4 ISP
Interface should as minimal as possible
= Don’t write unused method in interface
= Child class must obeys all parent class (same as LSP)

```python
# Printer interface
class Printer:
    def print(self, document):
        pass

    def scan(self, document):  # This method violates ISP, so removing it can solve this problem.
        pass

# Simple printer that only prints
class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

# Printer scanner that can print and scan
class PrinterScanner(Printer):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")
```

###### 5 DIP
Calling obj.details (concrete implementations) should depend on abstractions.

```python
# High-level module (NotificationService) depends on low-level module (EmailService)
class EmailService:
    def send_email(self, to_address, message):
        print(f"Sending email to {to_address}: {message}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, to_address, message):
        self.email_service.send_email(to_address, message)  # must use interface

# Usage
notification_service = NotificationService()
notification_service.send_notification("example@example.com", "Hello!")

#Improved:

# Abstraction (interface)
class NotificationSender:
    def send(self, to_address, message):
        pass

# Low-level modules depend on the abstraction
class EmailService(NotificationSender):
    def send(self, to_address, message):
        print(f"Sending email to {to_address}: {message}")

# High-level module depends on the abstraction
class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def send_notification(self, to_address, message):
        self.sender.send(to_address, message)

# Usage
email_service = EmailService()
notification_service = NotificationService(email_service)
notification_service.send_notification("example@example.com", "Hello!")
```

###### 1 SRP
for leaf classes

#### 3.3 static tools
+ tools:
    + Visualization of dependency: Graphviz
    + module: pipdeptree
    + import: pydeps
    + call: pyan3

+ Coding style check
```bash
pip install pylint
pylint xxx.py
```
Also you can customize your pylinter

+ More tools:
    + Tools of complexity check (although is subjective)
    + Mccabe: Control flow
    + White space checking: indentation count

+ Tools of Security 
    + Dodgy
    + Bandit

## 4 testing and dynamic tools
+ Testing pyramid
    + UI
    + integrated
    + Unit

+ pytest
    + function name should start with test_
```bash
pip install pytest
Pytest xxx.py
```

+ More tools:
    + E.g. behave, hypothesis, mutmut

## 5 Design patterns

```
5.1 Creational patterns

5.1.1 Factory method
Raw: A (factory) -> B (truck) -> C (product). But now I want ship for factory
Soulution
Abstract transportation -> concrete truck, concrete ship

5.1.2 prototype
Raw: how to copy a object (include private attributes)
Solution: implement __copy__ and __deepcopy__
https://refactoring.guru/design-patterns/prototype/python/example

5.1.3 

….

Observation pattern (multiple instance follow 1 changeable instance)
e.g. subscriber implements update
       Youtuber implements
Add_subscriber
Remove_subscriber
Notify_subscribers (iterate all subscribers when video update)
https://medium.com/enjoy-life-enjoy-coding/design-pattern-%E5%8F%AA%E8%A6%81%E4%BD%A0%E6%83%B3%E7%9F%A5%E9%81%93-%E6%88%91%E5%B0%B1%E5%91%8A%E8%A8%B4%E4%BD%A0-%E8%A7%80%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F-observer-pattern-feat-typescript-8c15dcb21622


And

Observation pattern + streaming e.g. RxPY

—---------

Template method pattern:
defining an algorithm with steps
Inheritance: main instance is subclass that implement steps

Strategy pattern:
defining a family of algorithms
Composition: main instance use one subclass of interface (remember DIP)

class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        pass

    def step_two(self):
        pass

    def step_three(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step One")

    def step_two(self):
        print("Step Two")

    def step_three(self):
        print("Step Three")

obj = ConcreteClass()
obj.template_method()

—

class Strategy:
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

… see more in github
```

## 6 Refactoring
In Github

## 7 CI/CD, devops

## More

+ Pyproject.toml
