#!/usr/bin/env python
import argparse
import numpy as np
from modules import in_out, interpolator, solver


def define_to_increase_pylintscore():
    """
    apparently contants have to be in upper case so
    we define a function to enjoy lower case
    """
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description=
                                         'Calculate the solution to the 1-dimensional'
                                         ' Schroedinger equation for a given Potential.')
        parser.add_argument('-i', '--input', type=str, required=False,
                            help='Path to the schroedinger.inp file')
        parser.add_argument('-o', '--output', type=str, required=False,
                            help='Directory of the output files.')
        args = parser.parse_args()

        if args.input is None:
            args.input = './schroedinger.inp'
        if args.output is None:
            args.output = './'

       #parameters set in input file
        params = in_out.params(args.input)

       #interpolated POTENTIAL
        potential = interpolator.interpolator(params['x_sup'], params['y_sup'], params['method'])

       #setting x-axis
        xnew = np.linspace(params['x_min'], params['x_max'], params['n_point'])

       #solverm
        energies, psi = solver.solver(potential, params['mass'], params['x_min'],
                                      params['x_max'], params['n_point'])

       #expectation values
        x_exp, sigma_x = solver.exp_values(psi, params['x_min'], params['x_max'], params['n_point'])

       #saving results to files
        in_out.output(potential, energies, psi, x_exp, sigma_x,
                      xnew, params['first'], params['last'], args.output)

define_to_increase_pylintscore()
