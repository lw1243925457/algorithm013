# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 249 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、字母异位词：内容相同，字母位置不同，则需满足下面的条件：
    1.长度相等
    2.各个字母出现相等
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for i in range(0, len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        return d1 == d2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert not Solution().isAnagram("a", "b")
    assert Solution().isAnagram("acb", "bca")
