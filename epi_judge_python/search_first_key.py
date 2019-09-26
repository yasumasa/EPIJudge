from test_framework import generic_test
import bisect

#def search_first_of_k(A, k):
#    if k not in set(A):
#        return -1
#    return bisect.bisect_left(A, k)

def search_first_of_k(A, k):
    l, r = 0, len(A) - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if A[m] > k:
            r = m - 1
        elif A[m] == k:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
