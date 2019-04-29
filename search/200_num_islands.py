from typing import *
import collections


class Solution:
    """
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

    示例 1:

    输入:
    11110
    11010
    11000
    00000

    输出: 1
    示例 2:

    输入:
    11000
    11000
    00100
    00011

    输出: 3
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        pass


def num_islands_back(grid: List[List[str]]) -> int:
    """
    :param grid:
    :return:
    >>> num_islands_back(
    ... [
    ... list('11110'),
    ... list('11010'),
    ... list('11000'),
    ... list('00000')
    ... ])
    1
    >>> num_islands_back(
    ... [
    ... list('11000'),
    ... list('11000'),
    ... list('00100'),
    ... list('00011')
    ... ])
    3
    >>> num_islands_back([["0","1","0"],["1","0","1"],["0","1","0"]])
    4
    """
    row_i: int = 0
    marked: Dict[int, Dict[int, bool]] = {}
    row_cnt: int = len(grid)
    is_lands_cnt: int = 0
    while row_i < row_cnt:
        col_i: int = 0
        col_cnt: int = len(grid[row_i])
        while col_i < col_cnt:
            if grid[row_i][col_i] == '1' and not marked.get(row_i, {}).get(col_i):
                is_lands_cnt += 1
                stack: List[List[int]] = [[row_i, col_i]]
                while stack:
                    curr: List[int] = stack.pop()
                    i: int = curr[0]
                    i_b: int = i + 2
                    while i < i_b and i < row_cnt:
                        j: int = curr[-1]
                        j_b: int = j + 2
                        while j < j_b and j < col_cnt:
                            if not marked.get(i, {}).get(j):
                                if grid[i][j] == '1':  # TODO: 遇见1继续，遇见0
                                    stack.append([i, j])
                                    if marked.get(i):
                                        marked[i][j] = True
                                    else:
                                        marked[i] = {j: True}
                                else:
                                    break
                            j += 1
                        i += 1
            col_i += 1
        row_i += 1
    return is_lands_cnt


def num_islands(grid: List[List[str]]) -> int:
    """
    :param grid:
    :return:
    >>> num_islands(
    ... [
    ... list('11110'),
    ... list('11010'),
    ... list('11000'),
    ... list('00000')
    ... ])
    1
    >>> num_islands(
    ... [
    ... list('11000'),
    ... list('11000'),
    ... list('00100'),
    ... list('00011')
    ... ])
    3
    >>> num_islands([["0","1","0"],["1","0","1"],["0","1","0"]])
    4
    >>> num_islands([])
    0
    """

    def dfs(grid: List[List[str]], row, col) -> None:
        if row < 0 or row >= row_cnt or col < 0 or col >= col_cnt or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        for direction in directions:
            dfs(grid, row + direction[0], col + direction[1])

    if not grid:
        return 0
    directions: List(List[int]) = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row_cnt: int = len(grid)
    col_cnt: int = len(grid[0])
    level: int = 0
    for i in range(row_cnt):
        for j in range(col_cnt):
            if grid[i][j] == '1':
                level += 1
                dfs(grid, i, j)
    return level


if __name__ == '__main__':
    import doctest

    doctest.testmod()
