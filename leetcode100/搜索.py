
#深度优先搜索
'''
一般来说，深度优先搜索类型的题可以分为主函数和辅函数，主函数用于遍历所有的搜索位置，判断是否可以开始搜索，如果可以即在辅函数进行搜索。辅函数则负责深度优先搜索的递归调用

'''

# 1.检测环路
# 题目描述给定一个二维的0-1矩阵，其中0表示海洋，1表示陆地。单独的或相邻的陆地可以形成岛屿，每个格子只与其上下左右四个格子相邻。求最大的岛屿面积。

class Solution(object):
    def dfs(self,grid,cur_i,cur_j):
        if cur_i<0 or cur_j<0 or cur_i==len(grid) or cur_j==len(grid[0]) or grid[cur_i][cur_j]!=1:
            return 0
        grid[cur_i][cur_j]=0
        ans=1
        for di,dj in ([0,1],[0,-1],[1,0],[-1,0]):
            next_i,next_j=cur_i+di,cur_j+dj
            ans+=self.dfs(grid,next_i,next_j)
        return ans

    #主函数
    def maxAreaof(self,grid):
        ans=0
        for i,l in enumerate(grid):
            for j,n in enumerate(l):
                ans=max(self.dfs(grid,i,j),ans)
        return  ans

