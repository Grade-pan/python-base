import numpy as np

a = np.arange(6).reshape(2, 3)
for x in np.nditer(a):
    print(x, ' ', end='')
print()
print('*' * 30)
for x in np.nditer(a.T):
    print(x, ' ', end='')
# 上述两组输出结果相同说明：选择顺序以匹配数组的内存布局，而不是使用标准C或Fortran排序。
# 这样做是为了提高访问效率，反映了默认情况下只需要访问每个元素而不关心特定排序的想法。
# 我们可以通过迭代前一个数组的转置来看到这一点，而不是以C顺序获取该转置的副本。
print()
print('*' * 30)
# 以C标准输出如下:'先转置再复制之后顺序发生变化'
for x in np.nditer(a.T.copy(order='C')):
    print(x, ' ', end='')

# a和a.T的元素以相同的顺序遍历，即它们存储在内存中的顺序， 而 a.T.copy(order='C') 的元素以不同的顺序访问，因为它们被放入不同的内存中布局。

# 控制迭代顺序
# 于C顺序，可以使用order ='C'覆盖它，对于Fortran顺序，可以使用order ='F'覆盖它。
print()
print('*' * 30)
print('C顺序覆盖')
for x in np.nditer(a, order='C'):
    print(x, ' ', end='')
print()
print('*' * 30)
print('F顺序覆盖')
for x in np.nditer(a, order='F'):
    print(x, ' ', end='')
print()
print('*' * 30)

# 修改数组值两种方法
# 使用 with 语句将nditer用作上下文管理器，并在退出上下文时写回临时数据。
# 完成迭代后调用迭代器的 close 方法，这将触发回写。
print('修改前的数组值')
print(a)
with np.nditer(a, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = 2 * x
print('*' * 30)
print('修改后的数组值')
print(a)

print('*' * 30)
# 使用外部循环
# 方法是将一维最内层循环移动到迭代器外部的代码中。 这样，NumPy的矢量化操作可以用在被访问元素的较大块上。
# 通过强制'C'和'F'顺序，我们得到不同的外部循环大小。通过指定迭代器标志来启用此模式。
for x in np.nditer(a, flags=['external_loop']):
    print(x, ' ', end=' ')
print()
print('*' * 30)

for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, ' ', end=' ')

# 缓冲数组元素
# 在强制迭代顺序时，我们观察到外部循环选项可以以较小的块提供元素，因为不能以恒定的步幅以适当的顺序访问元素。
# 编写C代码时，这通常很好，但在纯Python代码中，这可能会导致性能显着降低。
# 通过启用缓冲模式，迭代器提供给内部循环的块可以变得更大，从而显着减少Python解释器的开销。
# 在强制Fortran迭代顺序的示例中，当启用缓冲时，内部循环可以一次性查看所有元素。
print()
print('*' * 30)
for x in np.nditer(a, flags=['external_loop', 'buffered'], order='F'):
    print(x, ' ', end=' ')
# 这个输出和上个输出形成了鲜明的对比

# 作为特定类型数据迭代
print()
print('*' * 30)
b = np.arange(6).reshape(2, 3) - 3
for x in np.nditer(b, op_flags=['readonly', 'copy'], op_dtypes=['complex128']):
    print(np.sqrt(x), ' ', end='')
print()
print('*' * 30)

for x in np.nditer(b, flags=['buffered'], op_dtypes=['complex128']):
    print(np.sqrt(x), ' ', end='')
# 迭代器使用NumPy的转换规则来确定是否允许特定转换。
# 默认情况下，它会强制执行“安全”投射。
# 这意味着，例如，如果您尝试将64位浮点数组视为32位浮点数组，则会引发异常。
# 在许多情况下，规则'same_kind'是最合理的规则，因为它允许从64位转换为32位浮点数，但不允许从float转换为int或从complex转换为float。
print()
print('*' * 30)
for x in np.nditer(a, flags=['buffered'], op_dtypes=['complex128'],
                   casting='same_kind'):
    print(x, end=' ')
