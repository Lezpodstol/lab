# Задание 1

x = int(input())
sX = format(x, '04d')
if sX == sX[::-1]:
    print(1)
else:
    print(-1)
    
# Задание 2

y = int(input('Введите год: '))
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print('YES')
else:
    print('NO')
    
    
# Задание 3

n = int(input('Введите целое число: '))
print(f'На лугу пасётся {n} коров', end='')
if 4 < n % 100 < 21 or n % 10 == 0 or 4 < n % 10 < 10:
    print('')
elif n % 10 == 1:
    print('а')
elif 1 < n % 10 < 5:
    print('ы')
    
# Задание 4.1

x = int(input('Введите число: '))
found = False
for de in range(2, int(x**0.5) + 1):
    if x % de == 0:
        print('Наименьший натуральный делитель числа', x, ':', de)
        found = True
        break
if not found:
    print('Наименьший натуральный делитель числа', x, ':', x)


# Задание 4.2

x = int(input('Введите число: '))
de = 2
found = False
while de <= int(x**0.5) + 1:
    if x % de == 0:
        print('Наименьший натуральный делитель числа', x, ':', de)
        found = True
        break
    de += 1
if not found:
    print('Наименьший натуральный делитель числа', x, ':', x)


# Задание 5

xLst = []
while True:
    x0 = int(input('Введите число: '))
    if x0 != 0:
        xLst.append(x0)
    else:
        break

variant = int(input('Введите вариант обработки: '))
if variant == 1:
    print('Сумма послед-сти', sum(xLst))
elif variant == 2:
    prod = 1
    for x in xLst:
        prod *= x
    print('Произведение послед-сти', prod)
elif variant == 3:
    print('Среднее значение послед-сти', sum(xLst)/len(xLst))
elif variant == 4:
    print('Макс. значение послед-сти', max(a))
elif variant == 5:
    print('Мин. значение послед-сти', min(a))
elif variant == 6:
    k_even = 0
    k_odd = 0
    for x in xLst:
        if x % 2 == 0:
            k_even += 1
        else:
            k_odd += 1
    print(f'В послед-сти чётных чисел - {k_even}, а нечётных - {k_odd}')
else:
    print('Недействительный ответ')