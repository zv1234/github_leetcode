#encoding:utf-8
'''
二叉树种类
满二叉树树
完全二叉树
二叉搜索树   左孩子小右孩子大
平衡二叉搜索树    左右高度不超过1

二叉树存储方式
    链式存储
    数组

二叉树遍历
    深度
        前
        中
        后
    广度
        层
'''
from collections import deque
class Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

'''
二叉树遍历leetcode 144，94 145
'''
'''
二叉树的层序遍历leetcode02，107，199，637，429，515，116，117
'''

# 对称二叉树101 不会看不懂