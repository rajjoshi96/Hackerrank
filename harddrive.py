#!/bin/python3

import os
import sys

#
# Complete the hardDrive function below.
#
def hardDrive(k, hdds):
    print(k)
    print(hdds)
    sum=0
    for x in range(len(hdds)):
        for y in range(len(hdds)):
            sum=hdds[x]+hdds[y]
            print("sum=",sum)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    hdds = []

    for _ in range(n):
        hdds.append(list(map(int, input().rstrip().split())))

    result = hardDrive(k, hdds)

    #fptr.write(str(result) + '\n')

    #fptr.close()
