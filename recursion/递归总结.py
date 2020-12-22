#encoding:utf-8

#合并两个有序的链表
'''
题解
1。递归
    递归基 l1为空返回l2  l2为空返回l1
    递归关系：
    list1[0]+merge(list[1:],list2) list1[0]<list[2]
    list2[0]+merge(list1,list2[1:])
2.迭代
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #递归基
        if not l1:
            return l2
        if not l2:
            return l1
        #规模缩小
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2