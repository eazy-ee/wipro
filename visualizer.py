import matplotlib.pyplot as plt
import numpy as np

def visualizer(psi, V, w, x_exp, sigma_x, xMin, xMax, nPoint, first, last):
    """script to plot wavefunctinos, energies, expectations values and uncertainty"""

    xnew=np.linspace(xMin,xMax,nPoint)
    f, axs = plt.subplots(1,2)
    for i in range(first-1,last):
       #sym=blau, asym=rot
       if i%2==0:
          color='blue'
       elif i%2==1:
          color='red'
       #psi plot um w geschifted und gestreckt/gestaucht
       axs[0].plot(xnew, psi[i]/3+w[i], color=color, linewidth=1)
       #transparenter grau ton für eigenwerte
       axs[0].axhline(w[i], xmin=xMin, xmax=xMax, linewidth=.3, color=(0, 0, 0, 0.75))
       axs[1].axhline(w[i], xmin=xMin, xmax=xMax, linewidth=.3, color=(0, 0, 0, 0.75))
       axs[0].scatter(x_exp[i],w[i],marker='x', color='green', s=100)
       axs[1].scatter(sigma_x[i], w[i], marker='+', color='red', s=100)
    #plotting first to last
    #potentialplot
    axs[0].plot(xnew, V(xnew),color='black', linewidth=1)
    #eigenfunktionen plot


    #achsenlimits
    axs[0].set_xlim(xMin,xMax)
    axs[0].set_ylim(w[0]-.5,w[last]+.5)
    return axs
