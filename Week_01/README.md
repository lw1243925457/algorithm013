# 学习笔记
***
## 总结
&ensp;&ensp;&ensp;&ensp;第一周学习了四种线性数据结构：数组、链表、栈、队列，对应进行相关题目的练习，下面进行简单的总结和一些相关联系扩展和布置的任务：

### 用 add first 或 add last 这套新的 API 改写 Deque 的代码
&ensp;&ensp;&ensp;&ensp;原来的代码如下：

```java
Deque<String> deque = new LinkedList<String>();

deque.push("a");
deque.push("b");
deque.push("c");
System.out.println(deque);

String str = deque.peek();
System.out.println(str);
System.out.println(deque);

while(deque.size() > 0) {
	System.out.println(deque.pop());
}
System.out.println(deque);
```

&ensp;&ensp;&ensp;&ensp;改写的代码如下：

```java
Deque<String> deque = new LinkedList<String>();

deque.addFirst("a");
deque.addFirst("b");
deque.addFirst("c");
System.out.println(deque);

String str = deque.	peekFirst();
System.out.println(str);
System.out.println(deque);

while(deque.size() > 0) {
	System.out.println(deque.pop());
}
System.out.println(deque);
```

### 分析 Queue 和 Priority Queue 的源码
#### Queue
&ensp;&ensp;&ensp;&ensp;Queue是一个接口，没有具体的实现，定义队列含有的方法，大致的方法如下：

- add：添加元素到队列中，队列满了会抛异常
- element:获取队列头部元素
- offer：插入元素到队列中
- peek：获取头部元素
- poll：获取并移除头部元素
- remove：移除头部元素

#### Priority Queue
&ensp;&ensp;&ensp;&ensp;源码链接：http://www.docjar.com/html/api/java/util/PriorityQueue.java.html

&ensp;&ensp;&ensp;&ensp;继承于Queue，由于插入元素有优先级，所有有一个比较器的东西。其中的插入和弹出都做了自己的特有的处理，关键入口函数是siftUp和siftDown，这两个函数里面进行一些优先级的比较，大致好像是基于比较进行一些处理

- add：添加元素到队列中，队列满了会抛异常，其中调用offer函数进行插入
- offer：插入元素到队列中，空就抛异常，原本没有元素就直接插入，有就调用siftUp函数进行插入
- peek：直接返回头部元素
- poll：获取并移除头部元素，siftDown返回数据
- remove：其中调用了siftDown函数进行一些处理，移除头部元素

### 数组
&ensp;&ensp;&ensp;&ensp;数组是连续的内存空间，大小固定，其增删改查的时间复杂度如下，改和查是指下标访问：

|操作|时间复杂度|
|----|---------|
|增|O(N)|
|删|O(N)|
|改|O(1)|
|查|O(1)|

&ensp;&ensp;&ensp;&ensp;其设计到相关的应用和算法由下面这些：

- 二分查找：时间复杂度为O(logN)的优秀查找算法
- 冒泡排序：O(N^2)
- 插入排序：O(N^2)
- 选择排序：O(N^2)
- 归并排序：O(NlogN)
- 快速排序：O(NlogN)

### 链表
&ensp;&ensp;&ensp;&ensp;链表是零散的内存块，大小动态，链表有可分为下面几种：

- 单链表：只记录后继节点信息
- 双向链表：记录前后节点信息，查询比单链快，删除比单链简单，前插快，查找能类二分
- 循环链表：头尾相连，可用于解决[约瑟夫问题](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98)
- 跳表：加多级索引的结构,支持类似“二分”的查找算法

&ensp;&ensp;&ensp;&ensp;其增删改查时间按复杂度如下：

|操作|时间复杂度|
|----|---------|
|增|O(1)|
|删|O(1)|
|改|O(N)|
|查|O(N)|

### 栈
&ensp;&ensp;&ensp;&ensp;后进者先出，先进者后出

&ensp;&ensp;&ensp;&ensp;可分为：

- 顺序栈：数组实现
- 链式栈：链表实现

&ensp;&ensp;&ensp;&ensp;LeetCode上有些题用栈来解决还是很好用的，栈的应用：函数调用栈、表达式求值、括号匹配、DFS深度优先搜索、前中后序二叉树遍历

### 队列
&ensp;&ensp;&ensp;&ensp;先进者先出

&ensp;&ensp;&ensp;&ensp;可分为：

- 顺序栈：数组实现
- 链式栈：链表实现

&ensp;&ensp;&ensp;&ensp;队列还有下面几种变形：

- 阻塞队列：类似生产消息模式那种
- 并发队列：基于数组的循环队列，利用CAS原子操作，可实现高并发