from typing import *

from common import init_data


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


def binary_tree_paths_back(root: TreeNode) -> List[str]:
    """
    :param root:
    :return:
    >>> node_1 = init_data.init_tree([1,2,3,None,5], 0)
    >>> binary_tree_paths_back(node_1)
    ['1->2->5', '1->3']
    """

    def search_path(paths: List[List[int]], current_path: List[int], node: TreeNode) -> None:
        if node is None:
            return
        current_path.append(node.val)
        if node.left is None and node.right is None:
            paths.append(current_path)
            return
        tmp: List[int] = current_path[:]
        search_path(paths, current_path, node.left)
        current_path = tmp
        search_path(paths, current_path, node.right)

    res_paths: List[List[int]] = []

    search_path(res_paths, [], root)
    res: List[str] = list(map(lambda x: '->'.join(map(lambda y: str(y), x)), res_paths))
    return res


def binary_tree_paths(root):
    """
    >>> node_1 = init_data.init_tree([1,2,3,None,5], 0)
    >>> binary_tree_paths(node_1)
    ['1->2->5', '1->3']
    """

    def join_paths(node: TreeNode, left_paths: List[List[int]]) -> List[List[int]]:
        return [[node.val] + p for p in left_paths]

    def search_paths(node: TreeNode) -> List[List[int]]:
        if not node:
            return []
        elif not node.left and not node.right:
            return [[node.val]]
        elif not node.left:
            return join_paths(node, search_paths(node.right))
        elif not node.right:
            return join_paths(node, search_paths(node.left))
        left_paths = search_paths(node.left)
        right_paths = search_paths(node.right)
        return join_paths(node, left_paths + right_paths)

    paths: List[List[int]] = search_paths(root)
    res: List[str] = list(map(lambda x: '->'.join(map(lambda y: str(y), x)), paths))
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
