#encoding:utf-8

#最小栈
'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素

题解：我们只需要设计一个数据结构，使得每个元素 a 与其相应的最小值 m 时刻保持一一对应。因此我们可以使用一个辅助栈，与元素栈同步插入与删除，用于存储与每个元素对应的最小值。

当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,  x) :
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) :
        self.stack.pop()
        self.min_stack.pop()

    def top(self) :
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


#20有效到括号给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
'''
题解：将左括号放入栈定，匹配右边括号，遇到一个右括号就将左括号弹出
时间复杂度：o（n）
'''


class Solution:
    def isValid(self, s) :
        #判断奇数项返回flase
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        #左括号入栈，如果右括号，进行对比
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

#739每日温度
'''
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
'''
'''
题解分析：单调栈
好像有点看不懂 时间复杂度o(n) 空间复杂度o(n)
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        length=len(T)
        ans=[0]*length
        stack=[]
        for i in range(length):
            temp=T[i]
            while stack and temp>T[stack[-1]]:
                prev=stack.pop()
                ans[prev]=i-prev
            stack.append(i)
        return ans
#单调栈问题模板
'''
class solution(object):
    def moban_single_stack(self,arr):
        stack=[]
        ans=定义一个长度和arr一样长的数组，并初始化为-1
        for i in range(arr):
            while stack and arr[i]>arr[栈顶元素]:
                peek=弹出栈顶元素
                ans[peek]=i-peek
            stack.append(i)
        return ans
'''


'''
总结：栈：单调栈使用 一般处理next greater element 
        循环数组 ，如果求next greater element ，假设数组是环形的 ，一般通过%运算来实现环形
'''

'''
练习：
42接雨水
84 柱状图中最大的矩形
去除重复字母
移除k位数字
下一个更大元素Ⅰ
最短无序连续子数组
股票价格跨度
'''