## Refactoring

+ No bloated classes, bloated method, magic number, duplication
+ Less code is easier and cheaper to maintain
+ Clean code can pass all test
+ Refactoring right ways:
    + become cleaner
    + no new functionality
    + pass all existing tests.
+ Metrics
	+ Reusability
	+ Readibility
	+ Scalability
	+ Maintainability
+ Delegation
```bash
class A:
	pass

class B:
	a: A
```

#### 6.1 composing methods

+ 6.1.1 extract method
	+ split a function to parts, each part do single type of thing

+ 6.1.2 inline Method
	+ one line clean code

+ 6.1.3 extract variable
	+ is_abc: bool

+ 6.1.4 inline temp
	+ one line clean code

+ 6.1.5 Replace Temp with Query
	+ ??? (maybe not really good)

+ 6.1.6 Split Temporary Variable
	+ rename vars to true meaning instead of using "tmp"
	+ multiple "tmp" make confuse 

+ 6.1.7 Remove Assignments to Parameters
	+ when a function input is changing, copy it and rename it instead of directly modify if needed

+ 6.1.8 Replace Method with Method Object
	+ when a function contains local variables, use class with methods instead

+ 6.1.9 Substitute Algorithm
	+ Large if-elif-... replaced as dict.get(x) 

#### 6.2 moving features between objects

+ 6.2.1 move method
	+ move a method from class 1 to class 2 if class 2 use it more frequently then class 1

+ 6.2.2 move field
	+ move attribute as 6.2.1

+ 6.2.3 extract class
	+ SRP

+ 6.2.4 inline class
	+ Over SRP may cause inline class, merge the classes back

+ 6.2.5 hide delegate
	+ Class relation
		+ class A -> class X
		+ class A -> class Y
		+ class X -> class Y
	+ refactor to class A -> class X -> class Y

+ 6.2.6 remove middle man
	+ reverse of 6.2.5
	+ class A -> class X -> class Y to 
		+ class A -> class X
		+ class A -> class Y
		+ class X -> class Y
	+ Choose 6.2.5 or 6.2.6 depends on the relation

+ 6.2.7 introduce foreign method
	+ when a method do something duplication, add a private method to do it

+ 6.2.8 introduce local extension
	+ inheritance

#### 6.3 organizing data

+ 6.3.1 self encapsulate field
	+ Access private a field (attribute or method) by using getter and setter

+ 6.3.2 replace data value with object
	+ convert string to class name

+ 6.3.3 change value to reference
	+ class relation use pointer instead of multiple values

+ 6.3.4 change reference to value
	+ reverse of 6.3.3
	+ suit for small object, infrequent changed field

+ 6.3.5 replace array with object
	+ for better understanding each column's meaning

+ 6.3.6 duplicate observed data:
	+ Separate data from GUI class and ensure the synchronization
	+ Window.load_data; backend.data

+ 6.3.7 Change Unidirectional Association to Bidirectional
	+ If the reversed calling is needed.

+ 6.3.8 Change Bidirectional Association to Unidirectional
	+ If one of the calls is not needed.

+ 6.3.9 Replace Magic Number with Symbolic Constant
	+ Human readable constant

+ 6.3.10 encapsulation field
	+ Make it private and create methods for it if needed.

+ 6.3.11 encapsulation collection
	+ use read-only data (python does not have absolute constant, but can use @property to emphasize the encapsulation)

+ 6.3.12 replace type code with class
	+ ??? 
 
+ 6.3.13 replace type code with subclass
	+ e.g. Employee has attr Engineer and Salesman
	+ refactor to Engineer(Employee) and Salesman(Employee)

+ 6.3.14 replace type code with state/strategy
	+ e.g. Employee has attr Engineer, Salesman
	+ refactor to Engineer(EmployeeType) and Salesman(EmployeeType) and Employtype -> Employ

+ 6.3.15 replace subclass with fields
	+ If two subclass behaves samething, merge them

#### 6.4 simplifying conditional expressions

+ 6.4.1 decompose conditional
	+ use is_... as a boolean function to prevent too long condition 

+ 6.4.2 consolidate conditional expression
	+ same as above, concat all if conditions as a single function

+ 6.4.3 consolidate duplicate conditional fragments
	+ if a block execute in if and else, move out of the condition

+ 6.4.4 remove control flag
	+ use break, continue and return properly

+ 6.4.5 replace nested conditional with guard clauses
	+ flatten the deep if-else condition

+ 6.4.6 replace conditional with polymorphism
	+ instead of multiple if-else for multuiple types, create each as a new class
	+ Bird.speed: if is_asian elif ...
	+ Refactor to - AsianBird(Bird).speed, ... 

+ 6.4.7 introduce null object
	+ Use null object to prevent None
	+ class NullObject: def is_null(self): return True

+ 6.4.8 introduce assertion
	+ Use if raise is better than assertion since raise type can be specified

#### 6.5 simplifying method calls

+ 6.5.1 rename method
	+ for better understanding

+ 6.5.2 add parameter
	+ add parameter into a method's arg if needed

+ 6.5.3 remove parameter
	+ remove parameter from a method's arg if does not used

+ 6.5.4 separate query from modifier
	+ a method returns a value but also changes data
	+ split into two methods

+ 6.5.5 parameterize method
	+ merge two similar methods to 1 by adding a parameter

+ 6.5.6 replace parameter with explicit methods
	+ split method

+ 6.5.7 preserve whole object
	+ inputs and outputs among methods does not need to put outside

+ 6.5.8 replace parameter with method call
	+ local variable can be moved into function should move into

+ 6.5.9 Introduce Parameter Object
	+ multiple arguments can be put into an object

+ 6.5.10 remove setting method
	+ If it will not be changed after initialization

+ 6.5.11 hide method
	+ encapsulation

+ 6.5.12 replace constructor with factory method
	+ A complex constructor do sets variables and more
	+ Use Factory method

+ 6.5.13 Replace Error Code with Exception

+ 6.5.14 Replace Exception with Test
	+ replace try except as if else

#### 6.6 Dealing with Generalization

+ 6.6.1 pull up field
	+ if an attribute is commmon in all subclass, put it to base class

+ 6.6.2 pull up method
	+ if a method is commmon in all subclass, put it to base class

+ 6.6.3 pull up constructor body
	+ if constructor are commmon in all class, set a base class

+ 6.6.4 push down method
	+ if a method is only for a single subclass, move it from base class to the subclass

+ 6.6.5 push down field
	+ if a attribute is only for a single subclass, move it from base class to the subclass

+ 6.6.6 extract subclass
	+ When some field is used in special cases, move it out

+ 6.6.7 extract superclass
	+ has common method for classes, set base class 

+ 6.6.8 extract interface
	+ has partially commond method for classes, set base class

+ 6.6.9 collapse hierarchy
	+ when a child class is same as its parent class, keep parent only
	+ Remember LSP

+ 6.6.10 form template method
	+ template method in design pattern
	
+ 6.6.11 Replace Inheritance with Delegation
	+ if a subclass only use part of parent class
	+ remove inheritance and use it as one attribute instead
	+ e.g. stack(vector), stack does not need popleft
	+ refactor to stack.vector

+ 6.6.12 Replace delegation with inheritance
	+ if delegation object use most of the target class
	+ change it to inheritance
