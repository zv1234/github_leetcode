#encoding:utf-8
#102二叉树层序遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        queue=[root]
        while queue:
            con=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                con.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(con)
        return result

#107二叉树层序遍历II
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if root is None:
            return []
        queue=[root]
        while queue:
            con=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                con.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(con)
        result.reverse()
        return result

#102.⼆叉树的层序遍历
# 107.⼆叉树的层次遍历II
# 199.⼆叉树的右视图
# 637.⼆叉树的层平均值
# 429.N叉树的前序遍历
# 515.在每个树⾏中找最⼤值
# 116. 填充每个节点的下⼀个右侧节点指针
# 117.填充每个节点的下⼀个右侧节点指针II




#226翻转二叉树
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if root is None:
        #      return root
        # root.left,root.right=root.right,root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        if root is None:
            return root
        stack=[root]
        while stack:
            node=stack.pop()
            node.left,node.right=node.right,node.left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
        #层序遍历
        # if root is None:
        #     return root
        # queue=[root]
        # while queue:
        #     for i in range(len(queue)):
        #         node=queue.pop(0)
        #         node.left,node.right=node.right,node.left
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root