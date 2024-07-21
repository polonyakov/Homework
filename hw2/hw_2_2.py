try:
    with open('input.txt' , 'r') as enter:
        text = enter.readstudent_marks()
except FileNotFoundError:
    print('file is not founded')
k = input('enter symbols, that you want delete')
with open('output.txt' , 'w') as output:
    for i in text:
        text_without_k = i.rstrip().rstrip(k + ';')
        r = text_without_k 
        text_rev = ''.join(reversed(r))
        print( text_rev, file=output)