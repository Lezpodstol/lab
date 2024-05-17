# Задание 1

!wget https://introcs.cs.princeton.edu/java/data/pi-10million.txt

def find_pi(s):
    with open("pi-10million.txt") as f:
        f_str = f.read(len(s))
        for i in range(len(s), 10000000):
            if f_str == s:
                return i - len(s)
            f_str = f_str[1:] + f.read(1)
    return -1

print(find_pi('9' * 6))
print(find_pi('8' * 6))
print(find_pi('0' * 6))
print(find_pi('1231231'))


# Задание 2


def bin_search(lst, find):
    mn, mx = 0, len(lst) - 1
    while mn <= mx:
        qKey = int((mn + mx) / 2)
        val = lst[qKey]
        if val == find:
            return qKey
        if val > find:
            mx = qKey - 1
        else:
            mn = qKey + 1
    return -1

def golden_sec_search(lst, find):
    mn, mx = 0, len(lst) - 1
    while mn < mx:
        s = (mx - mn) /1.618034
        key1 = int(mx - s)
        key2 = int(mn + s)
        val1 = lst[key1]
        val2 = lst[key2]
        if val1 == find:
            return key1
        elif val2 == find:
            return key2
        elif val1 < find:
            mn = key1
        else:
            mx = key2
    return -1

def interpolation_search(lst, find):
    mn, mx = 0, len(lst) - 1
    while mn <= mx  and lst[mx] > find:
        if lst[mx] == lst[mn]:
            return -1
        qKey = mn + ((find - lst[mn])*(mx - mn))//(lst[mx] - lst[mn])
        val = lst[qKey]
        if val == find:
            return qKey
        if val > find:
            mx = qKey - 1
        else:
            mn = qKey + 1
    if lst[mn] == find:
        return mn
    if lst[mx] == find:
        return mx
    return -1
	
# Задание 1 невозможно выполнить методами из задания 2 - числа в последовательности pi 
# являются не отсортированными => найти искомые последовательности данными методами
# невозможно