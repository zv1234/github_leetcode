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