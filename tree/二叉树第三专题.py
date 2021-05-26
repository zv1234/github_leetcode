#encoding:utf-8
#100求相同的树
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q!=None:
            return False
        elif p!=None and q==None:
            return False
        elif p==None and q==None:
            return True
        elif p.val!=q.val:
            return False
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        return left and right

#404左边叶子和
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left=self.sumOfLeftLeaves(root.left)
        right=self.sumOfLeftLeaves(root.right)
        mid=0
        if root.left and ( not root.left.left) and not(root.left.right):
            mid=root.left.val
        Sum=mid+left+right
        return Sum
    # 前中后序迭代
    # if root is None:
    #     return 0
    # Sum = 0
    # stack = [root]
    # while stack:
    #     node = stack.pop()
    #     if node.left and (not node.left.left) and not (node.left.right):
    #         Sum += node.left.val
    #     if node.right:
    #         stack.append(node.right)
    #     if node.left:
    #         stack.append(node.left)
    # return Sum

#513树左下角的值

#回溯法不是很理解
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result=[]
        queue=[root]
        while queue:
            cov=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                cov.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cov)
        return result[-1][0]

#112路径总和
#超出内存限制


#113路径总和二
# 典型回溯算法
#超出内存限制


#构造二叉树105，106

