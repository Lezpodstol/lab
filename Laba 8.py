# Задание 1

class Pair:
    def __init__(self, n1, n2):
        self.n1_ = n1
        self.n2_ = n2

    def nPrint(self):
        print(f'n1 = {self.n1_}, n2 = {self.n2_}')

    def set_n(self):
        self.n1_ = float(input('Новый n1: '))
        self.n2_ = float(input('Новый n2: '))

    def nSum(self):
        return self.n1_ + self.n2_

    def nMax(self):
        return max(self.n1_, self.n2_)

x1, x2 = list(map(float, input('Первая пара чисел: ').split()))
p = Pair(x1,x2)
p.nPrint()
print('Сумма чисел в паре: ', p.nSum())
print('Макс. число в паре: ', p.nMax())
p.set_n()
print('Новое макс. число в паре: ', p.nMax())

# Задание 2

class Polynom:
    def __init__(self, *ps):
        self.prods = list(ps)
        self.n = len(ps) - 1

    def x(self, x):
        res = 0
        for i, p in enumerate(self.prods):
            res += p * x ** i
        return res

    def __str__(self):
        res = ''
        for i, p in enumerate(self.prods):
            if p == 0:
                continue
            if res:
                sSign = ' + ' if p > 0 else ' - '
            else:
                sSign = '- ' if p < 0 else ''
            sVal = str(abs(p)) if abs(p) != 1 else ''
            if i > 1:
                sPol = f'x^{i}'
            elif i == 1:
                sPol = 'x'
            elif not  sVal:
                sPol = '1'
            else:
                sPol = ''
            res += (sSign + sVal + sPol)
        return res

    def __add__(self, other):
        prods = []
        for i in range(max(self.n, other.n)+1):
            p0 = 0
            if i <= self.n:
                p0 += self.prods[i]
            if i <= other.n:
                p0 += other.prods[i]
            prods.append(p0)
        return Polynom(*prods)


    def __sub__(self, other):
        prods = []
        for i in range(max(self.n, other.n)+1):
            p0 = 0
            if i <= self.n:
                p0 += self.prods[i]
            if i <= other.n:
                p0 -= other.prods[i]
            prods.append(p0)
        return Polynom(*prods)


    def __mul__(self, other):
        prods = [0] * (self.n + other.n + 1)
        for i, p1 in enumerate(self.prods):
            for j, p2 in enumerate(other.prods):
                prods[i + j] += p1 * p2
        return Polynom(*prods)

p1 = Polynom(1, 2, 1)
print('p1(x) = ', str(p1))
print('p1(2) = ', p1.x(2))
p2 = Polynom(3,2)

print('(', str(p1), ') + (', str(p2), ') = ', str(p1+p2), sep='')
print('(', str(p2), ') + (', str(p1), ') = ', str(p2+p1), sep='')
print('(', str(p1), ') - (', str(p2), ') = ', str(p1-p2), sep='')
print('(', str(p2), ') - (', str(p1), ') = ', str(p2-p1), sep='')
print('(', str(p1), ') * (', str(p2), ') = ', str(p1*p2), sep='')
print('(', str(p2), ') * (', str(p1), ') = ', str(p2*p1), sep='')

# Задание 3

class Vec:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({str(self.x)}, {self.y}, {self.z})'

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) is Vec:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return Vec(self.x * other, self.y * other, self.z * other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def cos(self, other):
        return (self * other) / (abs(self) * abs(other))


v1 = Vec(1, 2, 3)
v2 = Vec(-3, -4, -1)
print(v1, '+', v2, '=', v1 + v2)
print(v1, '-', v2, '=', v1 - v2)
print(v1, '*', v2, '=', v1 * v2)
print('cos(', v1, ', ', v2, ') = ', v1.cos(v2), sep='')
print(v1, '*', 2, ' = ', v1 * 2)

# Задание 4

from datetime import time

class train:
    def __init__(self, p0, p1, t0, t1):
        self.p_start = p0
        self.p_dest = p1
        self.t_start = t0
        self.t_dest = t1

    def __add__(self, other):
        if self.p_dest == other.p_start and self.t_dest < other.t_start:
            return train(self.p_start, other.p_dest, self.t_start, other.t_dest)
        else:
            return None

train1 = train("Москва", "Волгоград", time(9,0), time(15,0))
train2 = train("Волгоград", "Сочи",  time(17,0),  time(23,0))

train12 = train1 + train2
if train12 is not None:
    print(train12.p_start, train12.t_start, '->', train12.p_dest, train12.t_dest)