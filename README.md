# tsase – Transition State Library for ASE

This repository contains Python code based on the **Atomic Simulation Environment (ASE)** to perform transition state calculations.

## Installation

Please follow the detailed installation instructions on the official website:
👉 [TSASE Installation Guide]([https://theory.cm.utexas.edu/tsase/index.html])

## Usage Example

Below is a minimal example Python script for a constrained, fixed-cell solid-state Nudged Elastic Band (**ssNEB**) calculation using a DeepMD calculator.

```python
import numpy as np
from ase.io import read
from deepmd.calculator import DP
from tsase import neb

# Initialize DeepMD calculator
dp = DP(model='PATH TO DP MODEL')
calc = dp
images = []

# Read predefined configurations (11 images)
for i in range(11):
    images.append(read('image' + str(i) + '.cif', format='cif'))

# Append calculator to all images
for i in range(len(images)):
    images[i].calc = calc

# Fix cell parameters
fix = np.zeros((3, 3))
nim = len(images)  

# Target Pressure in GPa (10 GPa)
pres = np.identity(3) * 10 

# Set up the solid-state NEB (ssNEB) band
band = neb.ssneb(
    images[0], 
    images[-1], 
    numImages=len(images),  
    k=5, 
    express=pres, 
    fixstrain=fix,  
    method='ci', 
    nebimages=images
)

# Optimize using the FIRE algorithm
opt = neb.fire_ssneb(band, maxmove=0.02, dtmax=0.01, dt=0.001)
opt.minimize(forceConverged=0.05, maxIterations=3000)
```

## References & Contributors

This library includes contributions from:
* Rye Terrell (UT)
* Sam Chill (UT)
* Penghao Xiao (UT)
* Juliana Duncan (UT)
* Shannon Stauffer (UT)
* Rileigh Bandy (UT)
* Jan Janssen (LANL)
