#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:52:15 2023

@author: dukpe
"""

# import libraries
import sys
import pandas as pd
from itertools import chain
import pubchempy as pcp
from pubchempy import Compound, get_compounds

# read the csv file
chem = pd.read_csv(sys.argv[1])

chem1 = chem.iloc[:,0].tolist()

ch = []
for c in chem1:
    c1 = pcp.get_compounds(c, 'smiles')
    ch.append(c1)
        
ch1 =  list(chain.from_iterable(ch))

ch2 = []
ch3 = []
ch4 = []

for compound in ch1:
    t= compound.iupac_name
    t1= compound.molecular_formula
    t2= compound.molecular_weight
    ch2.append(t)
    ch3.append(t1)
    ch4.append(t2)


chem['compounds'], chem['iupac_name'], chem['mol_weight'], chem['weight'] = ch1, ch2, ch3, ch4

chem.to_csv('smiles_iupacname.csv')
