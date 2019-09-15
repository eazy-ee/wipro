# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:19:02 2019

@author: Emanuel
"""

#interpolation of potential
#defines interpolation methods

from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
from scipy.interpolate import interp1d
#from scipy.interpolate import BarycentricInterpolator as bary



def polynomial(x,y):
   return lagrange(x,y)

def linear(x,y):
   return interp1d(x,y,kind='linear')

def cspline(x,y):
   return CubicSpline(x,y,bc_type='natural')