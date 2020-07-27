"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
通过次数373,579提交次数732,404


解题思路 1刷：
使用双指针
指针1指向当前不需要替换的位置
指针2向后遍历，当两个值不相等时，指针1后移并替换值为指针2所指的值
最后返回指针1的index+1即可
时间复杂度O(N)
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # 如果数组只有0和1个元素，直接返回即可
        if n < 2:
            return len(nums)

        left = 0
        right = 1
        while right < n:
            if nums[right] != nums[left]:
                left += + 1
                nums[left] = nums[right]
            right += 1
        return left + 1


if __name__ == "__main__":
    s = Solution()
    assert s.removeDuplicates([]) == 0
    assert s.removeDuplicates([1]) == 1
    assert s.removeDuplicates([1, 2, 3]) == 3
    nums = [1, 1, 1, 2, 2, 3]
    assert s.removeDuplicates(nums) == 3
    print(nums)
