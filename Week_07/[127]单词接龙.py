# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 436 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、双边bfs：优化单边bfs，每次选取数量较多的一边进行遍历,需要注意的点如下：
    1.终止条件的变化：当两个栈中有相同节点时表示完成
    2.需要各自持有两边的遍历层次、访问过的节点列表
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        beginStack = [beginWord]
        endStack = [endWord]
        begineLength, endLength = 1, 1
        chars = "qwertyuiopasdfghjklzxcvbnm"
        wordList = set(wordList)
        beginVisited = set()
        endVisited = set()
        while len(beginStack) != 0 or len(endStack) != 0:
            # 获取当前栈大小，一次性遍历完
            size = len(beginStack)
            for i in range(0, size):
                word = beginStack.pop(0)
                for j in range(0, len(word)):
                    for c in chars:
                        newWord = word[:j] + c + word[j + 1:]
                        if newWord not in wordList:
                            continue
                        if newWord in endStack:
                            return begineLength + endLength
                        if newWord not in beginVisited:
                            beginVisited.add(newWord)
                            beginStack.append(newWord)
            begineLength += 1
            # print(begineLength, endLength, endWord, beginStack, endStack)
            if len(beginStack) == 0:
                beginStack, endStack = endStack, beginStack
                beginWord, endWord = endWord, beginWord
                beginVisited, endVisited = endVisited, beginVisited
                begineLength, endLength = endLength, begineLength
            elif len(beginStack) > len(endStack):
                beginStack, endStack = endStack, beginStack
                beginWord, endWord = endWord, beginWord
                beginVisited, endVisited = endVisited, beginVisited
                begineLength, endLength = endLength, begineLength
        return 0


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
