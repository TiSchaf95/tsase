Follow installation instructions on https://theory.cm.utexas.edu/tsase/index.html

Minimal example python script for constrained, fixed cell ssNEB calculation:

import numpy as np
from ase.io import read
from deepmd.calculator import DP
from tsase import neb

dp=DP(model='PATH TO DP MODEL')

calc=dp
images=[]

for i in range(11):
    images.append(read('image'+str(i)+'.cif', format='cif'))  # read predefined configurations


for i in range(len(images)):
    images[i].calc = calc # append calculator to images

fix=np.zeros((3,3)) # Fix cell parameters
nim = len(images)  

pres=np.identity(3)*10 # Target Pressure in GPa

band = neb.ssneb(images[0], images[-1], numImages = len(images),  k=5, express=pres, fixstrain=fix,  method = 'ci', nebimages=images)
opt = neb.fire_ssneb(band, maxmove =0.02, dtmax = 0.01, dt=0.001)
opt.minimize(forceConverged=0.05, maxIterations =3000)
