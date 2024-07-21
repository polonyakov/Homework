def stupenki(n):
    if n<2:
        return n
    return stupenki(n-1) + stupenki(n-2)
print(stupenki(int(input())+1))