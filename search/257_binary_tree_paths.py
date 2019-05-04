from typing import *

import common


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    给定一个二叉树，返回所有从根节点到叶子节点的路径。

    说明: 叶子节点是指没有子节点的节点。

    示例:

    输入:

       1
     /   \
    2     3
     \
      5

    输出: ["1->2->5", "1->3"]

    解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
    """

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        pass


def binary_tree_paths(root: TreeNode) -> List[str]:

    def search_path(paths: List[List[int]], current_path: List[int], node: TreeNode, visited: List[TreeNode]) -> None:
        if node is None:
            paths.append(current_path)
        paths.append(node.val)
        search_path(paths, node.left)
        search_path(paths, node.right)

    search_path([], root)



if __name__ == '__main__':
    import doctest

    doctest.testmod()