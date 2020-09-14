# 给你两个数组，arr1 和 arr2， 
# 
#  
#  arr2 中的元素各不相同 
#  arr2 中的每个元素都出现在 arr1 中 
#  
# 
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。 
# 
#  
# 
#  示例： 
# 
#  输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#  
# 
#  
# 
#  提示： 
# 
#  
#  arr1.length, arr2.length <= 1000 
#  0 <= arr1[i], arr2[i] <= 1000 
#  arr2 中的元素 arr2[i] 各不相同 
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中 
#  
#  Related Topics 排序 数组 
#  👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：
    一、首先对array1进行排序并统计出现次数，然后按照array2的顺序组合新数组
    """
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 统计数字出现的次数
        d = {}
        for num in arr1:
            d[num] = d.get(num, 0) + 1
        set2 = set(arr2)
        arr1.sort()
        ans = []
        # 优先按照array2进行排列
        for num in arr2:
            ans += [num] * d[num]
        # array1排序后，没有出现在2中的数字一次排列
        for i in range(0, len(arr1)):
            if i != 0 and arr1[i] == arr1[i-1]:
                continue
            num = arr1[i]
            if num not in set2:
                ans += [num] * d[num]
        return ans

# leetcode submit region end(Prohibit modification and deletion)
