#encoding:utf-8
#使用场景：
'''
when：
1。优化o（n）的时间复杂度
2。
how：
找到满足某个条件的第一个或者最后一个位置
'''
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r,ans=0,x,-1
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=x:
                ans=mid
                l+=1
            else:
                r-=1
        return ans


# 写出一个高效的算法来搜索 m × n矩阵中的值。
# 这个矩阵具有以下特性：
# 每行中的整数从左到右是排序的。
# 每行的第一个数大于上一行的最后一个整数。
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True

        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False

# 给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
# 你可以假设在数组中无重复元素。
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A)==0:
            return 0
        start,end=0,len(A)-1
        #first posttion >=target
        while start+1<end:
            mid=(start+end)/2
            if A[mid]>=target:
                end=mid
            else:
                start=end
        if A[start]>=target:
            return start
        if A[end]>=target:
            return end
        return len(A)

# 给定一个整数数组 （下标由 0 到 n-1，其中 n 表示数组的规模，数值范围由 0 到 10000），以及一个 查询列表。对于每一个查询，将会给你一个整数，请你返回该数组中小于给定整数的元素的数量。

