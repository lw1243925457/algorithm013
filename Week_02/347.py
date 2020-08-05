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
使用小顶堆实现，因为要返回前最大K个数，小顶堆就可以保存着K个数，而堆顶是最小数，剩下的都是大于它的

1.先使用hashmap统计保存数字的出现次数
2.使用k个数据初始化小顶堆
3.比堆顶大的就插入，小于就说明前K大的数没它的份

统计N，遍历N，大顶堆操作logK，则最大时间复杂度O(N)

自己实现个堆来尝试尝试
内置的跑了60ms，自写的56，感觉差不多
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
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)

        # 使用K个数初始化堆
        minHeap = MinHeap(k, count)
        keys = list(count.keys())
        print(keys)
        for i in range(0, k):
            minHeap.push(keys[i])

        # 大于堆顶才插入，小于的就说明前K个数没有它的份
        for i in range(k, len(keys)):
            if count[keys[i]] > count[minHeap.getMinest()]:
                minHeap.push(keys[i])

        return minHeap.toList()


class MinHeap:
    def __init__(self, size: int, myDict: dict):
        """
        堆的初始化，设置堆的大小
        :param size: 堆的大小
        """
        # 这里有个小技巧，数组下标不从0开始，而从1开始，这样父子节点的下标获取和计算方便，所有这里数组空间为size+1
        self.data = [None] * (size + 1)
        self.size = size
        self.used = 0
        self.myDict = myDict
        print("init heap:", self.data)

    def push(self, value: int) -> None:
        """
        堆的插入操作
        :return:
        """
        print("insert value:", value, end=" ")
        if self.used == self.size:
            self.pop()

        self.used += 1
        print("insert:", self.used, value, self.data, end="==>")
        self.data[self.used] = value
        self._shitUp()
        print(self.data)

    def pop(self) -> None:
        """
        堆的删除操作
        :return:
        """
        if self.used == 0:
            return

        self.data[1] = self.data[self.used]
        print("pop:", self.data, end="==>")
        self.used -= 1
        self._shitDown()
        print(self.data)

    def _shitUp(self):
        """
        自下向上的堆化
        与父节点进行比较，大于则交换
        :return:
        """
        child = self.used
        while child // 2 > 0 and self.myDict[self.data[child]] < self.myDict[self.data[child // 2]]:
            self.data[child], self.data[child // 2] = self.data[child // 2], self.data[child]
            child = child // 2

    def _shitDown(self):
        """
        自上向下的堆化
        这里是与最大值的子节点进行交换，则用了一个maxPos保存最大值的位置
        如果是当前父节点的位置，则堆化结束
        不是则交换父子节点，继续循环
        :return:
        """
        parent = 1
        while True:
            minPos = parent
            if parent * 2 <= self.used and self.myDict[self.data[parent * 2]] < self.myDict[self.data[parent]]:
                minPos = parent * 2
            if parent * 2 + 1 <= self.used and self.myDict[self.data[parent * 2 + 1]] < self.myDict[self.data[minPos]]:
                minPos = parent * 2 + 1
            if minPos == parent:
                break
            self.data[minPos], self.data[parent] = self.data[parent], self.data[minPos]
            parent = minPos

    def getMinest(self) -> int:
        """
        返回堆顶元素值
        :return:
        """
        return self.data[1]

    def toList(self):
        return self.data[1:]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    # [-3,-4,0,1,4,9]
    print(s.topKFrequent(nums=[6, 0, 1, 4, 9, 7, -3, 1, -4, -8, 4, -7, -3, 3, 2, -3, 9, 5, -4, 0], k=6))
