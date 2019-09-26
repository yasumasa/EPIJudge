from test_framework import generic_test
from test_framework.test_failure import TestFailure
import copy

STR2INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
INT2STR = {v:k for k, v in STR2INT.items()}


def int_to_string(x):
    ans = []
    i = 1
    sign = 1
    if x < 0:
        sign = -1
        x *= -1
    while True:
        r = x % 10
        x -= r
        x //= 10
        ans.insert(0, INT2STR[r])
        if x == 0:
            break
        i += 1
    if sign < 0:
        ans.insert(0, '-')
    return ''.join(ans)


def string_to_int(s):
    sign = 1
    if s.startswith('-'):
        sign = -1
    ans = 0
    for i in range(len(s.lstrip('-'))):
        ans += 10**i * STR2INT[s[~i]]
    return ans * sign


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
