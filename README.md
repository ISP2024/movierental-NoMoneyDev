## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

2.1: Inappropriate Intimacy

2.2: SRP. Movie class, as the name suggests, should only hold data for a movie and not its pricing methods.

5.2: I chose to implement price_code_for_movie inside movie module as it has the data needed to determine the price_code (Information Expert), and as the program grows, this function can be easily maintained (Low Coupling) because the algorithm to determine the price_code most likely need to rely only on the movie data itself.