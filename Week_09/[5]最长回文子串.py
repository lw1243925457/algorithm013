# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2722 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、中心扩散法，数据复杂度为O(N^2)
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        left = 0
        right = 0
        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len3 = max(len1, len2)
            if len3 > right - left:
                left = i - int((len3 - 1) / 2)
                right = i + int(len3 / 2)
        print(left, right + 1)
        return s[left:right + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return int(r - l - 1)
# leetcode submit region end(Prohibit modification and deletion)
