from test_framework import generic_test


def is_balanced_binary_tree(tree):
    ans = True
    def helper(root, ans):
        if root is None:
            return 0, ans
        left_depth, ans = helper(root.left, ans)
        right_depth, ans = helper(root.right, ans)
        if abs(left_depth - right_depth) > 1:
            ans = False
        if left_depth > right_depth:
            return left_depth + 1, ans
        else:
            return right_depth + 1, ans
    _, ans = helper(tree, ans)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
