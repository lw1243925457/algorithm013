"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
通过次数1,241,101提交次数2,529,280


解题思路：
1刷：一次遍历法还巧妙

给的数组不一定有序，同一个元素不能使用两次是值不能相同，还是下标不同即可？这里看返回下标，则认定下标不同即可吧
用hash给值保存下标
后面遍历数组，判断是否有符合的

hash查找时O(1)，遍历一次，则是O(N)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num2index = {}
        for i in range(0, n):
            remain = target - nums[i]
            if remain in num2index and num2index[remain] != i:
                return [i, num2index[remain]]
            num2index[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum(nums=[2, 7, 11, 15], target=9) in [[0, 1], [1, 0]]
    assert s.twoSum(nums=[3, 2, 4], target=6) in [[1, 2], [2, 1]]
