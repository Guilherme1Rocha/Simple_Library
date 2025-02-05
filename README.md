Text Justification, Hondt Method, and Linear Equations Solver

Overview

This repository contains three independent programming exercises designed to reinforce fundamental programming concepts. The exercises cover text formatting, election result calculations using the Hondt method, and solving linear equation systems.

Exercises

1. Text Justification

Objective: Implement a function that justifies a given text to a specified column width.

Description:

The function receives a non-empty string and an integer representing the column width.

The output is a tuple of strings, each exactly matching the column width.

Words must be evenly spaced across each line.

Additional spaces should be added from left to right when needed.

The last line and single-word lines should be left-aligned with extra spaces at the end.

Example Input:

"This is an example of text justification"
Column width: 20

Example Output:

("This   is  an  example",
 "of   text  justification")

2. Hondt Method for Seat Allocation

Objective: Implement an algorithm to allocate parliamentary seats based on the Hondt method.

Description:

The Hondt method is a proportional representation system used in elections.

Given the number of votes each party receives and the number of seats available, seats are allocated iteratively.

Each party’s vote count is divided by divisors (1, 2, 3, ... up to the total seats).

The highest quotients receive the seats in descending order.

If a tie occurs for the last seat, the party with fewer total votes is prioritized.

3. Solving Systems of Linear Equations

Objective: Implement an algorithm to solve systems of linear equations using Jacobi’s method.

Description:

A system of equations is given in matrix form: A * x = c.

Jacobi’s iterative method starts with an initial estimate and refines it iteratively.

The method updates each variable based on the current estimates of others.

Convergence is achieved when the solution approximates the correct values within a defined tolerance.


Usage

Each exercise is implemented as an independent function. You can run them by providing the required inputs and observing the outputs.
