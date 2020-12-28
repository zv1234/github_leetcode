#encoding:utf-8

# 打印二叉树到边界节点
'''
1。头节点为边界节点
2。叶子节点为边界节点
3。如果节点在其所在层中是最左或者最右，也是边界节点
'''
class node(object):
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None


def gethight(head,height=0):
    if head==None:
        return 1
    return max(gethight(head.left,height+1),gethight(head.right,height+1))+1

def printedgle(self,head):
    if head==None:
        return
    hight=gethight(head)
    #打印左边界
    pass
