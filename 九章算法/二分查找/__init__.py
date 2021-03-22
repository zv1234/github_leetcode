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



# 给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。如果目标值不在数组中，则返回[-1, -1]
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here

        def low(A,target):
            if len(A)==0:
                return [-1,-1]
            l,r=0,len(A)-1
            while l+1<r:
                mid=(l+r)//2
                if A[mid]<=target:
                    l=mid
                else:
                    r=mid
            if A[l]<=target:
                return l
        def high(A,target):
            if len(A)==0:
                return [-1,-1]
            l,r=0,len(A)-1
            while l+1<r:
                mid=(l+r)//2
                if A[mid]>=target:
                    r=mid
                else:
                    l=mid
            if A[r]>=target:
                return r

        return [low(A,target),high(A,target)]

# 假设一个排好序的数组在其某一未知点发生了旋转（比如0 1 2 4 5 6 7 可能变成4 5 6 7 0 1 2）。你需要找到其中最小的元素。
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            #正常情况下nums[mid]<nums[end]
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end])


# 假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。你可以假设数组中不存在重复的元素。
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

'''
你给出一个整数数组(size为n)，其具有以下特点：
相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
'''
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        start, end = 1, len(A) - 2
        while start + 1 <  end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                return mid
        if A[start] < A[end]:
            return end
        else:
            return start


# 给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)。
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, str,offset):
        # write your code here
        '''
        输入:  str="abcdefg", offset = 3
        输出:  str = "efgabcd"
        样例解释:  注意是原地旋转，即str旋转后为"efgabcd"
        '''
        offest=offset%len*(str)
        str.split("")
        for i in range(offest):
            str[i]
            pass