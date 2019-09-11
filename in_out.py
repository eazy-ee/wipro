"""
Reading input and savin results
"""

import numpy as np

def params():
    """
    Reading inputfile.

    inp: Path to input file
    """
    inp=input("Please enter path to the input file if the file is not located in the same directory as the script file or if the filename is not \"schroedinger.inp\": ")

    if inp=="":
        inp="./schroedinger.inp"
    else:
        inp=inp

    with open(inp, 'r') as inp:
       for line in inp:
          if 'mass' in line:
             M=float(np.fromstring(line, dtype=float, sep=' '))
          elif 'xMin' in line:
             xMin=np.fromstring(line, dtype=float, sep=' ')[0]
             xMax=np.fromstring(line, dtype=float, sep=' ')[1]
             nPoint=int(np.fromstring(line, dtype=float, sep=' ')[2])
          elif 'first and last' in line:
             first=np.fromstring(line, dtype=int, sep=' ')[0]
             last=np.fromstring(line, dtype=int, sep=' ')[1]
          elif 'type' in line:
             method=line.split(' ')[0]
          elif 'nr. of' in line:
             pot=np.loadtxt(inp.readlines())
             x=pot[:,0]
             y=pot[:,1]
    return M, xMin, xMax, nPoint, first, last, method, pot, x, y

def output(potential, energies, wavefuncs, x_exp, sigma_x, xnew, first, last):
    """
    Save potential, eigenvalues, eigenfunctions, expactation value and uncertainty of x
    """
    np.savetxt('potential.dat', np.concatenate((np.reshape(xnew, (1999,1)), np.reshape(potential(xnew),(1999,1))),axis=1))
    np.savetxt('energies.dat', energies[first-1:last])
    np.savetxt('wavefuncs.dat', np.concatenate((np.reshape(xnew,(1999,1)), np.transpose(wavefuncs[first-1:last])),axis=1))
    np.savetxt('expvalues.dat', np.concatenate((np.reshape(x_exp, (1999,1)), np.reshape(sigma_x,(1999,1))),axis=1))
