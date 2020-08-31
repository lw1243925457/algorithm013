# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  示例 1: 
# 
#  输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2: 
# 
#  输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
#  Related Topics 字符串 动态规划 
#  👍 487 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题方法：
    一、递归：按照独立成单字符或者与后面以为形成双子符的两种情况进行递归求解
    最后形成了一颗递归树，时间复杂度有点像O(2^N)

    二、动态规划：
    空字符串0，”1“=1，”11“=2,”111“=3，”1111“=5,"11111"=8
    如111 = 1,1,1；11,1；1,11，观察规律可得“111” = 1 + fun(11) + "11" + fun(1)
    即f(n) = f(n-1) + f(n-2),其中成双有小于26的限制
    注：输入还有非1-26的，原理还是不变的，那n-1和n-2都有进行判断限制了
    注：还有不合法输入，如130，测试发现直接返回0即可
    注：01的初始化情况，"0", "1-9", "01", "10", "11-26", "27"
    数据遍历一次，时间复杂度为O(N)
    边界条件搞的人心态有点崩，后面需要在梳理梳理
    """
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return size
        dp = [0] * size
        if s[0] == "0":
            return 0
        dp[0] = 1
        if size > 1:
            if int(s[:2]) == 10 or int(s[:2]) == 20 or int(s[:2]) >= 27:
                dp[1] = 1
            else:
                dp[1] = 2
            if int(s[1]) == 0 and (int(s[:2]) > 26 or int(s[:2]) < 1):
                return 0

        for i in range(2, size):
            if i-1 >= 0 and int(s[i]) > 0:
                dp[i] += dp[i-1]
            if s[i-1] != "0" and i-2 >= 0 and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
            if int(s[i]) == 0 and (int(s[i-1:i+1]) > 26 or int(s[i-1:i+1]) < 1):
                return 0
        return dp[-1]

    def _recursion(self, s, index, size):
        """方法一：递归；独立成单或者与后面成双"""
        if index >= size:
            return 1
        ans = 0
        ans += self._recursion(s, index+1, size)
        if index + 1 < size and int(s[index:index+2]) <= 26:
            ans += self._recursion(s, index+2, size)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    print(Solution().numDecodings("226"))
    print(Solution().numDecodings("0"))
    print(Solution().numDecodings("27"))
    print(Solution().numDecodings("10"))
    print(Solution().numDecodings("100"))
