from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    heap = []
    for i, a in enumerate(sorted_arrays):
        if a:
            heapq.heappush(heap, (a.pop(0), i))
    ans = []
    while heap:
        m, i = heapq.heappop(heap)
        if len(sorted_arrays[i]) > 0:
            heapq.heappush(heap, (sorted_arrays[i].pop(0), i))
        ans.append(m)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
