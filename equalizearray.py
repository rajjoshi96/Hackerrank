from collections import Counter
def equalizeArray(arr):
    return len(arr)-max([arr.count(x) for x in arr])