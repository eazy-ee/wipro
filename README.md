# wipro
=======
=======
***************************************************************
Solver for Schroedinger-Equation in an one-dimensional potential
***************************************************************

The executable Python programm solves the Schroedinger-Equation
for a one-dimensional potential depending on the data given in an input file
and plots the results.

Prerequisites
============
The Solver needs Python 3 (version 3.5 or above), as well as the Numpy-, Scipy-
and Matplotlib-packages.

Creating the input
================
The input file needs to consist of values for mass and position of the particle as
well as the potential and interpolation method. It should be saved as .inp file.

Interpolator
============
The potential is interpolated by built-in interpolation functions of scipy.

Solver
======
The Solver creates arrays containing the eigenvalues, discrete wavefunction values
and expectation values calculated by built-in functions of scipy.

Input and Output
===============
The in_out module reads the input file and saves the values in a dictionary which is
then used in the other modules. Also it writes the arrays created by the solver module
into .dat files.

Tests
=====
The test files can be used with pytest to compare the results of the first version of
the programm to the results of any further changed programm version.
