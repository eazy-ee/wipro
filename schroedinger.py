# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:59:53 2019

@author: Emanuel
"""

import numpy as np
import matplotlib.pyplot as plt
import interpolator
import in_out
import solver
import visualizer

#parameters set in input file
M, xMin, xMax, nPoint, first, last, method, pot, x, y = in_out.params()

#interpolated potential
V = interpolator.interpolator(x,y,method)

#setting x-axis
xnew=np.linspace(xMin,xMax,nPoint)

#delta x
delta=xnew[1]-xnew[0]

#solver
w, psi = solver.solver(V, M, xMin, xMax, nPoint)

#expectation values
x_exp, sigma_x = solver.exp_values(psi, xMin, xMax, nPoint, first, last)

#saving results to files
in_out.output(V,w,psi,x_exp,sigma_x, xnew, first, last)

#visualizing data
visualizer.visualizer(psi, V, w, x_exp, sigma_x, xMin, xMax, nPoint, first, last)
plt.show()
