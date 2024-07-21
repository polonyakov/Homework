count = 0
n = 0
try:
    with open('input.txt','r') as enter:
        massive = enter.readlines()
except FileNotFoundError:
    print('file is not founded')
for i in massive:
    student_mark = i.split(',')
    student_mark[0] = student_mark[0].strip()
    student_mark[1] = student_mark[1].strip()
    count += int(student_mark[1])
    n += 1
men_value = count / n
for i in massive:
    student_mark = i.split(',')
    student_mark[0] = student_mark[0].strip()
    student_mark[1] = student_mark[1].strip()
    if float(student_mark[1]) > men_value:
        with open ('output.txt','a') as output:
            print(str(student_mark[0]) + ', ' + str(student_mark[1]),file=output)