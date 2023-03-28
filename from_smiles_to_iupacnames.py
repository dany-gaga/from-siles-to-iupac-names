#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:52:15 2023

@author: dukpe
"""

import pubchempy as pcp
import os
import pandas as pd

from pubchempy import Compound, get_compounds

os.chdir('/home/dukpe/Desktop/git repository  forked/')

chem = pd.read_csv('predictedpkd_100.csv')

chem1 = chem["SMILES"].tolist()

ch = []
for c in chem1:
    c1 = pcp.get_compounds(c, 'smiles')
    ch.append(c1)
    
from itertools import chain
    
ch1 =  list(chain.from_iterable(ch))

ch2 = []
for compound in ch1:
    t= compound.iupac_name
    ch2.append(t)


chem['compounds'], chem['iupac_name'] = ch1, ch2
