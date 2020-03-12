#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
	hcount=0
	hmax=scores[0]
	for i in range(len(scores)):
		if scores[i]>hmax:
			hmax=scores[i]
			hcount+=1
	lmax=scores[0]
	lcount=0
	for i in range(len(scores)):
		if scores[i]<lmax:
			lmax=scores[i]
			lcount+=1
	print(hcount,lcount)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
