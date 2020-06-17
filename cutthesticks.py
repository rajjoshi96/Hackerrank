#def cutthesticks(arr)
from collections import Counter
def cutTheSticks(arr):

    l = len(arr) ; c = Counter(arr)
    for k in sorted(c) : yield l ; l -= c[k]



#sample input: 6 newline: 5 4 4 2 2 8
#sample Output: 6 4 2 1