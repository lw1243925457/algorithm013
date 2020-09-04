# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。 
# 
#  
# 
#  示例： 
# 
#  输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC" 
# 
#  
# 
#  提示： 
# 
#  
#  如果 S 中不存这样的子串，则返回空字符串 ""。 
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = s + s
        n = len(s)
        target = collections.Counter(t)
        counter = collections.defaultdict(lambda: 0)

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for r in range(n):
            if s[r] in target:
                counter[s[r]] += 1
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                if s[l] in target:
                    counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans
# leetcode submit region end(Prohibit modification and deletion)
