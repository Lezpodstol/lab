# Задание 1

def write_to_file():
    nLst = input('Ввод чисел в одну строку: ').split()
    with open('t1_file.txt', 'a') as f:
        f.writelines([n + '\n' for i, n in enumerate(nLst)])

def read_from_file():
    err = False
    s = 0
    max_n = None
    min_n = None
    try:
        with open('t1_file.txt', 'r') as f:
            for l in f:
                if len(l) == 0:
                    continue
                n = float(l)
                if min_n is None:
                    max_n = n
                    min_n = n
                max_n = max(max_n, n)
                min_n = min(min_n, n)
                s += n
    except:
        return print('File Error')
        err = True
    if not err:
        with open('t1_file.txt', 'a') as f:
          f.writelines([str(max_n) + '\n', str(min_n) + '\n', str(s) + '\n'])


write_to_file()
read_from_file()

write_to_file()
read_from_file()

# Задание 2

def write_to_file():
    nLst = input('Ввод чисел в одну строку: ').split()
    with open('t2_file.txt', 'a') as f:
        f.writelines([n + '\n' for i, n in enumerate(nLst)])

def read_from_file():
    err = False
    s = 0
    max_n = None
    min_n = None
    try:
        with open('t2_file.txt', 'r') as f:
            for l in f:
                try:
                    n = float(l)
                except:
                    continue
                if min_n is None:
                    max_n = n
                    min_n = n
                max_n = max(max_n, n)
                min_n = min(min_n, n)
                s += n
    except:
        return print('File Error')
        err = True
    if not err:
        with open('t2_file.txt', 'a') as f:
          f.writelines([str(max_n) + '\n', str(min_n) + '\n', str(s) + '\n'])

for i in range(3):
    write_to_file()
    read_from_file()
    
# Задание 3

def cinema_stats(filename, row=-1, place=-1):
    n_all = 0
    n_fre = 0
    n_occ = 0
    res = 'Место не запрошено' if row <= 0 else 'Место не найдено'

    with open(filename, 'r') as f:
        for i, l in enumerate(f):
            places = list(map(int, l.split()))
            n0_all = len(places)
            n0_occ = sum(places)
            n0_fre = n0_all - n0_occ
            print(f'Ряд: {i+1}, мест: {n0_all}, занято: {n0_occ}, свободно: {n0_fre}')
            n_all += n0_all
            n_fre += n0_fre
            n_occ += n0_occ
            if (i+1) == row:
                if 0 < place <= n_all:
                    res = 'Место занято' if places[place-1] == 1 else 'Место свободно'
        print(f'Итого, мест: {n_all}, занято: {n_occ}, свободно: {n_fre}')
        print(res)


with open('t3_file.txt', 'w') as f:
    f.writelines(['0 0 1 1\n', '0 0 0 1 1\n', '1 1 0 1\n'])

r = int(input('Номер ряда: '))
p = int(input('Номер места: '))
cinema_stats('t3_file.txt', r, p)

# Задание 5

from os.path import abspath
print(abspath("Laba 6.ipynb"))


# Доп задание 2 (Ctrl-C)

import os
filename = input('Имя файла для копии')
cmd = 'cp ' + filename +' "Copy ' + filename + '"'
os.system(cmd)