from typing import *


class Solution:
    """
    给定一个二维网格和一个单词，找出该单词是否存在于网格中。

    单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

    示例:

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


def exist(board: List[List[str]], word: str) -> bool:
    """
    :param board:
    :param word:
    :return:
    >>> exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'ABCCED')
    """

    def exist_core(current: List[int], deep: int, tmp_str: str) -> bool:
        if deep == len_word:
            if ''.join(tmp_str) == word:
                return True
            return False
        for direction in directions:
            next_location: List[int] = [current[0] + direction[0], current[1] + direction[1]]
            if 0 <= next_location[0] < row_cnt and 0 <= next_location[1] < col_cnt:
                tmp_str += board[next_location[0]][next_location[1]]
                if exist_core(next_location, deep + 1, tmp_str):
                    return True
        return False

    if not board or not word:
        return False
    len_word: int = len(word)
    row_cnt: int = len(board)
    col_cnt: int = len(board[0])
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for row in range(row_cnt):
        for col in range(col_cnt):
            if board[row][col] == word[0]:
                if exist_core([row, col], 1, board[row][col]):
                    return True
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
