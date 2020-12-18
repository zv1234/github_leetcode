'''
递归：1.递归终止条件
    2.递推公式
将问题逐步分解成较小的范围，
调用函数 f(x0),f(x1)递归解决这些子问题；
最后，处理调用递归函数得到的结果来解决对应 X{X}X 的问题。
 
'''

#相反顺序打印字符串
def reverse(p_str):
    l = len(p_str)
    if l == 0:
        return
    print(p_str[l - 1])
    reverse(p_str[:l - 1])

'''
反转字符串编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def help(left,right):
            if left<right:
                s[left],s[right]=s[right],s[left]
                help(left+1,right-1)
        left=0
        right=len(s)-1
        help(left,right)


#两两交换链表中的节点 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # head, head.next, head.next.next =  head.next, head, head.next.next
        # head.next.next = self.swapPairs(head.next.next)
        head, head.next, head.next.next = head.next, head, self.swapPairs(head.next.next)

        return head

if __name__ == '__main__':
    a='123456'
    reverse(a)