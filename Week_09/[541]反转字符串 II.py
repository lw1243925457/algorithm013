# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例: 
# 
#  输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#  
# 
#  
# 
#  提示： 
# 
#  
#  该字符串只包含小写英文字母。 
#  给定字符串的长度和 k 在 [1, 10000] 范围内。 
#  
#  Related Topics 字符串 
#  👍 91 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    一、遍历获取前2k个字符，反转前k个
    一次遍历，时间复杂度应该为O(N)
    """
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        size = len(s)
        index = 0
        while index + 2 * k < size:
            ans += s[index:index+k][::-1]
            ans += s[index+k:index + 2*k]
            index += k * 2
        ans += s[index:index + k][::-1]
        ans += s[index+k:]
        # print(ans)
        return ans

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"
    assert Solution().reverseStr("abcdefgbh", 2) == "bacdfegbh"
    assert Solution().reverseStr("abcd", 2) == "bacd"
