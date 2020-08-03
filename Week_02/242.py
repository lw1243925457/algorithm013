"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


解题思路
字母异位词：所有字母出现次数相同
用hashmap统计字母出现次数是否相同即可
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        shash = {}
        thash = {}
        for i in range(0, n):
            shash[s[i]] = shash.get(s[i], 0) + 1
            thash[t[i]] = thash.get(t[i], 0) + 1

        for key in shash.keys():
            if shash.get(key, 0) != thash.get(key, 0):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert not s.isAnagram("s", "")
    assert not s.isAnagram("s", "b")
    assert s.isAnagram("ssffdd", "sfdsfd")
    assert not s.isAnagram("ssffdf", "sfdsfd")
