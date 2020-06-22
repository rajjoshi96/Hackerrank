def fairRations(B):
    total = 0
    a = None
    flips = 0
    for i in range(len(B)):
        if B[i]%2 and a == None:
            total += 1
            a = i
        elif B[i]%2:
            total += 1
            flips += i - a
            a = None             
    return 'NO' if total%2 else flips * 2