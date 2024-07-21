def evklid(a,b):
    if a != 0 and b != 0:
        if a>b:
            a=a%b
        else:
            b=b%a
        return evklid(a,b)
    else:
        return a+b
print(evklid(int(input()),int(input())))