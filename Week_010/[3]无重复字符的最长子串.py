# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4380 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、双指针：使用左右指针移动，记录其中出现过的字符
    1.当出现重复的时候，左指针向后移动，移除左侧元素，右边不动
    2.记录最大长度
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        left, right = 0, 0
        record = set()
        record.add(s[0])
        while right + 1 < len(s):
            if s[right + 1] in record:
                ans = max(ans, len(record))
                record.remove(s[left])
                left += 1
            else:
                right += 1
                record.add(s[right])
        ans = max(ans, len(record))
        # print(ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("pwke") == 4
