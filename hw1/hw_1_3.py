n=input()
while not n.isdigit():
    n=input()
n=int(n)
while n > 9:
    n=sum([int(i) for i in str(n)])
print(n)