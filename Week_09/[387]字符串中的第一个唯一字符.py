# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 268 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、哈希表
    直接用哈希表统计存储，而后遍历次数为1的返回
    遍历两次，时间复杂度为O(N)
    """
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1
        for i in range(0, len(s)):
            if m[s[i]] == 1:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)
