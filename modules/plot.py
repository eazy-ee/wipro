"""
Creates a plot of the previously calculated results of 'schroedinger.py'
"""


import matplotlib.pyplot as plt
import numpy as np


def visualizer(path, scale):
    """script to plot wavefunctinos, energies, expectations values and uncertainty

    Args:
        path: path to the output of a previous calculation
        scale: Scales the wavefunctions

    Returns:
        matplotlib subplot containing two plots of given output.
    """
    potential = np.loadtxt(str(path)+'potential.dat')
    psi = np.loadtxt(str(path)+'wavefuncs.dat')
    energies = np.loadtxt(str(path)+'energies.dat')
    x_exp = np.loadtxt(str(path)+'expvalues.dat')[:, 0]
    sigma_x = np.loadtxt(str(path)+'expvalues.dat')[:, 1]

    fig, axs = plt.subplots(1, 2)
    for i in range(0, len(energies)):
       #sym=blau, asym=rot
        if i%2 == 0:
            color = 'blue'
        elif i%2 == 1:
            color = 'red'
        #psi plot um w geschifted und gestreckt/gestaucht
        axs[0].plot(psi[:, 0], psi[:, i+1]*float(scale)+energies[i], color=color, linewidth=1)
        #transparenter grau ton für eigenwerte
        axs[0].axhline(energies[i], xmin=potential[0, 0], xmax=potential[-1, 0],
                       linewidth=.3, color=(0, 0, 0, 0.75))
        axs[1].axhline(energies[i], xmin=potential[0, 0], xmax=potential[-1, 0],
                       linewidth=.3, color=(0, 0, 0, 0.75))
        axs[0].scatter(x_exp[i], energies[i], marker='x', color='green', s=100)
        axs[1].scatter(sigma_x[i], energies[i], marker='+', color='red', s=100)
    #plotting params['first'] to params['last']
    #potentialplot
    axs[0].plot(potential[:, 0], potential[:, 1], color='black', linewidth=1)

    #achsenlimits
    axs[0].set_xlim(potential[0, 0], potential[-1, 0])
    axs[0].set_ylim(energies[0]-.5, energies[-1]+.5)
    return axs
