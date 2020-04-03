def composite(b):
    l=[]
    for num in range(4, 5000 + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0 and num % 2 != 0:
                    l.append(num)
                    break
            else:
                print(num)
    print("The n composite term is: ",l[b-1])
composite(333)