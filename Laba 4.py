# Задание 1

def try_to_sum(s1, s2):
    try:
        res = int(s1) + int(s2)
    except:
        res = str(s1) + str(s2)
    return res

s1 = input()
s2 = input()
print(try_to_sum(s1, s2))

# Задание 2

from math import ceil

def log_rez(k,n,r):
    if k > n:
        return r
    return log_rez(2*k, n, r+1)


n = int(input('Гостей: '))
print(f'{log_rez(1, n, 0)} разрезов, чтобы каждому из гостей достался хотя бы 1 кусок')
print(f'{log_rez(1, n + ceil(n/2), 0)} разрезов, чтобы минимум половине досталось по 2 куска')
print(f'{log_rez(1, n + 10, 0)} разрезов, чтобы каждому по куску и осталось минимум 10')

# Задание 3

def fib_exp(n):
    s5 = 5 ** 0.5
    return (((1 + s5) / 2) ** (n+1) - ((1 - s5) / 2) ** (n+1)) / s5

i = 1
f0 = 0
f1 = 1
while True:
    ft = f0 + f1
    if abs(fib_exp(i) - (ft)) > 0.001:
        print('n =', i)
        print(fib_exp(i), (ft))
        break
    f0 = f1
    f1 = ft
    i += 1
    
# Задание 4
    
def play(n, m):
    n0 = 0
    m0 = 1
    while True:
        if m - m0 > 0:
            m -= m0
            #print(n0+1, m)
        else:
            print('Проиграл №', n0 + 1, sep='')
            break
        m0 = (m0 * 2) % 25
        n0 = (n0 + 1) % n

kp = int(input('Число игроков: '))
kd = int(input('Кол-во кубиков: '))

play(kp, kd)
