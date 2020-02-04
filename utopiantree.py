#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
	h=1
	a=n
	for i in range(0,a):
		if n % 2 != 0:
			h=n*2
		elif n % 2 == 0:
			h=((n-1)*2)+1

	print('H=',h)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        #fptr.write(str(result) + '\n')

    #fptr.close()
