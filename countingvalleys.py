#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	c=valley=0
	#a=list(s)
	for i in s:
		if i=='U':
			c+=1
		else:
			c-=1
		if i=='U' and c==0:
			valley+=1
	'''altitude = valley = 0

	for step in s:
		altitude += 1 if step == 'U' else -1
		if altitude == 0 and step == 'U':
			valleys += 1'''
	print(valley)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    #fptr.write(str(result) + '\n')

    #fptr.close()
