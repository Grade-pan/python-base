import json
import os
import random
import time
from io import BytesIO
from multiprocessing import Pool
from multiprocessing import Process

f = BytesIO()
f1 = BytesIO()
f.write('中文'.encode('gbk'))
f1.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f1.getvalue())
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print(2 ** 5 * 6)
