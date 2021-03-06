# 学习笔记
***
## 递归
&ensp;&ensp;&ensp;&ensp;递归是一种应用非常广泛的算法（或者编程技巧）

### 递归需要满足的三个条件
- 1.一个问题的解可以分解为几个子问题的解
- 2.这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
- 3.存在递归终止条件

### 如何编写递归代码
&ensp;&ensp;&ensp;&ensp;关键点：写出递归公式，找到递归条件，下面是递归的代码模板

```python
def func(param1, param2, ...):
	# 写出终止条件，结束递归

	# 数据处理，操作

	# 函数再次调用

	# 数据的后续操作，清理之类的

	pass
```

### 递归代码要警惕堆栈溢出
&ensp;&ensp;&ensp;&ensp;LeetCode刷题倒是没注意，但开发过程中的递归代码可以会遇到堆栈溢出的问题，这时可以使用一个深度的参数限制递归深度：

```java
// 全局变量，表示递归的深度,作为参数参入应该也可以
int depth = 0;

int f(int n) {
  ++depth；
  if (depth > 1000) throw exception;
  
  if (n == 1) return 1;
  return f(n-1) + 1;
}
```

### 递归代码要警惕重复计算
&ensp;&ensp;&ensp;&ensp;很多的递归问题可以画出一颗递归树，而递归树中有很多节点是相同的，导致了很多的重复计算，这个时候可以缓存计算结果来避免。

&ensp;&ensp;&ensp;&ensp;缓存的方法有很多，比如数组，hashmap之类的，这里记录一个Python3的@lru_cache装饰器，其作用是：把耗时的函数的结果保存起来，避免传入相同的参数时重复计算

&ensp;&ensp;&ensp;&ensp;下面是拿经典的斐波那契数列计算函数来举例

```python
@lru_cache(None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 2) + fib_with_cache(n - 1)
```

### 递归代码改写非递归
&ensp;&ensp;&ensp;&ensp;递归是借助栈实现的，改写的时候注意数据的入栈和出栈顺序即可

## 做题技巧
- 排列组合类的不重复问题：可以使用排序+此次选取中不等于上次值来达到目的