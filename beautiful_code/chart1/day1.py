#cpu的利用率在50%


'''
没看懂

'''

#中国象棋将帅问题 使用一个变量
'''
暴力法 位运算  一个byte有8个字节，前面4个字节存储A,H后面存储B ,A,B的位置取3模比较两者相等
'''

#定义数据结构
class node(object):
    def __init__(self,val):
        self.val=val

class solution(object):
    def __init__(self):
        for i in range(1,9):
            for j in range(1,9):
                if i%3==j%3:
                    print((i,j))


