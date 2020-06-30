def chocolateFeast(n, c, m):
    chocolate = n//c
    wrappers = chocolate

    while wrappers // m > 0:
        new_chocolate = wrappers // m
        wrappers -= new_chocolate * m
        wrappers += new_chocolate
        chocolate += new_chocolate
        
    return chocolate