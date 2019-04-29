from typing import *


class Solution:
    """

    给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

    找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

    示例:

    X X X X
    X O O X
    X X O X
    X O X X
    运行你的函数后，矩阵变为：

    X X X X
    X X X X
    X X X X
    X O X X
    解释:

    被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


def solve_back(board: List[List[str]]) -> None:
    """
    :param board:
    :return:
    >>> b1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    >>> solve_back(b1)
    >>> b1
    [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
    >>> b2 = [["O"]]
    >>> solve_back(b2)
    >>> b2
    [['O']]
    """
    if not board:
        return
    row_cnt: int = len(board)
    col_cnt: int = len(board[0])
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(row_cnt):
        for j in range(col_cnt):
            if board[i][j] == 'O':
                records: List[List[int]] = [[i, j]]
                boundaries: List[bool] = []
                for direct in directions:
                    x: int = i + direct[0]
                    y: int = j + direct[-1]
                    while 0 <= x < row_cnt and 0 <= y < col_cnt:
                        if board[x][y] == 'X':
                            boundaries.append(True)
                            break
                        else:
                            p1: List[int] = [x, y]
                            if p1 not in records:
                                records.append(p1)
                        x += direct[0]
                        y += direct[-1]
                if all(boundaries) and len(boundaries) == 4:
                    for record in records:
                        board[record[0]][record[-1]] = 'X'


def solve(board: List[List[str]]) -> None:
    """
    将边界的O先置为T，再将所有的T置为O，把O置为X
    :param board:
    :return:
    >>> b1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    >>> solve(b1)
    >>> b1
    [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
    >>> b2 = [["O"]]
    >>> solve(b2)
    >>> b2
    [['O']]
    """

    def dfs(row: int, col: int):
        if 0 <= row < row_cnt and 0 <= col < col_cnt and board[row][col] == 'O':
            board[row][col] = 'T'
            for direction in directions:
                dfs(row + direction[0], col + direction[-1])

    if not board:
        return
    row_cnt: int = len(board)
    col_cnt: int = len(board[0])
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(row_cnt):
        dfs(i, 0)
        dfs(i, col_cnt - 1)
    for j in range(col_cnt):
        dfs(0, j)
        dfs(row_cnt - 1, j)
    for i in range(row_cnt):
        for j in range(col_cnt):
            if board[i][j] == 'T':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
