#encoding:utf-8
#101对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def help(left,right):
            if left!=None and right==None:
                return False
            elif left==None and right!=None:
                return False
            elif left==None and right==None:
                return True
            elif left.val!=right.val:
                return False
            out=help(left.left,right.right)
            inside=help(left.right,right.left)
            return out and inside
        a=help(root.left,root.right)
        return a

#104二叉树最大深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+max(left,right)

    #迭代法

#111最小深度最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 画图  迭代法层序遍历
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_dp=self.minDepth(root.left)
        right_dp=self.minDepth(root.right)
        if root.left==None and root.right!=None:
            return 1+right_dp
        if root.left!=None and root.right==None:
            return 1+left_dp
        result=1+min(left_dp,right_dp)
        return result

#222完全二叉树节点个数    迭代层序遍历
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        result=1+left+right
        return result

#110平衡二叉树
