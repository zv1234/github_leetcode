#encoding:utf-8

#队列与广度优先遍历

#岛屿的数量
'''
11000
11000
00100
00011
'''
import collections
#广度优先遍历
class solution(object):
    def numislands(self,grid):
        num_row=len(grid)
        if num_row==0:
            return 0
        num_column=len(grid[0])
        #岛屿数量
        num_island=0
        for i in range(num_row):
            for j in range(num_column):
                if grid[i][j]=="1":
                    num_island+=1
                    grid[i][j]="0"
                    queue=collections.deque([(i,j)])
                    while queue:
                        current_x, current_y = queue.popleft()
                        for x, y in [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1),
                                     (current_x, current_y + 1)]:
                            if 0<=x<num_row and 0<=y<num_column and grid[x][y] == "1":
                                queue.append((x,y))
                                grid[x][y]="0"
        return num_island

#递归实现


#347前k个高频元素


