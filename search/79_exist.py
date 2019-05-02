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


def exist_back(board: List[List[str]], word: str) -> bool:
    def exist_core(current: List[int], deep: int, tmp_str: str, last_direction: List[int]) -> bool:
        if deep == len_word:
            if tmp_str == word:
                return True
            return False
        t: str = tmp_str
        for direction in directions:
            # 避免回退
            if last_direction and direction[0] == -last_direction[0] and direction[1] == -last_direction[1]:
                continue
            next_location: List[int] = [current[0] + direction[0], current[1] + direction[1]]
            if 0 <= next_location[0] < row_cnt and 0 <= next_location[1] < col_cnt:
                tmp_str += board[next_location[0]][next_location[1]]
                if exist_core(next_location, deep + 1, tmp_str, direction):
                    return True
                tmp_str = t
        return False

    if not board or not word:
        return False
    len_word: int = len(word)
    row_cnt: int = len(board)
    col_cnt: int = len(board[0])
    if row_cnt * col_cnt < len_word:
        return False
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for row in range(row_cnt):
        for col in range(col_cnt):
            if board[row][col] == word[0]:
                if exist_core([row, col], 1, board[row][col], []):
                    return True
    return False


def exist(board: List[List[str]], word: str) -> bool:
    """
    :param board:
    :param word:
    :return:
    >>> exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'ABCCED')
    True
    >>> exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'SEE')
    True
    >>> exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'ABCB')
    False
    >>> exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], 'aaaaaaaaaaaaa')
    False
    """

    def exist_core(curr_len: int, current: List[int]) -> bool:
        if current[0] < 0 or current[0] >= row_cnt or \
                current[1] < 0 or current[1] >= col_cnt or \
                visited[current[0]][current[1]] or \
                board[current[0]][current[1]] != word[curr_len]:
            return False

        if curr_len == len_word - 1:
            return True
        visited[current[0]][current[1]] = True
        for direction in directions:
            next_location: List[int] = [current[0] + direction[0], current[1] + direction[1]]
            if exist_core(curr_len + 1, next_location):
                return True
        visited[current[0]][current[1]] = False
        return False

    if not board:
        return False
    if not word:
        return True
    len_word: int = len(word)
    row_cnt: int = len(board)
    col_cnt: int = len(board[0])
    # 使用need判断是否要继续，节省计算
    need = {}
    for c in word:
        if c not in need:
            need[c] = 1
        else:
            need[c] += 1
    for i in range(row_cnt):
        for j in range(col_cnt):
            if board[i][j] in need:
                need[board[i][j]] -= 1
    for c in need:
        if need[c] > 0:
            return False
    visited: List[List[bool]] = [[False for _ in range(col_cnt)] for _ in range(row_cnt)]
    directions: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for row in range(row_cnt):
        for col in range(col_cnt):
            if exist_core(0, [row, col]):
                return True
    return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
