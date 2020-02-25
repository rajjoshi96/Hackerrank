#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    d=k
    for i in reversed(range(k)):
        c=a[k:] + a[:k]
        #print(c)
        k-=1
    for e in range(d+1):
        print(c[e])
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
