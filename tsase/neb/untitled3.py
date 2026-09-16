#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:27:14 2023

@author: tim
"""

from ase.io import read,write
test=read('/home/tim/Schreibtisch/300_d/geo_end.geninput', format='gen')
from ase.build import make_supercell
test=make_supercell(test, [[2,0,0], [0,1,0],[0,0,2]])
write('Coesite_SC_Chimes.cif', test, format='cif')
