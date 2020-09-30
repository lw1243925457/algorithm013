# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#  
# 
#  示例: 
# 
#  输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"] 
# 
#  说明: 
# 你可以假设所有输入都由小写字母 a-z 组成。 
# 
#  提示: 
# 
#  
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？ 
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。 
#  
#  Related Topics 字典树 回溯算法 
#  👍 239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、字典树：先将单词列表构造成字典树，然后遍历二维数组，看齐上下左右移动是否能构成一个单词
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node[c] = node.get(c, {})
                node = node[c]

        ans = set()
        words = set(words)

        height, width = len(board), len(board[0])
        for i in range(0, height):
            for j in range(0, width):
                self._search(board, i, j, height, width, trie, words, "", ans)
        return list(ans)

    def _search(self, board, row, col, height, width, node, words, path, ans):
        if not 0 <= row < height or not 0 <= col < width or board[row][col] == "#" or board[row][col] not in node:
            return
        word = path + board[row][col]
        if word in words:
            ans.add(word)

        board[row][col] = "#"
        self._search(board, row - 1, col, height, width, node[word[-1]], words, word, ans)
        self._search(board, row + 1, col, height, width, node[word[-1]], words, word, ans)
        self._search(board, row, col - 1, height, width, node[word[-1]], words, word, ans)
        self._search(board, row, col + 1, height, width, node[word[-1]], words, word, ans)
        board[row][col] = word[-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    words = ["oath", "pea", "eat", "rain", "aaaa"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(Solution().findWords(board, words))
