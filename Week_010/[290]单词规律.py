# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  示例1: 
# 
#  输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false 
# 
#  示例 4: 
# 
#  输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false 
# 
#  说明: 
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
#  Related Topics 哈希表 
#  👍 195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、边遍历边映射，判断映射是否相同；遍历一次，时间复杂度为O(N)
    """

    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        m = {}
        for p, word in zip(pattern, s.split()):
            c = "_" + p
            if c not in m and word not in m:
                m[c] = word
                m[word] = c
            elif c not in m or word not in m or m[c] != word or m[word] != c:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().wordPattern(pattern="abba", s="dog cat cat dog")
    assert not Solution().wordPattern(pattern="abba", s="dog cat cat fish")
    assert not Solution().wordPattern(pattern="aaaa", s="dog cat cat dog")
    assert not Solution().wordPattern(pattern="abba", s="dog dog dog dog")
    assert Solution().wordPattern(pattern="abc", s="b c a")
