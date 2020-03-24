#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c=s.count('a')
    a=n//len(s)
    b=n%len(s)
    co=c*a + s[:b].count('a')
    return(co)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
