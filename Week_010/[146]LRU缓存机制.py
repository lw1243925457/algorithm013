# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。 
# 
#  获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。 
# 写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在
# 写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。 
# 
#  
# 
#  进阶: 
# 
#  你是否可以在 O(1) 时间复杂度内完成这两种操作？ 
# 
#  
# 
#  示例: 
# 
#  LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#  
#  Related Topics 设计 
#  👍 886 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class DoubleLink:
    def __init__(self, key, value):
        self.key, self.value, self.prev, self.next = key, value, None, None


class LRUCache:

    def __init__(self, capacity: int):
        self._cache = {}
        self._head, self._tail = DoubleLink(0, 0), DoubleLink(0, 0)
        self._head.prev = self._tail
        self._tail.next = self._head
        self._used = 0
        self._size = capacity

    def get(self, key: int) -> int:
        # print("get:", key, self._cache)
        if key in self._cache:
            self._sperate(key)
            self._addToHead(key)
            return self._cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        # print("put:", self._used, self._size, self._cache)
        if key in self._cache:
            self._cache[key].value = value
            self._sperate(key)
        else:
            self._cache[key] = DoubleLink(key, value)
            if self._used >= self._size:
                self._cache.pop(self._tail.next.key)
                self._removeTail()
            else:
                self._used += 1
        self._addToHead(key)

    def _removeTail(self):
        """删除最后一个元素"""
        nnext = self._tail.next.next
        self._tail.next = nnext
        nnext.prev = self._tail

    def _addToHead(self, key):
        """将元素添加/移动到头部"""
        phead = self._head.prev
        phead.next = self._cache[key]
        self._cache[key].prev = phead

        self._cache[key].next = self._head
        self._head.prev = self._cache[key]

    def _sperate(self, key):
        """让当前元素脱离，两端元素相连"""
        prev, next = self._cache[key].prev, self._cache[key].next
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# assert cache.get(1) == 1
# cache.put(3, 3)
# assert cache.get(2) == -1
# cache.put(4, 4)
# assert cache.get(1) == -1
# assert cache.get(3) == 3
# assert cache.get(4) == 4

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
assert cache.get(2) == 2
cache.put(1, 1)
cache.put(4, 1)
assert cache.get(2) == -1