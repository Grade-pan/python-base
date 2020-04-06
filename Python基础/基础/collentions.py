from collections import OrderedDict
from collections import deque
from collections import namedtuple, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)  # 坐标
print(p.y)  # 坐标
Circle = namedtuple('Circle', ['x', 'y', 'r'])  # 要用坐标和半径表示一个圆

q = deque(['a', 'b', 'c'])  # 高效实现插入和删除操作的双向列表
q.append('x')
print(q)
q.appendleft('y')
print(q)
print(q.pop())
print(q.popleft())

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # 按插入顺序排列
print(od)


# 实现FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


c = Counter()  # 计数器
for ch in 'hello word':
    c[ch] = c[ch] + 1
print(c)
