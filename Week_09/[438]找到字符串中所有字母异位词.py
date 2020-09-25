# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表 
#  👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、先统计p的字母，在动态统计s遍历中的字母出现次数，进行判断即可
    时间复杂度应该为（NM），N为s长度，M为p长度
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pdict = {}
        for c in p:
            pdict[c] = pdict.get(c, 0) + 1

        l, r = 0, len(p) - 1
        sdict = {}
        for i in range(l, r + 1):
            sdict[s[i]] = sdict.get(s[i], 0) + 1

        size = len(s)
        ans = []
        while r < size:
            # print(pdict, sdict)
            if pdict == sdict:
                ans.append(l)

            if not r + 1 < size:
                break
            sdict[s[l]] = sdict.get(s[l], 0) - 1
            if sdict[s[l]] <= 0:
                del sdict[s[l]]
            sdict[s[r+1]] = sdict.get(s[r+1], 0) + 1

            l += 1
            r += 1
        return ans

    def _check(self, pdict, sdict):
        for key in pdict:
            if key not in sdict or pdict[key] != sdict[key]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
    assert Solution().findAnagrams("abab", "ababc") == []
