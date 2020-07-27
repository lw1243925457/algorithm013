"""
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。


解题思路：
1刷：想到了一种解法，还是错误的。。。。。。

[1,2,3] 3
1 [3,1,2]
2 [2,3,1]
3 [1,3,3]
关于移动步数K，k可能很大，但移动步数只在0-len（nums）之间，则移动步数为 k % len（nums），如何为0，直接返回数组,示例如上

1.暴力解：直接模拟k步移动,
2.使用一个额外数组,也就是原本数组里下标为 ii 的我们把它放到 (i+k)\%数组长度(i+k)%数组长度的位置
3.环状替换：还不太很明白。。。。。。
4.使用反转：思路很巧妙,技巧性强，作为模块记住掌握,感觉它最优，就参照它写一个解
5.参考第一名跑的最快的Python3解：利用切片，直接nums[:] = nums[lenth-k:]+nums[:lenth-k]，不知道这个方法空间复杂度是？
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k % n == 0:
            return None

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    print(nums)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
