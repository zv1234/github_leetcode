#encoding:utf-8

#前序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1=[]
        def help(root):
            if root is None:
                return
            list1.append(root.val)
            help(root.left)
            help(root.right)
        help(root)
        return list1

#非递归先序遍历
    def preordefunrecur(self,head):
        '''
        1。申请新栈stack，将头节点压入
        2。stack 弹出栈顶节点，cur，打印cur的值 将节点的cur的右孩子压入栈，再将左孩子压入
        3。不断重复2，直到stack为kong
        '''
        if head==None:
            return
        stack=[]
        stack.append(head)
        while stack:
            node=stack.pop()
            print (node.val)
            if head.right!=None:
                stack.append(head.right)
            if head.left!=None:
                stack.append(head.left)

#中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1=[]
        def help(root):
            if root is None:
                return
            help(root.left)
            list1.append(root.val)
            help(root.right)
        help(root)
        return list1
    def inorderunrecur(self,head):
        '''
        :param head:
        :return:
        1.新栈stack ， 变量cur=head
        2。先把cur节点压入栈中，对于cur节点为头的整棵子树来说，依次将左边界压入栈中，cur=cur。left
        3。不断重复步骤2 ，直到cur为空，从stack中弹出一个节点，记node，打印node值，让cur=node。left，重复步骤2
        4。当stack为空时候，整个停止
        '''
        cur=head
        stack=[]
        while head!=None  or len(stack)>0 :
            if head:
                stack.append(head)
                cur=cur.left
            else:
                head=stack.pop()
                print head.val
                head=head.right




#后序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1=[]
        def help(root):
            if root is None:
                return
            help(root.left)
            help(root.right)
            list1.append(root.val)
        help(root)
        return list1

    def posorderunrecur(self,head):
        '''

        :param head:
        :return:
        1。栈s1,将头节点head压入s1
        2。从s1中弹出当节点记cur，依次将cur当左孩子和有孩子压入s1
        3。在整个过程中每一个从s1中弹出当节点放入到s2中
        4。不断重重2和3步骤，直到s1为空
        5。从s2中依次弹出节点打印
        '''
        s1=[]
        s2=[]
        s1.append(head)
        while s1:
            head=s1.pop()
            s2.append(head)
            if head.left!=None:
                s1.append(head.left)
            if head.right!=None:
                s1.append(head.right)
        while s2:
            print (s2.pop().val)
