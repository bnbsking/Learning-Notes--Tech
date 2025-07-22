### Design patterns

##### pipeline multi-step

1. command
    + [intent] multiple steps in a pipeline.
    + [classes]
        + Invoker: define methods (steps), then execute each sequentially.
    + [example] MetricsCollection
    + [category] behavioral

2. facade
    + [intent] multiple steps (allow within different class) in a pipeline.
    + [classes]
        + Facade: define methods (steps) within classes, then execute each (allow from different classes) sequentially.
    + [category] structural

3. template_method
    + [intent] base class contains a series of steps (method), override some at subclass
    + [example] Trainer
    + [category] behavioral
    + Like **command** but must inherit from base

4. builder
    + [intent] build house by step1, step2, ..., stepN. M * N -> M + N
    + [classes]
        + Builder: step1, step2, ..., stepN
        + Director: different permutation methods from builder
    + [category] creational
    + Like **facade** but all methods are collected in a class (like a toolbox)

5. chain of responsibility
    + [intent] request -> handler1 (execute or pass) -> handler2 (execute or pass) -> ... -> failed
    + [classes]
        + BaseHandler: attribute "next", method "handle"
        + EachHandler: attribute "next", method "handle"
    + [category] behavioral
    + linked list process

6. composite
    + [intent] represent classes as tree structure (if is possible). non-leaf call or children (no execute), whereas leaf executes.
    + [classes]
        + non_leaf: call_children
        + leaf: execute
    + [category] structural
    + tree process

7. state
    + [intent] design extenable FSM
    + [classes]
        + state: context, handle-i
        + context: state, call_handle-i
    + [category] behavioral
    + acyclic graph process

##### pipeline single-step

8. strategy
    + [intent] C(N, 1)
    + [classes]
        + Strategy-i: algorithm-i
        + Context: Choose one algorithm to execute
    + [category] behavioral
    + Single step version of **builder**

##### pipeline two steps (classes decrease: M * N to M)

9. abstract factory
    + [intent] Warriors (M) * Equipments (N) -> M
    + [classes]
        + Warriors-i: methods equip1, equip2, ..., equipN
    + [category] creational

10. bridge
    + [intent] Warriors (M) * Equipments (N) -> M
    + [classes]
        + Abstract_Warrior: abstract method equip1, equip2, ..., equipN
        + Warriors-i: methods equip1, equip2, ..., equipN
    + [category] structural
    + add abstract to **abstract factory**

##### requests -> intermediate -> system

11. adaptor
    + [intent] new module want to use api but in inconsistet format 
    + [example] e.g. raw: xml api; new data is in json
    + inherits new module (json) plus format conversion

12. proxy
    + [intent] multiple user access DB cause low performance
    + [classes]
        + Proxy: a method address_request and a method access_db
    + [category] structural

13. meditator
    + [intent] aircraft-i <-> control power <-> aircraft-j. communication between pairs
    + [classes]
        + meditator: notify
        + aircrafts: different notification methods by self.meditator
    + [category] behavioral
    + **proxy** plus multiple targets

##### Programming language and OOP

14. iterator
    + generator
    + [category] behavioral

15. decorator
    + decorator
    + [category] structural

16. flyweight
    + defaultdict
    + [category] structural

17. factory
    + [intent] Polymorphism

##### More - Programming

18. prototype
    + [intent] shallow copy and deep copy of an object
    + implement \_\_copy\_\_ and \_\_deep\_\_ (recusive function with memo arg of all attributes)

19. visitor
    + [intent] when subclass name is different in polymorphism, want to unfiy it
    + Component: define unified function name (e.g. accept) and use visitor to call self custom function.
    + Visitor: input component and execute the unified function name (e.g. accept)

20. singleton
    + [intent] ensure a class has one instance only
    + make constructor private by metaclass 

##### More - Applications
21. memento
    + [intent] edit a document and can be undo many steps
    + [classes]
        + document: edit, save, undo
        + memento: stack memory
        + caretaker: save, undo
    + [category] behavioral

22. observation
    + [intent] when youtuber update videos, notify all followers.
    + [classes]
        + youtuber: add, delete, notify (iterate over followers)
        + followers: update
    + [category] behavioral
