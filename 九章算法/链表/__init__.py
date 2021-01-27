#encoding:utf-8

#当发现头节点会发生改变时候，创建一个头节点，当返回还是head时候不需要生成头节点

# 1.introduce dummy node是否添加头节点

# 给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def deleteduplicates(self,head):
        if head==None or head.next==None:
            return head
        new_head=ListNode(-1)
        new_head.next=head
        parent=new_head
        cur=head
        while cur!=None and cur.next!=None:
            if cur.val==cur.next.val:
                val=cur.val
                while cur!=None and val==cur.val:
                    cur=cur.next
                parent.next=cur
            else:
                cur=cur.next
                parent=parent.next
        return head.next

#翻转链表中第m个节点到第n个节点的部分
'''
创建head.
找到m的前一个节点-Pre
记录Pre的下一个节点，它会是翻转链的尾部。
翻转指定区间的链表，翻到最后一个节点时，把reverseTail.next指向它的next。这样就把翻转链表与之后 的链表接起来了。
返回dummynode的下一个节点。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self,head):
        prev=None
        while head!=None:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev

    def findkth(self,head,k):
        for i in range(k):
            if head is None:
                return None
            head=head.next
        return head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(-1,head)
        mth_pre=self.findkth(dummy,m-1)
        mth=mth_pre.next
        nth=self.findkth(dummy,n)
        nth_next=nth.next
        nth.next=None
        self.reverse(mth)
        mth_pre.next=nth
        mth.next=nth_next
        return dummy.next
'''当头节点不确定创建的时候'''




#2.basic linked list skills
'''
1. Insert a Node in Sorted List
2. Remove a Node from Linked List
3. Reverse a Linked List
4. Merge Two Linked Lists
5. Middle of a Linked List
'''

# 3.two pointers in linked list
