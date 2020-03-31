#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    res=[]
    for i in s:
        if res and res[-1] == i:
            res.pop()
        else:
            res.append(i)
    res=''.join(res)
    return(res or 'Empty String')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

