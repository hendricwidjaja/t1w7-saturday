# t1w7-saturday

# Wildcard Arguments
- When you don't know how many arguments to pass in a function
- Non-keyword arguments, *args
- Keyword arguments, **kwargs

# Modules
- One of the techniques for following DRY Coding Principles
- Group similar codes and functions together in a separate file
- Solves the problem of code files being too lengthy and complex
- Can be reused across several programs
- Python comes with a lot of modules as well (Python Standard Library)

# Packages
- A collection of modules
- Organise related modules under one directory
- Initialise a package using __init__.py file

## Practical Example
Task:
- Create a package for basic text processing with modules for:
    - Counting words in a string,
    - Counting characters in a string, and
    - Reversing strings.

# Slicing a sequence
- A way to extract parts of data structures, like strings, lists, tuples.
- Syntax: sequence[start:stop:step] (like range)
    - Default of start = 0
    - Default of step = 1
    - Default of stop = last
    - If only 1 value is input, ensure to place the ":" in correct position

# Object Oriented Programming
- It is a way to help programmers structure the functionality of your program that would make sense to humans and would allow computers to run it efficiently.
- Almost all programming languages use this concept.
- It uses "objects" to model real-world entities.

## Key Concepts in OOP
- Class
    - A blueprint for creating objects.
    - Defines a set of attributes or methods that the created objects (instances) will have
    - E.g. Blueprint provided while building ahouse, defining what an animal is
    - NOTE: Needs to start with captial letter

- Object
    - An instance of a class
    - It represents a specific entity with attributes (data) and methods (functions) which are defined by class.
    - E.g. A built house with many functions (as functions)
    - E.g. class_eg(Dog)
    - E.g. BankAccount

- 4 Pillars of OOP
    - Encapsulation, Abstraction, Inheritance, Polymorphism

## Encapsulation
- Technique of keeping internal state of object hidden from the outside. (keeping variables private)
- Achieved using private attributes and providing public methods to access and update them.
- Syntax: __varname

## Abstraction
- Concept of hiding the complex implementation details and showing only the necessary features of an object
- Achieved by using Abstract class and method. 

### Abstraction Class and Method
- 


## Inheritance
- Mechanism of creating a new class based on an existing class, by inheriting properties (attributes and/or methods)
- Parent Class: The class from where the features are inherited from. (super class)
- Child class: The class that inherits the features (sub class)
- Benefits: Classes are created easily, easy maintenance as well.

## Polymorphism
- Ability to present the same interface for different data types.
- Allows methods to do different things based on the object it is acting upon