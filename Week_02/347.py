"""
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。


解题思路：
1.先使用hashmap统计保存数字的出现此时
2.遍历hashmap，使用大顶堆维护前k个
3.返回大顶堆所有数据

统计N，遍历N，大顶堆操作logK，则最大时间复杂度O(N)

想自己实现个堆来尝试尝试
看看与内置有多大差别
"""
import collections
from typing import List
import heapq


class SolutionP:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = MaxHeap(k)

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        print(count)
        count[-pow(2, 31)] = -pow(2, 31)
        for key in count.keys():
            maxHeap.push(count, key)
            print("push:", key, maxHeap.data)
        return maxHeap.data


class MaxHeap:
    def __init__(self, size: int):
        self.MIN = -pow(2, 31)
        self.data: list = [self.MIN] * size
        self.size = size
        self.used = 0

    def push(self, count: dict, key: int) -> None:
        if self.used == self.size:
            self.pop(count)

        self.data[self.used] = key
        self._shitUp(count)
        self.used += 1

    def pop(self, count: dict) -> None:
        if self.used == 0:
            return

        self.data[0] = self.data[self.used - 1]
        print("pop:", self.data)
        self._shitDown(count)
        self.used -= 1

    def _shitUp(self, count: dict):
        """与其父节点进行比较，大于则交换位置"""
        child = self.used
        parent = child // 2
        while True:
            if count[self.data[child - 1]] > count[self.data[parent - 1]]:
                self.data[child - 1], self.data[parent - 1] = self.data[parent - 1], self.data[child - 1]
                child = parent
                parent = child // 2
            else:
                break

    def _shitDown(self, count: dict):
        """与其子节点进行比较，小于两儿子，则与最大儿子进行交换"""
        parent = 1
        lchild = parent * 2
        rchild = parent * 2 + 1
        while lchild <= self.used:
            if rchild > self.used:
                if count[self.data[parent - 1]] < count[self.data[lchild - 1]]:
                    self.data[parent - 1], self.data[lchild - 1] = self.data[lchild - 1], self.data[parent - 1]
                break

            maxChild = max(count[self.data[lchild - 1]], count[self.data[rchild - 1]])
            if count[self.data[parent - 1]] < maxChild:
                if count[self.data[lchild - 1]] < count[self.data[rchild - 1]]:
                    self.data[rchild - 1], self.data[parent - 1] = self.data[parent - 1], self.data[rchild - 1]
                    parent = rchild
                else:
                    self.data[lchild - 1], self.data[parent - 1] = self.data[parent - 1], self.data[lchild - 1]
                    parent = lchild

                lchild = parent * 2
                rchild = lchild + 1

    def toList(self):
        return self.data


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
