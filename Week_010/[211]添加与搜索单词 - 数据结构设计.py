# 如果数据结构中有任何与word匹配的字符串，则bool search（word）返回true，否则返回false。 单词可能包含点“。” 点可以与任何字母匹
# 配的地方。 
# 
#  请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。 
# 
#  实现词典类 WordDictionary ： 
# 
#  
#  WordDictionary() 初始化词典对象 
#  void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配 
#  bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 '
# .' ，每个 . 都可以表示任何一个字母。 
#  
# 
#  
# 
#  示例： 
# 
#  输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search","se
# arch"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length <= 500 
#  addWord 中的 word 由小写英文字母组成 
#  search 中的 word 由 '.' 或小写英文字母组成 
#  最调用多 50000 次 addWord 和 search 
#  
#  Related Topics 设计 字典树 回溯算法 
#  👍 164 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = [[None, False] for _ in range(0, 26)]

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self._root
        last = node
        pos = None
        for c in word:
            pos = ord(c) - ord("a")
            if node[pos][0] is None:
                node[pos][0] = [[None, False] for _ in range(0, 26)]
            last = node
            node = node[pos][0]
        last[pos][1] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._find(word, 0, self._root, False)

    def _find(self, word, index, node, isEnd):
        if not index < len(word):
            if isEnd:
                return True
            return False
        if word[index] == ".":
            for i in range(0, 26):
                if node[i][0] is not None:
                    if self._find(word, index + 1, node[i][0], node[i][1]):
                        return True
            return False
        else:
            pos = ord(word[index]) - ord("a")
            if node[pos][0] is None:
                return False
            return self._find(word, index + 1, node[pos][0], node[pos][1])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
assert not wordDictionary.search("pad")
assert wordDictionary.search("bad")
assert wordDictionary.search(".ad")
assert wordDictionary.search("b..")
assert not wordDictionary.search("b")
