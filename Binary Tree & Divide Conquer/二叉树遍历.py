#encoding:utf-8

'''

[二叉树的前序遍历](  # 二叉树的前序遍历)
[二叉树的中序遍历](  # 二叉树的中序遍历)
[二叉树的后序遍历](  # 二叉树的后序遍历)
def preTraverse(root):

    """前序遍历"""
    if root ==None:
        return
    print root.value
    preTraverse(root.left)
    preTraverse(root.right)
def midTraverse(root):
    """中序遍历"""
    if root==None:
        return
    midTraverse(root.left)
    print root.value
    midTraverse(root.right)
def afterTraverse(root):
    """后序遍历"""
    if root==None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print root.value


'''
"""
Definition of TreeNode:
"""
from collections import deque
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        # if root is None:
        #     return []
        # # 根左右
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
    @staticmethod
    def preorderTraversal(root):
        stack = []
        res = []
        if not root:
            return []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left  # 一直遍历到最左边的那个节点
            if stack:
                temp = stack.pop()
                root = temp.right
        return res


    #中序遍历http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/
    def inorderTraversal(self, root):
        # write your code here
        # if root is None:
        #     return []
        # return self.inorderTraversal(root.left)+[root]+self.inorderTraversal(root.right)
        dummy=TreeNode(0)
        dummy.right=root
        stack=[]
        stack.append(dummy)
        inorder=[]
        while stack:
            node=stack.pop()
            if node.right:
                node=node.right
                while node:
                    stack.append(node)
                    node=node.left
            if stack:
                inorder.append(stack[-1].val)
        return inorder
    def inorderTraversal(self, root):
        if root == None:
            return []
        stack = []
        output = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.val)
            node = node.right
        return output

    def inorderTraversal(root):
        stack = []
        res = []
        if not root:
            return []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                temp = stack.pop()
                root = temp.right
                res.append(temp.val)
        return res
    #后序遍历
    def postorderTraversal(self, root):
        # write your code here
        # if root is None:
        #      return []
        # return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        stack = []
        result = []
        curnode = root
        while stack or curnode:
            while curnode:
                stack.append(curnode)
                curnode = curnode.left if curnode.left else curnode.right
            curnode = stack.pop()
            result.append(curnode.val)
            if stack and stack[-1].left == curnode:
                curnode = stack[-1].right
            else:
                curnode = None
        return result

    def postorderTraversal(root):
        res = []
        if not root:
            return res
        stack = []
        stack.append(root)
        while stack:  # 这里的stack 同时存有节点与节点的值
            temp = stack.pop()
            if type(temp) is TreeNode:  # 判断当前的值的类型是否是二叉树节点
                stack.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
            else:  # 若为节点值则存入
                res.append(temp)
        return res

    #二叉树层序遍历
    def levelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# 97Maximum Depth of Binary Tree
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return max(left,right)+1

# 93. 平衡二叉树
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1


# 94. 二叉树中的最大路径和
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    import sys
    def maxPathSum(self, root):
        maxSum, _ = self.maxPathHelper(root)
        return maxSum

    def maxPathHelper(self, root):
        import sys
        if root is None:
            return sys.maxint, 0

        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)

        return maxpath, single


# 70. 二叉树的层次遍历 II
from collections import deque
class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if root is None :
            return []
        stack=deque([root])
        result=[]
        while stack:
            lever=[]
            for _ in range(len(stack)):
                node=stack.popleft()
                lever.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(lever)
        result.reverse()
        return result

# 71. 二叉树的锯齿形层次遍历
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """

    def zigzagLevelOrder(self, root):
        #注释的方法有错误不能100%通过
        # write your code here
        # length=1
        # if root is None:
        #     return []
        # stack=deque([root])
        # result=[]
        # while len(stack) is not 0:
        #     lever=[]
        #     for _ in range(len(stack)):
        #         node=stack.popleft()
        #         lever.append(node.val)
        #         if length%2==0:
        #             if node.left:
        #                 stack.append(node.left)
        #             if node.right:
        #                 stack.append(node.right)
        #         else:
        #             if node.right:
        #                 stack.append(node.right)
        #             if node.left:
        #                 stack.append(node.left)
        #     length+=1
        #     result.append(lever)
        # return result
        import collections
        # write your code here
        if root is None:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        # 正反向标志
        isForward = 1
        while len(q) is not 0:
            row = []
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                row.append(q[0].val)
                q.popleft()
            # 根据标志来确认当前层遍历的方向
            row = row[::isForward]  # 翻转
            ans += [row]
            # 方向反转
            isForward *= -1
        return ans


# 95. 验证二叉查找树

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    #中序遍历
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)

# 86. 二叉查找树迭代器
"""
Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left
    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0
    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node


# 11. 二叉查找树中搜索区间
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if root is None:
            return []
        stack=[]
        result=[]
        node=root
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            if k1<=node.val<=k2:
                result.append(node.val)
            node=node.right
        return result

