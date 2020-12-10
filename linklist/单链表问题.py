#encoding:utf-8


#反转链表
'''
方法1：按照原始顺序迭代节点，并且逐步移动到列表到头部 时间复杂度：o(n)
'''

#迭代
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre

    #好像没看懂
    def reverlist_digui(self,head):
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur

#203移除链表元素，删除链表中给定val到所有节点

'''
题解：删除节点为中间节点，找到节点前驱即可，当删除为头节点时候，可以通过设置哨兵节点来实现
哨兵节点广泛应用于树和链表中，如伪头、伪尾、标记等，它们是纯功能的，通常不保存任何数据，其主要目的是使链表标准化，如使链表永不为空、永不无头、简化插入和删除。
初始化哨兵节点为 ListNode(0) 且设置 sentinel.next = head。
初始化两个指针 curr 和 prev 指向当前节点和前继节点。
当 curr != nullptr：
比较当前节点和要删除的节点：
若当前节点就是要删除的节点：则 prev.next = curr.next。
否则设 prve = curr。
遍历下一个元素：curr = curr.next。
返回 sentinel.next
时间复杂度为o(n)
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        sb=ListNode(0,head)
        cur=head
        pre=sb
        while cur:
            if cur.val==val:
                pre.next=cur.next
            else:
                pre=cur
            cur=cur.next
        return sb.next

#328 奇偶链表 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性






