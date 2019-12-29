#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
	c=[0,0,0,0,0]
	for i in range(len(arr)):
		if arr[i]==1:
			c[0]+=1
		elif arr[i]==2:
			c[1]+=1
		elif arr[i]==3:
			c[2]+=1
		elif arr[i]==4:
			c[3]+=1
		else:
			c[4]+=1

	return c.index(max(c))+1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