#85. 在二叉查找树中插入节点
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode1(self, root, node):
        # write your code here
        if root is None:
            root = node
            return root

        if node.val < root.val:
            root.left = self.insertNode1(root.left, node)
        else:
            root.right = self.insertNode1(root.left, node)

        return root

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            root=node
            return root
        t=root
        while t:
            if node.val<t.val:
                if t.left is None:
                    t.left=node
                    return root
                else:
                    t=t.left
                    continue
            else:
                if t.right is None:
                    t.right=node
                    return root
                else:
                    t=t.right
                    continue


# 87. 删除二叉查找树的节点

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    #没看懂
    def removeNode(self, root, value):
        # write your code here
        # if root is None:
        #     return
        # node=root
        # while node:
        #     if node.val>value
        #         pre_node=node
        #         node=node.left
        #         continue
        #     elif node.val<value:
        #         pre_node=node
        #         node=node.right
        #         continue
        #     else:
        #         if node.left is None and node.right is not None:
        #             pre_node.left=node.right
        #         elif node.right is None and node.left is not None:
        #             node=node.left
        #         elif node.left is None and node.left is None:
        #             node=None
        #         else:
        #             pre_node.left=node.left
        # return root
        if root is None:
            return None
        if root.val == value:
            if root.left is None:
                if root.right is None: #无子节点，直接删除
                    return None
                else:
                    root = root.right #只有右儿子节点，用右儿子替换
            elif root.right is None:
                root = root.left #只有左儿子节点，用左儿子替换
            else:
                buffer = None #buffer用于存放要替换节点的父节点
                tmp = root.right
                while tmp.left is not None:
                    buffer = tmp
                    tmp = tmp.left
                root.val, tmp.val = tmp.val, root.val
                if buffer is None: #buffer为空，则root的右儿子即是目标替换节点
                    root.right = self.removeNode(tmp, value)
                else:
                    buffer.left = self.removeNode(tmp, value)
        elif value < root.val:
            root.left = self.removeNode(root.left, value)
        else:
            root.right = self.removeNode(root.right, value)
        return root



# 101对称二叉树

# class Solution:
#     def isSymmetric(self, root):
#         if not root:
#             return  True
# 	    def dfs(left,right):
# 			# 递归的终止条件是两个节点都为空
# 			# 或者两个节点中有一个为空
# 			# 或者两个节点的值不相等
# 			if not (left or right):
# 				return True
# 			if not (left and right):
# 				return False
# 			if left.val!=right.val:
# 				return False
# 			return dfs(left.left,right.right) and dfs(left.right,right.left)
# 		# 用递归函数，比较左节点，右节点
# 	    return dfs(root.left,root.right)
#
#     def issysmmetric(self,root):
#         if not root or not (root.left or root.right):
#             return True
# 		# 用队列保存节点
# 		queue = [root.left,root.right]
# 		while queue:
# 			# 从队列中取出两个节点，再比较这两个节点
# 			left = queue.pop(0)
# 			right = queue.pop(0)
# 			# 如果两个节点都为空就继续循环，两者有一个为空就返回false
# 			if not (left or right):
# 				continue
# 			if not (left and right):
# 				return False
# 			if left.val!=right.val:
# 				return False
# 			# 将左节点的左孩子， 右节点的右孩子放入队列
# 			queue.append(left.left)
# 			queue.append(right.right)
# 			# 将左节点的右孩子，右节点的左孩子放入队列
# 			queue.append(left.right)
# 			queue.append(right.left)
# 		 return True

# 104二叉树的最大深度
class Solution:
    def maxDepth(self, root):
        # if root is None:
        #     return 0
        # left= self.maxDepth(root.left)
        # right=self.maxDepth(root.right)
        # return max(left,right)+1
    #层序遍历
        if root is None:
            return 0
        queue=[root]
        a=0
        while queue:
            for _ in range(len(queue)):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            a+=1
        return a

# 111二叉树最小深度
class Solution:
    def minDepth(self, root):
        #递归
        def dfs(root):
            if root is None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            # // 当⼀个左⼦树为空，右不为空，这时并不是最低点
            if root.left is None and  root.right is not None :
                return 1+right
            # // 当⼀个右⼦树为空，左不为空，这时并不是最低点
            if root.right is None and  root.left is not None:
                return 1+left
            return 1+min(left,right)

        return dfs(root)

        #迭代


#222完全二叉树节点个数
class Solution:
    def countNodes(self,root):
        # if root is None:
        #     return 0
        # left=self.countNodes(root.left)
        # right=self.countNodes(root.right)
        # return left+right+1
        if root is None:
            return 0
        queue=[root]
        result=0
        while queue:
            for _ in range(len(queue)):
                node=queue.pop(0)
                result+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

# 110平衡二叉树
# 257 二叉树所有路径

#100相同的树
class Solution:
    def isSameTree(self, p,q):
        #递归
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    #迭代

# 572另一个树的子树
