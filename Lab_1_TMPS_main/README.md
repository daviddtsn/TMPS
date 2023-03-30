# Lab_1_TMPS - Banking System App in Python

## by Detisin David

## Task : Build an app that will follow SOLID Principles using an OOP programing language

## General Theory : 
### S - Single Responsibility Principle: a class should have only one reason to change.

### O - Open/Closed Principle: entities should be open for extension but closed for modification.

### L - Liskov Substitution Principle: subtypes must be substitutable for their base types.

### I - Interface Segregation Principle: clients should not be forced to depend on interfaces they do not use.

### D - Dependency Inversion Principle: high-level modules should not depend on low-level modules. Both should depend on abstractions.

## Description :
Simple banking system that allows users to create accounts, deposit and withdraw funds, and view account balances.

Single Responsibility Principle (SRP)
The Account class has a single responsibility - managing the account balance. The AccountRepository class is responsible for managing the collection of accounts, while the AccountService class is responsible for orchestrating the creation, deposit, withdrawal, and balance inquiry operations.

Open/Closed Principle (OCP)
The Account, AccountRepository, and AccountService classes are open for extension, but closed for modification. For example, if we want to add a new type of account, we can do so by creating a new subclass of Account, rather than modifying the existing class.

Liskov Substitution Principle (LSP)
The Account class and its subclasses can be substituted for each other without affecting the correctness of the program. For example, if we create a SavingsAccount subclass that has additional methods for calculating interest, we can still use it in place of the Account class in the AccountRepository and AccountService classes.

Interface Segregation Principle (ISP)
The Account class does not implement any unnecessary methods, and the AccountRepository and AccountService classes only depend on the methods they need from the Account class.

Dependency Inversion Principle (DIP)
The AccountRepository and AccountService classes depend on abstractions (the Account