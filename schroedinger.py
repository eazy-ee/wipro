# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:59:53 2019

@author: Emanuel
"""
import numpy as np
import matplotlib.pyplot as plt
import in_out
import interpolator
import solver
import visualizer


def schroedinger():
    """
    Solves the 1-dimensional stationary schroedinger equation
    """
   #parameters set in input file
    params = in_out.params()

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
    visualizer.visualizer(psi, potential, energies, x_exp, sigma_x, **params)

schroedinger()
plt.show()
