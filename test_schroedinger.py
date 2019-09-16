#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatic tests using pytest. Compares results of the modules to reference data.
"""

import os.path
import numpy as np
import pytest
from modules import in_out as io
from modules import interpolator, solver


TOLERANCE = 1e-10
TESTDATADIR = 'references'

TESTS_SUCCESSFUL = ['infinite_box', 'finite_box', 'harmonic',
                    'double_linear', 'double_cspline', 'asymmetric']

def _read_input(testname):
    """
    Gets input from reference files

    Args:
        testname: Name of the directory the reference data is in.

    Returns:
        Returns a dictionary containing input information.
    """
    inputfile = os.path.join(TESTDATADIR, testname, 'schroedinger.inp')
    params = io.params(inputfile)
    return params


def _read_output(testname):
    """
    Gets output from reference files

    Args:
        testname: Name of the directory the reference data is in.

    Returns:
        Returns a dictionary containing output of ref data.
    """
    results = {'potential': 0, 'psi': 0, 'energies': 0, 'x_exp': 0, 'sigma_x': 0}
    outfiledir = os.path.join(TESTDATADIR, testname)

    results['potential'] = np.loadtxt(str(outfiledir)+'/potential.dat')
    results['psi'] = np.loadtxt(str(outfiledir)+'/wavefuncs.dat')
    results['energies'] = np.loadtxt(str(outfiledir)+'/energies.dat')
    results['x_exp'] = np.loadtxt(str(outfiledir)+'/expvalues.dat')[:, 0]
    results['sigma_x'] = np.loadtxt(str(outfiledir)+'/expvalues.dat')[:, 1]
    return results

@pytest.mark.parametrize("testname", TESTS_SUCCESSFUL)
def test_potential(testname):
    """
    Tests whether the potential and eigenvalues match the reference data

    Args:
        testname: Name of the directory the reference data is in.
    """
    pot_expected = _read_output(testname)['potential'][:, 1]
    x_sup = _read_input(testname)['x_sup']
    y_sup = _read_input(testname)['y_sup']
    x_min = _read_input(testname)['x_min']
    x_max = _read_input(testname)['x_max']
    n_point = _read_input(testname)['n_point']
    method = _read_input(testname)['method']
    first = _read_input(testname)['first']
    last = _read_input(testname)['last']
    xnew = np.linspace(x_min, x_max, n_point)
    pot_calc = interpolator.interpolator(x_sup, y_sup, method)

    assert np.all(np.abs(pot_expected - pot_calc(xnew)) < TOLERANCE)

    #compares energie eigenvalues with ref
    energies_exp = _read_output(testname)['energies']
    mass = _read_input(testname)['mass']
    energies_calc = solver.solver(pot_calc, mass, x_min,
                                  x_max, n_point)[0][first-1:last]

    assert np.all(np.abs(energies_calc - energies_exp) < TOLERANCE)
