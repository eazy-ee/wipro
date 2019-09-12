# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:19:02 2019

@author: Emanuel

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
    """
    if method == 'polynomial':
        return poly(x_sup, y_sup)
    elif method == 'linear':
        return interp1d(x_sup, y_sup, kind='linear')
    elif method == 'cspline':
        return CubicSpline(x_sup, y_sup, bc_type='natural')
    print("\nInterpolation method doesn't exist. Chose either linear, polynomial or cspline.\n")
    sys.exit(1)
     