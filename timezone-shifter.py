# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:43:16 2022

@author: albertodonazzan
"""

import os
import datetime as dt
import dateutil as du
import re
from tabulate import tabulate


def filenameTimeShift(filename, timeshift):
    '''

    Parameters
    ----------
    filename : str
        Filename
    timeshift : list
        Desired time shift in the list format [days, hours, minutes, seconds].

    Returns
    -------
    tsstr : str
        New shifted time string for filename renaming.

    '''
    
    d, H, M, S = timeshift
    # t, fuz = du.parser.parse(filename, fuzzy=True, yearfirst=True, 
    #                          fuzzy_with_tokens=True)
    
    # extract date
    r = re.findall('\d+', filename )
    r = [d for d in r if (len(d) in [6,8,12,14])]
    tstr = ''.join(r)                         # build time string in desired format
    
    presuf = filename.rsplit(r[0])[0] + filename.rsplit(r[-1])[-1] # take prefix and suffix
    
    t = dt.datetime.strptime(tstr, '%Y%m%d%H%M%S')   # parse substring
    ts = t + dt.timedelta(days=d, hours=H, minutes=M, seconds=S) # add timeshift
    
    tsstr = ts.strftime('%Y%m%d_%H%M%S') # convert to string
    
    # build new filename
    fn_shift = tsstr + presuf
    
    return fn_shift


# fld = r'D:\WIP\[2022-11-13] Japan\temp\\'
fld = r'C:\_WORK\git\timezone-shifter\test'
timeshift = [0, 0, -10, 0] # time shift in [days, hours, minutes, seconds]

ls = os.listdir(fld)

# loop through folder and show names preview
lss =[]
for fn in ls:
    lss.append(filenameTimeShift(fn, timeshift))
print('Files will be renamed as follows:\n')
print(tabulate(list(zip(*[ls,lss])))) # build 2D list, transpose, tabulate


user_input = input('Do you want to proceed (yes/no): ')

if user_input.lower() in ['yes', 'y']:
    # loop through folder and rename
    for fn in ls: 
        fns = filenameTimeShift(fn, timeshift)
        os.rename(fld+'\\'+fn, fld+'\\'+fns)
    print('All files renamed.')
elif user_input.lower() in ['no', 'n']:
    print('Calceled')
else:
    print('Canceled.')

