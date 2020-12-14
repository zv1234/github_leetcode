#encoding:utf-8

#最小栈
'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素
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