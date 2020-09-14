# 学习笔记

---

*题目：力扣排行榜，是付费的，就暂时不做了*

## 常用排序算法实现

### 冒泡排序

&ensp;&ensp;&ensp;&ensp;比较相邻的两元素，不满足大小关系则互换，一次遍历能将一个元素放到正确的位置上。完成排序需要 N 次遍历，则事件复杂度 O(N^2)，可以不使用额外的数据结构，则空间复杂度为 O(1)，可以相等时不交换，则是稳定的排序算法。

&ensp;&ensp;&ensp;&ensp;Python3 代码大致如下：

```python3
from typing import List

def bubbleSort(nums: List[int])-> None:
    n = len(nums)
    if n < 2:
        return

    for i in range(0, n):
        for j in range(0, n-i-1):
            if nums[j] < nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

nums = [2, 3, 5, 7, 1, 9, 3]
bubbleSort(nums)
print(nums)
```

### 插入排序

&ensp;&ensp;&ensp;&ensp;开始将第一个元素划分为有序区间，后面为无序区间，逐步将无序区间的元素插入到有些区间中。两层循环，一个区间划分遍历一次数据，第二层插入数据，大致为 O(N^2)，空间复杂度为 O(1)，数据相等时不交换，稳定的排线算法。代码大致如下：

```python3
from typing import List

def insertionSort(nums: List[int])-> None:
    n = len(nums)
    if n < 2:
        return

    for i in range(1, n):
        value = nums[i]
        # 寻找插入的位置
        j = i - 1
        while j > -1:
            # 数据往后移
            if nums[j] < value:
                nums[j+1] =  nums[j]
            else:
                break
            j = j - 1
        # 插入数据
        nums[j+1] = value

nums = [2, 3, 5, 7, 1, 9, 3]
insertionSort(nums)
print(nums)
```

### 选择排序

&ensp;&ensp;&ensp;&ensp;开始划分 1 个有序区间，后面查找最小或最大元素放入区间内。时间复杂度 O(N^2)，空间 O(1),不稳定。代码大致如下：

```python3
from typing import List

def selectSort(nums: List[int])-> None:
    n = len(nums)
    if n < 2:
        return

    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

nums = [2, 3, 5, 7, 1, 9, 3]
selectSort(nums)
print(nums)
```

### 归并排序

&ensp;&ensp;&ensp;&ensp;使用分治的思路，把数组分成两半，分别排序，排序后进行合并。大致代码如下：

```python
from typing import List

def mergeSort(nums: List[int])-> List[int]:
    n = len(nums)
    if n == 1:
        return nums

    mid = n // 2
    lsort = mergeSort(nums[:mid])
    rsort = mergeSort(nums[mid:])
    return merge(lsort, rsort)

def merge(nums1: List[int], nums2: List[int])-> List[int]:
    nums = []
    n = len(nums1)
    m = len(nums2)
    index1 = 0
    index2 = 0
    while index1 < n or index2 < m:
        if index1 >= n:
            nums.append(nums2[index2])
            index2 = index2 + 1
        elif index2 >= m:
            nums.append(nums1[index1])
            index1 = index1 + 1
        elif nums1[index1] < nums2[index2]:
            nums.append(nums1[index1])
            index1 = index1 + 1
        else:
            nums.append(nums2[index2])
            index2 = index2 + 1
    return nums


nums = [2, 3, 5, 7, 1, 9, 3]
print(mergeSort(nums))
```

### 快速排序

&ensp;&ensp;&ensp;&ensp;也是使用分治的思路，随机选取其中一个数最为分界点，把小于其的数反左边或右边，大于其的数类似。大致代码如下：

```python
from typing import List

def quickSort(nums: List[int], start: int, end: int)-> None:
    if start >= end:
        return

    mid = partition(nums, start, end)
    # 注意后面排序的序号，排序是不包括分界元素的
    quickSort(nums, start, mid-1)
    quickSort(nums, mid+1, end)

def partition(nums: List[int], start: int, end: int)-> int:
    """
    选取最后一个元素为分界，小于的放左，使用了双指针交换元素
    """
    value = nums[end]
    index = start
    for i in range(start, end):
        if nums[i] < value:
            nums[i], nums[index] = nums[index], nums[i]
            index = index + 1
    nums[index], nums[end] = nums[end], nums[index]
    return index


nums = [2, 3, 5, 7, 1, 9, 3]
quickSort(nums, 0, len(nums)-1)
print(nums)
```

## 位运算符

| 运算符 | 含义     | 示例                    |
| ------ | -------- | ----------------------- |
| &#124; | 按位或   | 0011 &#124; 1011 = 1011 |
| &      | 安慰与   | 0011 & 1011 = 0011      |
| ~      | 按位取反 | ~0011=1100              |
| ^      | 按位异或 | 0011^1011=1000          |

### XOR-异或高级操作
&ensp;&ensp;&ensp;&ensp;异或：相同为0，不同为1，具备以下的特点：

- x^0=x
- x^1s=~x:1s=~0
- x^(~x)=1s
- x^x=0
- c=a^b;a^c=b;b^c=a：交换两个数
- a^b^c=a^(b^c)

### 指定位置的位运算

- 1.将x最右边的n位清零：x & (~0 << n)
- 2.获取x的第n位置值（0或者1）：(x >> n) & 1
- 3.获取x的第n位的幂值：x & (1 << n)
- 4.仅将第n位置为1：x | (1 << n)
- 5.仅将第n位置为0：x & (~(1 << n))
- 6.将x最高位至第n位（含）清零：x & ((1 << n) - 1)

### 实战位运算要点

- 判断奇偶：
  - x % 2 == x & 1：10为奇偶
- x / 2 == x >> 1
- x = x & (x - 1):清零最低位的1
- x & -x:得到最低位的1
- x & ~x = 0

### 实战练习题目（LeetCode）

- [位 1 的个数](https://leetcode-cn.com/problems/number-of-1-bits/)
- [2 的幂](https://leetcode-cn.com/problems/power-of-two/)
- [颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)
- [N 皇后](https://leetcode-cn.com/problems/n-queens/description/)
- [N 皇后 II ](https://leetcode-cn.com/problems/n-queens-ii/description/)
- [比特位计数](https://leetcode-cn.com/problems/counting-bits/description/)