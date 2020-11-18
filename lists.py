if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(0,N):
        a=(input().split(' '))
        cmd=a[0]
        arg=a[1:]
        if cmd!='print':
            cmd += "(" + ",".join(arg) + ")"
            eval("l."+cmd)
        else:
            print(l)