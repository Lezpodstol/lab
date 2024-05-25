# Задание 1

def task11(x):
    return (100 <= x <= 999) and (x % 10 == 0)

def task12(x):
    return (x % 2 == 1) and (x % 3 == 0) and (x % 5 == 0)

def task13(x):
    return 2 <= x <= 6

def task14(x):
    return (100 <= abs(x) <= 999) and (abs(x) % 10 == abs(x) % 100 // 10 == abs(x) // 100)

print('task11(', 110, '): ',  task11(110), sep='')
print('task11(', -15, '): ',  task12(-15), sep='')
print('task11(', 2, '): ',    task13(2), sep='')
print('task11(', -222, '): ', task14(222), sep='')

# Задание 2

def task2true(x):
    return (x % 3) < 5

def task2false(x):
    return (x > 5) and (x < 3)

x = float(input())
print(task2true(x))
print(task2false(x))

# Задание 3

def task31(x,y):
    return (x > 4 and y > 3) or ((x <= 4 and y <= 3) and x <= -y)

def task32(x,y):
    return (x**2 + y**2 >= 3) and (abs(x) <= 3) and (abs(y) <= 3)

def task33(x,y):
    return ((x-5) ** 2 + (y - 5) ** 2 >= 5) and (0 < x <= 5) and (0 < y <= 5)


print(task31(4, -4))
print(task32(3, 3))
print(task33(0.1, 0.1))

# Задание 4

def positive():
    print('Положительное')

def negative():
    print('Отрицательное')

def test(x):
    if (x > 0):
        positive()
    if (x < 0):
        negative()

test(-3)
test(2)
test(0)

# Задание 5

def getInput():
    return input()

def testInput(x):
    return (x) < ('-0123456789') and (x[1:]) < ('0123456789')

def strToInt(x):
    return int(x)

def printInt(x):
    return print(x)

s = getInput()
if testInput(s):
    printInt(strToInt(s))
