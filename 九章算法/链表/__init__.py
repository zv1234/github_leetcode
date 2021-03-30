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
        return new_head.next

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
# '''
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 进阶：
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """



# 3.two pointers in linked list
'''
1. Middle of Linked List
2. Remove Nth Node From End of List
3. Linked List Cycle I, II
4. Rotate List
'''
# 141给定一个链表，判断链表中是否有环。
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


# 61给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return


#203移除链表元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        sentinel = ListNode(0)
        sentinel.next = head # 设置哨兵节点
        prev, cur = sentinel, head # 前继节点，当前节点
        while cur: # 循环终止条件
            if cur.val == val:
                prev.next = cur.next  # 删除节点
            else:
                prev = cur # 前继指针滑动
            cur = cur.next # 当前指针滑动
        return sentinel.next

#707设计链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        # index steps needed
        # to move from sentinel node to wanted index
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val) :
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length,
        # the node will not be inserted.
        if index > self.size:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next


#206反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head) :
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre

# 19删除链表倒数n的节点

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = head
        p = dummy_node
        for i in range(n):
            cur = cur.next
        while cur:
            cur = cur.next
            p = p.next
        p.next = p.next.next
        return dummy_node.next

        # dummy = ListNode(0, head)
        # first = head
        # second = dummy
        # for i in range(n):
        #     first = first.next

        # while first:
        #     first = first.next
        #     second = second.next

        # second.next = second.next.next
        # return dummy.next


