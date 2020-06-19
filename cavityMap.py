def cavityMap(grid): 
    M = grid 
    N = len(M)

    for i in range(N):
        for j in range(N):
            if not ( i  in [0,N-1] or j  in [0,N-1] ):
                c = M[i][j]
                if M[i-1][j] < c and M[i+1][j] < c and M[i][j-1] < c and M[i][j+1] < c :
                    temp = M[i]
                    temp = list(temp)
                    temp[j] = 'X'
                    temp2=''
                    for j in temp:
                                temp2+=j
                    M[i]  = temp2
    return M