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



