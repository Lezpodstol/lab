# Задание 1

import numpy as np
import matplotlib.pyplot as plt

class Geomfig:
    def __init__(self, coords, P = None, S = None):
        self.main_coords = coords
        self.P = P
        self.S = S

class Circle(Geomfig):
    def __init__(self, coords, r):
        Geomfig.__init__(self, coords, np.pi * r ** 2, 2 * np.pi * r)
        self.r = r
    def Paint(self):
        plt.gca().add_patch(plt.Circle(self.main_coords, self.r, fill =False));

class Triangle(Geomfig):
    def __init__(self, xs, ys):
        assert len(xs) == 3 and len(ys) == 3, 'число точек не соотв. треугольнику'
        Geomfig.__init__(self, (xs[0], ys[0]), \
                               np.linalg.norm(np.array([xs[0] - xs[1], ys[0] - ys[1]])) +  np.linalg.norm(np.array([xs[1] - xs[2], ys[1] - ys[2]])) + np.linalg.norm(np.array([xs[2] - xs[0], ys[2] - ys[0]])), \
                               0.5 * ((xs[0] - xs[2]) * (ys[1] - ys[2]) - (ys[0] - ys[2]) * (xs[1] - xs[2])))
        self.xs = list(xs)
        self.ys = list(ys)
    def Paint(self):
        plt.plot(self.xs + [self.xs[0]], self.ys + [self.ys[0]])

class Rectangle(Geomfig):
    def __init__(self, xs, ys):
        assert len(xs) == 4 and len(ys) == 4, 'число точек не соотв. прямоугольнику'
        Geomfig.__init__(self, (xs[0], ys[0]), \
                               2 * (np.linalg.norm(np.array([xs[0] - xs[1], ys[0] - ys[1]])) + np.linalg.norm(np.array([xs[1] - xs[2], ys[1] - ys[2]]))), \
                               (np.linalg.norm(np.array([xs[0] - xs[1], ys[0] - ys[1]])) * np.linalg.norm(np.array([xs[1] - xs[2], ys[1] - ys[2]]))))
        self.xs = list(xs)
        self.ys = list(ys)
    def Paint(self):
        plt.plot(self.xs + [self.xs[0]], self.ys + [self.ys[0]])


t = Triangle((0, 1, 1), (0, 0, 1))
t.Paint()
print(t.S, t.P)

с = Circle((0.5, 0.5), 1)
с.Paint()
print(с.S, с.P)

r = Rectangle((-0.1, 1.1, 1.1, -0.1), (-0.1, -0.1, 1.1, 1.1))
r.Paint()
print(r.S, r.P)

# Задание 2

import numpy as np


class Matrix:
    def __init__(self, lst):
        self.data = np.array(lst).copy()

    def __str__(self):
        res = ''
        n1, n2 = self.size()
        for i in range(n1):
            for j in range(n2): 
                res += str(self.data[i][j]) 
                res += '\t' if j + 1 < n2 else ''
            res += '\n' if i + 1 < n1 else ''
        return res

    def size(self):
        return self.data.shape

    def __add__(self, other):
        assert self.size() == other.size(), 'Неравенство размеров матриц'
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Matrix(self.data * other)
        if type(self) == float or type(self) == int:
            return Matrix(self * other.data)
        assert self.size()[1] == other.size()[0], "Несоответствие матриц для умножения"
        return Matrix(self.data @ other.data)

    __rmul__ = __mul__

    def T(self):
        return Matrix(self.data.T)

m1 = Matrix([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
m12 = Matrix([[1, 1, 1],[2, 2, 2],[3,3,3]])
m2 = Matrix([[0, 1, 2]])
print('m1 + m12 = \n', str(m1 + m12), sep='')
print('m2 @ m1 = \n', str(m2 * m1), sep='')
print('m1 = \n', str(m1))
print('m1^T = \n', str(m1.T()))
print('m1 * 3 = \n', str(m1 * 3))
print('4 * m1 = \n', str(4 * m1))

# Задание 3

class Vector(Matrix):
    def __init__(self, start, end):
        assert len(end) == len(start), 'параметр неравной размерности'
        lst = [[end[i] - start[i] for i in range(len(start))]]
        super().__init__(lst)
        self.p0 = start
        self.p1 = end


    def dot(self, other):
        assert self.size() == other.size(), 'вектора неравной размерности для скалярного произведения'
        return np.dot(self.data[0], other.data[0])


    def norm(self):
        return np.linalg.norm(self.data)

    def cos(self, other):
        return self.dot(other) / (self.norm() * other.norm())

    def info(self):
        print('Вектор = ', self)
        print('Нач. точка = ', self.p0)
        print('Конеч. точка = ', self.p1)
        print('Длина = ', self.norm())

    def cross(self, self2):
        return Vector([0, 0, 0], np.cross(self.data[0], self2.data[0]))

b = Vector([0, 0, 0], [1, 2, 3])
b.info()
a = Vector([1, 1, 1], [3, 2, 1])
print('Скалярное произведение:', a.dot(b))
print('Косинус угла:', a.cos(b))
print('Вектор, перпендикулярный обоим векторам:', a.cross(b))
