#encoding:utf-8

"满二叉树"
# 完全二叉树
# 二叉搜索数
# 「二叉搜索树是一个有序树」。
# 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为二叉排序树

"二叉树递归 递归三要素" \
"1。确定递归函数参数与返回值" \
"确定终止条件" \
"确定单层递归逻辑"

#二叉树递归遍历
#144二叉树前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def help(node):
            if node is None:
                return
            result.append(node.val)
            help(node.left)
            help(node.right)
        help(root)
        return result

#145二叉树后序遍历class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        reslut=[]
        def help(node):
            if node is None:
                return
            help(node.left)
            help(node.right)
            reslut.append(node.val)
        help(root)
        return reslut

#94二叉树中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        reslut=[]
        def help(node):
            if node is None:
                return
            help(node.left)
            reslut.append(node.val)
            help(node.right)
        help(root)
        return reslut