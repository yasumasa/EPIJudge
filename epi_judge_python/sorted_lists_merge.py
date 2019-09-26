from test_framework import generic_test
from list_node import ListNode

def merge_two_sorted_lists(L1, L2):
    sent = ListNode()
    prev = sent
    while L1 and L2:
        if L1.data < L2.data:
            prev.next = L1
            L1 = L1.next
        else:
            prev.next = L2
            L2 = L2.next
        prev = prev.next
    if L1:
        prev.next = L1
    if L2:
        prev.next = L2
    return sent.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
