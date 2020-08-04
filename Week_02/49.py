"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

所有输入均为小写字母。
不考虑答案输出的顺序。
通过次数93,188提交次数148,148

解题思路：
1刷

1.借鉴hashmap和压缩的思路，一次遍历实现
    - 1.压缩当前字符串，压缩规则为：单字符+出现次数
    - 2.判断压缩后的字符是否在hashmap中，加入其中，没有就新建
    - 3.遍历hashmap返回即可
遍历一次所有字符串N，排序一个字符串MlogM,总时间复杂度应该是N * MlogM

2.方法1改进，借鉴官方题解思路
    1.1中的压缩复杂度有点高，可以使用排序一个字符串，使用26个字母的列表代替

疑问：
但这种统计的思路，没有字符串排序的思路快？是测试的字符串比较短，sort比统计快，还是hash的list相关操作慢？


看大佬们的题解，学到了好多简明的python写法
# 1.字符转数字统计：
```python
count = [0] * 26
count[ord(c) - ord('a')] += 1
```

# 2.将list作为key，并取默认值为空list再添加元素
```python
ansDict[tuple(count)] = ansDict.get(tuple(count), []) + [s]
```

# 3.将dict作为二维list返回
```python
list(dict.values())
```

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []

        # 直接字符串排序的思路，明显快
        ans = {}
        for s in strs:
            value = ''.join(sorted(s))
            ans[value] = ans.get(value, []) + [s]
        return list(ans.values())

        """
        # 统计的思想，按理说排序NlogN，统计N，这个应该比上面快
        ansDict = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ansDict[tuple(count)] = ansDict.get(tuple(count), []) + [s]
        return list(ansDict.values())
        """

    def compress(self, s):
        """
        压缩统计，但返回时需要确保字母顺序
        排序导致性能下降了
        :param s:
        :return:
        """
        m = {}
        for c in s:
            m[c] = m.get(c, 0) + 1

        cs = ""
        for key in sorted(m.keys()):
            cs += key + str(m[key])
        return cs


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))