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
    """
    解题思路：
    一、滑动窗口：大致思路为，统计s子串和t，如果包含t中的所有，则符合，更新最小值即可
    但暴力会超时，需要对判断S子串是否包含T这个判断进行优化，优化的方法如下：
    1.使用一个变量needAmount记录所需的字母总数（小于等于0表示满足了），counter表示各个字母所需的数量（小于等于0则表示满足了）
    2.needAmount的更新判断比较重要，更新的条件是，T中的字母大于0（表示还需要当前这个字母），才进行加/减操作
    3.因为当前使用的是while循环，right会停止，用preRight来暂停right指针的操作，移动left指针操作
    """
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or not self._isEqual(collections.Counter(t), collections.Counter(s)):
            return ""
        counter = collections.Counter(t)
        needAmount = len(t)

        ans = s
        left, right, preRight = 0, 0, -1

        while right < len(s):
            if right != preRight and s[right] in counter:
                if counter[s[right]] > 0:
                    needAmount -= 1
                counter[s[right]] = counter[s[right]] - 1
            # print(s[left], s[right], left, right, needAmount, counter, ans)

            if needAmount <= 0:
                if right - left < len(ans):
                    ans = s[left:right+1]

                if s[left] in counter:
                    counter[s[left]] = counter[s[left]] + 1
                    if counter[s[left]] > 0:
                        needAmount += 1
                left += 1
                preRight = right
            else:
                right += 1

        # print(ans)
        return ans

    def _isEqual(self, ts, ss):
        for key in ts:
            if key not in ss or ts[key] > ss[key]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert Solution().minWindow(s="ADOBECODEBANC", t="ABCG") == ""
