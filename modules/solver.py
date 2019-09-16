"""
Script to find eigenvalues/eigenvectors of the 1-dim schroedinger equation and calculation expectation values of x for a given problem.
"""

import numpy as np
from scipy import linalg as LA

def solver(potential, mass, x_min, x_max, n_point):
    """
    Script to solve the 1-dimensional, stationary schroedinger equation for a given potential. Returns eigenvalues (energielevels) and normalised wavefunctions.

    Args:
        potential: Potential of the problem
        mass: Mass of particle
        x_min: Left end of the x-axis
        x_max: Right end of the x-axis
        n_point: Number of points the x-axis contains
    """
    #setting x-axis
    xnew = np.linspace(x_min, x_max, n_point)

    #delta x
    delta = xnew[1]-xnew[0]

    #diagonals of coeff matrix, eigenvalues w and eigenvectors v
    sub_diagonal = np.array([-1/(2*mass*delta**2) for i in range(len(xnew)-1)])
    main_diagonal = np.array([1/(mass*delta**2)+potential(i) for i in xnew])
    eigenvalue, eigenvector = LA.eigh_tridiagonal(main_diagonal, sub_diagonal)

    #normalised wavefunction
    wavefunc = np.array([eigenvector[:, i]/np.sqrt(delta) for i in range(0, len(xnew))])

    return eigenvalue, wavefunc


def exp_values(wavefunc, x_min, x_max, n_point):
    """
    Calculating the expectation values and uncertainty of x. Returns $<x>$ and sigma_x

    Args:
        wavefunc: Previously calculated wavefunctions to the problem
        x_min: Left end of the x-axis
        x_max: Right end of the x-axis
        n_point: Number of points the x-axis contains
    """
    #setting x-axis
    xnew = np.linspace(x_min, x_max, n_point)

    #delta x
    delta = xnew[1]-xnew[0]

    #expectation values
    x_exp = delta*np.array([np.sum(wavefunc[i]*xnew*wavefunc[i]) for i in range(0, len(wavefunc))])
    xsq_exp = delta*np.array([np.sum(wavefunc*xnew**2*wavefunc) for wavefunc in wavefunc])

    #uncertainty
    sigma_x = np.sqrt(xsq_exp-x_exp**2)

    return x_exp, sigma_x
