# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:19:02 2019

@author: Emanuel

"""




from scipy.interpolate import lagrange as poly
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
#from scipy.interpolate import BarycentricInterpolator as poly
"""import interpolation methods from scipy. Lagrange is very basic and is numerically unstable. Uncomment last line to use differenct interpolating method"""


def interpolator(x,y,method):
    """Used to interpolate the Potential from a given set of points using a given method. The method can either be polynomial, linear or cspline (natural cubic spline))."""
    if method=='polynomial':
        return poly(x,y)
    elif method=='linear':
        return interp1d(x,y,kind='linera')
    elif method=='cspline':
        return CubicSpline(x,y,bc_type='natural')
