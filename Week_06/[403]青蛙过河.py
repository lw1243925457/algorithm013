# 一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。 
# 
#  给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以
# 假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。 
# 
#  如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。 
# 
# 
#  请注意： 
# 
#  
#  石子的数量 ≥ 2 且 < 1100； 
#  每一个石子的位置序号都是一个非负整数，且其 < 231； 
#  第一个石子的位置永远是0。 
#  
# 
#  示例 1: 
# 
#  
# [0,1,3,5,6,8,12,17]
# 
# 总共有8个石子。
# 第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
# 第三个石子在序号为3的单元格的位置， 以此定义整个数组...
# 最后一个石子处于序号为17的单元格的位置。
# 
# 返回 true。即青蛙可以成功过河，按照如下方案跳跃： 
# 跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着 
# 跳2个单位到第4块石子, 然后跳3个单位到第6块石子, 
# 跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。
#  
# 
#  示例 2: 
# 
#  
# [0,1,2,3,4,8,9,11]
# 
# 返回 false。青蛙没有办法过河。 
# 这是因为第5和第6个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
#  
#  Related Topics 动态规划 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、暴力递归：
    1.结束条件：刚好位于最后一个单元格，返回True，超过False
    2.递归式子：k-1，k，K+1处有石子则挑，且不能后退
    按照递归树的状态，时间复杂度达到了恐怖的O(3^N)


    二、记录最大跳跃距离：从跳跃游戏启发的解法
    [0,1,3,5,6,8,12,17]
    记录当前位置能跳的长度和步数：如
    0 (能跳跃的长度和步数为 1 1, 生成下一步能跳到的距离和使用的步数): {1: [1]}
    1 (查询到上一步能跳到1，且步数为1, 生成下一步能跳到的距离和使用的步数,小于下一块石头位置排除，下同理）:{3: [2]}
    1 {3: [2]}
    3 {5: [2], 6: [3]}
    5 {6: [3, 1], 7: [2], 8: [3]}
    6 {7: [2], 8: [3, 2], 9: [3], 10: [4]}
    8 {7: [2], 9: [3], 10: [4], 12: [4]}
    12 {7: [2], 9: [3], 10: [4], 17: [5]}

    1.初始化0格的下一步跳跃数据
    2.遍历1到n-1的石头位置
        1.如果上一步能当前石头位置则更新下一步跳跃数据（k-1，k，K+1），因为当前石头位置已经跳到了，后面也用不到，删除其跳跃数据
        2.如果上一步不能跳到当前石头位置，则返回False
    3.遍历完成后查看能跳到石头位置是否包含最后一块石头位置，返回相应结果即可

    遍历一次数据，其中遍历步数数据做了排重应该较小，也可视为O(N)，则整体时间复杂度大致为O(N^2)
    """

    def canCross(self, stones: List[int]) -> bool:
        # return self._method1(tuple(stones), 0, 1)
        return self._method2(stones)

    def _method1(self, stones, pos, step):
        if pos == stones[-1]:
            return True
        if pos > stones[-1]:
            return False
        if step < 1:
            return False
        if pos not in stones:
            return False
        return self._method1(stones, pos + step - 1, step - 1) or \
               self._method1(stones, pos + step, step) or \
               self._method1(stones, pos + step + 1, step + 1)

    def _method2(self, stones):
        nextPos = {1: [1]}
        for i in range(1, len(stones)-1):
            stone = stones[i]
            if stone not in nextPos:
                continue
            for step in nextPos[stone]:
                if step - 1 > 0:
                    self._updateStep(nextPos, stone, step - 1, stones[i+1])
                self._updateStep(nextPos, stone, step, stones[i+1])
                self._updateStep(nextPos, stone, step + 1, stones[i+1])
            del nextPos[stone]
            # print(stone, nextPos)
        return stones[-1] in nextPos

    def _updateStep(self, nextPos, pos, step, nextStone):
        if pos + step < nextStone:
            return
        if pos + step not in nextPos:
            nextPos[pos + step] = []
        if step not in nextPos[pos + step]:
            nextPos[pos + step].append(step)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17])
    assert not Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])
