### Design patterns

##### requests -> intermediate -> system

1. command
    + [intent] multiple steps (class) in pipeline.
    + Invoker: to collect commands (classes), then execute each class sequentially.
        + e.g. MetricsCollection

2. facade
    + [intent] multiple steps (class methods) in pipeline.
    + Facade: to collect classes, then execute each class methods (different class methods can be interleaved) sequentially.

3. proxy
    + [intent] Multiple user access DB cause low performance
    + Proxy: address_request, access_db

##### python tools

4. iterator
    + generator

5. decorator
    + decorator

6. flyweight
    + defaultdict

##### decrease subclasses

7. builder
    + [intent] build house by step1, step2, ..., stepN. P(M, N) -> M + N
    + Builder: step1, step2, ..., stepN
    + Director: different permutation methods from builder 

8. abstract factory
    + [intent] Warriors (M) * Equipments (N) -> M + N
    + Warriors-i: equip1, equip2, ..., equipN

9. bridge
    + [intent] same as abstract factory
    + Warriors-i: call equip1.method, equip2.method, ..., equipN.method

##### data structure of class relations
10. chain of responsibility
    + [intent] request -> handler1 (execute or pass) -> handler2 (execute or pass) -> ... -> failed
    + handler: next, handle

11. composite
    + [intent] represent classes as tree structure (if is possible). non-leaf call or children (no execute), whereas leaf executes.
    + non_leaf: call_children
    + leaf: execute

##### More

12. meditator
    + [intent] aircraft-i <-> control power <-> aircraft-j. communication between pairs
    + meditator: notify
    + aircrafts: different notification methods by self.meditator

13. memento
    + [intent] edit a document and can be undo many steps
    + document: edit, save, undo
    + memento: stack memory
    + caretaker: save, undo

14. observation
    + [intent] when youtuber update videos, notify all followers.
    + youtuber: add, delete, notify (iterate over followers)
    + followers: update

15. state
    + [intent] design extenable FSM
    + state: context, handle-i
    + context: state, call_handle-i

16. strategy
    + [intent] C(N, 1)
    + Strategy-i: algorithm-i
    + Context: Choose one algorithm to execute

17. template_method
    + [intent] base class contains a series of steps (method), override 1 at subclass
    + e.g. Trainer

18. visitor
    + [intent] when subclass name is different in polymorphism, want to unfiy it
    + Component: define unified function name (e.g. accept) and use visitor to call self custom function.
    + Visitor: input component and execute the unified function name (e.g. accept)

19. factory
    + [intent] Polymorphism

20. prototype
    + [intent] shallow copy and deep copy of an object
    + implement \_\_copy\_\_ and \_\_deep\_\_ (recusive function with memo arg of all attributes)

21. singleton
    + [intent] ensure a class has one instance only
    + make constructor private by metaclass 

22. adaptor
    + [intent] format conversion e.g. xml -> json
    + inherits json-module and do format conversion
