T# Text Justification, Hondt Method, and Linear Equations Solver

## Overview
This repository contains three independent programming exercises designed to reinforce fundamental programming concepts. The exercises cover **text formatting**, **election result calculations using the Hondt method**, and **solving linear equation systems**.

## Exercises

### 1. Text Justification

**Objective:**  
Implement a function that justifies a given text to a specified column width.

**Description:**  
- The function receives a **non-empty string** and an **integer** representing the column width.  
- The output is a **tuple of strings**, each exactly matching the column width.  
- Words must be **evenly spaced** across each line.  
- Additional spaces should be added **from left to right** when needed.  
- The last line and single-word lines should be **left-aligned** with extra spaces at the end.  



### 2. Hondt Method for Seat Allocation

**Objective:**  
Implement an algorithm to allocate parliamentary seats based on the **Hondt method**.

**Description:**  
- The **Hondt method** is a proportional representation system used in elections.  
- Given the **number of votes** each party receives and the **number of seats available**, seats are allocated iteratively.  
- Each party’s vote count is **divided by divisors** (1, 2, 3, ... up to the total seats).  
- The **highest quotients** receive the seats in descending order.  
- If a **tie occurs** for the last seat, the party with **fewer total votes** is prioritized.  


### 3. Solving Systems of Linear Equations Using Jacobi’s Method

**Objective**:
Implement an algorithm to solve systems of linear equations using Jacobi’s method.

**Description**:

A system of equations can be represented in matrix form as:

\[ A \cdot x = c \]

Where:
- \( A \) is the coefficient matrix,
- \( x \) is the vector of unknowns (variables),
- \( c \) is the vector of constants.

### Jacobi’s Iterative Method:
Jacobi’s method is an iterative technique for solving systems of linear equations. The method starts with an initial estimate of the solution and refines it iteratively. 

In each iteration, the method updates the value of each variable based on the current estimates of the other variables.

For the system of equations \( A \cdot x = c \), the Jacobi method is applied as follows:

- Start with an initial guess for \( x^{(0)} \), the vector of unknowns.
- Update each component of \( x^{(k+1)} \) based on the previous iteration’s values:
  
  \[
  x_i^{(k+1)} = \frac{1}{a_{ii}} \left( c_i - \sum_{j \neq i} a_{ij} \cdot x_j^{(k)} \right)
  \]
  
  where:
  - \( a_{ii} \) are the diagonal elements of the matrix \( A \),
  - \( a_{ij} \) are the off-diagonal elements of the matrix \( A \),
  - \( c_i \) are the components of the vector \( c \),
  - \( x_j^{(k)} \) are the values of the variables from the previous iteration.

### Convergence:
The method converges when the difference between successive iterations is smaller than a defined tolerance, i.e., when:

\[
\| x^{(k+1)} - x^{(k)} \| < \epsilon
\]

Where:
- \( \epsilon \) is the tolerance level, a small positive value.

## Key Steps:
1. Choose an initial estimate for the solution vector \( x^{(0)} \).
2. Perform iterative updates based on the Jacobi formula.
3. Continue iterating until the solution converges to the desired tolerance.


## Usage

Each exercise is implemented as an independent function. You can run them by providing the required inputs and observing the outputs.
