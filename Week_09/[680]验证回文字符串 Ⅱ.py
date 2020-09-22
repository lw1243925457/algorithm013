# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  示例 1: 
# 
#  
# 输入: "aba"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#  
# 
#  注意: 
# 
#  
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
#  
#  Related Topics 字符串 
#  👍 263 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        return self._check(s, l, r)

    def _check(self, s, l, r, remain=True):
        if not l < r:
            return True
        if s[l] == s[r]:
            return self._check(s, l+1, r-1, remain)
        elif not remain:
            return False
        else:
            return self._check(s, l+1, r, False) or self._check(s, l, r - 1, False)
# leetcode submit region end(Prohibit modification and deletion)
