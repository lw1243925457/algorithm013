# 给定两个字符串 s 和 t，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。 
# 
#  所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。 
# 
#  示例 1: 
# 
#  输入: s = "egg", t = "add"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "foo", t = "bar"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: s = "paper", t = "title"
# 输出: true 
# 
#  说明: 
# 你可以假设 s 和 t 具有相同的长度。 
#  Related Topics 哈希表 
#  👍 239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        reflect = set()
        for i in range(0, len(s)):
            if s[i] not in m:
                m[s[i]] = t[i]
                if t[i] in reflect:
                    return False
                reflect.add(t[i])
            if m[s[i]] != t[i]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().isIsomorphic(s = "egg", t = "add")
    assert not Solution().isIsomorphic(s = "foo", t = "bar")
    assert Solution().isIsomorphic(s = "paper", t = "title")
    assert not Solution().isIsomorphic("ab", "aa")
