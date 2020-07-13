def swap_case(s):
    c=''
    for i in s:
        if i.isupper():
            c+=i.lower()
        elif i.islower():
            c+=i.upper()
        else:
            c+=i
    return c

if __name__ == '__main__':