"""
127. 单词接龙
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


解题思路：
参考官方题解
题目可以看做是寻找一条单词变换的路径，将问题转换成图的遍历
通过对字符串的通配符处理，将具体的字符串连接起来成一个图
使用广度优先求解，使用深度优先好像不行，太多的话深度太深？
这种类型不太熟练，需要多练练了
后面尝试首尾广度试试
"""
from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        reqDict = defaultdict(list)
        for word in wordList:
            for i in range(0, len(word)):
                reqWord = word[:i] + "*" + word[i + 1:]
                reqDict[reqWord].append(word)

        length = len(beginWord)
        visited = [beginWord]
        stack = [[beginWord, 1]]
        while stack:
            word, level = stack.pop(0)
            for i in range(0, length):
                reqWord = word[:i] + "*" + word[i + 1:]
                if reqWord not in reqDict:
                    continue
                for nextWord in reqDict[reqWord]:
                    if nextWord == endWord:
                        return level + 1
                    if nextWord not in visited:
                        visited.append(nextWord)
                        stack.append([nextWord, level+1])
        return 0


if __name__ == "__main__":
    solution = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution.ladderLength(beginWord, endWord, wordList))

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(solution.ladderLength(beginWord, endWord, wordList))

    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
                "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh",
                "co", "ga",
                "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la",
                "st", "er",
                "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr",
                "sq", "ye"]
    print(solution.ladderLength(beginWord, endWord, wordList))
