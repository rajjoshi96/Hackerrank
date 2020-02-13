#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
	l=[]
	count=0
	rev=str(n)
	for i in rev:
		l.append(int(i))
	print(l)
	for i in range(0,len(l)):
		if l[i]==0:
			i+=1
		elif n % l[i] == 0:
			count+=1
	print(count)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        #fptr.write(str(result) + '\n')

    #fptr.close()
