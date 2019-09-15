#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:57:20 2019

@author: blacksam
"""

import numpy as np
import pytest
from modules import in_out as io
from modules import solver as sv
from modules import interpolator

"""
comparing the results of the programm to reference data from the first solver
"""

def test_solver():
    path = "/schroedinger.inp.dat"
    wavefunc = sv.solver(interpolator.interpolator(io.params(path)['x_sup'], io.params(path)['y_sup'], io.params(path)['method']), io.params(path)['mass'], io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    wavefunc_exp = np.loadtxt("/references/wavefuncs.dat")
    
    assert np.all(np.abs(wavefunc - wavefunc_exp)) < 1e-10
    
def test_exp_values():
    path = "/schroedinger.inp.dat"
    wavefunc = sv.solver(interpolator.interpolator(io.params(path)['x_sup'], io.params(path)['y_sup'], io.params(path)['method']), io.params(path)['mass'], io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    x_exp = sv.exp_values(wavefunc, io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[0]
    sigma_x = sv.exp_values(wavefunc, io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    x_exp_exp = np.loadtxt("/references/expvalues.dat")[:, 0]
    sigma_x_exp = np.loadtxt("/references/expvalues.dat")[:, 1]
    
    assert np.all(np.abs(x_exp - x_exp_exp)) < 1e-10 and np.all(np.abs(sigma_x - sigma_x_exp)) < 1e-10
