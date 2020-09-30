# 给定两个字符串 s 和 t，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例: 
# 
#  输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
#  
#  Related Topics 位运算 哈希表 
#  👍 156 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、哈希统计：统计S和T中字母出现次数，次数多一个即为被添加的字母
    二、ASCII码之和：T的所有字母码-S的所有字母码=多的字母码
    三、异或法：使用0想将s相关位置置为1，再消T相关位置，最后得到的就是多余的
    """
    def findTheDifference(self, s: str, t: str) -> str:
        # return self._method1(s, t)
        # return self._method2(s, t)
        return self._method3(s, t)

    def _method1(self, s, t):
        sdict, tdict = {}, {}
        for c in s:
            sdict[c] = sdict.get(c, 0) + 1
        for c in t:
            tdict[c] = tdict.get(c, 0) + 1

        for c in tdict:
            if c not in sdict:
                return c
            if tdict[c] - sdict[c] == 1:
                return c
        return ""

    def _method2(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

    def _method3(self, s, t):
        n = 0
        for c in s:
            n ^= ord(c)
        for c in t:
            n ^= ord(c)
        return chr(n)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().findTheDifference("abcd", "abcde") == "e"
