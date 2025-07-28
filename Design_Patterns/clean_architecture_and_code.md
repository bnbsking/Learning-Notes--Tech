## Clean architecture
+ Programming
    + Structural: struct
    + OOP: inheritance, encapsulation, polymorphism
    + Functional: no and less varied variables

+ principles
    + SOLID   
        + SRP: a class is responseible for a single character
            + modify it do not change the other
        + OCP
        + LSP
        + ISP
        + DIP
    + Component = deploy unit
        + REP: Reuse equivalance principle
            + component = deploy unit = reusable unit
            + general SRP
        + CCP: Common closure principle
            + Classes will be varied by same time should be grouped into a unit
            + Classes will not be varied by same time should be seperated from a unit.
            + general OCP
        + CRP
            + general ISP
        + compare:
            + REP amd CCP makes commponent greater but CRP makes it smaller
            + trade-off between them
                + REP too low -> hard to reuse
                + CRP too low -> hard to vary
                + CRP too low -> too many unused released
    + Acyclic dependency principle (ADP)
        + component dependency should not have cycle
    
    + Stabability dependency principle (SDP)
        + X is a stable component (FanIn)
            + e.g. A -> X; B -> X; C -> X
        + Y is an unstable component (FanOut)
            + e.g. Y -> A; Y -> B; Y -> C
        + formula:
            ```
            instabability = FanOut / (FanIn + FanOut)
            ```
        + SDP ensures: instabibility decrease by the dependency!
            + do many to 1, do not do 1 to many
    
    + Stable abstraction principle (SAP)
        + to compute a component's abstraction, formula
            ```
            abstraction = num_abstract_classes / num_classes
            ```
        + A-I diagram
            + (I=0, A=1): full abtract class, fan out only
            + (I=1, A=0): full concrete class, fan in only
            + (I=0, A=0): Zone of Pain - bad style. full concrete class fans out
            + (I=1, A=1): Zone of Useless - useless style. abstract class has no fans out
            + D-value = sum_i(|A_i + I_i - 1|)
                + ideal case: D=0

+ Architecture
    + Do focus on requirements, do not focus on details (which tools to use)
    + Consider
        + Development
        + Deployment
        + Run
        + Maintanance
    + If duplication will be diverse in the future, do not merge them
    + Decoupling level: there is no absoulute correct answer
        + source code level
        + deploy (component) level
        + service-level (SoA = service oriented architecture)
    + Entity -> Use cases -> Controller -> Framework and tools e.g. web, db
        + left is core, out are details
    + Humble object patterns
        + data -> presenter -> view -> GUI show
        + presenter: data formatting, test unit, hard to test
        + view: data getter, test unit, easy to test
    + Testing
        + Use testing API to decouple core code and testing functions
        + tests are always at the outest, depends to the core and never be depends by others         
    + Firmware
        + Software > OS abstraction layer (OSAL) > OS > Hardware abstraction layer (HAL) > Firmware > Hardware
        + HAL does not show details about hardware e.g. LedTurnOn(5)
        + HAL does not depends on CPU ideally

+ Details
    + e.g. DB, Web, framework...
    + choosing framework must be meticulous, do not couple with your core
 
## Clean Code  
+ common rules
    + meaningful names
    + no magic numbers
    + distinguishable
    + consistency
    + use prefix
    + type hint
    + no encoding

+ comments
    + readibility > add comment

+ no `a.b().C()`, Demeter law

+ about third party tool
    + learning tests: write testing functions for better unstanding
    + should minimal use the tool
    + Adapter is a possilbe solution

+ tests
    + must be mutually independent
    + for a time-consuming pipeline test, use yield or return

+ parallel
    + SRP decouple
    + minimize the locking area
    + consider the aftermath of shuting down a certain thread

+ Synchronous
    + Deadlock - 4 necessary criterion
        + 1 mutex -> cannot prevent
        + 2 hold and wait -> can prevent if always release all resource before aquire
        + 3 preemption -> use (priority) queue to prevent (priority might cause starvation)
        + 4 circular waiting -> map PID to order, alternatively acquire resource  
        + (Most common are 4)
    + classical problem
        + Reader-Writer: queue + lock
        + Producer-Consumer: queue + lock
    + [example](../python/advanced_internal_features/parallel_lock.ipynb)
