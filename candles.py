#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
	l1=list(ar)
	a=max(l1)
	count=0
	for i in range(len(l1)):
		if l1[i]==a:
			count+=1
	#print(f'count = {count}')
	return count
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
