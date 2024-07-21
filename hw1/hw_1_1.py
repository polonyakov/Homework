n=input()
while not n.isdigit():
    n=input()
n=int(n)
for i in range(0,n+1):
    print(' '*(n-i) + '*'*(2*i-1))