# 给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 109 + 7的值。 
# 
#  学生出勤记录是只包含以下三个字符的字符串： 
# 
#  
#  'A' : Absent，缺勤 
#  'L' : Late，迟到 
#  'P' : Present，到场 
#  
# 
#  如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。 
# 
#  示例 1: 
# 
#  
# 输入: n = 2
# 输出: 8 
# 解释：
# 有8个长度为2的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# 只有"AA"不会被视为可奖励，因为缺勤次数超过一次。 
# 
#  注意：n 的值不会超过100000。 
#  Related Topics 动态规划 
#  👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkRecord(self, n: int) -> int:
        if n==1:
            return 3
        if n==2:
            return 8
        # L LL O
        haveA=[1,0,3]
        noA=[1,1,2]
        for i in range(n-2):
            tempA=[0]*3
            tempNoA=[0]*3
            #用a l p 分别更新上两个数组
            #a
            tempA[2]+=noA[0]+noA[1]+noA[2]
            #p
            tempA[2]+=haveA[0]+haveA[1]+haveA[2]
            tempNoA[2]+=noA[0]+noA[1]+noA[2]
            #l
            tempA[0]+=haveA[2]
            tempA[1]+=haveA[0]
            tempNoA[0]+=noA[2]
            tempNoA[1]+=noA[0]
            haveA=[x%(10**9 + 7) for x in tempA]
            noA=[x%(10**9 + 7) for x in tempNoA]
        return (sum(haveA)+sum(noA))%(10**9 + 7)
# leetcode submit region end(Prohibit modification and deletion)
