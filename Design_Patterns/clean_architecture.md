## Clean architecture
+ Programming
    + Structural: struct
    + OOP: inheritance, encapsulation, polymorphism
    + Functional: no and less varied variables

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
