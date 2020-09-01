# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 378 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、动态规划：https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
    结合超哥讲的和上面这位老哥讲的，可以加深一下理解
    1.重复子结构：s[i:j+1]是否是回文，取决于s[i]==s[j] and s[i+1:j]是回文
    2.递推状态：dp[i][j]
    3.递推方程：dp[i][j] = s[i] == s[j] and s[i+1:j]
    注：扫描方向需要注意，从左上角开始扫描的方法;即选定右边界，再从头开始扫
    两层循环，时间复杂度就是O(N^2)

    二：中心扩散法:时间复杂度也是O(N^2)：
    """
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [[False] * size for i in range(0, size)]
        ans = 0
        dp[0][0] = True
        # i 为右边界，j从0开始扫描，避免出现递推前步骤漏掉
        for i in range(0, size):
            for j in range(0, i+1):
                if i - j == 0:
                    dp[j][i] = True
                    ans += 1
                elif i - j == 1 and s[i] == s[j]:
                    dp[j][i] = True
                    ans += 1
                elif i - j >= 2 and s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = True
                    ans += 1
        # print(ans)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().countSubstrings("abc") == 3
    assert Solution().countSubstrings("aaa") == 6
    assert Solution().countSubstrings("fdsklf") == 6
