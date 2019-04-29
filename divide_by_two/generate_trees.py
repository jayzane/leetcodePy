from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

    示例:

    输入: 3
    输出:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释:
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
    """

    def generateTrees(self, n: int) -> List[TreeNode]:
        pass


def generate_trees(n: int) -> List[TreeNode]:
    """
    :param n:
    :return:
    >>> len(generate_trees(3))
    5
    >>> generate_trees(0)
    []
    """
    if n <= 0:
        return []
    res = generate_trees_core(1, n)
    return res


def generate_trees_core(start: int, end: int) -> List[TreeNode]:
    if start > end:
        return [None]
    elif start == end:
        return [TreeNode(start)]
    result: List[TreeNode] = []
    for i in range(start, end + 1):
        left_trees: List[TreeNode] = generate_trees_core(start, i - 1)
        right_trees: List[TreeNode] = generate_trees_core(i + 1, end)
        for l in left_trees:
            for r in right_trees:
                root: TreeNode = TreeNode(i)
                root.left = l
                root.right = r
                result.append(root)
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
