def func1(text):
    lst = text.split(' ')
    text2=''
    for vava in lst:
        if len(vava)>5:
            text2+=' '+vava
    return text2[1:]

def func2(text):
    lst = text.split('_')
    print('\tФИО\t\tКатегория\t\tВозраст')
    for vava in lst[1:]:
        a= vava.split(';')
        print(a[0] + ' ' +a[1]+' '+a[2]+'\t'+a[4]+'\t\t'+a[3])

def func3(text):
    lst = text.split('_')
    for vava in lst[1:]:
        a = vava.split(';')
        if a[0].split(' ')[0]=='Петров':
            print(a)


def func4():
    n = int(input('Введите количество чисел '))
    lst = []
    for i in range(n):
        lst.append(int(input('Введите число ')))
    lst.pop(0)
    lst.pop(0)
    lst.append(int(input('Введите число ')))
    lst.append(int(input('Введите число ')))
    for vava in lst:
        print(str(vava))
    print(len(lst))
