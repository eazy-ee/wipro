"""
Reading input and saving output.
"""


import sys
import numpy as np


def params(file):
    """
    Reads the inputfile.

    Args:
        file: The path to the input file. Usually 'schroedinger.inp'

    Returns:
        A dictionary containing input information.
    """

    data = {'mass': 0, 'x_min': 0, 'x_max': 0, 'n_point': 0, 'first': 0,
            'last': 0, 'method': 0, 'pot': 0, 'x_sup': 0, 'y_sup': 0}

    with open(file, 'r') as inp:
        try:
            for line in inp:
                if 'mass' in line.lower():
                    mass = float(np.fromstring(line, dtype=float, sep=' '))
                    data['mass'] = mass
                elif 'xmin' in line.lower():
                    x_min = np.fromstring(line, dtype=float, sep=' ')[0]
                    x_max = np.fromstring(line, dtype=float, sep=' ')[1]
                    n_point = int(np.fromstring(line, dtype=float, sep=' ')[2])
                    data['x_min'] = x_min
                    data['x_max'] = x_max
                    data['n_point'] = n_point
                elif 'first and last' in line.lower():
                    first = np.fromstring(line, dtype=int, sep=' ')[0]
                    last = np.fromstring(line, dtype=int, sep=' ')[1]
                    data['first'] = first
                    data['last'] = last
                elif 'type' in line.lower():
                    method = line.split(' ')[0]
                    data['method'] = method
                elif 'nr. of' in line.lower():
                    pot = np.loadtxt(inp.readlines())
                    data['x_sup'] = pot[:, 0]
                    data['y_sup'] = pot[:, 1]
            return data
        except OSError:
            print("Input file couldn't be read.")
            sys.exit(1)



def output(potential, energies, wavefuncs, x_exp, sigma_x, xnew, first, last, path):
    """
    Save potential, eigenvalues, eigenfunctions, expactation value
    and uncertainty of x into the path folder.

    Args:
        potential: Potential of the problem
        energies: Energy eigenvalues
        wavefuncs: Eigenfunctions
        x_exp: The expectation value of x
        sigma_x: Uncertainty of x
        xnew: x-axis
        first: Index of the first eigenvalue/eigenvector to include
        last: Index of the last eigenvalue/eigenvector to include
        path: Where the output is stored
    """
    np.savetxt(str(path)+'potential.dat',
               np.concatenate((np.reshape(xnew, (1999, 1)),
                               np.reshape(potential(xnew), (1999, 1))), axis=1))
    np.savetxt(str(path)+'energies.dat', energies[first-1:last])
    np.savetxt(str(path)+'wavefuncs.dat',
               np.concatenate((np.reshape(xnew, (1999, 1)),
                               np.transpose(wavefuncs[first-1:last])), axis=1))
    np.savetxt(str(path)+'expvalues.dat',
               np.concatenate((np.reshape(x_exp, (1999, 1)),
                               np.reshape(sigma_x, (1999, 1))), axis=1))
