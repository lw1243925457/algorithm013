"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。



说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
通过次数181,303提交次数376,269


解题思路：
1 刷
使用双指针，类似合并两链表,但是现在从尾到头，比较获取最大值，逐步从后面填充到前面
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, n):
            nums1[m + i] = nums2[i]

        p1 = m - 1
        p2 = n - 1
        index = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                nums1[index] = nums2[p2]
                p2 -= 1
            elif p2 < 0:
                nums1[index] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
    assert nums1 == [1, 2, 2, 3, 5, 6]
