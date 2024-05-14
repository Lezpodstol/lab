# Задание 1

def regstat(s):
    u = 0
    l = 0
    for c in s:
        if str.isupper(c):
            u += 1
        if str.islower(c):
            l += 1
    return u, l

s0 = input()
u, l = regstat(s0)
if u > l:
    print(str.upper(s0))
elif u < l:
    print(str.lower(s0))
else:
    print(s0)

# Задание 2

s0 = 'объектно-ориентированный'

print(s0[:6])
print(s0[9:17])
print(s0[14:17])
print(s0[4:15:5])
print(s0[10]+s0[12:15]+s0[-5])
print(s0[:6]+s0[15:20:3])

# Задание 3

sNum = []
sNum0 = []
while len(sNum) == 0:
    sInput = input()
    for i, c in enumerate(sInput):
        if str.isdigit(c):
            sNum0.append(c)
        if c == ' ':
            sNum.append(sNum0) if len(sNum0) > 0 else 0
            sNum0 = []
sNum.append(sNum0) if len(sNum0) > 0 else 0
print(sum(list(map(lambda s: int(''.join(s)),sNum))))

# Задание 4

def reverse_dict(item_list):
    res = {}
    for k,v in item_list:
        res[v] = k
    return res

d = {1: 'one', 2: 'two', 3: 'three'}
dict_items = d.items()
reverse_dict(dict_items)

# Задание 5

def getclass(s):
    res = []
    for c in s:
        if str.isdigit(c):
            res.append(c)
    return int(''.join(res))

def update(d, key, new_k):
    cl = getclass(key)
    d[cl][key] = new_k

def insert(d, new_key, new_k):
    cl = getclass(new_key)
    if cl not in d.keys():
        d[cl] = dict()
    d[cl][new_key] = new_k

def delete(d, del_key):
    cl = getclass(del_key)
    rem_cl = len(d[cl]) - 1
    k_del = d[cl].pop(del_key,0)
    if rem_cl > 0:
        k_rem_to_all = k_del // rem_cl
        k_rem_rem = k_del % rem_cl
        for k in d[cl]:
            d[cl][k] += k_rem_to_all + (1 if k_rem_rem > 0 else 0)
            k_rem_rem -= 1

def select(d):
    sum_k = 0
    k_cl = 0
    for cl in sorted(d.keys()):
        for cl0 in d[cl].keys():
            k_cl += 1
            sum_k += d[cl][cl0]
            print(cl0, ': ', d[cl][cl0])
    print('Всего классов: ', k_cl)
    print('Всего учеников: ', sum_k)

school = {1: {'1a': 21, '1б': 16, '1в': 11}, 2:{'2б': 31}, 6: {'6а': 25}, 7:{'7в': 27}}

select(school)
delete(school, '1в')
select(school)
insert(school, '5а', 25)
select(school)
update(school, '5а', 15)
select(school)