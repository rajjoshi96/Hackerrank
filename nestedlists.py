if __name__ == '__main__':
    sc=[]
    na=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        na+=[[name,score]]
        sc+=[score]
    a=sorted([set(sc)])[1]
    for b,n in na:
        if a==n:
            print(b)