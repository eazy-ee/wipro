import numpy as np
from scipy import linalg as LA

def solver(V, M, xMin, xMax, nPoint):
    """
    Script to solve the 1-dimensional, stationary schroedinger equation for a given potential. Returns eigenvalues (energielevels) and normalised wavefunctions.
    """
    #setting x-axis
    xnew = np.linspace(xMin,xMax,nPoint)

    #delta x
    delta = xnew[1]-xnew[0]

    #diagonals of coeff matrix, eigenvalues w and eigenvectors v
    N = np.array([-1/(2*M*delta**2) for i in range(len(xnew)-1)])
    H = np.array([1/(M*delta**2)+V(i) for i in xnew])
    w, v = LA.eigh_tridiagonal(H,N)

    #normalised wavefunction
    psi = np.array([v[:,i]/np.sqrt(delta) for i in range(0,len(xnew))])

    return w, psi


def exp_values(psi, xMin, xMax, nPoint, first, last):
    """
    Calculating the expectation values and uncertainty of x. Returns $<x>$ and $\sigma_x$
    """
    #setting x-axis
    xnew = np.linspace(xMin,xMax,nPoint)

    #delta x
    delta = xnew[1]-xnew[0]

    #expectation values
    x_exp= delta*np.array([np.sum(psi[i]*xnew*psi[i]) for i in range(0,len(psi))])
    xsq_exp= delta*np.array([np.sum(psi*xnew**2*psi) for psi in psi])

    #uncertainty
    sigma_x = np.sqrt(xsq_exp-x_exp**2)

    return x_exp, sigma_x
