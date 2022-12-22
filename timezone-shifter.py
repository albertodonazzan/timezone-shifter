# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:43:16 2022

@author: albertodonazzan
"""

import os

fld = r'F:\WIP\[2022-11-13] Japan\temp\\'
timeshift = 8 #time shift in hours

ls = os.listdir(fld)


n = ls[0]

nsplit = n.split('_')
HH = nsplit[1][0:2]
HHs = f'{int(HH) + timeshift:02}'

nsplit[1] = nsplit[1].replace(HH, HHs, 1) # replace only first instance

ns = '_'.join(nsplit)

# rename file...