#encoding:utf-8
'''
让我们简要回顾一下单链表和双链表的表现。

它们在许多操作中是相似的。
它们都无法在常量时间内随机访问数据。
它们都能够在 O(1) 时间内在给定结点之后或列表开头添加一个新结点。
它们都能够在 O(1) 时间内删除第一个结点。
但是删除给定结点(包括最后一个结点)时略有不同。
在单链表中，它无法获取给定结点的前一个结点，因此在删除给定结点之前我们必须花费 O(N) 时间来找出前一结点。
在双链表中，这会更容易，因为我们可以使用“prev”引用字段获取前一个结点。因此我们可以在 O(1) 时间内删除给定结点。

'''

#21合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
题解：使用头部到哨兵节点依次对比
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead=ListNode(-1)
        pre=prehead
        while l1 and l2:
            if l1.val<=l2.val:
                pre.next=l1
                l1=l1.next
            else:
                pre.next=l2
                l2=l2.next
        return pre.next
        #判断链表是否为空，并且将后面到节点加到新表到结尾
        pre.next=l1 if l1 is not  None else l2
        #此处注意应该为prehead.next
        return prehead.next


#两数相交给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

'''
题解：双指针进位+1

现在好像有点不想看了
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead=ListNode(-1)
        pre=prehead
        a=l1
        b=l2

