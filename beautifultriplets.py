# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:01:22 2020

@author: Paresh Joshi
"""

#!/bin/python3

import math
import os
import random
import re
import sys

n,d=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n-2):
    if l[i]+d in l and l[i]+2*d in l:
        c+=1
print (c)
    #fptr.write(str(result) + '\n')

    #fptr.close()
