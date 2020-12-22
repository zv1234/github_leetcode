#encoding:utf-8
'''
代码实现
第一步：判断输入或者状态是否合法
第二步：判断递归是否应该结束
第三步：缩小问题规模
第四步：整合结果
'''

#杨辉三角

'''
题解：
递归：
    递归基数条件
    numrows=0 return []
    numrows=1 return [1]
    s[n]=s[n-1]+o(n-1)
    o(n-1)=([1]+[s[-1][i-1]+s[-1][i] for i in range(1,len(s))]+[1]
    
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #基本条件
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        # 缩小问题规模
        s = self.generate(numRows - 1)
        s.append([1] + [s[-1][i - 1] + s[-1][i] for i in range(1, len(s))] + [1])
        return s

#杨辉三角二 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

'''
题解：
1。递归
    f(k)=f(k-1)+o(k-1)
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        s=self.getRow(rowIndex-1)
        s=[1]+[s[i-1]+s[i] for i in range(1,len(s))]+[1]
        return s


#反转链表 反转单链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
题解：
1。递归
    递归基
    head=None return None
    单节点  return head
    
    规模减少
    reverlist(head.next)
    
    合并
    head.next.next=head
    head.next=None
    
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        cur=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return cur



