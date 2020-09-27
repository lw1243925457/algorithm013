# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8956 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、排序加双指针，O(NlogN)
    二、一次遍历哈希统计比较，O(N)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in m and i != m[remainder]:
                return [m[remainder], i]
            m[nums[i]] = i
        return []


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
