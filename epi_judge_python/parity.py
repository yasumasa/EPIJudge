from test_framework import generic_test

"""
4.1 
"""

def parity1(x):
    num_ones = 0
    while x:
        if x & 1:
            num_ones += 1
        x >>= 1
    if num_ones % 2 == 0:
        return 0
    else:
        return 1


def parity2(x):
    r = 0
    while x:
        r ^= x & 1
        x >>= 1
    return r


def parity3(x):
    r = 0
    while x:
        r ^= 1
        x &= x - 1
    return r

def parity4(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

def parity5(x):
    x |= (x-1)
    #x =
    return x != 0 and ((x & (x - 1)) == 0)


if __name__ == '__main__':
    for func in [parity1, parity2, parity3, parity4]:
        print('\n[' + func.__name__ + ']')
        generic_test.generic_test_main("parity.py", 'parity.tsv', func)

