# Задание 1

x = 2
print('Значение: ', x, 'тип: ', type(x))
x = x + 3
print('Значение: ', x, 'тип: ', type(x))
x = (x+1)/2
print('Значение: ', x, 'тип: ', type(x))
x = x + 1/2
print('Значение: ', x, 'тип: ', type(x))
x = x < 5
print('Значение: ', x, 'тип: ', type(x))
x = str(x)
print('Значение: ', x, 'тип: ', type(x))

# Задание 2

s = 0
for i in range(1, 6):
    s += i
mean_s = s / 5
print("Среднее значение этих 5 чисел равно", format(mean_s, '.5f'))


# Задание 3

s = 0
for i in range(1, 6):
    s += i
k = 5
mean_s = s / k
print("Среднее значение этих 5 чисел равно", format(mean_s, '.5f'))
s0 = float(input('Введите новое число (0 прекратит программу): '))
while s0 != 0:
    s = s + s0
    k += 1
    mean_s = s / k
    print(f"Среднее значение этих {k} чисел равно", format(mean_s, '.5f'))
    s0 = float(input('Введите новое число (0 прекратит программу): '))
    
    
# Доп. задание 2

a = int(input('Введите целое число: '))
sa = 0
while True:
    da = a
    sa = 0
    while da != 0:
        sa += da % 10
        da = da // 10
    if a == sa:
        break
    else:
        print('Новое число:', sa)
        a = sa
        
        
#Доп. задание 3

a = float(input('Введите число: '))
max_a = a
min_a = a
while True:
    a = float(input('Введите новое число: '))
    if a >= max_a:
        max_a = a
    if a <= min_a:
        min_a = a
    print(f'максимум :{max_a}, минимум {min_a}')

