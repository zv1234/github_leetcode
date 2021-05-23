#encoding:utf-8
#前序遍历迭代
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

#中序遍历迭代
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        reslut=[]
        cur=root
        stack=[]
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                reslut.append(cur.val)
                cur=cur.right
        return reslut

#后序遍历迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node:
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        result.reverse()
        return result