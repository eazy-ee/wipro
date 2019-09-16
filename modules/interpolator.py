# -*- coding: utf-8 -*-
"""
Script to find the intepolating function to a given set of support (x,y).

"""
import sys


from scipy.interpolate import lagrange as poly
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
#from scipy.interpolate import BarycentricInterpolator as poly

#import interpolation methods from scipy. Lagrange is very basic and is numerically unstable.
#Uncomment last line to use differenct interpolating method



def interpolator(x_sup, y_sup, method):
    """
    Used to interpolate the Potential from a given set of points using a given method.
    The method can either be polynomial, linear or cspline (natural cubic spline)).

    Args:
        x_sup: Supporting x coordinates of the potential
        y_sup: Supporting y coordinates of the potential
        method: Either polynomial, linear or a cubi spline

    Returns:
        The interpolation function of the potential.
    """
    if method == 'polynomial':
        return poly(x_sup, y_sup)
    elif method == 'linear':
        return interp1d(x_sup, y_sup, kind='linear')
    elif method == 'cspline':
        return CubicSpline(x_sup, y_sup, bc_type='natural')
    print("\nInterpolation method doesn't exist. Chose either linear, polynomial or cspline.\n")
    sys.exit(1)

