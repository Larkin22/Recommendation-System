# -*- coding: utf-8 *--
"""
Created on Mon Jun 27 16:42:20 2016

@author: Pavilion
"""

#build a dataset
from deliciousrec import *
delusers=initializeUserDict('programming')
#delusers ['tsegaran']={} # Add yourself to the dictionary if you use delicious
fillItems(delusers)