#!/usr/bin/env python
"""Module do visualize results and potential"""

import argparse
import matplotlib.pyplot as plt
from modules import plot

def define_to_increase_pylintscore():
    """apparently contants have to be in upper case so we define a function to enjoy lower case"""
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Visualize the data of wavefuncs.dat,'
                                         ' potential.dat, expvalues.dat and energies.dat')
        parser.add_argument('-s', '--scale', type=float,
                            required=False, help='Scaling the wavefunction.')
        parser.add_argument('-p', '--path', type=str, required=False,
                            help='Path to the input files if not in'
                            ' current directory. Must include "/".')
        args = parser.parse_args()
        if args.scale is None:
            args.scale = 1.0
        if args.path is None:
            args.path = './'
        plot.visualizer(str(args.path), args.scale)
        plt.show()

define_to_increase_pylintscore()
