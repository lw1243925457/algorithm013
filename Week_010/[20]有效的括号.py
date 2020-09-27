# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 1879 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    解题思路：
    首先括号是成对的，则数量一定是偶数
    一、使用六个变量统计六种括号，当成对相等则是true，这种方法不行，括号的嵌套必须是正确的如："([)]"是不对的
    二、使用栈，遇到右类型括号时弹出，无法弹出或者最后不为空则False
    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ltor = {"]": "[", "}": "{", ")": "("}
        stack = []
        for c in s:
            if c in ltor:
                if len(stack) == 0 or stack.pop() != ltor[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().isValid("")
    assert not Solution().isValid("{")
    assert not Solution().isValid("{}(")
    assert not Solution().isValid("{}(}")
    assert Solution().isValid("()")
    assert Solution().isValid("[()()]{}[]")
    assert not Solution().isValid("([)]")
    assert not Solution().isValid("}(")
