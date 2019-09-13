#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:59:53 2019

@author: Emanuel
"""
#import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt
import in_out
import interpolator
import solver
import visualizer

def schroedinger(scale, inp):
    """
    Solves the 1-dimensional stationary schroedinger equation
    """
   #parameters set in input file
    params = in_out.params(inp)

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
    in_out.output(potential, energies, psi, x_exp, sigma_x, xnew, params['first'], params['last'])

   #visualizing data
    visualizer.visualizer(psi, potential, energies, x_exp, sigma_x, scale, **params)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and visualize the solution to the 1-dimensional Schroedinger equation for a given Potential.')
    parser.add_argument('-s', '--scale', type=float, required=False, help='Scaling the wavefunction.')
    parser.add_argument('-p', '--path', type=str, required=False,  help='Path of the input file.')
    args = parser.parse_args()
    if args.scale is None:
        args.scale = 1.0
    if args.path is None:
       args.path = './schroedinger.inp'
    schroedinger(args.scale, str(args.path))
    plt.show()
