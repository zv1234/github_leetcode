#encoding:utf-8

#141 环形链表 给定一个链表判断是否又环为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

'''
题解 双指针法
快慢指针，慢指针每次移动一步，快指针每次移动两步
初始化 慢指针在head，快指针在head.next 如果快指针追上慢指针则又环，否则快指针到达链表尾部没有环
边界条件 指针为空或者指针长度为1
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hascycle(self,head):
        #判断head是否为空或者长度为1
        if not head or not head.next:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            #fast为空的时候返回false
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True

#160 相交链表 找到两个但链表相交的启始节点
'''
题解分析
快慢指针pa与pb，初始化为链表的a，b的头节点，然后逐渐遍历
当pa到达尾部时候，重新定位到链表到b头节点，同理，当pb到达尾部时候定位到a，
当pa与pb相遇则一定相交，否则不相交
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p=headA
        q=headB
        while p!=q:
            if p:
                p=p.next
            else:
                p=headB
            if q:
                q=q.next
            else:
                q=headA
        return p



