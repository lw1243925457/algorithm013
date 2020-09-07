# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。 
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树 
#  👍 396 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._array = [None] * 26
        self._flag = [0] * 26

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        index = 0
        for c in word:
            index = ord(c) - ord('a')
            if node._array[index] is None:
                node._array[index] = Trie()
            node = node._array[index]
        node._flag[index] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        index = 0
        for c in word:
            index = ord(c) - ord('a')
            if node._array[index] is None:
                return False
            node = node._array[index]
        if node._flag[index] == 0:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            index = ord(c) - ord('a')
            if node._array[index] is None:
                return False
            node = node._array[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
