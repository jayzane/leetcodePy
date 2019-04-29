from typing import *
import collections


class Solution:
    """
    给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:

    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:

    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    输出: 5

    解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
         返回它的长度 5。
    示例 2:

    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    输出: 0

    解释: endWord "cog" 不在字典中，所以无法进行转换。
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass


def ladder_length_back(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    :param beginWord:
    :param endWord:
    :param wordList:
    :return:
    >>> ladder_length_back('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
    5
    >>> ladder_length_back('hit', 'cog', ["hot","dot","dog","lot","log"])
    0
    """
    queue = collections.deque()
    queue.append(beginWord)
    level: int = 0
    marked: Dict[str, bool] = {}
    while queue:
        size: int = len(queue)
        level += 1
        while size > 0:
            word: str = queue.popleft()
            for w in wordList:
                if w in marked:
                    continue
                if is_diff_one_char(word, w):
                    if w == endWord:
                        return level + 1
                    else:
                        queue.append(w)
                        marked[w] = True
            size -= 1
    return 0


def is_diff_one_char(source: str, target: str) -> bool:
    """
    :param source:
    :param target:
    :return:
    >>> is_diff_one_char('hot', 'hit')
    True
    >>> is_diff_one_char('hot', 'hto')
    False
    """
    flag = 0
    for i, s in enumerate(source):
        if s != target[i]:
            flag += 1
            if flag > 1:
                return False
    return True


def ladder_length(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    双端交替迫近目标层，根据一层数量最多节点确定为目标层
    :param beginWord:
    :param endWord:
    :param wordList:
    :return:
    >>> ladder_length('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
    5
    >>> ladder_length('hit', 'cog', ["hot","dot","dog","lot","log"])
    0
    >>> ladder_length("hit","cog",["hot","dot","dog","lot","log"])
    """
    if not beginWord or not endWord or endWord not in wordList:
        return 0
    all_chars: List[str] = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    curr_word_set: Set[str] = {beginWord}  # 当前层的节点
    end_word_set: Set[str] = {endWord}  # 目标层的节点
    word_set: Set[str] = set(wordList)  # 加速单词是否在字典中的判断
    level: int = 1
    while curr_word_set:
        # 避免同层节点临接
        level += 1
        for cw in curr_word_set:
            # beginWord不重复出现在wordList(word_set)
            if cw != beginWord:
                word_set.remove(cw)
        tmp_set: Set[str] = set()
        for curr_word in curr_word_set:
            for i, w in enumerate(curr_word):
                for letter in all_chars:
                    if w == letter:
                        continue
                    changed: str = curr_word[:i] + letter + curr_word[i + 1:]
                    if changed in end_word_set:
                        return level
                    if changed in word_set:
                        tmp_set.add(changed)
        # 让层节点最多的层作为目标层
        if len(tmp_set) <= len(end_word_set):
            curr_word_set = tmp_set
        else:
            # 逆转方向
            curr_word_set = end_word_set
            end_word_set = tmp_set
    return 0


if __name__ == '__main__':
    import doctest

    doctest.testmod()
