import math
from functools import reduce
from operator import add


def f(x):
    return str(x)


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(char2num, '123456789')))
print(reduce(fn, map(char2num, '123456789')))
L1 = [1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(map(add, L1, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def Upe(x):
    return x.capitalize()


print(list(map(Upe, ['adam', 'kill', 'odor'])))


def is_odd(n):
    return n % 2 == 0


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


L = []
for n in primes():
    if n < 1000:
        L.append(n)
    else:
        break

print(L)
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper, reverse=False))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(a):
    return a[0]


def by_score(a):
    return a[1]


L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score, reverse=True)
print(L2)

fs = []


def count():
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(math.pow(2, 1000))
