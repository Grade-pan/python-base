import numpy as np


def print_table(ntypes):
    print('X'),
    for char in ntypes:
        print(char),
        print
        for row in ntypes:
            print(row),
            print
        for col in ntypes:
            print(int(np.can_cast(row, col))),
            print
