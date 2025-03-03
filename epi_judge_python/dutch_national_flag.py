import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(A, pivot_index):
    p = A[pivot_index]
    n = len(A)
    l = []
    r = []
    for i in range(n):
        if i != p:
            if A[i] < p:
                l.append(A[i])
            else:
                r.append(A[i])

    A = l + [p] + r
    return

'''
def dutch_flag_partition(A, pivot_index):
    p = A[pivot_index]
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                break
    for i in range(n):
        for j in range(i):
            if A[j] > p:
                A[i], A[j] = A[j], A[i]
                break
    return
'''

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(generic_test.generic_test_main("dutch_national_flag.py",
                                           'dutch_national_flag.tsv',
                                           dutch_flag_partition))
