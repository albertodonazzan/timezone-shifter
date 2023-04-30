# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:43:16 2022

@author: albertodonazzan
"""

import os

def timezoneShifter(DD, HH, timeshift):
    '''Shifts time zone of timestamp string with 1hour precision.

    Parameters
    ----------
    DD : int
        Day number.
    HH : int
        Hour.
    timeshift : TYPE
        Timeshift in hours.

    Returns
    -------
    DDs : int
        Day after shift.
    HHs : int
        Hour after shift.

    '''
    HHs = HH + timeshift
    HHs_mod = HHs % 24
    
    if HHs == HHs_mod:
        DDs = DD
    elif HHs < HHs_mod:
        DDs = DD-1
    else:
        DDs = DD+1
    HHs = HHs_mod
    
    return DDs, HHs


def filenameTimezoneShifter(filename, timeshift):
    '''Take filename and return filename with shifted timestamp.
    
    '''
    # take filename and extract day (DD) and hour (HH)
    nsplit = filename.split('_')
    DD = int(nsplit[0][-2:])
    HH = int(nsplit[1][0:2])
    
    DDs, HHs = timezoneShifter(DD, HH, timeshift)
      
    HH = f'{HH:02}'
    DD = f'{DD:02}'  
    HHs = f'{HHs:02}'
    DDs = f'{DDs:02}'
    
    nsplit[0] = nsplit[0].replace(DD, DDs, -1) # replace only last instance
    nsplit[1] = nsplit[1].replace(HH, HHs, 1)  # replace only first instance
    
    return '_'.join(nsplit)


# fld = r'F:\WIP\[2022-11-13] Japan\temp\\'
fld = r'C:\_WORK\git\timezone-shifter\test'
timeshift = 8 # time shift in hours

ls = os.listdir(fld)

for fn in ls: # loop through folder
    fns = filenameTimezoneShifter(fn, timeshift)
    os.rename(fld+'\\'+fn, fld+'\\'+fns)