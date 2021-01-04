#encoding:utf-8

#一维数组
#198打家劫舍你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''
1.定义dp[i]
2.定义dp关系 如果偷i房间 dp[i]=dp[i-2]+nums[i]   如果不偷的话dp[i]=dp[i-1]
3.边界条件 dp[0]=nums[0]  dp[1]=max(nums[0],nums[1])
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]

# 给出一个非负整数数组，你最初定位在数组的第一个位置。　　　
# 数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　
# 判断你是否能到达数组的最后一个位置。
# [2,3,1,1,4]
'''
1.初始化
2.dp[i]=if dp[j]==True and j+A[i]>=i dp[i]=True
3.初始化条件dp[0]=True
'''
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        if not A:
            return False
        n = len(A)
        # state: dp[i] 代表能否跳到坐标 i
        dp = [False] * n
        # initialization: 一开始站在0这个位置
        dp[0] = True
        # function
        for i in range(1, n):
            for j in range(i):
                # 高效的写法:
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
                # 偷懒的写法
                # dp[i] = dp[i] or dp[j] and (j + A[j] >= i)

        # answer
        return dp[n - 1]


# 413.ArithmeticSlices(Medium)题目描述给定一个数组，求这个数组中连续且等差的子数组一共有多少个。
'''
1.定义dp[i]表示当前以第i个数字结尾的数字有多少个等差数组
2.规则 dp[i]=dp[i-1]+1 if nums[i]-nums[i-1]=nums[i-1]-nums[i-2] 
        dp[i]=dp[i-1]
3.初始化条件  dp[0]=0 dp[1]=0 
'''
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lens=len(A)
        if lens<3:
            return 0
        dp=[0]*lens
        for i in range(2,lens):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
        return sum(dp)


#二维数组动态规划

#64 给定一个m×n大小的非负整数矩阵，求从左上角开始到右下角结束的、经过的数字的和最小的路径。每次只能向右或者向下移动。
'''
1.定义dp数组 d[i][j] 在[i][j]位置最小
2.规则 d[i][j]=min(dp[i-1][j]+nums[i][j],dp[i][j-1]+nums[i][j]) 如果在第一行dp[i][j]=dp[i][j-1]+nums[i][j] 在第一列dp[i][j]=dp[i-1][j]+nums[i][j]
3.边界dp[0][0]=nums[0] 
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[-1][-1]

#542 题目描述给定一个由0和1组成的二维矩阵，求每个位置到最近的0的距离。
'''
1.定义dp dp[i][j] 当前点从左上到右下的最近的0 的距离
'''





#221给定一个二维的0-1矩阵，求全由1构成的最大正方形面积。
'''
1.定义dp dp[i][j]当前位置以dp[i][j]为右下角的正方形面积
2.规则  如果nums[i][j]=0的话则dp[i][j]=0 
        if nums[i][j]=1:  dp[i][j]=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1
3.边界条件 if nums[0][0]==1 dp[0][0]=1  nums[0][0]=0 dp[0][0]=0
'''


class Solution:
    def maximalSquare(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare


#分割类型题 对于分割类型题，动态规划的状态转移方程通常并不依赖相邻的位置，而是依赖于满足分割条件的位置
#279给定一个正整数，求其最少可以由几个完全平方数相加构成。
'''
1.dp(i)代表当前数字最少有几个完全平方相加构成
2.规则 dp(i)=1+min(dp(i-k**2)) k=1,2,3,4,5
3.边界条件 dp(0)=0 dp(1)=1

'''
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]

