# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:59:53 2019

@author: Emanuel
"""


import time
import numpy as np
import matplotlib.pyplot as plt
import interpolator
import scipy.linalg as sp



start= time.time()


with open('schroedinger.inp.dat', 'r') as inp:
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




print('%s seconds at reading inp' % (time.time()-start))




V = getattr(interpolator, method)(x,y)
xnew=np.linspace(xMin,xMax,nPoint)

#writing potential to potential.dat
with open('potential.dat', 'w') as pot:
   for i in xnew:
      pot.write(str(i)+' '+str(V(i)))

#delta x
delta=xnew[1]-xnew[0]

print('%s seconds at pot interpol' % (time.time()-start))


#haupt/nebendiagonalen  und loesung der eig gl
N = np.array([-1/(2*M*delta**2) for i in range(len(xnew)-1)])
H = np.array([1/(M*delta**2)+V(i) for i in xnew])

w, v = sp.eigh_tridiagonal(H,N)



print('%s seconds at solving eigh' % (time.time()-start))



#eigenwerte speichern
# =============================================================================
# with open('energies.dat', 'w') as energies:
#    for i in range(first-1,last):
#       energies.write(str(w[i])+'\n')
# =============================================================================
np.savetxt('energies.dat', w[first-1:last])


#Normierung psi wellenfunktknnnnnnnnnnnnnnnn xd
psi = np.array([v[:,i]/np.sqrt(delta) for i in range(0,len(xnew))])

#wellenfunktionen speichern

# =============================================================================
# with open('wavefuncs.dat', 'w') as wavefuncs:
#    for i in range(0,len(xnew)):
#       wavefuncs.write(str(xnew[i]))
#       for j in range(first-1,last):
#          wavefuncs.write(' '+str(psi[j][i]))
#       wavefuncs.write('\n')
# =============================================================================

np.savetxt('test.dat', np.concatenate((np.reshape(xnew,(1999,1)), np.transpose(psi[first-1:last])),axis=1))


print('%s seconds at saving wavefuncs' % (time.time()-start))


#erwartungswert und quadr. erwartungswert
x_exp= delta*np.array([np.sum(psi[i]*xnew*psi[i]) for i in range(0,len(psi))])
xsq_exp= delta*np.array([np.sum(psi*xnew**2*psi) for psi in psi])
#unschaerfe
sigma_x = np.sqrt(xsq_exp-x_exp**2)

#erwartungswerte speichern
with open('expvalues.dat', 'w') as expvalues:
   for i in range(first-1,last):
      expvalues.write(str(x_exp[i])+' '+str(sigma_x[i])+'\n')


#plotting first to last
#potentialplot
plt.plot(xnew, V(xnew),color='black', linewidth=1)
#eigenfunktionen plot
for i in range(first-1,last):
   #sym=blau, asym=rot
   if i%2==0:
      color='blue'
   elif i%2==1:
      color='red'
   #psi plot um w geschifted und gestreckt/gestaucht
   plt.plot(xnew, psi[i]/3+w[i], color=color, linewidth=1)
   #transparenter grau ton für eigenwerte
   plt.axhline(w[i], xmin=xMin, xmax=xMax, linewidth=.3, color=(0, 0, 0, 0.75))
   plt.scatter(x_exp[i],w[i],marker='x', color='green', s=100)
   
#achsenlimits
plt.xlim(xMin,xMax)
plt.ylim(w[0]-.5,w[last]+.5)



print('%s seconds at end' % (time.time()-start))


