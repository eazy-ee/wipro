#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:57:20 2019

@author: blacksam
"""

import numpy as np
import pytest
import in_out as io
import solver as sv

path = "/home/blacksam/wipro/reference/schroedinger.inp.dat"

def test_solver():
    path = "/home/blacksam/wipro/reference/schroedinger.inp.dat"
    eigenvalue = sv.solver(io.params(path)['pot'], io.params(path)['mass'], io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[0]
    wavefunc = sv.solver(io.params(path)['pot'], io.params(path)['mass'], io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    eigenvalue_exp = np.loadtxt("/home/blacksam/wipro/wipro2/energies.dat")
    wavefunc_exp = np.loadtxt("/home/blacksam/wipro/wipro2/wavefuncs.dat")
    
    assert np.all(np.abs(wavefunc - wavefunc_exp)) < 1e-10
    
def test_exp_values():
    path = "/home/blacksam/wipro/reference/schroedinger.inp.dat"
    wavefunc = sv.solver(io.params(path)['pot'], io.params(path)['mass'], io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    x_exp = sv.exp_values(wavefunc, io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[0]
    sigma_x = sv.exp_values(wavefunc, io.params(path)['x_min'], io.params(path)['x_max'], io.params(path)['n_point'])[1]
    x_exp_exp = np.loadtxt("/home/blacksam/wipro/wipro2/expvalues.dat")[:, 0]
    sigma_x_exp = np.loadtxt("/home/blacksam/wipro/wipro2/expvalues.dat")[:, 1]
    
    assert np.all(np.abs(x_exp - x_exp_exp)) < 1e-10 and np.all(np.abs(sigma_x - sigma_x_exp)) < 1e-10
