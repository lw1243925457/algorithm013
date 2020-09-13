# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。 
# 
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。 
# 
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。 
# 
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。 
# 
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。 
# 
#  注意: 
# 
#  
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。 
#  所有的目标基因序列必须是合法的。 
#  假定起始基因序列与目标基因序列是不一样的。 
#  
# 
#  示例 1: 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
#  
# 
#  示例 2: 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
#  
# 
#  示例 3: 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
#  
#  👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    """
    解题思路：双边bfs，类似单词接龙
    """
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if not end or end not in bank or len(start) != len(end):
            return -1

        startLength, endLength = 0, 0
        startStack, endStack = [start], [end]
        startVisited, endVisited = set(), set()
        startVisited.add(start)
        endVisited.add(end)

        while len(startStack) != 0 and len(endStack) != 0:
            startLength += 1
            size = len(startStack)
            for _ in range(0, size):
                node = startStack.pop(0)
                for i in range(0, len(node)):
                    for c in "ACGT":
                        newNode = node[:i] + c + node[i+1:]
                        if newNode not in bank:
                            continue
                        if newNode in endStack:
                            return startLength + endLength
                        if newNode not in startVisited:
                            startVisited.add(newNode)
                            startStack.append(newNode)

            if len(startStack) > len(endStack):
                startLength, endLength = endLength, startLength
                startStack, endStack = endStack, startStack
                startVisited, endVisited = endVisited, startVisited

        return -1
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
    assert Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) == 3
