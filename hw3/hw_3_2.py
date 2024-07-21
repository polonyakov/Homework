try:
    with open('input.txt' , 'r') as enter:
        text = enter.readlines()
except FileNotFoundError:
    print('file is not founded')
dic = {} 
massive =[]
for i in text:
    if '{' not in i and '}' not in i:
        massive.append(i)
for y in massive:
    inp = y.split(':')
    inp[0] = inp[0].strip()
    inp[1] = inp[1].strip().strip(',')
    if inp[0] not in dic:

        dic[inp[0]] = inp[1]
    else :
        dic[inp[0]] = int(inp[1]) + int(dic[inp[0]]) 
with open ('output.txt', 'w') as output:
    for z,y in dic.items():
        print (z , ':' , y,file=output)

print(dic)