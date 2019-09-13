"""Module do visualize results and potential"""

import matplotlib.pyplot as plt
import numpy as np

<<<<<<< HEAD
def visualizer(psi, potential, energies, x_exp, sigma_x, scale, **params):
=======
def visualizer(psi, potential, energies, x_exp, sigma_x, **params):
>>>>>>> 0e99165d292b14170ead09a40d4fe3392d11410f
    """script to plot wavefunctinos, energies, expectations values and uncertainty"""

    xnew = np.linspace(params['x_min'], params['x_max'], params['n_point'])
    fig, axs = plt.subplots(1, 2)
    for i in range(params['first']-1, params['last']):
       #sym=blau, asym=rot
        if i%2 == 0:
            color = 'blue'
        elif i%2 == 1:
            color = 'red'
         #psi plot um w geschifted und gestreckt/gestaucht
<<<<<<< HEAD
        axs[0].plot(xnew, np.array(psi[i])*float(scale)+energies[i], color=color, linewidth=1)
=======
        axs[0].plot(xnew, psi[i]/3+energies[i], color=color, linewidth=1)
>>>>>>> 0e99165d292b14170ead09a40d4fe3392d11410f
        #transparenter grau ton für eigenwerte
        axs[0].axhline(energies[i], xmin=params['x_min'], xmax=params['x_max'],
                       linewidth=.3, color=(0, 0, 0, 0.75))
        axs[1].axhline(energies[i], xmin=params['x_min'], xmax=params['x_max'],
                       linewidth=.3, color=(0, 0, 0, 0.75))
        axs[0].scatter(x_exp[i], energies[i], marker='x', color='green', s=100)
        axs[1].scatter(sigma_x[i], energies[i], marker='+', color='red', s=100)
    #plotting params['first'] to params['last']
    #potentialplot
    axs[0].plot(xnew, potential(xnew), color='black', linewidth=1)
    #eigenfunktionen plot


    #achsenlimits
    axs[0].set_xlim(params['x_min'], params['x_max'])
    axs[0].set_ylim(energies[0]-.5, energies[params['last']]+.5)
    return axs
