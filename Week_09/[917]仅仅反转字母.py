# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入："ab-cd"
# 输出："dc-ba"
#  
# 
#  示例 2： 
# 
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  示例 3： 
# 
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S 中不包含 \ or " 
#  
#  Related Topics 字符串 
#  👍 61 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l, r = 0, len(S) - 1
        ans = list(S)
        while l < r:
            if S[l].isalpha() and S[r].isalpha():
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
            elif not S[l].isalpha() and not S[r].isalpha():
                l += 1
                r -= 1
            elif S[l].isalpha() and not S[r].isalpha():
                r -= 1
            elif not S[l].isalpha() and S[r].isalpha():
                l += 1
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)
