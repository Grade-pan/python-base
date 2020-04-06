x = b'abc'.hex()
print(x)

m = memoryview(b"abcdefghijklmnopqrstuvwxyz").tolist()
print(m)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0], reverse=True)
print(pairs)
