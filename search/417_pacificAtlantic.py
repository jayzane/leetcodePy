from typing import *


class Solution:
    """
    给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

    规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

    请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。



    提示：

    输出坐标的顺序不重要
    m 和 n 都小于150


    示例：



    给定下面的 5x5 矩阵:

      太平洋 ~   ~   ~   ~   ~
           ~  1   2   2   3  (5) *
           ~  3   2   3  (4) (4) *
           ~  2   4  (5)  3   1  *
           ~ (6) (7)  1   4   5  *
           ~ (5)  1   1   2   4  *
              *   *   *   *   * 大西洋

    返回:

    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
    """

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pass


def pacific_atlantic(matrix: List[List[int]]) -> List[List[int]]:
    """
    从边界先广度后深度搜索
    :param matrix:
    :return:
    >>> pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    """

    def dfs(row: int, col: int, can_reach: List[List[bool]]):
        if can_reach[row][col]:
            return
        can_reach[row][col] = True
        for direction in directions:
            next_row: int = row + direction[0]
            next_col: int = col + direction[-1]
            if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt and matrix[next_row][next_col] >= matrix[row][col]:
                dfs(next_row, next_col, can_reach)

    if not matrix:
        return []

    res: List[List[int]] = []
    row_cnt: int = len(matrix)
    col_cnt: int = len(matrix[0])
    can_read_p: List[List[bool]] = [[False for _ in range(col_cnt)] for _ in range(row_cnt)]  # 能到达太平洋
    can_read_a: List[List[bool]] = [[False for _ in range(col_cnt)] for _ in range(row_cnt)]  # 能到达大西洋
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(row_cnt):
        dfs(i, 0, can_read_p)
        dfs(i, col_cnt - 1, can_read_a)
    for j in range(col_cnt):
        dfs(0, j, can_read_p)
        dfs(row_cnt - 1, j, can_read_a)
    for i in range(row_cnt):
        for j in range(col_cnt):
            if can_read_p[i][j] and can_read_a[i][j]:
                res.append([i, j])
    return res


# if not matrix:
#     return []
# m = len(matrix)
# n = len(matrix[0])
#
#
# def dfs(x, y, tagMatrix):
#     tagMatrix[x][y] = True
#     if x - 1 >= 0 and matrix[x - 1][y] >= matrix[x][y] and not tagMatrix[x - 1][y]:
#         dfs(x - 1, y, tagMatrix)
#     if x + 1 < m and matrix[x + 1][y] >= matrix[x][y] and not tagMatrix[x + 1][y]:
#         dfs(x + 1, y, tagMatrix)
#     if y - 1 >= 0 and matrix[x][y - 1] >= matrix[x][y] and not tagMatrix[x][y - 1]:
#         dfs(x, y - 1, tagMatrix)
#     if y + 1 < n and matrix[x][y + 1] >= matrix[x][y] and not tagMatrix[x][y + 1]:
#         dfs(x, y + 1, tagMatrix)
#
#
# Pacific = [[False for i in range(n)] for j in range(m)]
# Atlantic = [[False for i in range(n)] for j in range(m)]
#
# Pacific_border = [(0, col) for col in range(n)] + [(row, 0) for row in range(m)]
# Atlantic_border = [(m - 1, col) for col in range(n)] + [(row, n - 1) for row in range(m)]
#
# for x, y in Pacific_border:
#     dfs(x, y, Pacific)
#
# for x, y in Atlantic_border:
#     dfs(x, y, Atlantic)
#
# points = []
# for i in range(m):
#     for j in range(n):
#         if Pacific[i][j] and Atlantic[i][j]:
#             points.append([i, j])
# return points

if __name__ == '__main__':
    import doctest

    doctest.testmod()
