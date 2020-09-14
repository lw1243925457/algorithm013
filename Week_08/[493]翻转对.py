# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。 
# 
#  你需要返回给定数组中的重要翻转对的数量。 
# 
#  示例 1: 
# 
#  
# 输入: [1,3,2,3,1]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: [2,4,3,5,1]
# 输出: 3
#  
# 
#  注意: 
# 
#  
#  给定数组的长度不会超过50000。 
#  输入数组中的所有数字都在32位整数的表示范围内。 
#  
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法 
#  👍 130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、暴力两层循环判断，时间复杂度为O(N^2)

    二、归并排序改造，对merge操作进行定制化，时间复杂度为O(NlogN)
    """
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(nums, l, mid, r) + left + right

    def merge(self, nums, l, mid, r):
        ans = 0
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            # i这个指针指的一直都是刚刚大于2倍nums[j]的元素，因为j所在的nums[mid+1, r]有序
            # 所以我们可以记录上一次的i，这样i最多也只从l到mid遍历一次
            while i <= mid and (nums[i] + 1) >> 1 <= nums[j]:
                i += 1
            while t <= mid and nums[t] < nums[j]:
                cache[c] = nums[t]
                c += 1
                t += 1
            cache[c] = nums[j]
            c += 1
            ans += mid - i + 1
        while t <= mid:
            cache[c] = nums[t]
            c += 1
            t += 1
        nums[l:r + 1] = cache
        return ans
# leetcode submit region end(Prohibit modification and deletion)
